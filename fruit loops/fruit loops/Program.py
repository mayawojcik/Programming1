colors = ["red", "green", "blue"]
print(colors) # will print list
print (colors[1]) # will print green
print("")

fruits = ["apple", "banana", "orange", "kiwi", "mango"]
# For-each loop
for item in fruits:
	print(item)
print("")

# For loop
for index in range(len(fruits)): # range(0, len(fruits))
	# len = length of list
	print(fruits[index])
print("")

# lastfruit = fruits[len(fruits)-1]
lastfruit = fruits[-1] # shows last item of the list
# [-1] the one can be any number and it will count backwards from the list
print(lastfruit)
input()

