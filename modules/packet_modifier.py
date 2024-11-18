# modules/packet_modifier.py
import base64
import json

class PacketModifier:
    @staticmethod
    def modify_packet(packet_data, byte_index=2, xor_value=0x01):
        """
        Modifies a specific byte in the packet data and re-encodes to Base64.
        
        Args:
            packet_data (str): The Base64 encoded data to modify.
            byte_index (int): The index of the byte to modify.
            xor_value (int): The value to XOR with the specified byte.
            
        Returns:
            str: Modified packet data in Base64 format.
        """
        # Decode Base64 data
        decoded_data = base64.b64decode(packet_data)

        # Modify the specified byte by XORing it with the given value
        modified_data = bytearray(decoded_data)
        modified_data[byte_index] ^= xor_value  # XOR modification

        # Re-encode to Base64
        return base64.b64encode(modified_data).decode('utf-8')

    @staticmethod
    def modify_packet_json():
        """
        Creates and modifies a sample JSON packet, returning the modified JSON.
        """
        # Original JSON packet
        packet = {
            "rxpk": [
                {
                    "jver": 1,
                    "tmst": 23346853,
                    "chan": 4,
                    "rfch": 0,
                    "freq": 867.300000,
                    "mid": 0,
                    "stat": 1,
                    "modu": "LORA",
                    "datr": "SF12BW125",
                    "codr": "4/5",
                    "rssis": -31,
                    "lsnr": 11.2,
                    "foff": 43,
                    "rssi": -31,
                    "size": 46,
                    "data": "QB5xCyaABAAeLwKbcFZDnKb4kxkJvtXpa1Qlc9TYUldNteYMYfhAbhtYDV/bJQ=="
                }
            ]
        }

        # Modify the Base64-encoded 'data' field
        original_data = packet['rxpk'][0]['data']
        modified_data = PacketModifier.modify_packet(original_data)
        packet['rxpk'][0]['data'] = modified_data

        # Return the modified packet as a JSON string
        return json.dumps(packet, indent=4)
