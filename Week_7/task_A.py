stitched_lines = ""
with open('pi_few.txt') as file_object:
    for i in range(3):
        lines = file_object.readline().rstrip()
        stitched_lines += lines

float_num = float(stitched_lines)        

result = 10 * (float_num)
print(result)

