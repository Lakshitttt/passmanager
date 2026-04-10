# Python Password Manager

![Python](https://img.shields.io/badge/Python-3.x-blue)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![Encryption](https://img.shields.io/badge/Security-Fernet-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A command-line password manager built with Python that securely stores credentials using encryption. The project focuses on combining encryption, database handling, and basic security practices in a practical implementation.

---

# Features

* Master password authentication
* Encryption of all stored credentials
* MySQL database storage
* Add, view, update, and delete passwords
* Password strength checker
* Strong password generator

---

# Tech Stack

* Python
* MySQL
* cryptography (Fernet)
* mysql-connector-python

---

# Database Setup

Run the following SQL commands:

```sql
CREATE DATABASE password_manager;

USE password_manager;

CREATE TABLE vault (
    id INT AUTO_INCREMENT PRIMARY KEY,
    site BLOB,
    username BLOB,
    password BLOB
);
```

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/lakshiiitttt/password-manager.git
cd password-manager
```

Install dependencies:

```bash
pip install cryptography mysql-connector-python
```

---

# Usage

Run the program:

```bash
python main.py
```

* Enter your master password
* Choose from the menu to manage credentials

---

# Security Overview

* Uses Fernet symmetric encryption
* Encryption key is derived from the master password
* All sensitive data is stored in encrypted form in MySQL
* Decryption happens only during runtime

---

# Password Strength Logic

Password strength is evaluated based on:

* Minimum length of 8 characters
* Use of uppercase and lowercase letters
* Inclusion of numbers
* Inclusion of special characters

---

#Project Structure

```
password-manager/
│
├── main.py
├── README.md
└── requirements.txt
```

---

# Disclaimer

This project is built for learning purposes. It does not include advanced security protections required for production environments.

---

# Future Improvements

* Stronger key derivation (PBKDF2 / bcrypt)
* Hidden master password input
* Login attempt restriction
* GUI-based interface
* Encrypted backup and restore

---
# License

Free to use for educational and personal projects.

---

# Author

Laksh Rajput
GitHub: https://github.com/lakshiiitttt
