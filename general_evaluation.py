from sklearn.metrics import normalized_mutual_info_score
import argparse
import numpy as np
from collections import defaultdict
import os

# python general_evaluation.py --measure purity --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./louvain/TC1-6.cmty --algorithm louvain&
# python general_evaluation.py --measure purity --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./louvain/TC1-1.cmty --algorithm louvain&
# python general_evaluation.py --measure purity --ground ./groundtruth/TC1-6/TC1-6.cmty --detected ./output/TC1-6/TC1-6.cmty --algorithm ours&
# python general_evaluation.py --measure purity --ground ./groundtruth/TC1-1/TC1-1.cmty --detected ./output/TC1-1/TC1-1.cmty --algorithm ours&

# Reading the Ground-Truth Community Data
def load_communities(file_path):
    node_to_community = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                node, community = int(parts[0]), int(parts[1])
                node_to_community[node] = community
    # Convert to list of lists for compatibility with F1 calculation
    community_to_nodes = {}
    for node, community in node_to_community.items():
        if community not in community_to_nodes:
            community_to_nodes[community] = []
        community_to_nodes[community].append(node)
    return list(community_to_nodes.values()), node_to_community

# Calculating NMI Score
def calculate_nmi(true_communities, detected_communities):
    true_labels = {}
    for i, community in enumerate(true_communities):
        for node in community:
            true_labels[node] = i
    detected_labels = {}
    for i, community in enumerate(detected_communities):
        for node in community:
            detected_labels[node] = i

    nodes = sorted(set(true_labels) | set(detected_labels))
    true_labels_vector = [true_labels[node] for node in nodes]
    detected_labels_vector = [detected_labels.get(node, -1) for node in nodes]

    return normalized_mutual_info_score(true_labels_vector, detected_labels_vector)

# Calculating F1 Score based on the given definition
def calculate_f1(true_communities, detected_communities):
    f1_scores = []
    for true_community in true_communities:
        best_f1 = 0
        for detected_community in detected_communities:
            intersection_size = len(set(true_community) & set(detected_community))
            if intersection_size == 0:
                continue

            precision = intersection_size / len(detected_community)
            recall = intersection_size / len(true_community)
            f1_score = (2 * precision * recall) / (precision + recall) if precision + recall > 0 else 0
            if f1_score > best_f1:
                best_f1 = f1_score
        f1_scores.append(best_f1)
    return np.mean(f1_scores)

# Calculating GINI Index and Purity
def calculate_gini_index(community, ground_truth):
    category_count = defaultdict(int)
    for node in community:
        category_count[ground_truth[node]] += 1
    total_nodes = sum(category_count.values())
    gini = 1 - sum((count / total_nodes) ** 2 for count in category_count.values()) if total_nodes > 0 else 0
    return gini

def calculate_purity(true_node_to_community, detected_communities):
    purities = []
    for community in detected_communities:
        gini = calculate_gini_index(community, true_node_to_community)
        purity = 1 - gini
        purities.append(purity)
    return purities

def eval(ground_truth_file_path, detected_communities_file_path, measure, algorithm):
    true_communities, true_node_to_community = load_communities(ground_truth_file_path)
    detected_communities, detected_node_to_community = load_communities(detected_communities_file_path)
    dataset = os.path.basename(ground_truth_file_path).split('.')[0]

    if measure == 'nmi':
        result = calculate_nmi(true_communities, detected_communities)
        output_dir = f"./output/NMI/{algorithm}/"
        # output_dir = f"./new_output/NMI/{algorithm}/"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{dataset}_NMI.txt")
        with open(output_file, 'w') as f:
            f.write(f"NMI score: {result}\n")
    elif measure == 'f1':
        result = calculate_f1(true_communities, detected_communities)
        output_dir = f"./output/F1/{algorithm}/"
        # output_dir = f"./new_output/F1/{algorithm}/"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{dataset}_F1.txt")
        with open(output_file, 'w') as f:
            f.write(f"F1 score: {result}\n")
    elif measure == 'purity':
        purities = calculate_purity(true_node_to_community, detected_communities)
        output_dir = f"./output/purity/{algorithm}/"
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{dataset}_purity.txt")
        with open(output_file, 'w') as f:
            for i, purity in enumerate(purities, 1):
                f.write(f"{i} {purity:.4f}\n")
    else:
        raise ValueError("Unsupported measure. Please choose either 'nmi', 'f1', or 'purity'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate community detection in a network.')
    parser.add_argument('--ground', '-g', type=str, help='The path of the ground truth community file.', required=True)
    parser.add_argument('--detected', '-d', type=str, help='The path of the detected communities file.', required=True)
    parser.add_argument('--measure', '-m', type=str, help='The measure to evaluate (nmi, f1, or purity).', required=True)
    parser.add_argument('--algorithm', '-a', type=str, help='The algorithm used for detection (for output path).', required=True)
    args = parser.parse_args()

    ground_truth_file_path = args.ground
    detected_communities_file_path = args.detected
    measure = args.measure
    algorithm = args.algorithm

    eval(ground_truth_file_path, detected_communities_file_path, measure, algorithm)
    print(f'{measure.upper()} score has been calculated and saved to the respective file.')
