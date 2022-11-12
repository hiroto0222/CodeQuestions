# "0 xj" add xj to all even elements
# "1 xj" add xj to all odd elements

# odd + odd = even
# even + odd = odd

for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    even_sum, even_cnt = 0, 0
    odd_sum, odd_cnt = 0, 0

    for val in a:
        if val % 2 == 0:
            even_sum += val
            even_cnt += 1
        else:
            odd_sum += val
            odd_cnt += 1
    
    for _ in range(q):
        qtype, x = map(int, input().split())
        
        if qtype == 0:
            if x % 2 == 0:
                even_sum += even_cnt * x
            else:
                even_sum += even_cnt * x
                odd_sum += even_sum
                odd_cnt += even_cnt
                even_sum, even_cnt = 0, 0
        else:
            if x % 2 == 0:
                odd_sum += odd_cnt * x
            else:
                odd_sum += odd_cnt * x
                even_sum += odd_sum
                even_cnt += odd_cnt
                odd_sum, odd_cnt = 0, 0

        print(even_sum + odd_sum)