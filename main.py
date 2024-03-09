from classes import AddressBook
from handlers import add_contact, change_contact, contact_phone, all_contacts, add_birthday, show_birthday, birthdays

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            response = add_contact(args, contacts)
            
            if 'overwrite' in response:
                option = input(response)
                try:
                    command = parse_input(option)[0]
                except ValueError:
                    print('Saving the contact was cancelled')
                    continue
                 
                if command == 'yes':
                    print(add_contact(args, contacts, True))
                else:
                    print('Saving the contact was cancelled')
            else:
                print(response)
                    
        elif command == 'change':
            print(change_contact(args, contacts))
            
        elif command == 'phone':
            print(contact_phone(args, contacts))
            
        elif command == 'all':
            print(all_contacts(contacts))
            
        elif command == 'add-birthday': 
            response = add_birthday(args, contacts)
            print(response)
            
        elif command == 'show-birthday':
            response = show_birthday(args, contacts)
            print(response)

        elif command == 'birthdays':
            birthdays(contacts)
            
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()