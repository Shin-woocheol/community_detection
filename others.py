# import os
# import networkx as nx
# import community as community_louvain
# import random
# import numpy as np
# import argparse
# import leidenalg as la
# import igraph as ig
#
# from sklearn.metrics.cluster import normalized_mutual_info_score
#
# random_seed = 42
# random.seed(random_seed)
# np.random.seed(random_seed)
#
#
# # Reading the Network Data
# def load_network(file_path):
#     G = nx.Graph()
#     with open(file_path, 'r') as f:
#         for line in f:
#             parts = line.strip().split()
#             if len(parts) == 2:
#                 G.add_edge(int(parts[0]), int(parts[1]))
#     return G
#
#
# # Applying the Louvain Algorithm
# def detect_communities_louvain(G):
#     partition = community_louvain.best_partition(G)
#     # Convert partition dictionary to list of lists for NMI calculation
#     community_to_nodes = {}
#     for node, community in partition.items():
#         if community not in community_to_nodes:
#             community_to_nodes[community] = []
#         community_to_nodes[community].append(node)
#     return list(community_to_nodes.values())
#
#
# # Applying the Leiden Algorithm
# def detect_communities_leiden(G):
#     # Relabel nodes to have consecutive integers starting from 0
#     mapping = {node: idx for idx, node in enumerate(G.nodes())}
#     G = nx.relabel_nodes(G, mapping)
#
#     # Convert NetworkX graph to igraph and preserve node IDs
#     ig_graph = ig.Graph(directed=False)
#     ig_graph.add_vertices(list(G.nodes()))
#     ig_graph.add_edges(list(G.edges()))
#
#     partition = la.find_partition(ig_graph, la.ModularityVertexPartition)
#
#     # Convert the partition to a list of lists for consistency with Louvain function
#     community_to_nodes = {}
#     for node, community in zip(ig_graph.vs["name"], partition.membership):
#         if community not in community_to_nodes:
#             community_to_nodes[community] = []
#         community_to_nodes[community].append(int(node))  # Node IDs are strings in igraph
#
#     # Revert mapping to original node IDs
#     reverse_mapping = {idx: node for node, idx in mapping.items()}
#     communities = [[reverse_mapping[node] for node in community] for community in community_to_nodes.values()]
#
#     return communities
#
#
# # Step 5: Save the result
# def save_communities_to_file(communities, file_path):
#     # Create output directory if it doesn't exist
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#
#     # Convert the list of lists into a dictionary with community as key and nodes as values
#     community_dict = {}
#     for community_id, nodes in enumerate(communities):
#         for node in nodes:
#             community_dict[node] = community_id
#
#     # Sort the dictionary by community key (which are the node numbers here)
#     sorted_community_items = sorted(community_dict.items())
#
#     # Write to file, now ensuring nodes are listed in the sorted order of their community keys
#     with open(file_path, 'w') as f:
#         for node, community_id in sorted_community_items:
#             f.write(f"{node} {community_id}\n")
#
#
# # Load the data
# parser = argparse.ArgumentParser(description='Detect communities in a network.')
# parser.add_argument('--networkFile', '-n', type=str, help='The path of the network file.',
#                     default="./dataset/TC1-1/network.txt")
# parser.add_argument('--algorithm', '-a', type=str, help='The community detection algorithm to use (louvain or leiden).',
#                     default="louvain")
# args = parser.parse_args()
#
# # Extract data name from the file path
# data_name = os.path.basename(os.path.dirname(args.networkFile))
#
# if args.algorithm.lower() == "leiden":
#     community_file_path = f"./leiden/{data_name}.cmty"
# else:
#     community_file_path = f"./louvain/{data_name}.cmty"
#
# G = load_network(args.networkFile)
#
# # Detect communities using the specified method
# if args.algorithm.lower() == "leiden":
#     detected_communities = detect_communities_leiden(G)
# else:
#     detected_communities = detect_communities_louvain(G)
#
# save_communities_to_file(detected_communities, community_file_path)
# import os
# import networkx as nx
# import community as community_louvain
# import random
# import numpy as np
# import argparse
# import leidenalg as la
# import igraph as ig
#
# from sklearn.metrics.cluster import normalized_mutual_info_score
#
# random_seed = 42
# random.seed(random_seed)
# np.random.seed(random_seed)
#
# # Reading the Network Data
# def load_network(file_path):
#     G = nx.Graph()
#     with open(file_path, 'r') as f:
#         for line in f:
#             parts = line.strip().split()
#             if len(parts) == 2:
#                 G.add_edge(int(parts[0]), int(parts[1]))
#     return G
#
# # Applying the Louvain Algorithm
# def detect_communities_louvain(G):
#     partition = community_louvain.best_partition(G)
#     # Convert partition dictionary to list of lists for NMI calculation
#     community_to_nodes = {}
#     for node, community in partition.items():
#         if (community not in community_to_nodes):
#             community_to_nodes[community] = []
#         community_to_nodes[community].append(node)
#     return list(community_to_nodes.values())
#
# # Applying the Leiden Algorithm
# def detect_communities_leiden(G):
#     # Relabel nodes to have consecutive integers starting from 0
#     mapping = {node: idx for idx, node in enumerate(G.nodes())}
#     G = nx.relabel_nodes(G, mapping)
#
#     # Convert NetworkX graph to igraph and preserve node IDs
#     ig_graph = ig.Graph(directed=False)
#     ig_graph.add_vertices(list(G.nodes()))
#     ig_graph.add_edges(list(G.edges()))
#
#     partition = la.find_partition(ig_graph, la.ModularityVertexPartition)
#
#     # Convert the partition to a list of lists for consistency with Louvain function
#     community_to_nodes = {}
#     for node, community in zip(ig_graph.vs["name"], partition.membership):
#         if (community not in community_to_nodes):
#             community_to_nodes[community] = []
#         community_to_nodes[community].append(int(node))  # Node IDs are strings in igraph
#
#     # Revert mapping to original node IDs
#     reverse_mapping = {idx: node for node, idx in mapping.items()}
#     communities = [[reverse_mapping[node] for node in community] for community in community_to_nodes.values()]
#
#     return communities
#
# # Applying the Girvan-Newman Algorithm
# def detect_communities_girvan_newman(G):
#     communities_generator = nx.community.girvan_newman(G)
#     top_level_communities = next(communities_generator)
#     next_level_communities = next(communities_generator)
#     # Select the next level communities
#     communities = sorted(map(sorted, next_level_communities))
#     return communities
#
# # Step 5: Save the result
# def save_communities_to_file(communities, file_path):
#     # Create output directory if it doesn't exist
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#
#     # Convert the list of lists into a dictionary with community as key and nodes as values
#     community_dict = {}
#     for community_id, nodes in enumerate(communities):
#         for node in nodes:
#             community_dict[node] = community_id
#
#     # Sort the dictionary by community key (which are the node numbers here)
#     sorted_community_items = sorted(community_dict.items())
#
#     # Write to file, now ensuring nodes are listed in the sorted order of their community keys
#     with open(file_path, 'w') as f:
#         for node, community_id in sorted_community_items:
#             f.write(f"{node} {community_id}\n")
#
# # Load the data
# parser = argparse.ArgumentParser(description='Detect communities in a network.')
# parser.add_argument('--networkFile', '-n', type=str, help='The path of the network file.',
#                     default="./dataset/TC1-1/network.txt")
# parser.add_argument('--algorithm', '-a', type=str, help='The community detection algorithm to use (louvain, leiden, or girvan_newman).',
#                     default="louvain")
# args = parser.parse_args()
#
# # Extract data name from the file path
# data_name = os.path.basename(os.path.dirname(args.networkFile))
#
# if args.algorithm.lower() == "leiden":
#     community_file_path = f"./leiden/{data_name}.cmty"
# elif args.algorithm.lower() == "girvan_newman":
#     community_file_path = f"./girvan_newman/{data_name}.cmty"
# else:
#     community_file_path = f"./louvain/{data_name}.cmty"
#
# G = load_network(args.networkFile)
#
# # Detect communities using the specified method
# if args.algorithm.lower() == "leiden":
#     detected_communities = detect_communities_leiden(G)
# elif args.algorithm.lower() == "girvan_newman":
#     detected_communities = detect_communities_girvan_newman(G)
# else:
#     detected_communities = detect_communities_louvain(G)
#
# save_communities_to_file(detected_communities, community_file_path)
# import os
# import networkx as nx
# import community as community_louvain
# import random
# import numpy as np
# import argparse
# import leidenalg as la
# import igraph as ig
#
# from sklearn.metrics.cluster import normalized_mutual_info_score
#
# random_seed = 42
# random.seed(random_seed)
# np.random.seed(random_seed)
#
# # Reading the Network Data
# def load_network(file_path):
#     G = nx.Graph()
#     with open(file_path, 'r') as f:
#         for line in f:
#             parts = line.strip().split()
#             if len(parts) == 2:
#                 G.add_edge(int(parts[0]), int(parts[1]))
#     return G
#
# # Applying the Louvain Algorithm
# def detect_communities_louvain(G):
#     partition = community_louvain.best_partition(G)
#     # Convert partition dictionary to list of lists for NMI calculation
#     community_to_nodes = {}
#     for node, community in partition.items():
#         if community not in community_to_nodes:
#             community_to_nodes[community] = []
#         community_to_nodes[community].append(node)
#     return list(community_to_nodes.values())
#
# # Applying the Leiden Algorithm
# def detect_communities_leiden(G):
#     # Relabel nodes to have consecutive integers starting from 0
#     mapping = {node: idx for idx, node in enumerate(G.nodes())}
#     G = nx.relabel_nodes(G, mapping)
#
#     # Convert NetworkX graph to igraph and preserve node IDs
#     ig_graph = ig.Graph(directed=False)
#     ig_graph.add_vertices(list(G.nodes()))
#     ig_graph.add_edges(list(G.edges()))
#
#     partition = la.find_partition(ig_graph, la.ModularityVertexPartition)
#
#     # Convert the partition to a list of lists for consistency with Louvain function
#     community_to_nodes = {}
#     for node, community in zip(ig_graph.vs["name"], partition.membership):
#         if community not in community_to_nodes:
#             community_to_nodes[community] = []
#         community_to_nodes[community].append(int(node))  # Node IDs are strings in igraph
#
#     # Revert mapping to original node IDs
#     reverse_mapping = {idx: node for node, idx in mapping.items()}
#     communities = [[reverse_mapping[node] for node in community] for community in community_to_nodes.values()]
#
#     return communities
#
# # Applying the Girvan-Newman Algorithm
# def detect_communities_girvan_newman(G):
#     communities_generator = nx.community.girvan_newman(G)
#     top_level_communities = next(communities_generator)
#     next_level_communities = next(communities_generator)
#     # Select the next level communities
#     communities = sorted(map(sorted, next_level_communities))
#     return communities
#
# # Applying the Label Propagation Algorithm
# def detect_communities_label_propagation(G):
#     communities = list(nx.community.label_propagation_communities(G))
#     return [list(community) for community in communities]
#
# # Step 5: Save the result
# def save_communities_to_file(communities, file_path):
#     # Create output directory if it doesn't exist
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#
#     # Convert the list of lists into a dictionary with community as key and nodes as values
#     community_dict = {}
#     for community_id, nodes in enumerate(communities):
#         for node in nodes:
#             community_dict[node] = community_id
#
#     # Sort the dictionary by community key (which are the node numbers here)
#     sorted_community_items = sorted(community_dict.items())
#
#     # Write to file, now ensuring nodes are listed in the sorted order of their community keys
#     with open(file_path, 'w') as f:
#         for node, community_id in sorted_community_items:
#             f.write(f"{node} {community_id}\n")
#
# # Load the data
# parser = argparse.ArgumentParser(description='Detect communities in a network.')
# parser.add_argument('--networkFile', '-n', type=str, help='The path of the network file.',
#                     default="./dataset/TC1-1/network.txt")
# parser.add_argument('--algorithm', '-a', type=str, help='The community detection algorithm to use (louvain, leiden, girvan_newman, or label_propagation).',
#                     default="louvain")
# args = parser.parse_args()
#
# # Extract data name from the file path
# data_name = os.path.basename(os.path.dirname(args.networkFile))
#
# if args.algorithm.lower() == "leiden":
#     community_file_path = f"./leiden/{data_name}.cmty"
# elif args.algorithm.lower() == "girvan_newman":
#     community_file_path = f"./girvan_newman/{data_name}.cmty"
# elif args.algorithm.lower() == "label_propagation":
#     community_file_path = f"./label_propagation/{data_name}.cmty"
# else:
#     community_file_path = f"./louvain/{data_name}.cmty"
#
# G = load_network(args.networkFile)
#
# # Detect communities using the specified method
# if args.algorithm.lower() == "leiden":
#     detected_communities = detect_communities_leiden(G)
# elif args.algorithm.lower() == "girvan_newman":
#     detected_communities = detect_communities_girvan_newman(G)
# elif args.algorithm.lower() == "label_propagation":
#     detected_communities = detect_communities_label_propagation(G)
# else:
#     detected_communities = detect_communities_louvain(G)
#
# save_communities_to_file(detected_communities, community_file_path)
import os
import networkx as nx
import community as community_louvain
import random
import numpy as np
import argparse
import leidenalg as la
import igraph as ig
from infomap import Infomap

from sklearn.metrics.cluster import normalized_mutual_info_score

random_seed = 42
random.seed(random_seed)
np.random.seed(random_seed)

# Reading the Network Data
def load_network(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                G.add_edge(int(parts[0]), int(parts[1]))
    return G

# Applying the Louvain Algorithm
def detect_communities_louvain(G):
    partition = community_louvain.best_partition(G)
    # Convert partition dictionary to list of lists for NMI calculation
    community_to_nodes = {}
    for node, community in partition.items():
        if community not in community_to_nodes:
            community_to_nodes[community] = []
        community_to_nodes[community].append(node)
    return list(community_to_nodes.values())

# Applying the Leiden Algorithm
def detect_communities_leiden(G):
    # Relabel nodes to have consecutive integers starting from 0
    mapping = {node: idx for idx, node in enumerate(G.nodes())}
    G = nx.relabel_nodes(G, mapping)

    # Convert NetworkX graph to igraph and preserve node IDs
    ig_graph = ig.Graph(directed=False)
    ig_graph.add_vertices(list(G.nodes()))
    ig_graph.add_edges(list(G.edges()))

    partition = la.find_partition(ig_graph, la.ModularityVertexPartition)

    # Convert the partition to a list of lists for consistency with Louvain function
    community_to_nodes = {}
    for node, community in zip(ig_graph.vs["name"], partition.membership):
        if community not in community_to_nodes:
            community_to_nodes[community] = []
        community_to_nodes[community].append(int(node))  # Node IDs are strings in igraph

    # Revert mapping to original node IDs
    reverse_mapping = {idx: node for node, idx in mapping.items()}
    communities = [[reverse_mapping[node] for node in community] for community in community_to_nodes.values()]

    return communities

# Applying the Girvan-Newman Algorithm
def detect_communities_girvan_newman(G):
    communities_generator = nx.community.girvan_newman(G)
    top_level_communities = next(communities_generator)
    next_level_communities = next(communities_generator)
    # Select the next level communities
    communities = sorted(map(sorted, next_level_communities))
    return communities

# Applying the Label Propagation Algorithm
def detect_communities_label_propagation(G):
    communities = list(nx.community.label_propagation_communities(G))
    return [list(community) for community in communities]

# Step 5: Save the result
def save_communities_to_file(communities, file_path):
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Convert the list of lists into a dictionary with community as key and nodes as values
    community_dict = {}
    for community_id, nodes in enumerate(communities):
        for node in nodes:
            community_dict[node] = community_id

    # Sort the dictionary by community key (which are the node numbers here)
    sorted_community_items = sorted(community_dict.items())

    # Write to file, now ensuring nodes are listed in the sorted order of their community keys
    with open(file_path, 'w') as f:
        for node, community_id in sorted_community_items:
            f.write(f"{node} {community_id}\n")

# Load the data
parser = argparse.ArgumentParser(description='Detect communities in a network.')
parser.add_argument('--networkFile', '-n', type=str, help='The path of the network file.',
                    default="./dataset/TC1-1/network.txt")
parser.add_argument('--algorithm', '-a', type=str, help='The community detection algorithm to use (louvain, leiden, girvan_newman, label_propagation, or infomap).',
                    default="louvain")
args = parser.parse_args()

# Extract data name from the file path
data_name = os.path.basename(os.path.dirname(args.networkFile))

if args.algorithm.lower() == "leiden":
    community_file_path = f"./leiden/{data_name}.cmty"
elif args.algorithm.lower() == "girvan_newman":
    community_file_path = f"./girvan_newman/{data_name}.cmty"
elif args.algorithm.lower() == "label_propagation":
    community_file_path = f"./label_propagation/{data_name}.cmty"
elif args.algorithm.lower() == "infomap":
    community_file_path = f"./infomap/{data_name}.cmty"
else:
    community_file_path = f"./louvain/{data_name}.cmty"

G = load_network(args.networkFile)

# Detect communities using the specified method
if args.algorithm.lower() == "leiden":
    detected_communities = detect_communities_leiden(G)
elif args.algorithm.lower() == "girvan_newman":
    detected_communities = detect_communities_girvan_newman(G)
elif args.algorithm.lower() == "label_propagation":
    detected_communities = detect_communities_label_propagation(G)
else:
    detected_communities = detect_communities_louvain(G)

save_communities_to_file(detected_communities, community_file_path)
