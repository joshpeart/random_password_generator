#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

#User defines the number of letters, symbols and numbers
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Temporary list to store the required random letters in the password
letters_container = []
letters_index = 0
x = range(nr_letters)


#Iterate and append letters to the list
for i in x:
  letters_container.append(letters[(random.randint(1,52))-1])
  letters_index += 1

#Temporary list to store the required random numbers in the password
numbers_container = []
numbers_index = 0
y = range(nr_numbers)

#Iterate and append numbers to the list
for i in y:
  numbers_container.append(numbers[(random.randint(1,9))-1])
  numbers_index +=1

#Temporary list to store the required random symbols in the password
symbols_container = []
symbols_index = 0
z = range(nr_symbols)

#Iterate and append symbols to the list
for i in z:
  symbols_container.append(symbols[(random.randint(1,9))-1])
  symbols_index +=1

#Combine the temporary indices for the total password length
password_length = numbers_index + letters_index + symbols_index

#Combine the temporary lists that we will later randomize
password_container = letters_container + numbers_container +symbols_container

#Will use to iterate in our For loop
v = range(password_length)

#List that we will used to store the randomly selected item from password_container to build our random password
password = []
password_temp_length = password_length

for i in v:
    
    random_index = random.randint(1,password_temp_length)

    password.append(password_container[(random_index-1)])
    del password_container[random_index-1]  
    password_temp_length -= 1

password_final = ''.join(password)
print(f"Your randomized password is: {password_final}")
