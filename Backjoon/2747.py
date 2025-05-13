n = int(input())

graph = [[] for _ in range(104)]
visited = [0] * 104

def dfs(n):
    visited[n] = 1
    for i in graph[n]:
        if visited[i] == 0:  # ✅ 연결된 노드 i가 방문되지 않았을 때
            dfs(i)
    print(f"{n}로부터 시작된 함수가 종료되었습니다.")  # 괄호 없이 변수 값 출력

graph[1].append(2)
graph[1].append(3)
graph[2].append(4)
graph[2].append(5)

dfs(1)
