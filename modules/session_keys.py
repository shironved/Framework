# modules/session_keys.py
import subprocess

class SessionKeysGenerator:
    @staticmethod
    def generate_session_keys(jaccept, jrequest, app_key):
        command = [
            "python3", "lorawan/SessionKeysGenerator.py",
            "-a", jaccept,
            "-r", jrequest,
            "-k", app_key
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        return result.stdout
