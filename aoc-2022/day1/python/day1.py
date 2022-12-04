if __name__ == "__main__":
    input = open("aoc-2022/day1/python/input.txt", "r")
    lines = input.readlines()
    calories = []
    elf= 0
    for line in lines:
        if line != "\n":
            elf = elf + int(line)
        else:
            calories.append(elf)
            elf = 0

    calories.sort(reverse=True)
    print(calories[0])
    print(sum(calories[0:3]))

