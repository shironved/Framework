LoRaWAN Security Framework

The LoRaWAN Security Framework is a comprehensive toolset for testing and analyzing the security of LoRaWAN networks. It includes functionality for brute-forcing join requests, generating session keys, modifying and decrypting LoRa packets, and managing unique AppKeys.
Features

    Brute Force Join Requests: Test AppKeys to identify valid keys for join requests and join accepts.
    Generate Session Keys: Create secure session keys (AppSKey and NwkSKey) from join requests and join accepts.
    Convert Packet Formats: Switch between Hex and Base64 formats for LoRa packets.
    Modify JSON Packet Data: Decode, alter, and re-encode JSON packet payloads.
    Decrypt LoRa Packets: Decrypt encrypted LoRaWAN packets using AppSKey and NwkSKey.
    Detect Duplicate AppKeys: Scan a list of AppKeys to find duplicates.
    Generate Unique AppKeys: Continuously generate unique AppKeys and save them to a file.
    Support for Large Files: Manage large files with Git LFS to stay within GitHub size limits.

Installation

Follow these steps to set up and run the framework on your system:
1. Clone the Repository

git clone https://github.com/shironved/Framework.git
cd Framework

2. Install Python Dependencies

    Install the required Python packages using the requirements.txt file:

pip install -r requirements.txt

3. Install Node.js Dependencies

    If you’re using the Node.js-based decryption functionality, install dependencies via npm:

npm install

4. Initialize Git LFS (if necessary)

    If the repository includes large files managed with Git LFS:

git lfs install
git lfs pull

Usage

Run the framework's main script:

./run.sh

Menu Options

When you run the framework, you'll see the following options:

    Brute Force Join Requests
    Launch the brute force module to test AppKeys with join requests.

    Generate Session Keys
    Generate AppSKey and NwkSKey from join request and join accept messages.

    Convert Packet Format
    Convert LoRaWAN packets between Hex and Base64 formats.

    Modify JSON Packet
    Decode a JSON packet payload, modify a specific byte, and re-encode it.

    Decode Hex Packet
    Decode a hex string into readable UTF-8 text.

    Decrypt LoRa Packet
    Decrypt a LoRaWAN packet using AppSKey and NwkSKey.

    Find Duplicate AppKeys
    Scan an AppKey list (appkeys.txt) to identify duplicate keys.

    Generate Unique AppKeys Continuously
    Generate unique AppKeys every few seconds and save them to appkeys.txt.

File Structure

The framework is organized as follows:

Framework/
├── main.py                  # Main entry point for the framework
├── requirements.txt         # Python dependencies
├── package.json             # Node.js dependencies
├── appkeys.txt              # Example AppKeys file for testing
├── modules/                 # Framework modules
│   ├── brute_force.py       # Brute-forcing functionality
│   ├── session_keys.py      # Session key generation
│   ├── packet_converter.py  # Hex and Base64 conversion
│   ├── packet_modifier.py   # JSON packet modification
│   ├── hex_decoder.py       # Hex packet decoding
│   ├── node_runner.py       # Node.js integration
│   └── duplicate_finder.py  # Detect duplicate AppKeys
├── scripts/                 # Original Python scripts
│   ├── BruteForcer.py       # Brute-forcing script
│   ├── SessionKeysGenerator.py # Session key generation script
│   └── packetcon.py         # Packet conversion script
└── node_modules/            # Node.js dependencies (if applicable)

