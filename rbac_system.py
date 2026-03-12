users = {
    "admin": "admin",
    "manager": "manager",
    "user": "user"
}

permissions = {
    "admin": ["read", "write", "delete"],
    "manager": ["read", "write"],
    "user": ["read"]
}

def authenticate(username):
    if username in users:
        role = users[username]
        print("\nAuthentication successful")
        print(f"User: {username}")
        print(f"Role: {role}")
        print(f"Permissions: {permissions[role]}")
    else:
        print("Authentication failed")

def main():
    print("RBAC Authentication System")
    print("--------------------------")

    username = input("Enter username: ")
    authenticate(username)

if __name__ == "__main__":
    main()
