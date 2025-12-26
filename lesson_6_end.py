# --- STANDING ON THE SHOULDERS OF GIANTS ---
# Using external tools to make our script powerful.

# 1. THE BUILT-IN TOOL (Standard Library)
import datetime

# 2. THE EXTERNAL TOOL (Requires 'pip install cowsay' in terminal)
import cowsay

# 3. THE LOGIC
# Get the current time from the 'datetime' module
now = datetime.datetime.now()
formatted_time = now.strftime("%A, %B %d, %Y | %H:%M:%S")

# 4. THE OUTPUT
print("--- SYSTEM START ---")

# Use cowsay to make a fun terminal announcement
cowsay.cow(f"Greetings, Developer!\nToday is: {formatted_time}")

# --- THE CHALLENGE (YOU DO) ---
# 1. Open your terminal and type: pip install wikipedia
# 2. Add 'import wikipedia' at the top of this script.
# 3. Use the tool to look up a summary: 
#    result = wikipedia.summary("Python (programming language)", sentences=2)
# 4. Print the result!