import os
import configparser
import time
import subprocess
import main_menu

CONFIG_PATH = 'Win11PerformanceApp_settings.ini'


def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config


def create_and_run_script(temp_folder, filename, content, delay, use_shell=True):
    script_path = os.path.join(temp_folder, 'Win11PerformanceApp_123keelos', filename)
    os.makedirs(os.path.dirname(script_path), exist_ok=True)

    with open(script_path, 'w') as f:
        f.write(content)

    time.sleep(delay)

    if filename.endswith('.reg'):
        subprocess.call(['regedit', script_path])
    else:
        subprocess.call([script_path], shell=use_shell)


def clear():
    os.system('cls')


def experimentaltweaks():
    config = load_config()
    temp_folder = config.get('Temporary Files', 'temp_file_folder')
    delay = config.getfloat('Initial', 'program_delay')

    tweaks = {
        '1': ("Dynamic Tick has been DISABLED",
              "1_disable_dynamic_tick.bat",
              "@echo off\nbcdedit /set disabledynamictick yes"),

        '2': ("Memory Compression has been DISABLED",
              "2_disable_memory_compression.bat",
              '@echo off\npowershell -Command "Disable-MMAgent -MemoryCompression"'),

        '3': ("CPU Quota has been DISABLED. Please accept registry prompt",
              "exp-tweaks_cpu_quota.reg",
              """Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Quota System]
"EnableCpuQuota"=dword:00000000"""),

        '4': ("Storage tweaks have been ENABLED",
              "4_disable_last_access_time.bat",
              """@echo off
fsutil.exe behavior set disableLastAccess 1
fsutil behavior set disableEncryption 1
fsutil 8dot3name set 1""")
    }

    while True:
        print("\n==EXPERIMENTAL TWEAKS==\n"
              "[1] Disable Dynamic Tick\n"
              "[2] Disable Memory Compression\n"
              "[3] Disable CPU Quota\n"
              "[4] Enable Storage Tweaks\n"
              "[5] Back to Main Menu")

        choice = input("\nEnter a number: ")

        if choice in tweaks:
            clear()
            message, filename, content = tweaks[choice]
            print(f"SUCCESS! {message}\n")

            create_and_run_script(temp_folder, filename, content, delay)

        elif choice == '5':
            clear()
            main_menu.menu()
            break

        else:
            clear()
            print("INVALID! Please try again...\n")