
import os
import argparse
import networkx as nx
from collections import defaultdict
import time

# python detection.py --network ./dataset/TC1-6 --mode normal
# python detection.py --network ./dataset/TC1-1 --mode purity
def load_network(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                G.add_edge(int(parts[0]), int(parts[1]))
    for node in G.nodes():
        G.nodes[node]['assigned'] = False
    return G

def load_ground_truth(file_path):
    ground_truth = {}
    with open(file_path, 'r') as file:
        for line in file:
            node_id, community = line.strip().split()
            ground_truth[int(node_id)] = int(community)
    return ground_truth

def calculate_gini_index(node, ground_truth):
    category_count = defaultdict(int)
    for vertex in node.nodes:
        category_count[ground_truth[vertex]] += 1
    total_vertices = sum(category_count.values())
    gini = 1 - sum((count / total_vertices) ** 2 for count in category_count.values()) if total_vertices > 0 else 0
    return category_count, gini

class TNode:
    def __init__(self, name, gnodes=None):
        self.name = name
        self.children = []
        self.gnodes = gnodes if gnodes else set()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

def construct_seed_tree(G, initial_k=3):
    root = TNode("root")
    truss = nx.k_truss(G, initial_k)  # 3-truss
    if truss.number_of_nodes() == 0:
        return print("there is no 3-truss")
    root.gnodes = set(G.nodes()).difference(truss.nodes())  # 3-truss에 속하지 않는 것만 가짐.
    ### isolated 처리
    iso_com = list(nx.connected_components(G))
    for iso_comp in iso_com:
        sub = G.subgraph(iso_comp)
        iso_truss = nx.k_truss(sub, 3)
        if iso_truss.number_of_nodes() == 0:
            iso_tnode = TNode("isolated")
            root.children.append(iso_tnode)
            iso_tnode.gnodes = set(sub.nodes())
            for v in iso_tnode.gnodes:
                G.nodes[v]['assigned'] = True
            root.gnodes = root.gnodes.difference(iso_tnode.gnodes)
    ###
    components = list(nx.connected_components(truss))
    for i, comp in enumerate(components):
        r_tree(G.subgraph(comp), initial_k, root)
    return root

def r_tree(G, k, parent):
    tnode = TNode(f"{k}-truss")
    parent.children.append(tnode)
    #to avoid stack overflow. if it occur, uncomment below.
    # if k > 500:
    #     tnode.gnodes = set(G.nodes())
    #     for v in tnode.gnodes:
    #         G.nodes[v]['assigned'] = True
    #     return

    truss = nx.k_truss(G, k + 1)
    tnode.gnodes = set(G.nodes()).difference(truss.nodes())
    if truss.number_of_nodes() == 0:
        for v in tnode.gnodes:
            G.nodes[v]['assigned'] = True
        return
    ### 더 branching
    print(k)
    sub = G.subgraph(tnode.gnodes)
    sub_truss = nx.k_truss(sub, k)
    sub_comp = list(nx.connected_components(sub_truss))
    for comp in sub_comp:
        tnode1 = TNode(f"{k}-truss")
        tnode.children.append(tnode1)
        tnode1.gnodes = comp
        tnode.gnodes = tnode.gnodes.difference(comp)
        for v in tnode1.gnodes:
            G.nodes[v]['assigned'] = True
    ###
    components = list(nx.connected_components(truss))
    for i, comp in enumerate(components):
        r_tree(G.subgraph(comp), k + 1, tnode)

    if len(tnode.children) == 1:  # has one child
        child = tnode.children[0]
        if len(child.children) == 0:  # child is seed node
            for v in tnode.gnodes:
                G.nodes[v]['assigned'] = True
            tnode.gnodes = tnode.gnodes.union(child.gnodes)
            tnode.children = []

def assign_nodes_in_intermediate_nodes(G, root):
    print("assign_nodes_in_intermediate_nodes")
    for tnode in PostOrderIter(root):
        if len(tnode.children) > 0:  # intermediate
            seeds = [leaf for leaf in PostOrderIter(tnode) if len(leaf.children) == 0]  # seed들 모음.
            while tnode.gnodes:  # 이거 for로 바꾸고 best gain도 -inf 되야함.
                best_gain = -float('inf')
                best_seed = None
                v = tnode.gnodes.pop()
                switch = True
                for u in G.neighbors(v):  # 이웃에 assign된거 하나라도 없으면 나중으로 미룸.
                    if G.nodes[u]['assigned']:  # assign된거 하나라도 있으면
                        switch = False
                        break
                if switch:
                    tnode.gnodes.add(v)
                    continue
                for seed in seeds:
                    increase = calculate_modularity_increase(G, seed.gnodes, v)
                    if increase > best_gain:
                        best_gain = increase
                        best_seed = seed
                best_seed.gnodes.add(v)
                G.nodes[v]['assigned'] = True

def calculate_modularity_increase(G, community, node):
    m = G.number_of_edges()  # Number of edges in the graph
    degree_node = G.degree(node)  # Degree of the node to be added
    # Number of edges inside the community that connect to the node
    edges_inside = sum(1 for neighbor in G.neighbors(node) if neighbor in community)
    # Sum of degrees of all nodes in the community
    sum_degrees_community = sum(G.degree(n) for n in community)
    # Expected number of edges if the edges were randomly distributed
    expected_edges = (degree_node * sum_degrees_community) / (2 * m)
    # Modularity change
    modularity_increase = (edges_inside / m) - (expected_edges / (2 * m))
    return modularity_increase

def PostOrderIter(node):
    result = []
    def recurse(n):
        for child in n.children:
            recurse(child)
        result.append(n)
    recurse(node)
    print(f"postorder: {result}")
    return result

def write_community_file(tree_root, file_path):
    community_number = 1
    with open(file_path, 'w') as file:
        for tnode in PostOrderIter(tree_root):
            if len(tnode.children) == 0:
                for member_node in tnode.gnodes:
                    file.write(f"{member_node}\t{community_number}\n")
                community_number += 1

def write_seed_purity_file(tree_root, ground_truth, file_path):
    with open(file_path, 'w') as file:
        seed_number = 1
        for node in PostOrderIter(tree_root):
            if node.type == 'Seed node':
                category_count, gini = calculate_gini_index(node, ground_truth)
                purity = 1 - gini
                file.write(f"{seed_number}\t{purity:.4f}\n")
                seed_number += 1

def write_num_of_seeds(tree_root, file_path):
    leaf_count = sum(1 for node in PostOrderIter(tree_root) if len(node.children) == 0)
    with open(file_path, 'w') as file:
        file.write(f"Number of seed nodes: {leaf_count}\n")

# Main script

def main(args):
    network_path = os.path.join(args.network, 'network.txt')
    dataset = os.path.basename(args.network)
    G = load_network(network_path)
    output_dir = f"./output/{dataset}/"
    # output_dir = f"./old_output/{dataset}/" #old전용
    os.makedirs(output_dir, exist_ok=True)
    run = time.time()
    root = construct_seed_tree(G)

    if args.mode == 'normal':
        assign_nodes_in_intermediate_nodes(G, root)
        run_time = time.time() - run
        output_file = os.path.join(output_dir, f"{dataset}.cmty")
        # output_file = os.path.join(output_dir, f"{dataset}_branch.cmty")
        write_community_file(root, output_file)
    elif args.mode == 'purity':
        assign_nodes_in_intermediate_nodes(G, root)
        run_time = time.time() - run
        ground_truth_path = f"./groundtruth/{dataset}/{dataset}.cmty"
        ground_truth = load_ground_truth(ground_truth_path)
        output_file = os.path.join(output_dir, f"{dataset}_seed_purity.txt")
        write_seed_purity_file(root, ground_truth, output_file)
    elif args.mode == 'tree':
        run_time = time.time() - run
        output_file = os.path.join(output_dir, 'num_of_seed.txt')
        write_num_of_seeds(root, output_file)

    runtime_file = os.path.join(output_dir, 'runtime.txt')
    with open(runtime_file, 'w') as f:
        f.write(f"Dataset: {dataset}\n")
        f.write(f"Run time: {run_time:.4f} seconds\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Community detection using k-truss decomposition.")
    parser.add_argument("--network", type=str, required=True,
                        help="Path to the dataset directory containing the network file.")
    parser.add_argument("--mode", type=str, default='normal', choices=['normal', 'purity', 'seed', 'tree'], help="Mode of operation.")

    args = parser.parse_args()
    main(args)
