# --- THE AI PERSONA GENERATOR ---
# This script automates the creation of a digital bio.

# 1. THE INPUTS (The 'Mailboxes')
name = input("Enter your name: ")
vibe = input("What is your vibe? (e.g. Chaotic, Professional, Chill): ")
skill = input("What is your #1 skill? ")

# 2. THE LOGIC (The 'Processing')
# We are combining the mailboxes into one message.
# The 'f' stands for 'Format'—it lets us drop variables into text.

bio = f"--- DIGITAL PERSONA: {name.upper()} ---"
description = f"Known for being incredibly {vibe}, {name} spends time mastering {skill}."
status = "Status: Online and Building with Python."

# 3. THE OUTPUT (The 'Result')
print("\n" + "="*30) # Visual separator for the terminal
print(bio)
print(description)
print(status)
print("="*30 + "\n")

# --- THE CHALLENGE (YOU DO) ---
# 1. Add a new input for 'location'.
# 2. Update the 'description' to include that location.
# 3. Print a final line saying: "Currently based in [location]."