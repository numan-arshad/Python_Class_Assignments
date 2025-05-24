
# Lesson 05: Control Flow & Loops

# if-elif-else
# Used for decision making based on conditions.
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# for loop
# Used to iterate over a sequence.
for i in range(5):
    print(i)

# while loop
# Repeats as long as the condition is true.
count = 0
while count < 5:
    print(count)
    count += 1

# break statement
# Exits the loop early when a condition is met.
for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement
# Skips the current iteration and moves to the next.
for i in range(5):
    if i == 2:
        continue
    print(i)

# pass statement
# Placeholder when a statement is required syntactically.
for i in range(5):
    if i == 3:
        pass
    print(i)


# Lesson 06: Lists, Tuples & Dictionary

# List Methods
# Lists are mutable sequences of items.
my_list = [1, 2, 3, 4]
my_list.append(5)          # Adds item to the end
my_list.extend([6, 7])     # Adds multiple items to the end
my_list.insert(2, 99)      # Inserts item at a specific position
my_list.remove(2)          # Removes first occurrence of item
popped_item = my_list.pop()# Removes and returns last item
index_of_99 = my_list.index(99)  # Returns index of first match
count_99 = my_list.count(99)     # Counts occurrences
my_list.sort()             # Sorts the list
my_list.reverse()          # Reverses the list
copy_list = my_list.copy()# Returns a copy of the list
my_list.clear()            # Clears all items
print("List methods output:", copy_list)

# Tuple Methods
# Tuples are immutable sequences.
tuple1 = (10, 20, 30, 10)
print("Index of 20:", tuple1.index(20))  # Returns index of item
print("Count of 10:", tuple1.count(10))  # Counts occurrences

# Dictionary Methods
# Dictionaries store key-value pairs.
dict1 = {"name": "Ali", "age": 22}
dict1["city"] = "Lahore"                # Add new key-value pair
print("Get name:", dict1.get("name"))   # Gets value of key
print("Keys:", dict1.keys())            # Returns all keys
print("Values:", dict1.values())        # Returns all values
print("Items:", dict1.items())          # Returns key-value pairs
dict1.update({"age": 23})              # Updates dictionary
removed_value = dict1.pop("city")      # Removes key and returns value
dict1.clear()                          # Removes all items
copy_dict = dict1.copy()               # Returns a shallow copy
print("Dictionary methods output:", copy_dict)


# Lesson 07: The Set & Frozenset

# Set Methods
# Sets are unordered collections of unique items.
set1 = {1, 2, 3, 4}
set1.add(5)               # Adds item to set
set1.remove(2)            # Removes item (error if not found)
set1.discard(10)          # Removes item (no error if not found)
popped_item = set1.pop() # Removes and returns a random item
set1.update([6, 7])       # Adds multiple items
print("Set after updates:", set1)

# Set Operations
set2 = {3, 4, 5, 6}
print("Union:", set1.union(set2))                  # Combines sets
print("Intersection:", set1.intersection(set2))    # Common items
print("Difference:", set1.difference(set2))        # Items in set1 not in set2
print("Symmetric Difference:", set1.symmetric_difference(set2)) # Items not common

# More Set Methods
print("Is subset:", set1.issubset(set2))            # Checks if set1 is subset of set2
print("Is superset:", set1.issuperset(set2))        # Checks if set1 is superset of set2
print("Is disjoint:", set1.isdisjoint(set2))        # Checks if sets have no common items

# Frozenset Methods
# Frozensets are immutable sets.
frozen = frozenset([1, 2, 3])
print("Frozenset:", frozen)
print("2 in frozen:", 2 in frozen)                         # Membership check
print("Union with frozenset:", frozen.union([4, 5]))      # Returns union
print("Intersection with frozenset:", frozen.intersection([2, 3])) # Returns intersection
