import os
import main_menu
import configparser
import time
import subprocess

def experimentaltweaks():
    while True:
        print("\n==EXPERIMENTAL TWEAKS==\n"
              "[1] Disable Dynamic Tick (do not apply on laptops or where power-saving is needed)\n"
              "[2] Disable Memory Compression (only for 16GB or higher RAM)\n"
              "[3] ...back to Main Menu")

        exptweaks_choice = input("\nEnter a number: ")

        if exptweaks_choice == '1':
            os.system('cls')

            print("SUCCESS! Dynamic Tick has been DISABLED\n")

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            temp_file_folder = config.get('Temporary Files', 'temp_file_folder')

            script_file_path = os.path.join(temp_file_folder, 'Win11PerformanceApp_123keelos', '1_disable_dynamic_tick.bat')
            os.makedirs(os.path.dirname(script_file_path), exist_ok=True)
            script_content = """@echo off
bcdedit /set disabledynamictick yes
                        """

            with open(script_file_path, 'w') as file:
                file.write(script_content)

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            program_delay = config.getfloat('Initial', 'program_delay')
            time.sleep(program_delay)

            subprocess.call([script_file_path], shell=True)

        elif exptweaks_choice == '2':
            os.system('cls')

            print("SUCCESS! Memory Compression has been DISABLED\n")

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            temp_file_folder = config.get('Temporary Files', 'temp_file_folder')

            script_file_path = os.path.join(temp_file_folder, 'Win11PerformanceApp_123keelos', '2_disable_memory_compression.bat')
            os.makedirs(os.path.dirname(script_file_path), exist_ok=True)
            script_content = """@echo off
powershell -Command "Disable-MMAgent -MemoryCompression"
                        """
            with open(script_file_path, 'w') as file:
                file.write(script_content)

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            program_delay = config.getfloat('Initial', 'program_delay')
            time.sleep(program_delay)

            subprocess.call([script_file_path], shell=True)

        elif exptweaks_choice == '3':
            os.system('cls')
            main_menu.menu()

        else:
            os.system('cls')
            print("INVALID! Please try again...\n")
