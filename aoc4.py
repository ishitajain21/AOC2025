f = open("aoc.txt", "r")
lines = f.readlines()
f.close() 
l = []
for line in lines:
    x = []
    for char in line.strip():
        x.append(char)
    l.append(x)
nums = 0 
nums_round = 0 
while nums_round != 0 or nums == 0:
    nums_round = 0
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == '@':
                count = 0  
                for dx, dy in [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,1], [-1,-1], [1,-1]]:
                    if i + dx >= 0 and j + dy >= 0 and i+dx < len(l) and j+dy < len(l[0]) and l[i+dx][j+dy] == '@':
                        count += 1 
                        if count >= 4: 
                            break 
                if count < 4: 
                    nums_round += 1 
                    l[i][j] = '.'
    nums += nums_round           
print(nums) 