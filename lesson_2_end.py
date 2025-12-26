# --- THE SMART GATEKEEPER ---
# This script decides if a user is allowed into a restricted area.

# 1. THE DATA (The Setup)
SECRET_PASSWORD = "python123"

# 2. THE INPUTS
print("--- SECURITY CHECK ---")
age = int(input("Enter your age: "))
password = input("Enter the secret password: ")

# 3. THE LOGIC (The Fork in the Road)
# We check age first, then the password.

if age >= 21 and password == SECRET_PASSWORD:
    print("ACCESS GRANTED: Welcome to the VIP Lounge.")
    
elif age >= 18:
    print("ACCESS GRANTED: Welcome to the General Area.")
    print("Note: You are not old enough for the VIP Lounge.")
    
else:
    print("ACCESS DENIED: You are too young to enter.")
    print("Security has been notified.")

# --- THE CHALLENGE (YOU DO) ---
# 1. Add a new 'elif' for a "Banned User."
# 2. If the user's name is "Bob", print "ACCESS DENIED: Bob is banned from this club!"
# (Hint: You'll need to add a name input at the top first!)