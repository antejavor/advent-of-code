from collections import deque
import re
if __name__ == "__main__":
    input = open("aoc-2022/day5/input.txt")
    lines = input.readlines()
    strings = lines[0:8]
    strings = [line.rstrip("\n").replace('[',' ').replace(']', ' ') for line in strings]
    strings = [''.join(chars) for chars in zip(*strings)]
    strings = [s.replace(' ', '') for s in strings]
    strings = [s[::-1] for s in strings if s]
    container = {}
    for i in range (1 ,len(strings) + 1):
        d = deque()
        container[i] = deque([c for c in strings[i-1]])
        print(container[i])
    
    
    for line in lines[10:]: 
        line =line.replace(' ', '').rstrip("\n")
        crates, _from, to = map(int, re.findall("\d+", line))
        while crates != 0: 
            container[int(to)].append(container[int(_from)].pop())
            crates -= 1
    
    value = [cont.pop() for key, cont in container.items()]
    print("".join(value))
   