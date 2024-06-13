#Determining String Composition

city = ["Dubai", "Charlotte", "Delhi", "Shanghai", "Tokyo"]

#put the words from the "city" list WITH letter "a" into another list
letter = "a" 

contains_letter = [] #creating a separate list to store words WITH letter "a"
no_letter = [] #creating a new list to store words without letter "a"
for word in city: #word describes the different elements in the "city" list
    if letter in word: #if the letter "a" is in the elements of the "city" list...
        contains_letter.append(word) #...then add those words into the new list
    else: #if the value of variable "letter" is not in the elements of "city" list...
        no_letter.append(word) #...then add those words into the new list
print("This list contains words WITH the letter 'a': ", contains_letter) #printing the new list with the words containing letter "a"
print("This list contains words WITHOUT the letter 'a': ", no_letter) #printing the new list WITHOUT the words containing letter "a"

#ANOTHER WAY FOR "else" = 
#put the words from "city" list WITHOUT letter "a" into another list
#no_letter = [] #creating a new list to store words without letter "a"
#for word in city: 
#   if letter not in word: #if the value of variable "letter" is not in the elements of "city" list...
#      no_letter.append(word) #...then add those words into the new list

#print("This list contains words WITHOUT the letter 'a': ", no_letter) #printing the new list WITHOUT the words containing letter "a"


