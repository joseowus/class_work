# question 3 creating a set 
names = {"joseph", "Godwin", "mboya", "maurice"}
print(names)
#Question 4 adding an element or member to a set
names.add("daniel")
print(names)

#Question 5 Display numbers from -10 to -1 using for loop
for number in range(-10, 0):
    print(number)
    
#Question 9 Given two lists of strings list1 and list2, find the common strings in the two lists. A common string is a string that appears in both list1 and list2. 

def find_common_strings(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    common_strings = set1.intersection(set2)
    
    return list(common_strings)

# Example usage:
list1 = ["apple", "banana", "orange", "kiwi"]
print(list1)
list2 = ["kiwi", "grape", "apple", "pear"]
print(list2)
result = find_common_strings(list1, list2)
print("Common Strings:", result)

# QUESTION 1 Write a Python script to add a key to a dictionary.
Sample_Dictionary : {0: 10, 1: 20}
Expected_Result : {0: 10, 1: 20, 2: 30}

# Sample Dictionary
sample_dict = {0: 10, 1: 20}

# Add a new key-value pair
new_key = 2
new_value = 30
sample_dict[new_key] = new_value

# Print the updated dictionary
print("Updated Dictionary:", sample_dict)

