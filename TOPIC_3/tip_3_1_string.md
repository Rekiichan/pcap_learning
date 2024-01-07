
# Built-in String Functions for PCAP Exam Preparation

Python's string data type has several built-in methods that you can use to perform common tasks. Here's a list of all the built-in string functions that you might find useful for the PCAP exam, with examples for each.

## Case Conversion
- `str.capitalize()`: Converts the first character to upper case
  - Example: `"hello".capitalize() # 'Hello'`
- `str.lower()`: Converts a string to lower case
  - Example: `"Hello".lower() # 'hello'`
- `str.upper()`: Converts a string to upper case
  - Example: `"hello".upper() # 'HELLO'`
- `str.title()`: Converts the first character of each word to upper case
  - Example: `"hello world".title() # 'Hello World'`
- `str.swapcase()`: Swaps cases, lower case becomes upper case and vice versa
  - Example: `"Hello World".swapcase() # 'hELLO wORLD'`
- `str.casefold()`: Converts string to lower case, more aggressive than lower()
  - Example: `"Hello World".casefold() # 'hello world'`

## Checking Content
- `str.endswith(suffix)`: Returns True if the string ends with the specified suffix
  - Example: `"Python.py".endswith('.py') # True`
- `str.startswith(prefix)`: Returns True if the string starts with the specified prefix
  - Example: `"Python.py".startswith('Py') # True`
- `str.isalnum()`: Returns True if all characters in the string are alphanumeric
  - Example: `"Python3".isalnum() # True`
- `str.isalpha()`: Returns True if all characters in the string are in the alphabet
  - Example: `"Python".isalpha() # True`
- `str.isdigit()`: Returns True if all characters in the string are digits
  - Example: `"1234".isdigit() # True`
- `str.isnumeric()`: Returns True if all characters in the string are numeric
  - Example: `"1234".isnumeric() # True`
- `str.islower()`: Returns True if all characters in the string are lower case
  - Example: `"hello".islower() # True`
- `str.isupper()`: Returns True if all characters in the string are upper case
  - Example: `"HELLO".isupper() # True`
- `str.istitle()`: Returns True if the string follows the rules of a title
  - Example: `"Hello World".istitle() # True`
- `str.isspace()`: Returns True if all characters in the string are whitespace
  - Example: `"   ".isspace() # True`

## Search and Replace
- `str.count(substring)`: Returns the number of occurrences of a substring in the string
  - Example: `"hello hello".count('hello') # 2`
- `str.find(substring)`: Returns the lowest index of the substring if it is found
  - Example: `"hello".find('e') # 1`
- `str.rfind(substring)`: Returns the highest index of the substring if it is found
  - Example: `"hello hello".rfind('hello') # 6`
- `str.index(substring)`: Like find(), but raises an exception if substring is not found
  - Example: `"hello".index('e') # 1`
- `str.rindex(substring)`: Like rfind(), but raises an exception if substring is not found
  - Example: `"hello hello".rindex('hello') # 6`
- `str.replace(old, new)`: Replaces all occurrences of the old substring with the new substring
  - Example: `"hello world".replace('world', 'Python') # 'hello Python'`

## Trimming and Adjusting
- `str.strip([chars])`: Returns a trimmed version of the string
  - Example: `"   hello   ".strip() # 'hello'`
- `str.rstrip([chars])`: Returns a right-trimmed version of the string
  - Example: `"hello   ".rstrip() # 'hello'`
- `str.lstrip([chars])`: Returns a left-trimmed version of the string
  - Example: `"   hello".lstrip() # 'hello'`

## Splitting and Joining
- `str.split(separator)`: Splits the string at the specified separator and returns a list
  - Example: `"hello,world".split(',') # ['hello', 'world']`
- `str.rsplit(separator)`: Splits the string at the specified separator, from the right
  - Example: `"hello,world".rsplit(',') # ['hello', 'world']`
- `str.splitlines()`: Splits the string at line breaks and returns a list
  - Example: `"hello\nworld".splitlines() # ['hello', 'world']`
- `str.join(iterable)`: Joins the elements of an iterable (e.g., a list) into a single string
  - Example: `','.join(['hello', 'world']) # 'hello,world'`

## Formatting
- `str.format()`: Formats the string using format specifiers
  - Example: `"Hello, {}".format('Python') # 'Hello, Python'`

## Miscellaneous
- `str.encode()`: Returns an encoded version of the string
  - Example: `"hello".encode() # b'hello'`
- `str.expandtabs(tabsize)`: Replaces tabs in a string with the specified number of spaces
  - Example: `"hello\tworld".expandtabs(4) # 'hello    world'`

These methods are essential for manipulating and examining the contents of strings in Python. Understanding how to use them effectively will help you solve string-related problems more efficiently in your PCAP exam and beyond.
