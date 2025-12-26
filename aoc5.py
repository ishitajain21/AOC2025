f = open("aoc.txt", "r")
lines = f.readlines()
f.close()

fresh = []
avails = []
found_space = False
for line in lines:
    if line.strip() == "":
        found_space = True
        continue
    if not found_space:
        fresh.append(line.strip().split('-'))
    else:
        avails.append(line.strip())

fresh = sorted(fresh, key=lambda x: int(x[0]))
avails = [int(x) for x in avails]
avails = sorted(avails)

def fix_intervals(fresh):
    merged = []
    for start, end in fresh:
        start, end = int(start), int(end)
        if not merged or merged[-1][1] < start - 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged 
merged_fresh = fix_intervals(fresh)

tot = 0 
for a,b in merged_fresh:
    tot += (b-a+1)
print(tot)

# print(merged_fresh) 
# count = 0
# ind = 1
# print(avails)
# for avail in avails:
#     print(avail)
#     a = int(avail)
#     for i in range(ind-1, len(merged_fresh)):
#         start, end = merged_fresh[i]
#         # print(start, end)
#         # if a < start:
#         #     print('less than')
#         #     break
#         if start <= a <= end:
#             count += 1
#             # ind = i
#             break
# print(count)