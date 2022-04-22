for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    seen = set()
    ans = []
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            ans.append(arr[i])

    print(*ans)

