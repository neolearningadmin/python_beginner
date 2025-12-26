for index, item in enumerate(tasks):
    hour = 9 + index
    if item == "Lunch":
        print(f"[{hour}:00] --- BREAK TIME ---")
    else:
        print(f"[{hour}:00] TASK: {item.upper()}")