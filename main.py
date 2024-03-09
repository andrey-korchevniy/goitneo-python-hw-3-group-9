from handlers import add_contact, change_contact, contact_phone, all_contacts

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}
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
                command = parse_input(option)[0]
 
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
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()