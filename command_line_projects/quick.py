# function - star star
# takes 2 strings : longerstr, shorterstr 
# input 2 strings - could be empty 
# output int index 
# no time space constraints

# ex:
# input 
# california
# lif

# process
# - check if either of them is empty 
# - check if which one is longer and shorter (str 2 is shorter)
# - check if shorter one substring of the other 

# str2 is always substring 

# california
# 0123456789
#     l 
# lif
#   i 
    
def find_start_idx(str1, str2):
    if len(str1)==0 or len(str2)==0:
        return -1
    # str2 has to be shorter
    if len(str2)>len(str1):
        return -1
    left = 0
    right = left
    i = 0 
    while left< len(str1):
        right = left
        while str1[right] == str2[i]:
            i+=1
            right+=1
            if i > len(str2)-1:
                return left
        left+=1
        right = left
    return -1

print(find_start_idx("california", "lif"))
print(find_start_idx("",""))
print(find_start_idx("ca","japan"))
    

