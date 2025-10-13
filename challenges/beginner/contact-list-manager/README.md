# 📇 Contact List Manager

**Difficulty**: Beginner  
**Estimated Time**: 30-45 minutes  
**Topics**: Data Structures (Lists/Arrays, Dictionaries/Maps), User Input, Loops, Functions

## 📝 Challenge Description

Create a simple command-line contact list manager. The program should allow users to add, view, and delete contacts.

## 🎯 Requirements

Your program must support the following commands:

1.  **`add`**: Prompt the user for a name and phone number, then add them to the contact list.
2.  **`view`**: Display all contacts in a clean, readable format.
3.  **`delete`**: Prompt the user for a name to delete and remove that contact.
4.  **`exit`**: Terminate the program.
5.  The program should run in a loop, continuously asking for commands until the user types `exit`.

## 📊 Example Interaction

```
--- Contact List Manager ---
Commands: add, view, delete, exit

Enter a command: add
Enter name: Alice
Enter phone number: 123-456-7890
Contact 'Alice' added.

Enter a command: add
Enter name: Bob
Enter phone number: 987-654-3210
Contact 'Bob' added.

Enter a command: view
--- Your Contacts ---
1. Alice - 123-456-7890
2. Bob - 987-654-3210
---------------------

Enter a command: delete
Enter name to delete: Alice
Contact 'Alice' deleted.

Enter a command: view
--- Your Contacts ---
1. Bob - 987-654-3210
---------------------

Enter a command: exit
Goodbye!
```

## 🛠️ Implementation Guidelines

*   You are free to use **any programming language**.
*   Use a suitable data structure to store the contacts (e.g., a list of dictionaries in Python, an array of objects in JavaScript).
*   Break your code into functions to handle different commands (e.g., `add_contact()`, `view_contacts()`, `delete_contact()`).

## 🧪 How to Test Your Solution

1.  Run your program.
2.  Add a few contacts.
3.  View the list to ensure they were added correctly.
4.  Delete a contact and view the list again to confirm removal.
5.  Try to delete a contact that doesn't exist and ensure your program handles it gracefully.
6.  Add your solution file to the `solutions/` directory in a sub-folder named after your GitHub username.

Happy coding! 🚀
