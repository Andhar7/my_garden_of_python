# Email
# Must not be empty
# Must contain exactly one @ symbol
# Must end with '.com', '.org', '.net'
# Must not be longer then 254 characters
# Must start and end with a letter or digit

email = "andrej@kling.com"

# Clean the string
email = email.strip()

if email == "":
    print("Email is empty")
elif not (
    "." in email and "@" in email
):  # Check is not True. '.' in email - False. and '@' in email - False
    print("Email must contain @ and '.' ")
elif email.count("@") != 1:
    print("Email must contain only one @ symbol!")
elif not (
    email.endswith((".com", ".org", ".net"))
):  # Check is not True. '.' in email - False. and '@' in email - False
    print("Email must contain '.com', '.org', '.net'")
elif len(email) > 256:
    print("Email must contain only 256 characters")
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with letter or digit")
else:
    print("Email is valid")
    

email = "andrej@kling.com"

# Clean the string
email = email.strip()
valid = True

if email == "":
    print("Email is empty")
    valid = False
if not (
    "." in email and "@" in email
):  # Check is not True. '.' in email - False. and '@' in email - False
    print("Email must contain @ and '.' ")
    valid = False
if email.count("@") != 1:
    print("Email must contain only one @ symbol!")
    valid = False
if not (
    email.endswith((".com", ".org", ".net"))
):  # Check is not True. '.' in email - False. and '@' in email - False
    print("Email must contain '.com', '.org', '.net'")
    valid = False
if len(email) > 256:
    print("Email must contain only 256 characters")
    valid = False
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with letter or digit")
    valid = False
if valid:
    print("Email is valid")
    

# Password
# Must be at least 8 characters
# Must include at least 1 uppercase
# Must include at least 1 lowercase
# Must not be same as email
# Must not contain any spaces
# Must start and end with a letter or digit

password = "dsdsQ"
password = password.strip()

valid = True

if password == "":
    print("Password is empty")
    valid = False
if len(password) <= 8:
    print("Password should be at least 8 characters please")
    valid = False
if not any(char.isupper() for char in password):
    print("Password must contain at least 1 character of uppercase")
    valid = False
if not any(char.islower() for char in password):
    print("Password must contain at least 1 character of lowercase")
    valid = False
if password == email:
    print("Password can´t to be same like email")
    valid = False
if " " in password:
    print("Password must not contain any spaces")
    valid = False
if not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with letter or digit")
    valid = False
if valid:
    print("Password is valid!")
