import argparse
import string

# 2. Write a quick and dirty program (not just a standalone function) to print a count of all the different "words" 
# in a text file. Use any definition of word that makes logical sense or makes your job easy.
# The output should be sorted like this:
    # ```
    # 17 a
    # 14 the
    # 9 of
    # 9 in
    # 8 com
    # 7 you
    # 7 that
    # 7 social
    # 6 to
    # ```
# For this input file, the word "a" occurred 17 times, "the" 14 times, etc.

# This file can be run with the following command:
# python two.py takeonme.txt

parser = argparse.ArgumentParser(description='Print the count of all unique words in a text file.')
parser.add_argument('fn', metavar='filename', type=str, help='the filename of the text file to count words for')

args = parser.parse_args()
fn = args.fn

word_dict = {}
with open(fn, 'r') as f:
    for line in f:
        for word in line.lower().split():
            word = word.strip(string.punctuation)
            if word not in word_dict:
                word_dict[word]=1
            else:
                word_dict[word]+=1
# print(word_dict)
ans = []
for k,v in word_dict.items():
    ans.append((v,k))
ans.sort(key=lambda x:-x[0])
print('`'*3)
for elem in ans:
    count,word = elem
    print(str(count) +' '+ word)
print('`'*3)
f.close()