f = open('aoc.txt', 'r')
lines = f.readlines()
f.close()

# Find the length of the longest line so we don't miss anything
max_len = max(len(line) for line in lines)
to_do = lines[-1]
lines = lines[:-1]

cols = []
# Iterate through every character index (the "column")
for i in range(max_len):
    column_chars = []
    for line in lines:
        # Check if the line is long enough to have a character at this index
        if i < len(line.rstrip('\n')):
            column_chars.append(line[i])
        else:
            column_chars.append(" ") # Use a space if the line is too short
            
    column_string = "".join(column_chars)
    cols.append(column_string) 
sum = 0 
cur_ind = 0 
cur_thing = 0 if to_do[0] == '+' else 1 
to_do = to_do.strip().split()
for i in cols: 
    print(cur_ind, to_do[cur_ind], i, cur_thing, sum)
    if i == '   ' or i == '    ': 
        cur_ind += 1 
        if cur_thing != 0: 
            sum += cur_thing 
        if cur_ind >= len(to_do):
            break
        cur_thing = 0 if to_do[cur_ind] == '+' else 1 
        continue
    if to_do[cur_ind] == '+':
        sum += int(i)
    else:
        if cur_thing == 0:
            cur_thing = int(i)
        else:
            cur_thing *= int(i)
        
print(sum + cur_thing)


# def split_line(line):
#     l =  line.strip().split()
#     return list(map(list, l))
# def parse_lines(lines):
#     return [split_line(line) for line in lines]
# parsed_lines = parse_lines(lines)
# to_do = parsed_lines[-1]
# numbers = parsed_lines[:-1]
# ans = [0] * len(parsed_lines[0])

# print(numbers[0])


# for i in range(len(to_do)):
#     if to_do[i] == '*': 
#         ans[i] = 1 
        
# # transpose list 
# # one column: [[6,4], [2,3], [3,1,4]]

# for i in range(len(numbers)):
#     # we are at gloibal column 
    
    
    
        
# for i in range(len(numbers)):
#     # i is the global column
#     for j in range(len(numbers[i])):
#         # j is the global row 
        
        
#         if to_do[j] == '*':
#             ans[j] *= int(numbers[i][j])
#         else:
#             ans[j] += int(numbers[i][j])
# print(sum(ans))
