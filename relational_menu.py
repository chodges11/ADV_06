"""
Provides a basic frontend
"""
# pylint: disable = import-error

import sys
import relational_main as rm


def load_users():
    """
    Loads user accounts from a file
    """
    filename = input('Enter filename of user file: ')
    rm.load_users(filename)


def load_status_updates():
    """
    Loads status updates from a file
    """
    filename = input('Enter filename for status file: ')
    rm.load_status_updates(filename)


def add_user():
    """
    Adds a new user into the database
    """
    user_id = input('User ID: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    email = input('User email: ')
    if rm.add_user(user_id,
                   user_name,
                   user_last_name,
                   email
                   ):
        print("User was successfully added")
    else:
        print("An error occurred while trying to add new user")


def update_user():
    """
    Updates information for an existing user
    """
    user_id = input('User ID: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    email = input('User email: ')
    if rm.update_user(user_id,
                      user_name,
                      user_last_name,
                      email
                      ):
        print("User was successfully updated")
    else:
        print("An error occurred while trying to update user")


def search_user():
    """
    Searches a user in the database
    """
    user_id = input('Enter user ID to search: ')
    result = rm.search_user(user_id)
    if result is None:
        print("ERROR: User does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Name: {result.user_name}")
        print(f"Last name: {result.user_last_name}")
        print(f"Email: {result.user_email}")


def delete_user():
    """
    Deletes user from the database
    """
    user_id = input('User ID: ')
    if not rm.delete_user(user_id):
        print("An error occurred while trying to delete user")
    else:
        print("User was successfully deleted")


def add_status():
    """
    Adds a new status into the database
    """
    status_id = input('Status ID: ')
    user_id = input('User ID: ')
    status_text = input('Status text: ')
    if rm.add_status(status_id, user_id, status_text):
        print("New status was successfully added")
    else:
        print("An error occurred while trying to add new status")


def update_status():
    """
    Updates information for an existing status
    """
    status_id = input('Status ID: ')
    user_id = input('User ID: ')
    status_text = input('Status text: ')
    if rm.update_status(status_id, user_id, status_text):
        print("Status was successfully updated")
    else:
        print("An error occurred while trying to update status")


def search_status():
    """
    Searches a status in the database
    """
    status_id = input('Enter status ID to search: ')
    result = rm.search_status(status_id)
    if result is None:
        print("ERROR: Status does not exist")
    else:
        print(f"User ID: {result.status_id}")
        print(f"Status ID: {result.user_id}")
        print(f"Status text: {result.status_text}")


def delete_status():
    """
    Deletes status from the database
    """
    status_id = input('Status ID: ')
    if not rm.delete_status(status_id):
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")


def quit_program():
    """
    Quits program
    """
    sys.exit()


if __name__ == '__main__':
    rm.init_collections()
    menu_options = {
        'A': load_users,
        'B': load_status_updates,
        'C': add_user,
        'D': update_user,
        'E': search_user,
        'F': delete_user,
        'G': add_status,
        'H': update_status,
        'I': search_status,
        'J': delete_status,
        'Q': quit_program
    }
    while True:
        user_selection = input("""
                            A: Load user database
                            B: Load status database
                            C: Add user
                            D: Update user
                            E: Search user
                            F: Delete user
                            G: Add status
                            H: Update status
                            I: Search status
                            J: Delete status
                            Q: Quit

                            Please enter your choice: """)
        if user_selection.upper() in menu_options:
            menu_options[user_selection.upper()]()
        else:
            print("Invalid option")
