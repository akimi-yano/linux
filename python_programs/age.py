# take csv as an input and print name in an ascending order of age 
# can not use csv parsing library
# assume that csv is in correct format

# name,age,location
# catherine,21,canada
# bob,10,usa
# charlie,23,united kingdom
    
import sys
import heapq 
data = sys.stdin.read()
info = data.split('\n')[1:]
# print(info)
minheap = []
for line in info:
    if len(line)==0:
        continue
    name, age, location = line.split(',')
    heapq.heappush(minheap,(age,name,location))
# print(minheap)
while minheap:
    age,name,location = heapq.heappop(minheap)
    print(name)
    

