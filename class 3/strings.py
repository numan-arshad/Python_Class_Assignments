
#/ Single quotes (')

str = 'Numan, Arshad!'
print(str)

#/ Double Quotes (")

str1 = "General Knowledge"
print(str1)

#/ Triple Quotes (''')

str2 = '''Python is a high-level 
general purpose programming language.'''
print(str2)

#/ String as an Array

text = "Numan"
print(text[0])   # Output: A
print(text[3])   # Output: S

#/ String Concatenation

first = "Numan "
second = "Arshad"
result = first + " " + second
print(result)  # Output: Numan Arshad

#/ String Length

text = "Programming"
print(len(text))  # Output: 11
 
#/ Escape Sequence Characters

print("Nu,\tman!")  #\t tab       (output : Anu,Sha!)
print("Nu, \"man!\"")#/           (output :Anu, "Sha!")
print("Nu,\\ man!")#/             (output : Anu, / Sha!)
print("Nu,\b man!") #\b backspace (output : Anu Sha!)

#/ If Else (control flow)

num = 10

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero") #/ (output:positive number)

#/  for loop

for a in range(7):
    print("Iteration:", a)
#/ (output : 0,1,2,3,4,5,6)

#/  while loop

count = 1
while count <= 5:
    print("Count:", count)
    count += 1
#/ (output : count:1, count:2, count:3, count:4, count:5)

#/ Nested Loops

for a in range(1, 4):
    for b in range(1, 4):
        print(f"a={a}, b={b}")

#/  Loop with else

for c in range(3):
    print(c)
else:
    print("Loop finished")
#/ (output : 0,1,2,Loop finished )

#/  Break Statement (Loop Control)

for j in range(5):
    if j == 3:
        break
    print(j)
#/ (output : 0,1,2)

#/ List 

names = ["Numan", "Arshad", "Nusrat"]
names.append("Tanzila")  # Adding an item
print(names)  # Output: ['Numan', 'Arshad', 'Nusrat', 'Tanzila']

#/ Tuple

colors = ("yellow", "purple", "grey")
print(colors[1])  # Output: purple

#/  Dictionary

student = {
    "name": "Numan",
    "age": 21,
    "course": "Python"
}
student["age"] = 22  # Updating value
print(student["name"])  # Output: Numan
print (student["age"])  # output : 22

 #/ set (Mutable)
 #/ creating a set 

my_set={4,5,6}
print(my_set)

#/ add number
my_set.add(7)
print (my_set)

#/ remove number
my_set.remove(5)
print(my_set)
