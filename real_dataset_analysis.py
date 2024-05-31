import os


def analyze_community_data(base_path='./dataset/real/'):
    result = []
    folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f)) and f != 'find']

    for folder in folders:
        folder_path = os.path.join(base_path, folder)

        # Initialize variables for each folder
        node_count = set()
        edge_count = 0
        community_count = set()

        # Process {foldername}.cmty file
        cmty_file = os.path.join(folder_path, f'{folder}.cmty')
        with open(cmty_file, 'r') as f:
            for line in f:
                node_id, community_id = map(int, line.strip().split())
                node_count.add(node_id)
                community_count.add(community_id)

        # Process network.txt file
        network_file = os.path.join(folder_path, 'network.txt')
        with open(network_file, 'r') as f:
            for line in f:
                node1, node2 = map(int, line.strip().split())
                edge_count += 1
                node_count.update([node1, node2])

        # Collect results for the current folder
        result.append({
            'folder': folder,
            'node_count': len(node_count),
            'edge_count': edge_count,
            'community_count': len(community_count)
        })

    # Write results to community_analysis.txt
    with open('community_analysis.txt', 'w') as f:
        for res in result:
            f.write(f"{res['folder']}:\n")
            f.write(f"  Node count: {res['node_count']}\n")
            f.write(f"  Edge count: {res['edge_count']}\n")
            f.write(f"  Community count: {res['community_count']}\n")
            f.write('\n')


# Run the function
analyze_community_data()
