kattisproblems = {}

timelimit = 100
n = int(input())

for _ in range(n):
    k, m, p, t = input().split()
    if k not in kattisproblems:
        kattisproblems[k] = []
    kattisproblems[k].append([m, int(p), int(t)])

number_problems = len(kattisproblems)
matrix = [[0] * (timelimit + 1) for _ in range((number_problems)*3 + 3)]

pointer_row = 2  # Current row index
prev_group_row = 0  # Last completed group row index

for k in kattisproblems:
    methods = kattisproblems[k]
    while len(methods) < 3:
        methods.append(["x", 0, 101]) 

    for m, p, t in methods:
        pointer_row += 1  # Go to next row
       
        #adding problem id and weight to end of row
        #matrix[pointer_row][-1] = t
        #matrix[pointer_row][-2] = m
        #matrix[pointer_row][-3] = k
        
        for w in range(1, timelimit + 1):

            if t > w: # not including this item
                value1 = matrix[prev_group_row][w]
                value2 = matrix[prev_group_row-1][w]
                value3 = matrix[prev_group_row-2][w]
                best = max(value1,value2,value3)
                matrix[pointer_row][w] = best

            else: # including this item
                value1_with = matrix[prev_group_row][w - t]
                value2_with = matrix[prev_group_row -1][w - t]
                value3_with = matrix[prev_group_row -2][w - t]   
                best_value_with = max(value1_with, value2_with, value3_with) + p
                
                value1_without = matrix[prev_group_row][w]
                value2_without = matrix[prev_group_row-1][w]
                value3_without = matrix[prev_group_row-2][w]
                best_value_without = max(value1_without, value2_without, value3_without)
                
                matrix[pointer_row][w] = max(best_value_with, best_value_without)

    # After this group, update reference to latest group
    prev_group_row = pointer_row

# Result is in matrix[pointer_row][timelimit]
value1 = matrix[pointer_row][timelimit]
value2 = matrix[pointer_row-1][timelimit]
value3 = matrix[pointer_row-2][timelimit]
print(max(value1,value2,value3))

