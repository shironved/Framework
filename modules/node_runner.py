# modules/node_runner.py
import subprocess

class NodeRunner:
    @staticmethod
    def run_decrypt_packet():
        """
        Calls the Node.js script `decrypt_packet.js` to prompt for packet and keys, then decrypts the payload.
        """
        try:
            # Run the Node.js script
            subprocess.run(["node", "node_modules/decrypt_packet.js"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running decrypt_packet.js: {e}")
