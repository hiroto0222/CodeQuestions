def main():
    # K people per ride
    # N people waiting in queue
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    rest = K
    res = 0
    for val in A:
        if val > rest:
            res += 1
            rest = K
        res -= val
    res += 1

    return res


if __name__ == "__main__":
    print(main())
