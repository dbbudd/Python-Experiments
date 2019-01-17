#!/usr/bin/env python
import re
'''
text = open("sample.txt")

for line in text:
    print(line)
    a = re.split('\W+', line)
    print(a)
'''


'''
text = 'That wayward #OldMan of "Kilkenny"'

lines = re.split('\W+', text)
for word in lines:
    print(word)
    
    
'''
'''
text = 'That wayward #OldMan of "Kilkenny"'
word = re.findall('\w+', text)
print(word[0])

text = 'That wayward #OldMan of "Kilkenny"'
word = re.findall('\w+', text)
print(word)


text = 'That wayward #OldMan of "Kilkenny"'
word = re.findall('#.*$', text)
print(word)


text = 'That wayward #OldMan of "Kilkenny"'
word = re.findall('^.*#', text)
print(word)


text = 'That wayward #OldMan of "Kilkenny"'
word = re.findall('#\w+', text)
print(word)


my_list = ["Kilkenny", "wayward", "cats"]
text = 'That wayward #OldMan of "Kilkenny"'

for words in my_list:
    if re.search(words, text):
        print("Okay")
    else:
        print("No")

'''

my_list = {"Kilkenny":"Cats", "wayward":"Dogs"}
text = 'That wayward #OldMan of "Kilkenny"'

for key in my_list.keys():
    change = re.sub(key, my_list[key], text)
    text = change

print(text)