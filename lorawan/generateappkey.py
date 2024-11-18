import secrets
import time

def generate_unique_appkey(existing_keys):
    """Generates a unique 128-bit AppKey in hex format, ensuring no duplicates."""
    while True:
        app_key = secrets.token_hex(16)  # Generates a 16-byte (128-bit) hex key
        if app_key not in existing_keys:
            existing_keys.add(app_key)
            return app_key

def continually_update_unique_keys(filename="appkeys.txt", interval=2):
    """Generates and appends a new unique AppKey to a text file at regular intervals."""
    existing_keys = set()

    # Load any previously generated keys from the file to prevent duplicates
    try:
        with open(filename, "r") as file:
            for line in file:
                key = line.strip()
                if key:  # Ignore empty lines
                    existing_keys.add(key)
    except FileNotFoundError:
        pass  # No file exists yet, so no keys are loaded

    # Start generating unique keys
    try:
        with open(filename, "a") as file:
            while True:
                # Generate a unique key and add it to the file
                app_key = generate_unique_appkey(existing_keys)
                file.write(f"{app_key}\n")
                file.flush()  # Ensure the write is saved immediately
                print(f"Generated unique AppKey: {app_key} (Appended to {filename})")
                
                # Wait for the specified interval before generating the next key
                time.sleep(interval)
    except KeyboardInterrupt:
        print("Stopped key generation.")

# Start generating unique keys, updating every 5 seconds (adjust interval as needed)
continually_update_unique_keys(interval=2)
