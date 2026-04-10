# Python Password Manager

![Python](https://img.shields.io/badge/Python-3.x-blue)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![Encryption](https://img.shields.io/badge/Security-Fernet-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A command-line password manager built with Python that securely stores credentials using encryption. The project focuses on combining encryption, database handling, and basic security practices in a practical implementation.

---

## Features

* Master password authentication with hidden input (via `getpass`)
* Master password validation before allowing vault access
* Encryption of all stored credentials using Fernet symmetric encryption
* MySQL database storage with automatic table creation on first run
* Add, view, update, and delete passwords
* Password strength checker
* Cryptographically secure password generator (via `secrets` module)

---

## Tech Stack

* Python 3.x
* MySQL
* `cryptography` (Fernet)
* `mysql-connector-python`
* `getpass` (standard library)
* `secrets` (standard library)

---

## Database Setup

No manual SQL setup is required. The table is automatically created when you run the program for the first time.

You only need to create the database beforehand:

```sql
CREATE DATABASE password_manager;
```

Make sure your MySQL credentials in `password_manager.py` match your local setup:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="password_manager"
)
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/lakshitttt/password-manager.git
cd password-manager
```

Install dependencies:

```bash
pip install -r Requirements.txt
```

---

## Usage

Run the program:

```bash
python password_manager.py
```

* Enter your master password (input is hidden — not shown while typing)
* If the vault already has entries, the master password is validated before granting access
* Choose from the menu to manage your credentials:

```
1. Add Password
2. View Passwords
3. Update Password
4. Delete Password
5. Exit
```

When adding or updating a password, you can either enter one manually or let the generator create a strong one for you.

---

## Security Overview

* Uses Fernet symmetric encryption
* Encryption key is derived from the master password using SHA-256
* Master password input is hidden using `getpass` (no echo in terminal)
* Master password is validated against existing vault data before access is granted — incorrect passwords are rejected immediately to prevent database corruption
* Password generator uses Python's `secrets` module for cryptographically secure randomness
* All sensitive data is stored encrypted in MySQL; decryption happens only at runtime

---

## Password Strength Logic

Password strength is evaluated based on:

* Minimum length of 8 characters
* Use of uppercase and lowercase letters
* Inclusion of numbers
* Inclusion of special characters

Scores are rated as **Weak**, **Moderate**, or **Strong**.

---

## Project Structure

```
password-manager/
│
├── password_manager.py
├── Requirements.txt
├── Readme.md
└── LICENSE
```

---

## Disclaimer

This project is built for learning purposes. It does not include all security protections required for production environments (e.g., PBKDF2/bcrypt key derivation, login attempt limiting).

---

## Future Improvements

* Stronger key derivation (PBKDF2 / bcrypt)
* Login attempt restriction
* GUI-based interface
* Encrypted backup and restore
* Search/filter passwords by site name

---

## License

Free to use for educational and personal projects.

---

## Author

Laksh Rajput  
GitHub: https://github.com/lakshitttt
