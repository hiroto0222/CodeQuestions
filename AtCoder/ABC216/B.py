N = int(input())
names = {}
ans = "No"
for i in range(N):
    curr_surname, curr_forename = input().split()
    if curr_forename in names:
        if curr_surname in names[curr_forename]:
            ans = "Yes"
            break
        else:
            names[curr_forename].append(curr_surname)
    else:
        names[curr_forename] = [curr_surname]

print(ans)