#Ejemplos 'list comprehension' comprension de listas.
#[<do-this> for <all-items> in <this-list>]

#[<do-this> for <all-items> in <this-list> if <condition-is-True>]


"""1. Find all of the numbers from 1–1000 that are divisible by 8
divisible = [ind for ind in range(1, 1000) if ind % 8 == 0]
print(divisible)"""

"""2. Find all of the numbers from 1–1000 that have a 6 in them
sixin = [ind if "6" in str(ind) else '*' for ind in range(1, 1000)]
print(sixin)"""

"""3. Count the number of spaces in a string
cont = 0
spaces = len([ind for ind in "P Y T H O N" if ind == ' '])
print(spaces)"""

"""4. Remove all of the vowels in a string
vowels = "".join([ind for ind in "FREDEV" if ind not in ["A", "E", "I", "O", "U"]])
print(vowels)"""

"""5. Find all of the words in a string that are less than 5 letters
text = "I want to be an excellent programmer"
text = text.split()
answer = [word for word in text if len(word) < 5]
print(answer)"""

"""6. Use a dictionary comprehension to count the length of each word in a sentence
text = "I want to be an excellent programmer"
text = text.split()
largo = {ind:len(ind) for ind in text}
print(largo)"""

"""7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
nums = [i for i in range(1,1001)]
listinlist = [num for num in nums if True in [True for divisor in range(2,10) if num % divisor == 0]]
print(listinlist)"""

"""8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is
divisible by
nums = [i for i in range(1,100)]
answer = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums}
print(answer)"""

"""9. You’re given the string “I’m learning Python in 2022”. You’d like to get a list of all digits in this string.
phrase = "I'm learning Python3 in 2022"
digits = [obj for obj in phrase if obj.isdigit()]
print(digits)"""

"""10. You have a list of fruits.And you’d like to create a list starts_with_b that contains all fruits from the fruits list 
that start with b"""
fruits = ["blueberry","apple","banana","pera","baicon"]
starts_with_b = [obj for obj in fruits if obj.startswith("b")]
print(starts_with_b)