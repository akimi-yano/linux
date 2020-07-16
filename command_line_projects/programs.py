import random
# 1. Given a one dimensional array of data write a function that returns a new array with the data reversed. 
# Don't just use the reverse function that is built into your environment.

def reverse_arr(arr):
    new_arr = []
    for i in range(len(arr)-1,-1,-1):
        new_arr.append(arr[i])
    return new_arr

# tests
print("**** Problem 1 ****")
print(reverse_arr([1,2,3,4,5]))
print(reverse_arr(['a','b','c','d','e']))
print(reverse_arr(['#','*','+','%','$']))
print(reverse_arr([]))

# 2. solution is in the separate two.py file
print("**** Problem 2 ****")
print("Please refer to two.py. It can be run by running 'python two.py takeonme.txt'")

# 3. Write a function that returns M random non-negative integers less than some value N. Each integer must also be unique.


# N has to be greater than or equal to 1 to have at least 1 non-negative integer (M=1)
# if M is larger than N, it will throw an exception: "*** Invalid input: M is larger than N ***"

def m_random_ints(M,N):
    ans = []
    if M>N:
        raise Exception("*** Invalid input: M is larger than N ***")
    unique = set([])
    while len(ans)<M and len(unique)<N:
        num = random.randint(0,N-1)
        if num not in unique:
            ans.append(num)
            unique.add(num)
    return ans
# Tests
print("**** Problem 3 ****")
print(m_random_ints(3,10))
print(m_random_ints(10, 10))

# 4. Given a one dimensional array of data write a function that return M random elements of that array. 
# Each element must also be from a different position in the array. 
# Don't just use the sample function that is built into your environment.

# if M is larger than the length of array, it will through an exception: 
# "*** Invalid input: M is larger than the number of elements in the array ***"

def random_m(arr,M):
    if M>len(arr):
        raise Exception("*** Invalid input: M is larger than the number of elements in the array ***")
    idx = set([])
    ans = []
    while len(ans)<M and len(idx)<len(arr):
        num=random.randint(0,len(arr)-1)
        if num not in idx:
            ans.append(arr[num])
            idx.add(num)
    return ans
        
print("**** Problem 4 ****")
print(random_m([1,3,5,7,9],3))

# 5. Briefly describe how a DNS server works.
ans = """DNS is like an address book for domain name and IP address ! 
It saves the trouble of users having to read and remember IP addresses. 
For example, when a user types "google.com", DNS finds the corresponding IP address for the domain name 
and let user's computer know so that user's computer can connect to the IP address. 
Because this can get expensive as the number of users and requests increase, there are cacheing mechanisms both in 
the user's computer and on the DNS server(s).
"""
print("**** Problem 5 ****")
print(ans)



# 6. Consider a directed graph of small non-negative integers where each integer is less than 60,000 and each integer is unique. 
# In this case, a directed graph is a data structure where a node is represented by a unique integer and each node has zero or 
# more child nodes. As above, don't just use an existing graph library.

# - Write a function that creates a node in a graph.
# - Write a function that inserts a node as a child of another node.
# - These functions should not allow cycles to be created. That is, a node may not directly or indirectly point to itself.
# - Write a function to print out a graph

# Here is a simple example graph without cycles:

# ```
# 1 -> 2, 3, 4
# 2 -> 5
# 3 -> 6
# 4 -> 3, 6
# 5 -> 6
# 6 -> No children
# ```

graph = {}

def create_node(node):
    if node<0 or 60000<=node:
        raise Exception("*** Invalid input: node must be non-negative integers where each integer is less than 60,000 ***")
    if node in graph:
        raise Exception("*** Invalid input: node already exists ***")
    else:
        graph[node]=set([])


# def will_be_circle(child_node, parent_node):
#     if child_node == parent_node:
#         return True
#     if child_node in graph:
#         for next_node in graph[child_node]:
#             if will_be_circle(next_node, parent_node):
#                 return True
#     return False

def will_be_circle(child_node, parent_node):
    found_circle = False
    if child_node in graph:
        for next_node in graph[child_node]:
            if next_node == parent_node:
                found_circle = True
            found_circle |= will_be_circle(next_node, parent_node)
            if found_circle:
                break
    return found_circle

def insert_child(parent_node, child_node):
    if parent_node<0 or 60000<=parent_node or child_node<0 or 60000<=child_node:
        raise Exception("*** Invalid input: each node must be non-negative integers where each integer is less than 60,000 ***")
    if parent_node == child_node:
        raise Exception("*** Invalid input: self edge is not allowed ***")
    if parent_node not in graph:
        raise Exception("*** Invalid input: such parent node does not exist ***")
    if child_node not in graph:
        raise Exception("*** Invalid input: such child node does not exist ***")
    elif child_node in graph[parent_node]:
        raise Exception("*** Invalid input: such node already exist as a child of the parent node ***")
    elif will_be_circle(child_node, parent_node):
        raise Exception("*** Invalid input: such input will create a circle in a graph ***")
    else:
        graph[parent_node].add(child_node)

def print_graph():
    print('`'*3)
    for k,v in graph.items():
        print('{} -> {}'.format(k, ', '.join(str(x) for x in v) or "No children"))
    print('`'*3)
    

# Tests
print("**** Problem 6 ****")
create_node(1)
create_node(2)
create_node(3)
create_node(4)
create_node(5)
create_node(6)
insert_child(1,2)
insert_child(1,3)
insert_child(1,4)
insert_child(2,5)
insert_child(3,6)
insert_child(4,3)
insert_child(4,6)
insert_child(5,6)   
print_graph()
