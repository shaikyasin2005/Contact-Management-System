# Contact Management System Using Python

## Project Overview

The Contact Management System is a console-based Python application that allows users to store, manage, search, update, and delete contact information. It uses JSON file storage to save contact details permanently, so the data remains available when the application is restarted.

## Problem Statement

Managing contact information manually can be difficult when the number of contacts increases. Finding, updating, and maintaining contact details becomes time-consuming.

This project provides a simple and organized solution for managing contact information using Python and JSON file handling.

## Objectives

- Develop a menu-driven contact management application.
- Store contact details in a structured format.
- Implement operations to add, view, search, update, and delete contacts.
- Validate phone numbers and email addresses.
- Store contact information permanently using JSON.
- Handle invalid inputs and file-related errors.

## Key Features

### 1. Add Contact

- Add a new contact with name, phone number, email address, and postal address.
- Validate phone number and email format.
- Prevent duplicate phone numbers.

### 2. View All Contacts

- Display all saved contacts.
- Sort contacts alphabetically by name.

### 3. Search Contact

- Search contacts using a name or phone number.
- Display matching contact details.

### 4. Update Contact

- Update an existing contact's name, email address, or postal address.
- Keep existing values by pressing Enter.

### 5. Delete Contact

- Delete a contact using its phone number.
- Ask for confirmation before deletion.

### 6. JSON Data Storage

- Store contact information in a JSON file.
- Load saved contacts when the application starts.
- Save changes when contacts are added, updated, or deleted.

### 7. Input Validation and Error Handling

- Validate phone numbers using regular expressions.
- Perform basic email format validation.
- Handle missing, unreadable, or invalid JSON files.

## Technologies Used

| Technology | Purpose |
| --- | --- |
| Python | Core programming language |
| JSON | Persistent contact data storage |
| Regular Expressions (`re`) | Phone number and email validation |
| `pathlib` | File path management |
| File Handling | Reading and writing contact data |

## Application Workflow

1. The application starts and loads existing contacts from `contacts.json`.
2. A menu displays the available operations.
3. The user selects an operation.
4. The application performs the requested action.
5. Input validation checks the provided information where applicable.
6. Changes are saved to the JSON file.
7. The menu appears again until the user selects Exit.

## Project Structure

```text
Contact-Management-System/
├── contact_manager.py
├── contacts.json
└── README.md
```

- `contact_manager.py` - Contains the main application code.
- `contacts.json` - Stores contact information and is created when data is saved.
- `README.md` - Contains project documentation.

Note: The JSON file may not exist until the application saves its first contact.

## Installation and Setup

### Prerequisites

- Python 3.8 or later
- Visual Studio Code or another Python-compatible editor
- Git, if you want to clone the repository

### Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Navigate to the Project Folder

```bash
cd Contact-Management-System
```

Use your actual project folder name if it differs.

### Step 3: Run the Application

```bash
python contact_manager.py
```

On some systems, use:

```bash
python3 contact_manager.py
```

No external Python packages are required because the project uses Python's standard library.

## How to Use

After running the application, the following menu appears:

```text
===== CONTACT MANAGEMENT SYSTEM =====
1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6):
```

Enter the corresponding number to perform an operation.

- Enter `1` to add a contact.
- Enter `2` to view all contacts.
- Enter `3` to search for a contact.
- Enter `4` to update a contact.
- Enter `5` to delete a contact.
- Enter `6` to exit the application.

## Data Storage

The application stores contact details in a JSON file named `contacts.json`.

Each contact contains the following fields:

- Name
- Phone number
- Email address
- Postal address

Example JSON structure:

```json
{
    "+919876543210": {
        "name": "Example User",
        "phone": "+919876543210",
        "email": "example@gmail.com",
        "address": "Hyderabad, India"
    }
}
```

The example uses fictional contact information. Do not upload real personal contact details to a public GitHub repository.

## Advantages

- Simple and user-friendly menu-driven interface.
- Persistent data storage using JSON.
- Supports essential contact management operations.
- Uses functions to organize the code.
- Includes basic input validation and error handling.
- Does not require third-party libraries.

## Limitations

- The application runs in the terminal and does not have a graphical user interface.
- Phone number validation checks the format, not whether the number is active.
- Email validation checks the basic format, not whether the email exists.
- Phone numbers are checked for exact duplicates, so different formats of the same number may be stored separately.
- The application does not include user authentication or encryption.

## Future Enhancements

- Develop a graphical user interface using Tkinter.
- Add contact grouping and category management.
- Implement more advanced phone number validation.
- Add sorting and filtering options.
- Introduce authentication and secure data storage.
- Add export and import functionality.
- Develop a web-based version using Flask or Django.

## Applications

- A personal contact management tool.
- A Python beginner project for learning functions and file handling.
- A practical demonstration of JSON data storage and regular expressions.
- A portfolio project for entry-level Python Developer roles.

## Author

**Shaik Yasin**

GitHub: [shaikyasin2005](https://github.com/shaikyasin2005)

## License

This project is intended for educational and personal portfolio purposes. A formal open-source license has not been specified.
