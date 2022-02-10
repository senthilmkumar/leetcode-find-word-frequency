import os
clear = lambda: os.system('clear')
clear()

print ("Find the words")
word_List = []
file_location = (os.getcwd()+'/leetcode-find-word-frequency/config/words.txt')

print (file_location)
# opening the text file
with open(file_location,'r') as file:
# reading each line    
    for line in file:
   
        # reading each word        
        for word in line.split():
   
            # displaying the words           
            # print(word) 
            # adding the element to the array
            word_List.append(word)

# print (len(word_List))

#Use Counter if you are using Python 2.7 or 3.x
from collections import Counter

#print (Counter(word_List))
pretty_print_list = Counter(word_List)
pretty_print_list.keys()

for key, value in pretty_print_list.most_common():
    print(key, value)



