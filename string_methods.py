word = input("Type a word here to test: ")

# 1: capitalize()
# it will capitalize the first char of a string
print(f"capitalize method: {word.capitalize()}")

# 2: casefold()
# converts all characters of the string into lowercase letters and returns a new string
print(f"casefold method: {word.casefold()}")

# 3: center() The center() method will center align the string, using a specified character (space is default) as the
# fill character.
print(f"center method: {word.center(14, '*')}")

# 4: count()
# count method will count a char or a word from a string
print(f"count method: {word.count('a')}")

# 5: encode()
# The encode() function in Python is responsible for returning the encoded form of any given string.
print(f"encode method: {word.encode(encoding='UTF-8', errors='error')}")

# 6: endswith()
# this method check if a string ends with a specific letter and return True or False
print(f"endswith method: {word.endswith('c')}")
print(f"endswith method: {word.endswith(('a', 'x'))}")

# 7: expandtabs()
# The expandtabs() method sets the tab size to the specified number of whitespaces
first_variable = "text1\ttext2\ttext3\ttext4"
print(f"expandtabs method: {first_variable.expandtabs(20)}")

# 8: find()
# The python string find() method is used to return the index of the created string where the substring is found
index_of_word = word.find("mustafa")
print(f"find method: {index_of_word}")
print(f"find method: {word[index_of_word:]}")

# 9: format()
# It is the process of inserting a custom string or variable in predefined text.
name = "mustafa"
age = 23
print("{} is {} years old".format(name, age))
print("{1} years old is {0}".format(name, age))

# 10: format_map()
# Python String format_map() method is an inbuilt function in Python, which is used to return a dictionary key’s value.
students = {"name": "mustafa", "age": 23}
sentence = "{name}, {age}"
print(f"format_map method: {sentence.format_map(students)}")
print(f"output type of format_map: {type(sentence.format_map(students))}")

# 11: index The index() method finds the first occurrence of the specified value. The index() method raises an
# exception if the value is not found.
print(f"index method: {word.index('mustafa')}")

# 12: isalnum()
# checks if a string contains letters or numbers and return true
print(f"isalnum method: {word.isalnum()}")
print("isalnum method:", "mustafa124!".isalnum())

# 13: isalpha()
# checks if a string is alphabetic or not, return true if it is.
print("isalpha method:", "mustafa".isalpha())
print(f"isalpha method: {word.isalpha()}")

# 14: isdecimal()
# checks if a string is decimal, digit and numeric
print("isdecimal method:", "1234".isdecimal())
print("isdecimal method:", "mustafa".isdecimal())

# 15: isdigit()
# if a string is digit
print("isdigit method:", "1232".isdigit())
print("isdigit method:", "dfsdfs".isdigit())

# 16: isidentifier()
# checks if a variable name is correct or not
print("isidentifier method:", "name".isidentifier())
print("isidentifier method:", "_name".isidentifier())
print("isidentifier method:", "1name".isidentifier())
print("isidentifier method:", "name-56".isidentifier())
print("isidentifier method:", "student_name".isidentifier())

# 17: islower()
# checks if a string is lowercase
print("islower method:", "mustafa".islower())
print("islower method:", "MUSTAFA".islower())
print("islower method:", "Mustafa".islower())

# 18: isprintable()
# return true if a string be printable and contain not any escape char
print("isprintable method:", "name\t".isprintable())
print("isprintable method:", "name\n".isprintable())
print("isprintable method:", "name".isprintable())

# 19: isspace()
# checks if a string contain only space
print("isspace method:", "  this is me".isspace())
print("isspace method:", "".isspace())
print("isspace method:", "  ".isspace())
print("isspace method:", "thisisme".isspace())

# 20: istitle()
# check every word of string to be in title mode
print("istitle method", "Mustafa Akbari Is A Programmer".istitle())
print("istitle method", "Mustafa akbari is a Programmer".istitle())

# 21: isupper()
# return true if all string contain uppercase
print("isupper method:", "MUSTAFA".isupper())
print("isupper method:", "mustafa".isupper())
print("isupper method:", "MUSTafa".isupper())

# 22: join() The string join() method returns a string by joining all the elements of an iterable (list, string,
# tuple), separated by the given separator
text = ["python", "is", "a", "programming", "language"]
print("join method:", " ".join(text))
print("join method:", "_".join(text))
print("join method:", "+".join(text))
sentence = "this is mustafa"
print("join method:", "!".join(sentence))
mytuple = ("this", "is", "python")
print("join method:", "=".join(mytuple))
my_dict = {"name": "mustafa", "age": 30}
print("join method:", "->".join(my_dict))


# 23: ljust() The ljust() method will left align the string, using a specified character (space is default) as the
# fill character.
print("mustafa".ljust(20, '_'))

# 24: rjust() The rjust() method will right align the string, using a specified character (space is default) as the
# fill character.
print("mustafa".rjust(20, '+'))

# 25: lower() will convert uppercase to lowercase
print("MUSTAFA".lower())

# 26: lstrip() will remove a character or a word from the left side of a sentence
print("mustafa is a programmer".lstrip("mustafa"))
print("mustafa is a programmer".lstrip("m"))

# 27: replace() is used to replace a word or a char with another word or char in a sentence
print("this is programming with java".replace("java", "python"))

# 28: split() The split() method splits a string into a list. You can specify the separator, default separator is any
# whitespace
print("this is programming with python and mustafa".split())
print("this, is, programing, with, python".split(sep=","))
print("this is some spacial staff".split(sep=" ", maxsplit=2))

# 28: rstrip() will remove a character or a word from the right side of a sentence
print("mustafa is a programmer".rstrip("programmer"))
print("mustafa is a programmer".rstrip("mmer"))

# 29: The splitlines() method splits a string into a list. The splitting is done at line breaks
print("this is mustafa\nand this is ali\nand this is fatima".splitlines())
print("this is mustafa\nand this is ali\nand this is fatima".splitlines(keepends=True))

# 30: startswith() will check a string to start with a char and return true or false
print("mustafa".startswith("m"))
print("mustafa".startswith("n"))

# 31: strip() The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end)
# characters (space is the default leading character to remove)
print("     mustafa is a programmer      ".strip())
print("    this is python".strip())
print("this is programming       ".strip())
print("python java python java".strip("java"))

# 32: title() will capitalize each first char of a word in a sentence
print("this is programming with mustafa".title())

# 33: upper() will convert lowercase to uppercase
print("i want to learn python".upper())