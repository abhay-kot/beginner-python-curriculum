import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
operating_systems = ["Windows", "macOS", "Linux"]
print(operating_systems[len(operating_systems) - 1])  # Print the last operating system
operating_systems.reverse()  # Reverse the list
print(operating_systems)  # Print the reversed list


# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
school_subjects = ["Math", "Science", "English", "History"]
print(school_subjects[1])  # Print the second subject
school_subjects.sort()  # Sort the list alphabetically
print(school_subjects)  # Print the sorted list 


# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.



# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
programming_languages = ["Python", "JavaScript"]
print(random.choice(programming_languages))  # Print a random programming language
programming_languages.append("Java")  # Append another language


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = ["pass1", "pass2", "pass3", "pass4", "pass5", "pass6"]
middle_index = len(passwords) // 2  # Calculate the index of the middle password
print(passwords[middle_index])  # Print the middle password
removed_password = passwords.pop(0)  # Remove the first password and store it
print(removed_password)  # Print the removed password
print(passwords)  # Print the remaining list of passwords   