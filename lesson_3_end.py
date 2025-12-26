# --- THE BULK TASK LABELER ---
# This script automates the formatting of a daily work schedule.

# 1. THE DATA (The List)
tasks = ["Check Email", "Code Review", "Team Meeting", "Deep Work", "Lunch", "Bug Fixing"]

# 2. THE PROCESSING (The Loop)
print("--- GENERATING TODAY'S SCHEDULE ---")

# We use 'enumerate' to get both the index (number) and the task name
for index, item in enumerate(tasks):
    
    # Calculate a starting hour (assuming work starts at 9:00 AM)
    hour = 9 + index
    
    # Python does the repetition for us!
    print(f"[{hour}:00] TASK: {item.upper()}")

# 3. THE SUMMARY
print(f"\nTotal tasks automated: {len(tasks)}")
print("Schedule Complete.")

# --- THE CHALLENGE (YOU DO) ---
# 1. Add a new task called "Workout" to the list.
# 2. Add an 'if' statement inside the loop:
#    If the 'item' is "Lunch", print "--- BREAK TIME ---" instead of the task.