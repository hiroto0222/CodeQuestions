N = int(input())
print("{}".format(0 if N % 1000 == 0 else 1000 - N % 1000))
