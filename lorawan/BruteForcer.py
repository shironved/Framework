# BruteForcer.py
# LoRaWAN Security Framework - BruteForcer
# Copyright (c) 2019 IOActive Inc.  All rights reserved.

import base64
import sys
import lorawanwrapper.LorawanWrapper as LorawanWrapper

keys = []

def bruteforce_accept_request(ja, jr, dont_generate_keys):
    global keys
    jr_result = LorawanWrapper.testAppKeysWithJoinRequest(keys, jr, dont_generate_keys)  

    if len(jr_result) > 0:
        valid_keys = [bytes(valid_key.upper(), encoding='utf-8') for valid_key in jr_result.split()]
        ja_result = LorawanWrapper.testAppKeysWithJoinAccept(valid_keys, ja, dontGenerateKeys=True)

        if len(ja_result) > 0:
            print("\n**** Key found: %s **** \n" % (ja_result.split()[0]))

def bruteforce_two_join_requests(jr1, jr2, dont_generate_keys):
    global keys
    jr_1_result = LorawanWrapper.testAppKeysWithJoinRequest(keys, jr1, dont_generate_keys)

    if len(jr_1_result) > 0:
        valid_keys = [bytes(valid_key.upper(), encoding='utf-8') for valid_key in jr_1_result.split()]
        jr_2_result = LorawanWrapper.testAppKeysWithJoinRequest(valid_keys, jr2, dontGenerateKeys=True)

        if len(jr_2_result) > 0:
            print("\n**** Key found: %s **** \n" % (jr_2_result.split()[0]))

def bruteforce_two_join_accepts(ja1, ja2, dont_generate_keys):
    global keys
    ja1_result = LorawanWrapper.testAppKeysWithJoinAccept(keys, ja1, dont_generate_keys)

    if len(ja1_result) > 0:
        valid_keys = [bytes(valid_key.upper(), encoding='utf-8') for valid_key in ja1_result.split()]
        ja_2_result = LorawanWrapper.testAppKeysWithJoinAccept(valid_keys, ja2, dontGenerateKeys=True)

        if len(ja_2_result) > 0:
            print("\n**** Key found: %s **** \n" % (ja_2_result.split()[0]))

def validate_keys(first, second, keys_path, dont_generate_keys):
    global keys
    # Load keys from file
    with open(keys_path) as f:
        for k in f:
            keys.append(bytes(k.rstrip().upper(), encoding='utf-8'))

    # Decode packets and determine message types
    first_decoded = base64.b64decode(first)
    first_m_type = first_decoded[0] & 0xE0
    second_decoded = base64.b64decode(second)
    second_m_type = second_decoded[0] & 0xE0

    # Route to appropriate brute force function based on message types
    if first_m_type == 0x00:
        if second_m_type == 0x00:
            bruteforce_two_join_requests(first, second, dont_generate_keys)
        elif second_m_type == 0x20:
            bruteforce_accept_request(second, first, dont_generate_keys)
        else:
            error_message(packet_order='second')
    elif first_m_type == 0x20:
        if second_m_type == 0x00:
            bruteforce_accept_request(first, second, dont_generate_keys)
        elif second_m_type == 0x20:
            bruteforce_two_join_accepts(first, second, dont_generate_keys)
        else:
            error_message(packet_order='second')
    else:
        error_message(packet_order='first')

def error_message(packet_order):
    print("\nMake sure the {0} packet provided is a valid JoinRequest or JoinAccept\n".format(packet_order))

if __name__ == '__main__':
    try:
        print("\n*****************************************************")
        print("LoRaWAN Security Framework - BruteForcer")
        print("*****************************************************\n")

        # Step-by-step input prompts
        first = input("Enter the first packet in Base64 format (JoinRequest/JoinAccept): ").strip()
        second = input("Enter the second packet in Base64 format (JoinRequest/JoinAccept): ").strip()
        
        keys_path = input("Enter the path to keys file (press Enter for default path '../../auditing/analyzers/bruteforcer/keys.txt'): ").strip()
        if not keys_path:
            keys_path = "../../auditing/analyzers/bruteforcer/keys.txt"
        
        dont_generate = input("Do you want to generate keys on the fly? (y/n): ").strip().lower() == 'n'

        print("\nValidating and attempting brute force attack...\n")
        validate_keys(first, second, keys_path, dont_generate)

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
# BruteForcer.py
# LoRaWAN Security Framework - BruteForcer
# Copyright (c) 2019 IOActive Inc.  All rights reserved.

import base64
import sys
import lorawanwrapper.LorawanWrapper as LorawanWrapper

keys = []

def bruteforce_accept_request(ja, jr, dont_generate_keys):
    global keys
    jr_result = LorawanWrapper.testAppKeysWithJoinRequest(keys, jr, dont_generate_keys)  

    if len(jr_result) > 0:
        valid_keys = [bytes(valid_key.upper(), encoding='utf-8') for valid_key in jr_result.split()]
        ja_result = LorawanWrapper.testAppKeysWithJoinAccept(valid_keys, ja, dontGenerateKeys=True)

        if len(ja_result) > 0:
            print("\n**** Key found: %s **** \n" % (ja_result.split()[0]))

def bruteforce_two_join_requests(jr1, jr2, dont_generate_keys):
    global keys
    jr_1_result = LorawanWrapper.testAppKeysWithJoinRequest(keys, jr1, dont_generate_keys)

    if len(jr_1_result) > 0:
        valid_keys = [bytes(valid_key.upper(), encoding='utf-8') for valid_key in jr_1_result.split()]
        jr_2_result = LorawanWrapper.testAppKeysWithJoinRequest(valid_keys, jr2, dontGenerateKeys=True)

        if len(jr_2_result) > 0:
            print("\n**** Key found: %s **** \n" % (jr_2_result.split()[0]))

def bruteforce_two_join_accepts(ja1, ja2, dont_generate_keys):
    global keys
    ja1_result = LorawanWrapper.testAppKeysWithJoinAccept(keys, ja1, dont_generate_keys)

    if len(ja1_result) > 0:
        valid_keys = [bytes(valid_key.upper(), encoding='utf-8') for valid_key in ja1_result.split()]
        ja_2_result = LorawanWrapper.testAppKeysWithJoinAccept(valid_keys, ja2, dontGenerateKeys=True)

        if len(ja_2_result) > 0:
            print("\n**** Key found: %s **** \n" % (ja_2_result.split()[0]))

def validate_keys(first, second, keys_path, dont_generate_keys):
    global keys
    # Load keys from file
    with open(keys_path) as f:
        for k in f:
            keys.append(bytes(k.rstrip().upper(), encoding='utf-8'))

    # Decode packets and determine message types
    first_decoded = base64.b64decode(first)
    first_m_type = first_decoded[0] & 0xE0
    second_decoded = base64.b64decode(second)
    second_m_type = second_decoded[0] & 0xE0

    # Route to appropriate brute force function based on message types
    if first_m_type == 0x00:
        if second_m_type == 0x00:
            bruteforce_two_join_requests(first, second, dont_generate_keys)
        elif second_m_type == 0x20:
            bruteforce_accept_request(second, first, dont_generate_keys)
        else:
            error_message(packet_order='second')
    elif first_m_type == 0x20:
        if second_m_type == 0x00:
            bruteforce_accept_request(first, second, dont_generate_keys)
        elif second_m_type == 0x20:
            bruteforce_two_join_accepts(first, second, dont_generate_keys)
        else:
            error_message(packet_order='second')
    else:
        error_message(packet_order='first')

def error_message(packet_order):
    print("\nMake sure the {0} packet provided is a valid JoinRequest or JoinAccept\n".format(packet_order))

if __name__ == '__main__':
    try:
        print("\n*****************************************************")
        print("LoRaWAN Security Framework - BruteForcer")
        print("*****************************************************\n")

        # Step-by-step input prompts
        first = input("Enter the first packet in Base64 format (JoinRequest/JoinAccept): ").strip()
        second = input("Enter the second packet in Base64 format (JoinRequest/JoinAccept): ").strip()
        
        keys_path = input("Enter the path to keys file (press Enter for default path '../../auditing/analyzers/bruteforcer/keys.txt'): ").strip()
        if not keys_path:
            keys_path = "../../auditing/analyzers/bruteforcer/keys.txt"
        
        dont_generate = input("Do you want to generate keys on the fly? (y/n): ").strip().lower() == 'n'

        print("\nValidating and attempting brute force attack...\n")
        validate_keys(first, second, keys_path, dont_generate)

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
