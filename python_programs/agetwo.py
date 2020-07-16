# take csv as an input and print name in an ascending order of age 
# can not use csv parsing library
# assume that csv is in correct format

# name,age,location
# catherine,21,canada
# bob,10,usa
# charlie,23,united kingdom
import argparse
import sys
import heapq 


parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--sort')
args = parser.parse_args()

# print(args.file) 
f = open(args.file, 'r')
data = f.read()
f.close()

sort_key = 'age'
if args.sort:
    sort_key = args.sort

def sort_by_key(key,age,name,location,minheap):
    if key == 'age':
        heapq.heappush(minheap,(age,name,location))
    elif key == 'name':
        heapq.heappush(minheap,(name,age,location))
    elif key == 'location':
        heapq.heappush(minheap,(location,name,age))

def print_result(key,minheap):
    while minheap:
        if key == 'age':
            age,name,location = heapq.heappop(minheap)
            print(name,age,location)
        elif key == 'name':
            name,age,location = heapq.heappop(minheap)
            print(name,age,location)
        elif key == 'location':
            location,name,age = heapq.heappop(minheap)
            print(name,age,location)
        
# data = sys.stdin.read()
info = data.split('\n')[1:]
# print(info)
heap = []
for line in info:
    if len(line)==0:
        continue
    name, age, location = line.split(',')
    sort_by_key(sort_key,age,name,location,heap)

# print(minheap)
print_result(sort_key, heap)






