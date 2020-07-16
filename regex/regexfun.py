import re

sentence = "Hello. Bello. World!"
print('Sentence: "{}"'.format(sentence))

pattern = r"ello"
print("\n######## Pattern 1: {}".format(pattern))
matched = re.match(pattern, sentence)
print("Using match(): {}".format(matched))
searched = re.search(pattern, sentence)
print("Using search(): {}".format(searched))

pattern_two = r".ello\."
print("\n######## Pattern 2: {}".format(pattern_two))
matched = re.match(pattern_two, sentence)
print("Using match(): {}".format(matched))
searched = re.search(pattern_two, sentence)
print("Using search(): {}".format(searched))
found = re.findall(pattern_two, sentence)
print("Using findall(): {}".format(found))

print("\n######## Replacing")
replace_with = "Goodbye"
replaced = re.sub(pattern_two, replace_with, sentence)
print("Using sub(): {}".format(replaced))

pattern_three = r"[aeiou]"
print("\n######## Pattern 3: {}".format(pattern_three))
found = re.findall(pattern_three, sentence)
print("Using findall(): {}".format(found))


"""
special characters:
"." - matches anything
"[abcde]" - matches any characters in the list
"""