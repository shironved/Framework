# modules/packet_converter.py
import subprocess

class PacketConverter:
    @staticmethod
    def convert_packet(packet):
        command = [
            "python3", "lorawan/packetcon.py", packet
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
        return result.stdout
