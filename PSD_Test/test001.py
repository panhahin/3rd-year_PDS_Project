# TP2 - Group 2 - Problem 2: My Shopping List
# Members: <name 1>, <name 2>, <name 3>, <name 4>

# Step 1
shopping = ["rice", "eggs", "milk"]
print("Start :", shopping)

# Step 2
shopping.append("bread")
shopping.insert(0, "water")
print("Added :", shopping)

# Step 3
shopping.remove("eggs")
last = shopping.pop()
print("Removed :", last)
print("Now :", shopping)

# Step 4
print("First 2 :", shopping[:2])
print("Last 2 :", shopping[-2:])
print("Reversed:", shopping[::-1])

# Step 5
print("Is milk in the list?", "milk" in shopping)
for i, item in enumerate(shopping, start=1):
    print(i, item)

# Q1. remove() vs pop()
# remove(value) deletes the first item that EQUALS the value.
# pop() deletes an item by POSITION (the last one by default)

# Q2. What happens with shopping.remove("fish")?
try:
    shopping.remove("fish")
except ValueError as error:
    print("Error:", error)  # list.remove(x): x not in list

# Q3. Does slicing change the original list?
# No. A slice creates a NEW list. We can check by printing
# the original list after slicing: it is the same as before.
first_two = shopping[:2]
print("Slice    :", first_two)
print("Original :", shopping)