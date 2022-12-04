def decode(pick):
    values = {
        "AY" : 4,
        "BY" : 5,
        "CY" : 6, 
        "AX" : 3,
        "BX" : 1,
        "CX" : 2,
        "AZ" : 8,
        "BZ" : 9,
        "CZ" : 7,
        
    }
    return values[pick]



if __name__ == "__main__":
    input = open("aoc-2022/day2/python/input.txt")
    lines = input.readlines()
    score = 0
    for line in lines:
        values = line.rstrip().split()
        v = "".join(values)
        score += decode(v)
        
    print(score)

