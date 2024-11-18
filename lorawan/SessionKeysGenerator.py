# SessionKeysGenerator.py
# LoRaWAN Security Framework - SessionKeysGenerator
# Copyright (c) 2019 IOActive Inc.  All rights reserved.

import os
import sys
import json
import lorawanwrapper.LorawanWrapper as LorawanWrapper

if __name__ == '__main__':
    print("\n*****************************************************")
    print("LoRaWAN Security Framework - SessionKeysGenerator")
    print("*****************************************************\n")

    try:
        # Step-by-step input prompts
        jaccept = input("Enter JoinAccept payload in Base64 format: ").strip()
        jrequest = input("Enter JoinRequest payload in Base64 format: ").strip()
        app_key = input("Enter the device AppKey in hex format (32 characters / 16 bytes): ").strip()

        print("\nGenerating session keys...\n")

        # Generate session keys using the provided inputs
        json_result = LorawanWrapper.generateSessionKeysFromJoins(jrequest, jaccept, app_key)
        keys = json.loads(json_result)

        # Output the generated keys
        print("NwkSKey: %s\nAppSKey: %s" % (keys["nwkSKey"], keys["appSKey"]))

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
