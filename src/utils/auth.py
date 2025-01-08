import streamlit_authenticator as stauth

# Hardcoded users (replace with your own secure data)
users = [
    {"name": "John Doe", "username": "johndoe", "password": "12345"},
    {"name": "Jane Smith", "username": "janesmith", "password": "password"},
]

# Encrypt passwords
hashed_passwords = stauth.Hasher([user['password'] for user in users]).generate()

# Create authenticator instance
authenticator = stauth.Authenticate(
    {user["username"]: {"name": user["name"], "password": hashed_passwords[i]} for i, user in enumerate(users)},
    "my_app_cookie",
    "my_app_signature",
    cookie_expiry_days=30,
)
