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


##### get dist #####
dist = 0

for idx, _ in enumerate(left_list):
    dist += abs(left_list[idx] - right_list[idx])

print ("dist = " + str(dist))


##### star 2 #####
# use a hash table for right list to make solution O(n) time
hash_offset = min(right_list)
hash_len = max(right_list) - min(right_list) + 1
hash_table = [0] * hash_len

# populate hash table
for val in right_list:
    hash_table[val - hash_offset] += 1


##### get similarity #####
sim = 0
for val in left_list:
    # If value outside of hash table indices, it isn't in right list
    if (val > hash_offset + hash_len) or (val < hash_offset):
        None
    
    else:
        sim += val * hash_table[val - hash_offset]

print ("sim = " + str(sim))
