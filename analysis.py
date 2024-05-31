import networkx as nx

def analyze_graph(file_path):
    # 그래프 생성
    G = nx.Graph()

    # 파일에서 엣지 읽기
    with open(file_path, 'r') as file:
        for line in file:
            node1, node2 = map(int, line.strip().split())
            G.add_edge(node1, node2)

    # 그래프가 연결되어 있는지 확인
    is_connected = nx.is_connected(G)
    connection_status = "Connected" if is_connected else "Disconnected"

    # isolated 노드 확인
    isolated_nodes = list(nx.isolates(G))
    has_isolated_nodes = len(isolated_nodes) > 0
    isolated_status = "Has isolated nodes" if has_isolated_nodes else "No isolated nodes"

    # 3-truss 구성요소 확인
    def has_k_truss(G, k):
        # connect = nx.connected_components(G)
        components = list(nx.connected_components(G))
        for comp in components:
            sub = G.subgraph(comp)
            truss = nx.k_truss(sub, k)
            if truss.number_of_nodes() == 0:
                return True
        # 하위 그래프에서 k-truss를 찾기 위한 함수
        return False

    truss_status = "Has components not forming a 3-truss" if has_k_truss(G, 3) else "All components form a 3-truss"

    return {
        "connection_status": connection_status,
        "isolated_status": isolated_status,
        "truss_status": truss_status,
        "isolated_nodes": isolated_nodes
    }

# 사용 예시
file_path = './dataset/real/dolphin/network.txt'
result = analyze_graph(file_path)
print(f"Graph Connection Status: {result['connection_status']}")
print(f"Isolated Node Status: {result['isolated_status']}")
print(f"Truss Status: {result['truss_status']}")
if result['isolated_nodes']:
    print(f"Isolated Nodes: {result['isolated_nodes']}")
