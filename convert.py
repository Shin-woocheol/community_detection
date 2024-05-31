def process_communities(input_file_path, output_file_path):
    community_id = 1
    node_community_list = []

    # 파일 읽기
    with open(input_file_path, 'r') as file:
        for line in file:
            nodes = list(map(int, line.strip().split()))
            nodes.sort()
            for node in nodes:
                node_community_list.append((node, community_id))
            community_id += 1

    # node id 기준으로 정렬
    node_community_list.sort()

    # 결과 파일 저장
    with open(output_file_path, 'w') as file:
        for node, community in node_community_list:
            file.write(f"{node} {community}\n")

# 사용 예시
input_file_path = './groundtruth/coauthorship/old_coauthorship.cmty'
output_file_path = './groundtruth/coauthorship/coauthorship1.cmty'
process_communities(input_file_path, output_file_path)
