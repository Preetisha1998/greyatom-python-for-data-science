# --------------
# Code starts here
print("Step 1\n")
print("Create a new register by combining data from two classes while making some modifications to the register.")

# Create the lists 
class_1= ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2= ['Hilary Mason','Carla Gentry','Corinna Cortes']
print("Class 1:\n {} \n Class 2:\n {}".format(class_1,class_2))
# Concatenate both the strings
new_class= class_1+class_2 # New class
print("New class:\n", new_class)
# Append the list
new_class.append('Peter Warden')
# Print updated list
print("The updated class list:\n", new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print("The final list is:\n", new_class)
print("\n \n")

print("Step 2\n")
print(" create a dictionary for Geoffrey Hinton in each subject to generate his progress report.\n")


# Create the Dictionary
print("Below are the details of 'Geoffery Hinton\n")
courses= {'Math':65,'English':70,'History':80,'French':70,'Science':60}

# Slice the dict and stores  the all subjects marks in variable
marks=[]
for key, value in courses.items():
    marks.append(value)
print("Marks:\n", marks)
# Store the all the subject in one variable `Total`
total= sum(marks)

# Print the total
print("Total marks:\n", total)

# Insert percentage formula
percentage= (total/500)*100

# Print the percentage
print("Percentage of marks scored by Geoffery Hinton is:\n {}%".format(percentage))
print("\n \n")

# Create the Dictionary
print("Step 3\n")
print(" For the student who got the highest marks in this subject, the school has decided to award a scholarship. Let's check who performed best in mathematics from all the students who appeared for the test.\n") 

mathematics= {'Geoffery Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}

topper=max(mathematics,key= mathematics.get)
print("The topper is:\n", topper)
print("\n \n")


print("Step 4")
print(" From the previous task, we know who is the 'Maths' topper in the class. You now have to print the name of the student on the certificate, but you will have to print his last name and then his first name.\n")
# Given string
print("The 'Maths' topper is:" ,topper)

# Create variable first_name 
first_name= topper.split()[0]

# Create variable Last_name and store last two element in the list
last_name= topper.split()[1]

# Concatenate the string
full_name= last_name+" "+first_name

# print the full_name
print("Full name is:\n", full_name)

# print the name in upper case
certificate_name= full_name.upper()
print("The name to be displayed on the certificate is:\n", certificate_name)

# Code ends here


