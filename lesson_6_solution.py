import wikipedia

# The Solution
print("\nFetching data from the web...")
summary = wikipedia.summary("Python (programming language)", sentences=1)
print(f"DID YOU KNOW? {summary}")