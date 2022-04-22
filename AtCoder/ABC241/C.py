N = int(input())
S = [input() for _ in range(N)]

def main():
    # check rows
    for row in S:
        hashtags = 0
        left = 0
        for right, val in enumerate(row):
            if val == "#": 
                hashtags += 1
            if (right - left == 5):
                if hashtags == 6 or hashtags == 4:
                    return True
                if row[left] == "#":
                    hashtags -= 1
                left += 1
    
    # check cols
    for col in range(N):
        hashtags = 0
        top_row = 0
        for bot_row in range(N):
            if S[bot_row][col] == "#":
                hashtags += 1
            
            if (bot_row - top_row == 5):
                if hashtags == 6 or hashtags == 4:
                    return True
                if S[top_row][col] == "#":
                    hashtags -= 1
                top_row += 1

    # check left to right diag
    for row in range(N - 5):
        for i in range(N - 5):
            hashtags = 0
            for j in range(6):
                if S[row + j][i + j] == "#":
                    hashtags += 1
            
            if hashtags == 6 or hashtags == 4:
                return True

    # check right to left diag
    for row in range(N - 5):
        for i in range(N - 1, 4, -1):
            hashtags = 0
            for j in range(6):
                if S[row + j][i - j] == "#":
                    hashtags += 1

            if hashtags == 6 or hashtags == 4:
                return True

    return False


print("Yes" if main() else "No")