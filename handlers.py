from error_handler import input_error
import re

PHONE_MASK = r"[0-9+()\s-]+"
BLUE = '\033[94m'
ENDC = '\033[0m'


@input_error
def add_contact(args, contacts, is_consent=False):
    name, phone = args
    
    if not bool(re.fullmatch(PHONE_MASK, phone)):
        raise TypeError
   
    if name in contacts and not is_consent:
        return f"Here is a contact with name {name} yet. To overwrite? Type yes/no: "
    
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    
    if name not in contacts:
        return f"There isn't a contacts with name {name}"
    
    if bool(re.match(PHONE_MASK, phone)):
        raise TypeError
    
    contacts[name] = phone
    return 'Contact changed'


def contact_phone(args, contacts):
    name = args[0]
    
    if name not in contacts:
        return f"There isn't a contacts with name {name}"
    
    return contacts[name]
    

def all_contacts(contacts):
    if not contacts:
        return "No contacts to display."

    max_name_length = max(len(contact) for contact in contacts.keys())
    contact_list = ''
    
    for contact, phone in contacts.items():
        contact_list += f"{BLUE}{contact:<{max_name_length}}{ENDC}: {phone}\n"
    return contact_list

