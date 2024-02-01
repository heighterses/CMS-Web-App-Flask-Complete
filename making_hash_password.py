# from werkzeug.security import generate_password_hash
#
# def generate_hash(password):
#     # Generate password hash using PBKDF2 with SHA256
#     hash_result = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
#     return hash_result
#
# if __name__ == "__main__":
#     # Get password input from the user
#     password_input = input("Enter the password: ")
#
#     # Generate and print the password hash
#     hashed_password = generate_hash(password_input)
#     print(f"Password Hash: {hashed_password}")
