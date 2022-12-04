def decode(left, right):
    left_set = set()
    for char in left: 
        left_set.add(char)

    right_set = set()
    for char in right: 
        right_set.add(char)

    x=left_set.intersection(right_set)
    value = ord(x.pop())
    if value > 97: 
        return value - 96;
    else: 
        return value - 38;




if __name__ == "__main__":
    input = open("aoc-2022/day3/input.txt")
    lines = input.readlines()
    sum = 0
    for line in lines:
        line = line.rstrip()
        middle = int(len(line)/2)
        left, right = line[0:middle], line[middle:]
        sum += decode(left, right)
    print(sum)

