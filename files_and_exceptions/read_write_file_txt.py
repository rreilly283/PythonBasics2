
#by default it opens the file as read-only
with open('./../data/students.txt') as students:
    names=students.read()
    print(names)

with open('./../data/students.txt', 'a') as students:
    students.write("\nLionel Messi")

with open('./../data/students.txt') as students:
    names=students.read()
    print(names)

msg="_hello_class_welcome_to_python!"
print(msg)
print(msg.replace("_", " "))
print(msg)
words= msg.split("_")
print(words)
print(f"there are {len(words)} number of words in the phrase")

msg1=input('enter the sentence to count words:')
words = msg1.split()
print(f"there are {len(words)} number of words in the phrase")

#garbage collector