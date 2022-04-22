from collections import deque

def main():
    def make_start():
        """9 is open space"""
        start = ["9"] * 9
        for piece, v in enumerate(P, 1):
            start[v] = str(piece)
        return start
    
    def bfs(start):
        def to_str(state):
            return "".join(state)
        
        goal = [str(i + 1) for i in range(9)]
        seen = set()
        que = deque()
        que.append((start, 0))

        while que:
            state, d = que.popleft()

            if state == goal:
                return d
            
            u_empty = state.index("9")
            for v in G[u_empty]:
                curr_state = state[:]
                curr_state[u_empty], curr_state[v] = curr_state[v], curr_state[u_empty]
                curr_state_str = to_str(curr_state)
                if curr_state_str not in seen:
                    seen.add(curr_state_str)
                    que.append((curr_state, d + 1))
        
        return -1

    """
    コマは1-8の8種類、頂点は-1して、0-8の9頂点とします
    コマが置かれていない「空の頂点」には、コマ9が置かれていることにします
    マスの状態は、『頂点i』に『コマj』が置いてある、というリストで管理します
    """
    
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u, v = (x - 1 for x in map(int, input().split()))
        G[u].append(v)
        G[v].append(u)
    
    P = [x - 1 for x in map(int, input().split())]
    start = make_start()
    print(bfs(start))


if __name__ == "__main__":
    main()