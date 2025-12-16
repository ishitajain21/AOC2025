f = open("aoc.txt", "r")
lines = f.readlines()

cur = 50
count = 0

for i in lines:
    dir = i.strip()[0]
    steps = int(i.strip()[1:])

    full_cycles = steps // 100
    rem = steps % 100

    # Full cycles: each passes 0 once
    count += full_cycles

    crossed_zero = False

    if dir == "R":
        # Right: position decreases
        if rem > 0 and cur > 0 and cur - rem < 0:
            crossed_zero = True
        cur = (cur - rem) % 100

    else:  # dir == "L"
        # Left: position increases
        if rem > 0 and cur + rem > 100:
            crossed_zero = True
        cur = (cur + rem) % 100

    # Count mid-rotation crossing ONLY if we didn't land on 0
    if crossed_zero and cur != 0:
        count += 1

    # Count landing on 0
    if cur == 0:
        count += 1

    print(cur, count)

print(f"Total count: {count}")
f.close()
