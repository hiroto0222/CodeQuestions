N, X = map(int, input().split())
balls = []
for _ in range(N):
    balls.append(list(map(int, input().split()))[1:])

stack = [X]
temp = []
for i in range(N):
    while stack:
        currVal = stack.pop(0)
        for j in range(len(balls[i])):
            if (currVal % balls[i][j] == 0):
                temp.append(currVal // balls[i][j])
        
    stack = temp
    temp = []

print(stack.count(1))