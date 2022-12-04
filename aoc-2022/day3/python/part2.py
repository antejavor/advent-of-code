def decode(one, two, three):
    one_set = set()
    for char in one: 
        one_set.add(char)

    two_set = set()
    for char in two: 
        two_set.add(char)

    three_set = set()
    for char in three:
        three_set.add(char)

    x=one_set.intersection(two_set.intersection(three_set))
    value = ord(x.pop())
    if value > 97: 
        return value - 96;
    else: 
        return value - 38;




if __name__ == "__main__":
    input = open("aoc-2022/day3/input.txt")
    lines = input.readlines()
    sum = 0
    group = []
    for line in lines:
        line = line.rstrip()
        group.append(line)
        if len(group) == 3:
            sum += decode(group[0], group[1], group[2])
            group.clear()
    print(sum)

