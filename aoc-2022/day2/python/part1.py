def decode(pick):
    values = {
        "AY" : 8,
        "BY" : 5,
        "CY" : 2, 
        "AX" : 4,
        "BX" : 1,
        "CX" : 7,
        "AZ" : 3,
        "BZ" : 9,
        "CZ" : 6,
        
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

