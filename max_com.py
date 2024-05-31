def get_max_community_id(file_path):
    max_community_id = 0

    with open(file_path, 'r') as file:
        for line in file:
            _, community_id = line.strip().split()
            community_id = int(community_id)
            if community_id > max_community_id:
                max_community_id = community_id

    return max_community_id


# 사용 예시
# file_path = './groundtruth/TC1-10/TC1-10.cmty'
# file_path = './leiden/livejounal.cmty'
file_path = './louvain/livejounal.cmty'
# file_path = 'dataset/real/railway/railway.cmty'
print(f"The maximum community ID is: {get_max_community_id(file_path)}")
