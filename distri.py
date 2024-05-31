import matplotlib.pyplot as plt
from collections import defaultdict
import sys


def read_community_file(file_path):
    community_assignments = defaultdict(list)

    with open(file_path, 'r') as f:
        for line in f:
            node, community = map(int, line.strip().split())
            community_assignments[community].append(node)

    return community_assignments


def compute_community_sizes(community_assignments):
    community_sizes = [len(nodes) for nodes in community_assignments.values()]
    return community_sizes


def plot_community_size_distribution(community_sizes):
    size_distribution = defaultdict(int)

    for size in community_sizes:
        size_distribution[size] += 1

    sizes = sorted(size_distribution.keys())
    counts = [size_distribution[size] for size in sizes]

    plt.plot(sizes, counts, linestyle='-', color='b')
    plt.xlabel('Community Size')
    plt.ylabel('Number of Communities')
    plt.title('Community Size Distribution')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    community_assignments = read_community_file(input_file_path)
    community_sizes = compute_community_sizes(community_assignments)
    plot_community_size_distribution(community_sizes)
