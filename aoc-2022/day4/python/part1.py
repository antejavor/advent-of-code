def decode(left, right):
    a, b= list(map(int, left.split("-")))
    x, y = list(map(int, right.split("-")))
  

    if a <= x and b >= y:
        return 1
    elif x <= a and  y >= b:
        return 1
    else: 
        return 0

if __name__ == "__main__":
    input = open("aoc-2022/day4/input.txt")
    lines = input.readlines()
    overlaps = 0
    for line in lines:
        left, right = line.rstrip("\n").split(",")
        print(line.rstrip())
        print(decode(left, right))
        overlaps = overlaps + decode(left, right)
    print(overlaps)