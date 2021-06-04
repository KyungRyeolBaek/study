name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
a = dict()
for line in handle:
    if not line.startswith('From:'): continue
    a[line.split()[1]] = a.get(line.split()[1], 0) + 1
#for key in a:
#    if a[key] == max(a.values()):
#        print(key, max(a.values()))
largest = 0
email = None
for key, value in a.items():
    if largest < value:
        largest = value
        email = key
print(email, largest)

# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Desired Output
# cwen@iupui.edu 5