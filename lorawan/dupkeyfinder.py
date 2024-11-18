from collections import Counter

def find_duplicates(filename="appkeys.txt"):
    """Reads AppKeys from a file, identifies duplicates, and prints them."""
    
    # Read keys from the file
    try:
        with open(filename, "r") as file:
            keys = [line.strip() for line in file if line.strip()]  # Remove any empty lines

        # Count occurrences of each key
        counter = Counter(keys)

        # Identify and print duplicates
        duplicates = [key for key, count in counter.items() if count > 1]
        if duplicates:
            print("Duplicate keys found:")
            for key in duplicates:
                print(f"{key} (appears {counter[key]} times)")
        else:
            print("No duplicates found.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Call the function to check for duplicates in appkeys.txt
find_duplicates("appkeys.txt")
