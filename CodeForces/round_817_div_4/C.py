def main():
    n = int(input())
    p1 = set(list(input().split()))
    p2 = set(list(input().split()))
    p3 = set(list(input().split()))
    total_words = set().union(p1, p2, p3)
    ans = [0, 0, 0]

    for word in total_words:
        print(word)
        if word in p1 and word in p2 and word in p3:
            continue
            
        if word in p1:
            ans[0] += 1
            if word in p2:
                ans[1] += 1
            elif word in p3:
                ans[2] += 1
            else:
                ans[0] += 2
        
        elif word in p2:
            ans[1] += 1
            if word in p1:
                ans[0] += 1
            elif word in p3:
                ans[2] += 1
            else:
                ans[1] += 2
        
        elif word in p3:
            ans[2] += 1
            if word in p1:
                ans[0] += 1
            elif word in p2:
                ans[1] += 1
            else:
                ans[2] += 2
    
    print(*ans)



for _ in range(int(input())):
    main()