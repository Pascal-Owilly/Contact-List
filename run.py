#!/usr/bin/env python3.9
from contact import Contact

# The shebang line in any script determines the script's ability to be executed like an standalone executable without typing python3.6 beforehand in the terminal. 
# Once we import the contact we create functions that implement the behaiours we have just created
# we runchmod +x run.py then ./run.py then import contact from Contact
# Then we create functions that implment the behaviours we have just created
def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

# We create a save_contacts function that takes in a contact object
#  and then calls the save_contact method to save the contact.
def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()


# We create a del_contact function that takes in a contact object and then calls the delete_contact() method
#  on the contact object deleting it from the contact list.
def del_contact(contact):
    '''
    Function to delete a contact
    '''
    contact.delete_contact()

# We create a function find_contact that takes in a number and calls the Contactclass method find_by_number that returns the contact.
def find_contact(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Contact.find_by_number(number)  

# The function check_existing_contacts takes in a number as an argument and calls the class method contact_exist which returns a boolean.      

def check_existing_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Contact.contact_exist(number)    

# Displaying all contacts
# 
def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_contacts()    



# MAIN FUNCTION
# We have defined the functions that implement the behaviors. Now let us call them.
def main():
    print("Hello Welcome to your contact list. What is your name?")
user_name = input()

print(f"Hello {user_name}. what would you like to do?")
print('\n')

while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

                    if __name__ == '__main__':

                     main()                            