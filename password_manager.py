import mysql.connector
from cryptography.fernet import Fernet
import base64
import hashlib
import os
import random
import string

#databaseconnecting
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="password_manager"
)

cursor = db.cursor()

#keygeneratingfor further use
def generate_key(master_password):
    key = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(key)

#pass strengthchecking
def check_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

#passgenerator
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

#addpass
def add_password(cipher):
    site = input("Enter site: ")
    username = input("Enter username: ")
    
    choice = input("Generate strong password? (y/n): ")
    
    if choice == 'y':
        password = generate_password()
        print("Generated Password:", password)
    else:
        password = input("Enter password: ")
    
    print("Strength:", check_strength(password))
    
    enc_site = cipher.encrypt(site.encode())
    enc_user = cipher.encrypt(username.encode())
    enc_pass = cipher.encrypt(password.encode())
    
    query = "INSERT INTO vault (site, username, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (enc_site, enc_user, enc_pass))
    db.commit()
    
    print("✅ Stored successfully")

#viewpass
def view_passwords(cipher):
    cursor.execute("SELECT * FROM vault")
    records = cursor.fetchall()
    
    print("\nStored Passwords:\n")
    
    for row in records:
        site = cipher.decrypt(row[1]).decode()
        username = cipher.decrypt(row[2]).decode()
        password = cipher.decrypt(row[3]).decode()
        
        print(f"ID: {row[0]}")
        print(f"Site: {site}")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print("-" * 30)
#deletepass
def delete_password():
    id = input("Enter ID to delete: ")
    cursor.execute("DELETE FROM vault WHERE id=%s", (id,))
    db.commit()
    print("🗑️ Deleted successfully")

#changepass
def update_password(cipher):
    id = input("Enter ID to update: ")
    
    new_password = input("Enter new password (or type 'gen'): ")
    
    if new_password == "gen":
        new_password = generate_password()
        print("Generated:", new_password)
    
    print("Strength:", check_strength(new_password))
    
    enc_pass = cipher.encrypt(new_password.encode())
    
    cursor.execute("UPDATE vault SET password=%s WHERE id=%s", (enc_pass, id))
    db.commit()
    
    print("✏️ Updated successfully")

#main run
def main():
    print("🔐 PASSWORD MANAGER")
    
    master_password = input("Enter master password: ")
    key = generate_key(master_password)
    cipher = Fernet(key)
    
    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Exit")
        
        choice = input("Choose: ")
        
        if choice == '1':
            add_password(cipher)
        elif choice == '2':
            view_passwords(cipher)
        elif choice == '3':
            update_password(cipher)
        elif choice == '4':
            delete_password()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

#finalrun command
if __name__ == "__main__":
    main()
