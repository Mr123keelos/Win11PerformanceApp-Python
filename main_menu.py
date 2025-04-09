import os
import information
import general_tweaks
import registry_tweaks
import useful_software
import useful_websites
import experimental_tweaks
import sys
import shutil
import configparser
import time


def menu():
    while True:
        print("\nWelcome to Windows 11 Performance Application - Python Edition by 123keelos\n")

        print("[1] Info")
        print("[2] General Tweaks")
        print("[3] Registry Tweaks")
        print("[4] Useful Software")
        print("[5] Useful Websites")
        print("[6] Experimental Tweaks (!)")
        print("[7] Exit + Clean up")

        choice = input("\nEnter a number : ")

        if choice == '1':
            os.system('cls')
            information.info()

        elif choice == '2':
            os.system('cls')
            general_tweaks.general_tweaks()

        elif choice == '3':
            os.system('cls')
            registry_tweaks.reg_tweaks()

        elif choice == '4':
            os.system('cls')
            useful_software.usefulsoftware()

        elif choice == '5':
            os.system('cls')
            useful_websites.usefulwebsite()

        elif choice == '6':
            os.system('cls')
            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            enable_experimental_tweaks = config.getboolean('Experimental Tweaks', 'enable_experimental_tweaks')
            if enable_experimental_tweaks:
                experimental_tweaks.experimentaltweaks()
            else:
                print("ERROR! Experimental Tweaks is DISABLED in the config")

        elif choice == '7':
            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')

            temp_file_folder = config.get('Temporary Files', 'temp_file_folder')

            folder_to_delete = os.path.join(temp_file_folder, 'Win11PerformanceApp_123keelos')

            if os.path.exists(folder_to_delete) and os.path.isdir(folder_to_delete):
                shutil.rmtree(folder_to_delete)
            else:
                print("")

            program_delay = config.getfloat('Initial', 'program_delay')
            time.sleep(program_delay)

            sys.exit()

        else:
            os.system('cls')
            print("INVALID! Please try again...")
