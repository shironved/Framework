# modules/brute_force.py
import subprocess

class BruteForcer:
    @staticmethod
    def run_brute_force(first_packet, second_packet, keys_path, dont_generate_keys=True):
        # Adjust the `dont_generate_keys` value to be a string argument
        dont_generate_keys_flag = "--no-generate" if dont_generate_keys else ""
        
        # Create the command, filtering out any empty arguments
        command = [
            "python3", "lorawan/BruteForcer.py",
            first_packet, second_packet, keys_path
        ]

        # Add the flag conditionally
        if dont_generate_keys_flag:
            command.append(dont_generate_keys_flag)
        
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        return result.stdout
