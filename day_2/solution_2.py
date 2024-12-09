import re

def safe(level: list) -> bool:
    # check increasing or decreasing
    sign = 1 # inc
    if ((level[0] - level[1]) < 0):
        sign = -1 # dec
    
    # test list
    for i, curr in enumerate(level):
        next = level_vals[i + 1]
        diff = sign * (curr - next) # if decreasing, diff always neg
        if (diff <= 3) and (diff >= 1):
            if i == (len(level_vals) - 2):
                return True

        else:
            return False


if __name__ == "__main__":
    
    ##### star 1 #####
    safe_levels = 0
    with open("input_2.txt") as input:
        for lines in input:
            level_vals = re.findall("\d+", lines)
            level_vals = list(map(int, level_vals))

            if safe(level_vals):
                safe_levels += 1

    print ("safe levels = " + str(safe_levels))