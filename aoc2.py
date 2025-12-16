def split_range(start, end):
    ranges = []
    cur = start

    while cur <= end:
        magnitude = 10 ** len(str(cur))
        next_9 = magnitude - 1

        stop = min(next_9, end)
        ranges.append((cur, stop))
        cur = stop + 1

    return ranges


f = open("aoc.txt", "r")
line = f.readline().strip()
f.close()

sum_invalid = 0
# split by commas first
for part in line.split(","):
    a, b = part.split("-")
    a, b = int(a), int(b)
    l = split_range(a, b)
    for inte in l:
        a, b = int(inte[0]), int(inte[1])
        l = len(str(a))
        s = set()
        for factor in range(2, l + 1):
            if l % factor != 0:
                continue
            new_l = l // factor

            for i in range(int(str(a)[:new_l]), int(str(b)[:new_l]) + 1):

                num_str = str(i) * factor
                num = int(num_str)
                if num >= a and num <= b:
                    s.add(num)
                if num > b:
                    break
        sum_invalid += sum(s)
        print(s)
print(sum_invalid)
