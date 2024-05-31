# import argparse
# import os
# import matplotlib.pyplot as plt
# import numpy as np
# from collections import Counter
#
#
# def read_purity_file(file_path):
#     ids = []
#     purities = []
#     with open(file_path, 'r') as f:
#         for line in f:
#             parts = line.strip().split()
#             if len(parts) == 2:
#                 id_, purity = int(parts[0]), float(parts[1])
#                 ids.append(id_)
#                 purities.append(purity)
#     return ids, purities
#
#
# def read_score_file(file_path):
#     with open(file_path, 'r') as f:
#         for line in f:
#             if line.startswith("NMI score:"):
#                 return float(line.split(":")[1].strip())
#             elif line.startswith("F1 score:"):
#                 return float(line.split(":")[1].strip())
#     return None
#
#
# def read_num_community_file(file_path):
#     data_names = []
#     ground_truth = []
#     ours = []
#     louvain = []
#     leiden = []
#
#     with open(file_path, 'r') as f:
#         lines = f.readlines()
#         i = 0
#         while i < len(lines):
#             if lines[i].strip():
#                 data_names.append(lines[i].strip())
#                 ground_truth.append(int(lines[i + 1].split(":")[1].strip()))
#                 ours.append(int(lines[i + 2].split(":")[1].strip()))
#                 louvain.append(int(lines[i + 3].split(":")[1].strip()))
#                 leiden.append(int(lines[i + 4].split(":")[1].strip()))
#                 i += 5
#             else:
#                 i += 1
#
#     return data_names, ground_truth, ours, louvain, leiden
#
#
# def read_community_file(file_path):
#     community_sizes = Counter()
#     with open(file_path, 'r') as f:
#         for line in f:
#             parts = line.strip().split()
#             if len(parts) == 2:
#                 _, community_id = int(parts[0]), int(parts[1])
#                 community_sizes[community_id] += 1
#     return community_sizes
#
#
# def plot_purity(ids_list, purities_list, labels, output_path, title, xlabel, markers):
#     plt.figure(figsize=(7, 3))
#     for ids, purities, label, marker in zip(ids_list, purities_list, labels, markers):
#         plt.scatter(ids, purities, marker=marker, label=label, alpha=0.8)
#     plt.xlabel(xlabel, fontsize=14)
#     plt.ylabel('Purity', fontsize=14)
#     plt.title(title, fontsize=16)
#     plt.ylim(0, 1.1)
#     plt.grid(True)
#     plt.legend(fontsize=12)
#     plt.tight_layout()
#
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)
#     plt.savefig(output_path)
#     plt.close()
#
#
# def plot_scores(data_names, algorithm_names, scores, output_path, title, ylabel, wide=False, show_xlabel=True):
#     x = np.arange(len(data_names))
#     width = 0.8 / len(algorithm_names)  # 막대의 너비를 자동으로 조정하여 더 많은 알고리즘을 지원
#
#     plt.figure(figsize=(14, 3) if wide else (7, 3))
#     for i, algorithm in enumerate(algorithm_names):
#         plt.bar(x + i * width - (0.4 - width / 2), scores[i], width, label=algorithm)
#
#     if show_xlabel:
#         plt.xlabel('Data', fontsize=14)
#     plt.ylabel(ylabel, fontsize=14)
#     plt.title(title, fontsize=16)
#     plt.xticks(x, data_names, fontsize=12, rotation=45, ha="right")
#     plt.legend(fontsize=12, loc='lower right')  # legend 위치 조정
#     plt.tight_layout()
#
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)
#     plt.savefig(output_path)
#     plt.close()
#
#
# def plot_num_community(data_names, ground_truth, ours, louvain, leiden, output_path, title, show_xlabel=True):
#     x = np.arange(len(data_names))
#     algorithms = ['Louvain', 'Leiden', 'Ours', 'Ground_truth']
#     width = 0.15  # 막대의 너비를 고정
#
#     plt.figure(figsize=(7, 3))
#     plt.bar(x - 1.5 * width, louvain, width, label='Louvain')
#     plt.bar(x - 0.5 * width, leiden, width, label='Leiden')
#     plt.bar(x + 0.5 * width, ours, width, label='Ours')
#     plt.bar(x + 1.5 * width, ground_truth, width, label='Ground_truth')
#
#     if show_xlabel:
#         plt.xlabel('Data', fontsize=14)
#     plt.ylabel('Number of Communities', fontsize=14)
#     plt.title(title, fontsize=16)
#     plt.xticks(x, data_names, fontsize=12, rotation=0, ha="right")
#     plt.legend(fontsize=12, loc='upper right')
#     plt.tight_layout()
#
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)
#     plt.savefig(output_path)
#     plt.close()
#
#
# def plot_community_distribution(data, algorithm_names, output_path):
#     plt.figure(figsize=(7, 3))
#     markers = ['o', 's', '*', 'D', 'v', '<', '>', 'p', '^', 'h']  # 다른 아이콘 리스트
#     colors = ['r', 'g', 'b', 'y', 'm', 'c', 'k']  # 다른 색상 리스트
#     marker_index = 0
#
#     groundtruth_path = f"./groundtruth/{data}/{data}.cmty"
#     groundtruth_sizes = read_community_file(groundtruth_path)
#     groundtruth_size_counts = Counter(groundtruth_sizes.values())
#     groundtruth_x, groundtruth_y = zip(*sorted(groundtruth_size_counts.items()))
#     plt.plot(groundtruth_x, groundtruth_y, label=f'Groundtruth', linestyle='-', marker=markers[marker_index],
#              color=colors[marker_index], alpha=0.7, markersize=5)
#     marker_index += 1
#
#     for algorithm in algorithm_names:
#         if algorithm == 'louvain':
#             algorithm_path = f"./louvain/{data}.cmty"
#         elif algorithm == 'ours':
#             algorithm_path = f"./output/{data}/{data}.cmty"
#         elif algorithm == 'leiden':
#             algorithm_path = f"./leiden/{data}.cmty"
#         elif algorithm == 'label_propagation':
#             algorithm_path = f"./label_propagation/{data}.cmty"
#         else:
#             continue
#
#         algorithm_sizes = read_community_file(algorithm_path)
#         algorithm_size_counts = Counter(algorithm_sizes.values())
#         algorithm_x, algorithm_y = zip(*sorted(algorithm_size_counts.items()))
#         plt.plot(algorithm_x, algorithm_y, label=f'{algorithm.capitalize()}', linestyle='-',
#                  marker=markers[marker_index], color=colors[marker_index], alpha=0.7, markersize=5)
#         marker_index += 1
#
#     plt.xlabel('Community Size', fontsize=14)
#     plt.ylabel('Number of Communities', fontsize=14)
#     plt.title(f'Community Size Distribution for {data}', fontsize=16)
#     plt.grid(True)
#     plt.legend(fontsize=12)
#     plt.tight_layout()
#
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)
#     plt.savefig(output_path)
#     plt.close()
#     print(f'Plot saved to {output_path}')
#
#
# def plot_scalability(data_names, runtimes, output_path):
#     x_labels = [10000, 20000, 40000, 80000, 160000]
#     x = np.arange(len(x_labels))
#
#     plt.figure(figsize=(7, 3))
#     plt.plot(x, runtimes, marker='o', linestyle='-', color='b', alpha=0.7)
#
#     plt.xlabel('Data Size', fontsize=14)
#     plt.ylabel('Runtime (seconds)', fontsize=14)
#     plt.title('Scalability Plot', fontsize=16)
#     plt.xticks(x, x_labels, fontsize=12)
#     plt.grid(True)
#     plt.tight_layout()
#
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)
#     plt.savefig(output_path)
#     plt.close()
#     print(f'Plot saved to {output_path}')
#
#
# def main(args):
#     if args.mode == 'seed':
#         data_names = args.data.split('#')
#         ids_list = []
#         purities_list = []
#         markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h']  # 다른 아이콘 리스트
#         for i, data in enumerate(data_names):
#             file_path = f"./output/seed/{data}_seed_purity.txt"
#             ids, purities = read_purity_file(file_path)
#             ids_list.append(ids)
#             purities_list.append(purities)
#         output_dir = "./draw/seed/"
#         output_path = os.path.join(output_dir, "seed_comparison.pdf")
#         plot_purity(ids_list, purities_list, data_names, output_path, 'Seed Purity Plot', 'Seed ID',
#                     markers[:len(data_names)])
#         print(f'Plot saved to {output_path}')
#
#     elif args.mode == 'community_purity':
#         data_names = args.data.split('#')
#         algorithm_names = args.algorithm.split('#')
#         ids_list = []
#         purities_list = []
#         labels = []
#         markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h']  # 다른 아이콘 리스트
#         algorithm_marker_map = {algorithm: markers[i % len(markers)] for i, algorithm in enumerate(algorithm_names)}
#
#         for algorithm in algorithm_names:
#             marker = algorithm_marker_map[algorithm]
#             for data in data_names:
#                 file_path = f"./output/purity/{algorithm}/{data}_purity.txt"
#                 ids, purities = read_purity_file(file_path)
#                 ids_list.append(ids)
#                 purities_list.append(purities)
#                 labels.append(f"{algorithm} - {data}")
#         output_dir = "./draw/community_purity/"
#         output_path = os.path.join(output_dir, "community_purity_comparison.pdf")
#         plot_purity(ids_list, purities_list, labels, output_path, 'Community Purity Plot', 'Community ID',
#                     [algorithm_marker_map[algorithm] for algorithm in algorithm_names for _ in data_names])
#         print(f'Plot saved to {output_path}')
#
#     elif args.mode in ['nmi', 'f1']:
#         data_names = args.data.split('#')
#         algorithm_names = args.algorithm.split('#')
#         scores = []
#
#         for algorithm in algorithm_names:
#             algorithm_scores = []
#             for data in data_names:
#                 score_file_path = f"./output/{args.mode.upper()}/{algorithm}/{data}_{args.mode.upper()}.txt"
#                 score = read_score_file(score_file_path)
#                 if score is None:
#                     raise FileNotFoundError(f"Score file not found: {score_file_path}")
#                 algorithm_scores.append(score)
#             scores.append(algorithm_scores)
#
#         output_dir = f"./draw/{args.mode.upper()}/"
#         output_path = os.path.join(output_dir, f"{args.mode.upper()}_comparison.pdf")
#         plot_scores(data_names, algorithm_names, scores, output_path, f'{args.mode.upper()} Score Comparison',
#                     f'{args.mode.upper()} Score')
#
#         print(f'Plot saved to {output_path}')
#
#     elif args.mode in ['nmilong', 'f1long']:
#         data_names = [
#             "TC1-1", "TC1-2", "TC1-3", "TC1-4", "TC1-5",
#             "TC1-6", "TC1-7", "TC1-8", "TC1-9", "TC1-10",
#             "dolphin", "football", "karate", "mexican", "polbooks",
#             "railway", "strike"
#         ]
#         algorithm_names = args.algorithm.split('#')
#         scores = []
#
#         for algorithm in algorithm_names:
#             algorithm_scores = []
#             for data in data_names:
#                 score_file_path = f"./output/{args.mode[:-4].upper()}/{algorithm}/{data}_{args.mode[:-4].upper()}.txt"
#                 score = read_score_file(score_file_path)
#                 if score is None:
#                     raise FileNotFoundError(f"Score file not found: {score_file_path}")
#                 algorithm_scores.append(score)
#             scores.append(algorithm_scores)
#
#         output_dir = f"./draw/{args.mode.upper()}/"
#         output_path = os.path.join(output_dir, f"{args.mode.upper()}_comparison.pdf")
#         plot_scores(data_names, algorithm_names, scores, output_path, f'{args.mode[:-4].upper()} Score Comparison',
#                     f'{args.mode[:-4].upper()} Score', wide=True, show_xlabel=False)  # show_xlabel=False로 설정
#
#         print(f'Plot saved to {output_path}')
#
#     elif args.mode == 'num_community':
#         data_names, ground_truth, ours, louvain, leiden = read_num_community_file('./num_of_community.txt')
#         selected_data = args.data.split('#')
#
#         tc_data = [data for data in selected_data if data.startswith('TC')]
#         other_data = [data for data in selected_data if not data.startswith('TC')]
#
#         def select_indices(data_list):
#             return [data_names.index(data) for data in data_list]
#
#         def select_data(indices):
#             return (
#                 [data_names[i] for i in indices],
#                 [ground_truth[i] for i in indices],
#                 [ours[i] for i in indices],
#                 [louvain[i] for i in indices],
#                 [leiden[i] for i in indices]
#             )
#
#         if tc_data:
#             tc_indices = select_indices(tc_data)
#             tc_selected_data = select_data(tc_indices)
#             output_path_tc = "./draw/num_community/num_community_tc_comparison.pdf"
#             plot_num_community(*tc_selected_data, output_path_tc, title='Number of Communities', show_xlabel=False)
#             print(f'TC Plot saved to {output_path_tc}')
#
#         if other_data:
#             other_indices = select_indices(other_data)
#             other_selected_data = select_data(other_indices)
#             output_path_other = "./draw/num_community/num_community_other_comparison.pdf"
#             plot_num_community(*other_selected_data, output_path_other, title='Number of Communities', show_xlabel=False)
#             print(f'Other Plot saved to {output_path_other}')
#
#     elif args.mode == 'distribution':
#         data_name = args.data  # 하나의 데이터만 받음
#         algorithm_names = args.algorithm.split('#')
#         output_dir = "./draw/distribution/"
#         output_path = os.path.join(output_dir, f"{data_name}_community_size_distribution.pdf")
#         plot_community_distribution(data_name, algorithm_names, output_path)
#
#     elif args.mode == 'scalability':
#         data_names = args.data.split('#')
#         runtimes = []
#         for data in data_names:
#             runtime_file_path = f"./output/{data}/runtime.txt"
#             with open(runtime_file_path, 'r') as f:
#                 for line in f:
#                     if line.startswith("Run time:"):
#                         runtimes.append(float(line.split(" ")[2]))
#                         break
#
#         output_dir = "./draw/scalability/"
#         output_path = os.path.join(output_dir, "scalability.pdf")
#         plot_scalability(data_names, runtimes, output_path)
#
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Plot purity and evaluation scores from given files.')
#     parser.add_argument('--mode', type=str, required=True,
#                         choices=['seed', 'community_purity', 'nmi', 'f1', 'num_community', 'distribution', 'scalability', 'nmilong', 'f1long'],
#                         help='Mode of operation.')
#     parser.add_argument('--file', type=str,
#                         help='Path to the purity file (required for seed and community_purity modes).')
#     parser.add_argument('--data', type=str, help='Dataset name (required for all modes except num_community).')
#     parser.add_argument('--algorithm', type=str,
#                         help='Algorithm names separated by # (required for community_purity, nmi, f1, distribution, nmilong, and f1long modes).')
#
#     args = parser.parse_args()
#
#     main(args)
import argparse
import os
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def read_purity_file(file_path):
    ids = []
    purities = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                id_, purity = int(parts[0]), float(parts[1])
                ids.append(id_)
                purities.append(purity)
    return ids, purities


def read_score_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("NMI score:"):
                return float(line.split(":")[1].strip())
            elif line.startswith("F1 score:"):
                return float(line.split(":")[1].strip())
    return None


def read_num_community_file(file_path):
    data_names = []
    ground_truth = []
    ours = []
    louvain = []
    leiden = []

    with open(file_path, 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            if lines[i].strip():
                data_names.append(lines[i].strip())
                ground_truth.append(int(lines[i + 1].split(":")[1].strip()))
                ours.append(int(lines[i + 2].split(":")[1].strip()))
                louvain.append(int(lines[i + 3].split(":")[1].strip()))
                leiden.append(int(lines[i + 4].split(":")[1].strip()))
                i += 5
            else:
                i += 1

    return data_names, ground_truth, ours, louvain, leiden


def read_community_file(file_path):
    community_sizes = Counter()
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                _, community_id = int(parts[0]), int(parts[1])
                community_sizes[community_id] += 1
    return community_sizes


def plot_purity(ids_list, purities_list, labels, output_path, title, xlabel, markers):
    plt.figure(figsize=(7, 3))
    for ids, purities, label, marker in zip(ids_list, purities_list, labels, markers):
        plt.scatter(ids, purities, marker=marker, label=label, alpha=0.8)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel('Purity', fontsize=14)
    plt.title(title, fontsize=16)
    plt.ylim(0, 1.1)
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()


def plot_scores(data_names, algorithm_names, scores, output_path, title, ylabel, wide=False, show_xlabel=True):
    x = np.arange(len(data_names))
    width = 0.8 / len(algorithm_names)  # 막대의 너비를 자동으로 조정하여 더 많은 알고리즘을 지원

    plt.figure(figsize=(14, 3) if wide else (7, 3))
    for i, algorithm in enumerate(algorithm_names):
        plt.bar(x + i * width - (0.4 - width / 2), scores[i], width, label=algorithm)

    if show_xlabel:
        plt.xlabel('Data', fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=16)
    plt.xticks(x, data_names, fontsize=12, rotation=45, ha="right")
    plt.legend(fontsize=12, loc='lower right')  # legend 위치 조정
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()


def plot_num_community(data_names, ground_truth, ours, louvain, leiden, output_path, title, show_xlabel=True):
    x = np.arange(len(data_names))
    algorithms = ['Louvain', 'Leiden', 'Ours', 'Ground_truth']
    width = 0.15  # 막대의 너비를 고정

    plt.figure(figsize=(7, 3))
    plt.bar(x - 1.5 * width, louvain, width, label='Louvain')
    plt.bar(x - 0.5 * width, leiden, width, label='Leiden')
    plt.bar(x + 0.5 * width, ours, width, label='Ours')
    plt.bar(x + 1.5 * width, ground_truth, width, label='Ground_truth')

    if show_xlabel:
        plt.xlabel('Data', fontsize=14)
    plt.ylabel('Number of Communities', fontsize=14)
    plt.title(title, fontsize=16)
    plt.xticks(x, data_names, fontsize=12, rotation=0, ha="right")
    plt.legend(fontsize=12, loc='upper right')
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()


def plot_community_distribution(data, algorithm_names, output_path):
    plt.figure(figsize=(7, 3))
    markers = ['o', 's', '*', 'D', 'v', '<', '>', 'p', '^', 'h']  # 다른 아이콘 리스트
    colors = ['r', 'g', 'b', 'y', 'm', 'c', 'k']  # 다른 색상 리스트
    marker_index = 0

    groundtruth_path = f"./groundtruth/{data}/{data}.cmty"
    groundtruth_sizes = read_community_file(groundtruth_path)
    groundtruth_size_counts = Counter(groundtruth_sizes.values())
    groundtruth_x, groundtruth_y = zip(*sorted(groundtruth_size_counts.items()))
    plt.plot(groundtruth_x, groundtruth_y, label=f'Groundtruth', linestyle='-', marker=markers[marker_index],
             color=colors[marker_index], alpha=0.7, markersize=5)
    marker_index += 1

    for algorithm in algorithm_names:
        if algorithm == 'louvain':
            algorithm_path = f"./louvain/{data}.cmty"
        elif algorithm == 'ours':
            algorithm_path = f"./output/{data}/{data}.cmty"
        elif algorithm == 'leiden':
            algorithm_path = f"./leiden/{data}.cmty"
        elif algorithm == 'label_propagation':
            algorithm_path = f"./label_propagation/{data}.cmty"
        else:
            continue

        algorithm_sizes = read_community_file(algorithm_path)
        algorithm_size_counts = Counter(algorithm_sizes.values())
        algorithm_x, algorithm_y = zip(*sorted(algorithm_size_counts.items()))
        plt.plot(algorithm_x, algorithm_y, label=f'{algorithm.capitalize()}', linestyle='-',
                 marker=markers[marker_index], color=colors[marker_index], alpha=0.7, markersize=5)
        marker_index += 1

    plt.xlabel('Community Size', fontsize=14)
    plt.ylabel('Number of Communities', fontsize=14)
    plt.title(f'Community Size Distribution for {data}', fontsize=16)
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    print(f'Plot saved to {output_path}')


def plot_scalability(data_names, runtimes, output_path):
    x_labels = [10000, 20000, 40000, 80000, 160000]
    x = np.arange(len(x_labels))

    plt.figure(figsize=(7, 3))
    plt.plot(x, runtimes, marker='o', linestyle='-', color='b', alpha=0.7)

    plt.xlabel('Data Size', fontsize=14)
    plt.ylabel('Runtime (seconds)', fontsize=14)
    plt.title('Scalability Plot', fontsize=16)
    plt.xticks(x, x_labels, fontsize=12)
    plt.grid(True)
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    print(f'Plot saved to {output_path}')


def plot_long_scores(data_names, algorithm_names, scores, output_path, title, ylabel, wide=True, show_xlabel=True):
    x = np.arange(len(data_names))
    plt.figure(figsize=(7, 3))
    markers = ['o', 's', 'v', '^', '<', '>', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']

    for i, algorithm in enumerate(algorithm_names):
        plt.plot(x, scores[i], marker=markers[i % len(markers)], label=algorithm, linestyle='-', linewidth=1, markersize=5)

    if show_xlabel:
        plt.xlabel('Data', fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=16)

    formatted_data_names = []
    for name in data_names:
        if name.startswith("TC"):
            parts = name.split("-")
            formatted_data_names.append(f"{parts[0][2:]}-{parts[1]}")
        else:
            formatted_data_names.append(name[0].upper())

    plt.xticks(x, formatted_data_names, fontsize=12, rotation=0, ha="center")
    # plt.legend(fontsize=12, loc='lower right', bbox_to_anchor=(0.85, 0))  # legend 위치 조정
    plt.legend(fontsize=12, loc='lower left')
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()


def main(args):
    if args.mode == 'seed':
        data_names = args.data.split('#')
        ids_list = []
        purities_list = []
        markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h']  # 다른 아이콘 리스트
        for i, data in enumerate(data_names):
            file_path = f"./output/seed/{data}_seed_purity.txt"
            ids, purities = read_purity_file(file_path)
            ids_list.append(ids)
            purities_list.append(purities)
        output_dir = "./draw/seed/"
        output_path = os.path.join(output_dir, "seed_comparison.pdf")
        plot_purity(ids_list, purities_list, data_names, output_path, 'Seed Purity Plot', 'Seed ID',
                    markers[:len(data_names)])
        print(f'Plot saved to {output_path}')

    elif args.mode == 'community_purity':
        data_names = args.data.split('#')
        algorithm_names = args.algorithm.split('#')
        ids_list = []
        purities_list = []
        labels = []
        markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h']  # 다른 아이콘 리스트
        algorithm_marker_map = {algorithm: markers[i % len(markers)] for i, algorithm in enumerate(algorithm_names)}

        for algorithm in algorithm_names:
            marker = algorithm_marker_map[algorithm]
            for data in data_names:
                file_path = f"./output/purity/{algorithm}/{data}_purity.txt"
                ids, purities = read_purity_file(file_path)
                ids_list.append(ids)
                purities_list.append(purities)
                labels.append(f"{algorithm} - {data}")
        output_dir = "./draw/community_purity/"
        output_path = os.path.join(output_dir, "community_purity_comparison.pdf")
        plot_purity(ids_list, purities_list, labels, output_path, 'Community Purity Plot', 'Community ID',
                    [algorithm_marker_map[algorithm] for algorithm in algorithm_names for _ in data_names])
        print(f'Plot saved to {output_path}')

    elif args.mode in ['nmi', 'f1']:
        data_names = args.data.split('#')
        algorithm_names = args.algorithm.split('#')
        scores = []

        for algorithm in algorithm_names:
            algorithm_scores = []
            for data in data_names:
                score_file_path = f"./output/{args.mode.upper()}/{algorithm}/{data}_{args.mode.upper()}.txt"
                score = read_score_file(score_file_path)
                if score is None:
                    raise FileNotFoundError(f"Score file not found: {score_file_path}")
                algorithm_scores.append(score)
            scores.append(algorithm_scores)

        output_dir = f"./draw/{args.mode.upper()}/"
        output_path = os.path.join(output_dir, f"{args.mode.upper()}_comparison.pdf")
        plot_scores(data_names, algorithm_names, scores, output_path, f'{args.mode.upper()} Score Comparison',
                    f'{args.mode.upper()} Score')

        print(f'Plot saved to {output_path}')

    elif args.mode in ['nmilong', 'f1long']:
        data_names = [
            "TC1-1", "TC1-2", "TC1-3", "TC1-4", "TC1-5",
            "TC1-6", "TC1-7", "TC1-8", "TC1-9", "TC1-10",
            "dolphin", "football", "karate", "mexican", "polbooks",
            "railway", "strike"
        ]
        algorithm_names = args.algorithm.split('#')
        scores = []

        for algorithm in algorithm_names:
            algorithm_scores = []
            for data in data_names:
                score_file_path = f"./output/{args.mode[:-4].upper()}/{algorithm}/{data}_{args.mode[:-4].upper()}.txt"
                score = read_score_file(score_file_path)
                if score is None:
                    raise FileNotFoundError(f"Score file not found: {score_file_path}")
                algorithm_scores.append(score)
            scores.append(algorithm_scores)

        output_dir = f"./draw/{args.mode.upper()}/"
        output_path = os.path.join(output_dir, f"{args.mode.upper()}_comparison.pdf")
        plot_long_scores(data_names, algorithm_names, scores, output_path, f'{args.mode[:-4].upper()} Score Comparison',
                         f'{args.mode[:-4].upper()} Score', wide=True, show_xlabel=False)  # show_xlabel=False로 설정

        print(f'Plot saved to {output_path}')

    elif args.mode == 'num_community':
        data_names, ground_truth, ours, louvain, leiden = read_num_community_file('./num_of_community.txt')
        selected_data = args.data.split('#')

        tc_data = [data for data in selected_data if data.startswith('TC')]
        other_data = [data for data in selected_data if not data.startswith('TC')]

        def select_indices(data_list):
            return [data_names.index(data) for data in data_list]

        def select_data(indices):
            return (
                [data_names[i] for i in indices],
                [ground_truth[i] for i in indices],
                [ours[i] for i in indices],
                [louvain[i] for i in indices],
                [leiden[i] for i in indices]
            )

        if tc_data:
            tc_indices = select_indices(tc_data)
            tc_selected_data = select_data(tc_indices)
            output_path_tc = "./draw/num_community/num_community_tc_comparison.pdf"
            plot_num_community(*tc_selected_data, output_path_tc, title='Number of Communities', show_xlabel=False)
            print(f'TC Plot saved to {output_path_tc}')

        if other_data:
            other_indices = select_indices(other_data)
            other_selected_data = select_data(other_indices)
            output_path_other = "./draw/num_community/num_community_other_comparison.pdf"
            plot_num_community(*other_selected_data, output_path_other, title='Number of Communities', show_xlabel=False)
            print(f'Other Plot saved to {output_path_other}')

    elif args.mode == 'distribution':
        data_name = args.data  # 하나의 데이터만 받음
        algorithm_names = args.algorithm.split('#')
        output_dir = "./draw/distribution/"
        output_path = os.path.join(output_dir, f"{data_name}_community_size_distribution.pdf")
        plot_community_distribution(data_name, algorithm_names, output_path)

    elif args.mode == 'scalability':
        data_names = args.data.split('#')
        runtimes = []
        for data in data_names:
            runtime_file_path = f"./output/{data}/runtime.txt"
            with open(runtime_file_path, 'r') as f:
                for line in f:
                    if line.startswith("Run time:"):
                        runtimes.append(float(line.split(" ")[2]))
                        break

        output_dir = "./draw/scalability/"
        output_path = os.path.join(output_dir, "scalability.pdf")
        plot_scalability(data_names, runtimes, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot purity and evaluation scores from given files.')
    parser.add_argument('--mode', type=str, required=True,
                        choices=['seed', 'community_purity', 'nmi', 'f1', 'num_community', 'distribution', 'scalability', 'nmilong', 'f1long'],
                        help='Mode of operation.')
    parser.add_argument('--file', type=str,
                        help='Path to the purity file (required for seed and community_purity modes).')
    parser.add_argument('--data', type=str, help='Dataset name (required for all modes except num_community).')
    parser.add_argument('--algorithm', type=str,
                        help='Algorithm names separated by # (required for community_purity, nmi, f1, distribution, nmilong, and f1long modes).')

    args = parser.parse_args()

    main(args)
