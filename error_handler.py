def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == 'add_contact' or func.__name__ == "change_contact":
                return "The command is bad. Give me name and phone please."
            elif func.__name__ == "contact_phone":
                 return "The command is bad. Give me name"
        except TypeError:
            return "Phone number is invalid"
        except IndexError:
            return "The command is bad. Enter a command again."
        except:
            return "Something is worng. Enter a command again."

    return inner