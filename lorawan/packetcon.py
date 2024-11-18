import binascii
import base64

def hex_to_base64(hex_string):
    # Remove any spaces and then convert hex to bytes, then encode to base64
    hex_string = hex_string.replace(" ", "")  # Remove any spaces
    bytes_data = binascii.unhexlify(hex_string)
    base64_data = base64.b64encode(bytes_data)
    return base64_data.decode('utf-8')

def base64_to_hex(base64_string):
    # Decode base64 to bytes, then convert to hex
    bytes_data = base64.b64decode(base64_string)
    hex_data = binascii.hexlify(bytes_data)
    return hex_data.decode('utf-8')

def detect_and_convert(packet):
    # Remove spaces for detection and processing
    packet = packet.replace(" ", "")  # Remove any spaces
    try:
        # Try to convert assuming it's hex
        bytes.fromhex(packet)
        # If successful, it's hex, so convert to base64
        print("Detected hex format. Converting to base64:")
        return hex_to_base64(packet)
    except ValueError:
        # If it's not hex, assume it's base64
        try:
            # Try to decode as base64 to verify
            base64.b64decode(packet)
            print("Detected base64 format. Converting to hex:")
            return base64_to_hex(packet)
        except binascii.Error:
            return "Invalid input format. Please enter a valid hex or base64 packet."

# Main function to prompt user
def main():
    packet = input("Enter the packet (hex or base64): ").strip()
    result = detect_and_convert(packet)
    print("Converted result:", result)

if __name__ == "__main__":
    main()
