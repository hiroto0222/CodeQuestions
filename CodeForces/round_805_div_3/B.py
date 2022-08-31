def main():
    # 3 distinct letters per day

    s = input()

    i = 0
    days = 0
    while i < len(s):
        seen = set()
        for j in range(i, len(s)):
            if s[j] not in seen:
                seen.add(s[j])
            if len(seen) > 3:
                break
            i = j

        days += 1
        i += 1

    return days

for _ in range(int(input())):
    print(main())