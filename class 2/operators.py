

# # 1. Arithmetic Operators 
# # These operators are used for mathematical calculations. 
# # Example: 

# a = 10 
# b = 3 
# print(a + b)  # Addition -> 13 
# print(a - b)   # Subtraction -> 7 
# print(a * b)   # Multiplication -> 30 
# print(a / b)   # Division -> 3.3333 
# print(a % b)   # Modulus -> 1 (remainder) 
# print(a // b)  # Floor Division -> 3 (removes decimal part) 
# print(a ** b)  # Exponentiation -> 10^3 = 1000 


# # 2. Comparison Operators 
# # These operators compare two values and return True or False. 
# # Example: 

# x = 5 
# y = 10 
# print(x == y)   # False (Equal to)
# print(x != y)   # True  (Not equal to)
# print(x > y)    # False (Greater than)
# print(x < y)    # True  (Less than) 
# print(x >= y)   # False (Greater than or equal to) 
# print(x <= y)   # True  (Less than or equal to) 
 
 
# # 3. Logical Operators 
# # Used to combine conditional statements. 
# # Example: 

# a = True 
# b = False 
# print(a and b)  # False 
# print(a or b)   # True 
# print(not a)  # False (Logical NOT)  
 


# # 4. Bitwise Operators 
# # Perform bitwise operations on binary numbers. 
# # Example: 

# a = 5  # 101 in binary 
# b = 3  # 011 in binary 
# print(a & b)  # AND -> 1 
# print(a | b)  # OR  -> 7 
# print(a ^ b)  # XOR -> 6 
# print(~a)  # NOT -> -6    
# print(a << 1) # Left Shift -> 10 
# print(a >> 1) # Right Shift -> 2 


# # 5. Assignment Operators 
# # Used to assign values to variables. 
# # Example: 

# x = 10 
# x += 5  # Same as x = x + 5 
# x -= 3  # Same as x = x - 3 
# x *= 2  # Same as x = x * 2 
# x /= 2  # Same as x = x / 2 
# x %= 3  # Same as x = x % 3 
# x //= 2 # Same as x = x // 2 
# x **= 3 # Same as x = x ** 3 

# # 6. Identity Operators 
# # Check if two variables point to the same object in memory. 
# # Example: 

# a = [1, 2, 3] 
# b = a 
# print(a is b)  # True 
# print(a is not b)  # False 


# # 7. Membership Operators 
# # Check if a value is present in a sequence (list, tuple, string). 
# # Example: 

# x = [1, 2, 3, 4] 
# print(3 in x)  # True 
# print(5 not in x)  # True 

# # 8. Ternary Operator (Conditional Expressions) 
# # Short form of if-else. 
# # Example: 

# a, b = 10, 20 
# min_value = a if a < b else b 
# print(min_value)  # 10 

# # Task 2: Understanding Byte Type and File Handling in Python 
# # Python provides a byte type for handling binary data. 
# # 1. Byte Type 

# byte_data = b"Hello"  # Byte type data 
# print(byte_data)  # Output: b'Hello' 
# print(type(byte_data))  # Output: <class 'bytes'> 


# # # 2. Read Binary File (rb Mode) 

# # with open("example.jpg", "rb") as image_file: 
# # content = image_file.read() 
# # print(content)  # Binary content of the file 


# # 3. Write Binary File (wb Mode) 
# # python 
# # CopyEdit 
# # binary_data = b"Some binary data" 
# # with open("output.bin", "wb") as file: 
# # file.write(binary_data) 


# # Task 3: Understanding Type Casting and isinstance() 
# # Python supports both explicit and implicit type casting. 
# # 1. Explicit Type Casting 


# num = "100" 
# int_num = int(num)  # Converting string to integer 
# print(int_num, type(int_num))  # 100 <class 'int'> 


# # 2. Implicit Type Casting 
# # Python automatically converts types where necessary. 

# x = 5  # int 
# y = 2.5  # float 
# result = x + y  # Python converts x to float automatically 
# print(result, type(result))  # 7.5 <class 'float'> 


# # 3. Checking Type with isinstance() 
# # Instead of using if-else, we can use isinstance(). 

# x = 10 
# print(isinstance(x, int))  # True 
# print(isinstance(x, float))  # False 


# # Task 4: Understanding chr() and id() Functions 
# # 1. chr() Function 
# # Returns the character of a given Unicode number. 

# print(chr(65))  # Output: 'A' 
# print(chr(97))  # Output: 'a'


# # 2. id() Function 
# # Returns the memory location of an object. 


# a = 10 
# print(id(a))  # Unique memory address of `a` 


# # Task 5: Understanding range() with 3 Arguments 
# # Python’s range(start, end, step) function generates a sequence of numbers. 

# for i in range(1, 10, 2):  # Start=1, End=10, Step=2 
# # print(i)  # Output: 1, 3, 5, 7, 9 


