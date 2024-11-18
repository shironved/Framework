# modules/hex_decoder.py

class HexDecoder:
    @staticmethod
    def decode_hex():
        """
        Prompts the user to enter a hex string and decodes it to plaintext.
        """
        hex_string = input("Please enter the hex packet to decode: ")

        try:
            # Convert the hex string to bytes, then decode to get the plaintext message
            decoded_text = bytes.fromhex(hex_string).decode("utf-8")
            print("Decoded text:", decoded_text)
        except ValueError:
            print("Invalid hex input. Please ensure you enter a valid hexadecimal string.")
