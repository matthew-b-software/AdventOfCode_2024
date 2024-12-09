import re

##### get and sort data ####
left_list = []
right_list = []

with open("input.txt") as input:
    for lines in input:
        values = re.findall("\d+",lines)
        left_list.append(int(values[0]))
        right_list.append(int(values[1]))

left_list.sort()
right_list.sort()


##### get dist  #####
dist = 0

for idx, _ in enumerate(left_list):
    dist += abs(left_list[idx] - right_list[idx])

print ("answer = " + str(dist))
