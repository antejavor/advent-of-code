from collections import deque 

def get_marker_index(line):
    length = 14
    for i in range(0, len(line)-length):
        marker = set(line[i:i + length])
        if len(marker) == length :
            print(i + length)
            return i
        marker.clear()


if __name__ == "__main__":
    input = open("aoc-2022/day6/input.txt")
    line = input.readline()
    get_marker_index(line)
  

    



 


    
 
            
               

        


        