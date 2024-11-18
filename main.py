# main.py
import subprocess
from modules.hex_decoder import HexDecoder
from modules.node_runner import NodeRunner
from modules.duplicate_finder import DuplicateFinder
from modules.key_generator import continually_update_unique_keys

def main():
    print("\n*****************************************************")
    print("RAL LoRaWAN Security Framework")
    print("*****************************************************\n")

    while True:
        print("\nSelect an option:")
        print("1. Brute Force Join Requests")
        print("2. Generate Session Keys")
        print("3. Convert Packet Format")
        print("4. Decode Hex Packet")
        print("5. Decrypt LoRa Packet")
        print("6. Find Duplicate AppKeys")
        print("7. Generate Unique AppKeys Continuously")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            # Call BruteForcer script
            print("\nLaunching Brute Forcer...")
            subprocess.run(["python3", "lorawan/BruteForcer.py"])

        elif choice == '2':
            # Call SessionKeysGenerator script
            print("\nLaunching Session Keys Generator...")
            subprocess.run(["python3", "lorawan/SessionKeysGenerator.py"])

        elif choice == '3':
            # Call Packet Converter script (assuming it was updated similarly)
            print("\nLaunching Packet Converter...")
            subprocess.run(["python3", "lorawan/packetcon.py"])
       
        elif choice == '4':
            # Call HexDecoder to decode hex packet
            print("\nDecoding Hex Packet...")
            HexDecoder.decode_hex()

        elif choice == '5':
            print("\nDecrypting LoRa Packet...")
            NodeRunner.run_decrypt_packet()
  
        elif choice == '6':
            print("\nFinding Duplicate AppKeys in appkeys.txt...")
            DuplicateFinder.find_duplicates()
 
        elif choice == '7':
            print("\nGenerating unique AppKeys every 2 seconds (press Ctrl+C to stop)...")
            continually_update_unique_keys(interval=2)


        elif choice == '8':
            print("\nExiting LoRaWAN Security Framework.")
            break


        else:
            print("Invalid option selected. Please choose a valid option.\n")

if __name__ == "__main__":
    main()
