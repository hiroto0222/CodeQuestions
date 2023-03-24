# AB:CD -> AC:BD valid?
# when 0 <= B <= 5 and 
# if AB >= 20 -> 0 <= C <= 3
# else anything

H, M = map(int, input().split())
if H < 20:
    if H >= 6 and H < 10:
        H, M = 10, 0
    if H >= 16:
        H, M = 20, 0
else:
    if M >= 40:
        H = (H + 1) % 24
        M = 0

print(H, M)