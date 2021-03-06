# --------------
#Code starts here

print("Step 1:\n")
print(" The first thing you have to do is to write a function that reads the contents of the files that we have.")
print("----------------------------------------------------------------------------------------------------------")

#Function to read file
def read_file(path):
    
    #Opening of the file located in the path in 'read' mode
    file= open(path,'r')
    
    #Reading of the first line of the file and storing it in a variable
    for i in file:
        sentence= i
        break
    
    #Closing of the file
    file.close()
    
    #Returning the first line of the file
    return sentence
    
    

#Calling the function to read file
sample_message= read_file(file_path)

#Printing the line of the file
print(sample_message)

print("----------------------------------------------------------------------------------------------------------")
print("Step 2:\n")
print(" In this task, you have to make use of messages of two different files. In the two files, we have one number each. You have to apply a certain operation to extract our message.")
print("----------------------------------------------------------------------------------------------------------")

#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quotient= int(message_b)//int(message_a)

    #Returning the quotient in string format
    return str(quotient)
    
#Calling the function to read file  
message_1= read_file(file_path_1)
print("Message 1:\n", message_1)

#Calling the function to read file
message_2= read_file(file_path_2)
print("Message 2:\n", message_2)

#Calling the function 'fuse_msg'
secret_msg_1= fuse_msg(message_1, message_2)

#Printing the secret message 
print("Extracted message:\n", secret_msg_1)

print("----------------------------------------------------------------------------------------------------------")
print("Step 3:")
print(" In this task, you have to substitute the message of the file for a secret message.")
print("----------------------------------------------------------------------------------------------------------")

#Function to substitute the message
def substitute_msg(message_c):
    
    #If-else to compare the contents of the file
    if message_c=='Red':
        sub= 'Army General'
    if message_c=='Green':
        sub='Data Scientist'
    if message_c=='Blue':
        sub= 'Marine Biologist'
    
    #Returning the substitute of the message
    return sub
    
    

#Calling the function to read file
message_3= read_file(file_path_3)
print("Message 3:\n", message_3)

#Calling the function 'substitute_msg'
secret_msg_2= substitute_msg(message_3)

#Printing the secret message
print("Secret Message:\n", secret_msg_2)

print('-----------------------------------------------------------------------------------------------------------')
print("Step 4:")
print('In this task, you have to make use of messages from two different files. You have to compare the two messages and take only those words that appear in first message but not in second message')
print('-----------------------------------------------------------------------------------------------------------')

#Function to compare message
def compare_msg(message_d,message_e):
    
    #Splitting the messages into a list
    a_list= message_d.split()
    b_list= message_e.split()

    #Comparing the elements from both the lists
    c_list=[i for i in a_list if i not in b_list]
    
    #Combining the words of a list back to a single string sentence
    final_msg= ' '.join(c_list)
    
    #Returning the sentence
    return final_msg
    

#Calling the function to read file
message_4= read_file(file_path_4)
print("Message 4:\n", message_4)

#Calling the function to read file
message_5= read_file(file_path_5)
print("Message 5:\n", message_5)

#Calling the function 'compare messages'
secret_msg_3= compare_msg(message_4, message_5)

#Printing the secret message
print("Secret Message:\n", secret_msg_3)

print('-------------------------------------------------------------------------------------------------------')
print("Step 5:")
print(" In this task, you have to extract only those words from the message in the file that are of even length")
print('--------------------------------------------------------------------------------------------------------')

#Function to filter message
def extract_msg(message_f):
    
    #Splitting the message into a list
    a_list= message_f.split()
    
    #Creating the lambda function to identify even length words
    even_word= lambda x:len(x)%2==0
    
    #Splitting the message into a list
    b_list= filter(even_word, a_list)
    
    #Combining the words of a list back to a single string sentence
    final_msg= ' '.join(b_list)
    
    #Returning the sentence
    return final_msg
    
#Calling the function to read file
message_6= read_file(file_path_6)
print("Message 6:\n", message_6)

#Calling the function 'filter_msg'
secret_msg_4= extract_msg(message_6)

#Printing the secret message
print("Secret Message:\n", secret_msg_4)

print('-------------------------------------------------------------------------------------------------------')
print("Step 6:")
print(" In this final task, we will combine all the message bits into a single message and write it in a file.")
print("--------------------------------------------------------------------------------------------------------")

#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message
secret_msg=' '.join(message_parts)

#Function to write inside a file
def write_file(secret_msg,path):
       
    #Opening a file named 'secret_message' in 'write' mode
    file = open(path,'a+')

    #Writing to the file
    file.write(secret_msg)

    #Closing the file
    file.close()

#Calling the function to write inside the file    
write_file(secret_msg, final_path)

#Printing the entire secret message
print("Final Secret Message:\n", secret_msg)

#Code ends here


