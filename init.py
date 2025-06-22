import ctypes
import configparser
import os
import sys
import requests
import psutil
import main_menu

USERNAME = 'Mr123keelos'
REPO_NAME = 'Win11PerformanceApp-Python'
version = 1.5

API_URL = f'https://api.github.com/repos/{USERNAME}/{REPO_NAME}/releases/latest'

PRIORITY_MAP = {
    "0": psutil.IDLE_PRIORITY_CLASS,
    "1": psutil.BELOW_NORMAL_PRIORITY_CLASS,
    "2": psutil.NORMAL_PRIORITY_CLASS,
    "3": psutil.ABOVE_NORMAL_PRIORITY_CLASS,
    "4": psutil.HIGH_PRIORITY_CLASS,
    "5": psutil.REALTIME_PRIORITY_CLASS
}


def settings_ini():
    try:
        if not os.path.exists('Win11PerformanceApp_settings.ini'):
            config = configparser.ConfigParser()
            config['Initial'] = {
                ';Allows the program to check for admin rights. NOTE: You still need admin rights to make system changes, this only disables the initial check. Recommended to only disable for debug purposes': '',
                'admin_check': 'true',
                '\n'
                ';Allows the program to check for updates on Github': '',
                'update_check': 'true',
                '\n'
                ';Delay in seconds after applying tweaks. Might have to be adjusted higher for low-end PCs, otherwise recommended to leave as default': '',
                'program_delay': '0.5',
                '\n'
                ';Program priority. 0=idle, 1=below normal, 2=normal, 3=above normal, 4=high, 5=realtime. I recommend keeping this at 2, increase only if there is app slowdown': '',
                'app_priority': '2',
            }

            config['Useful Software'] = {
                ';In the USEFUL SOFTWARE section, the input will also open the associated link on your default browser': '',
                'browser_open': 'true',
            }

            config['Experimental Tweaks'] = {
                ';Enable the EXPERIMENTAL TWEAKS section. This section contains tweaks that could have some unwanted side effects and should only be used if you know what you are doing': '',
                'enable_experimental_tweaks': 'false',
            }

            config['Temporary Files'] = {
                ';Change the path of where this program will save temporary files. Make sure the path is accessible and also exists': '',
                'temp_file_folder': 'C:\Windows\Prefetch',
            }

            config['Version'] = {
                ';Config version, DO NOT CHANGE': '',
                'config_version': version,
            }

            with open('Win11PerformanceApp_settings.ini', 'w') as configfile:
                config.write(configfile)

            print("Welcome to Windows 11 Performance Application - Python Edition by 123keelos")
            print("https://github.com/Mr123keelos/Win11PerformanceApp-Python\n")
            print("ERROR! Win11PerformanceApp_settings.ini does not exist and this program created one in the same path as where this .exe is located. Edit the Win11PerformanceApp_settings.ini file to your liking and reopen the program.\n")
            input("Press ENTER to exit...")
            sys.exit()
        else:
            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')

            admin_check = config.get('Initial', 'admin_check', fallback=None)
            if admin_check not in ['true', 'false']:
                raise ValueError(f"Invalid value for 'admin_check' (true/false)")

            update_check = config.get('Initial', 'update_check', fallback=None)
            if update_check not in ['true', 'false']:
                raise ValueError(f"Invalid value for 'update_check' (true/false)")

            try:
                program_delay = float(config.get('Initial', 'program_delay', fallback='0.5'))
                if program_delay < 0:
                    raise ValueError(f"Invalid value for 'program_delay' (> 0.0)")
            except ValueError:
                raise ValueError(f"Invalid value for 'program_delay' (> 0.0)")

            app_priority = config.get('Initial', 'app_priority', fallback='2')
            if app_priority not in ['0', '1', '2', '3', '4', '5']:
                raise ValueError(f"Invalid value for 'app_priority' (0,1,2,3,4,5)")

            browser_open = config.get('Useful Software', 'browser_open', fallback=None)
            if browser_open not in ['true', 'false']:
                raise ValueError(f"Invalid value for 'browser_open' (true/false)")

            enable_experimental_tweaks = config.get('Experimental Tweaks', 'enable_experimental_tweaks', fallback=None)
            if enable_experimental_tweaks not in ['true', 'false']:
                raise ValueError(f"Invalid value for 'enable_experimental_tweaks' (true/false)")

            temp_file_folder = config.get('Temporary Files', 'temp_file_folder', fallback=None)

            if temp_file_folder:
                if not os.path.isdir(temp_file_folder):
                    raise ValueError(f"Invalid path for 'temp_file_folder'. The directory does not exist or is inaccessible.")
            else:
                raise ValueError("Invalid value for 'temp_file_folder'. Please specify a valid directory path.")

    except (ValueError, Exception) as e:
        print("Welcome to Windows 11 Performance Application - Python Edition by 123keelos")
        print("https://github.com/Mr123keelos/Win11PerformanceApp-Python\n")
        print(f"ERROR! {e}")
        input("Press ENTER to exit...")
        sys.exit()


def check_version():
    config = configparser.ConfigParser()
    config.read('Win11PerformanceApp_settings.ini')
    ini_version = config.get('Version', 'config_version', fallback=None)

    if ini_version is None or ini_version != str(version):
        print("Welcome to Windows 11 Performance Application - Python Edition by 123keelos")
        print("https://github.com/Mr123keelos/Win11PerformanceApp-Python\n")
        print("ERROR! Version mismatch. Delete Win11PerformanceApp_settings.ini and reopen the program.\n")
        input("Press ENTER to exit...")
        sys.exit()


def set_priority():
    config = configparser.ConfigParser()
    config.read('Win11PerformanceApp_settings.ini')
    app_priority = config.get('Initial', 'app_priority', fallback='2')
    try:
        priority_class = PRIORITY_MAP.get(app_priority, psutil.NORMAL_PRIORITY_CLASS)
        psutil.Process(os.getpid()).nice(priority_class)
    except Exception as e:
        print("")


settings_ini()
check_version()
set_priority()


def is_admin():
    try:
        config = configparser.ConfigParser()
        config.read('Win11PerformanceApp_settings.ini')
        if config.getboolean('Initial', 'admin_check'):
            return ctypes.windll.shell32.IsUserAnAdmin()
        else:
            return True
    except:
        return False


if is_admin():
    while True:
        print("Welcome to Windows 11 Performance Application - Python Edition by 123keelos")
        print("https://github.com/Mr123keelos/Win11PerformanceApp-Python\n")

        print("==NOTE==")
        print("I cannot guarantee your safety when using these tweaks! I tested them on my PCs and it is unproblematic, this might not be the same for you! Make a RESTORE POINT or BACKUP just incase of any issues that could occur. By using this software, you agree that I take no responsibility whatsoever for happens with your PC!\n")

        print("Before using this application, make sure your Windows 11 has the latest updates as changes may be undone after an update. You may have to run the tweaks in this application twice as something in Windows could have reverted it.\n")

        print("If you are still unable to change settings even with admin, try turning off Real-time Protection in Windows Security.\n")

        print("If you want to know the technical details of each tweak and what it will change in your system, refer to the Github source code. I will add information built in the program in the future.\n")

        print("After you are done with everything, reboot your PC to apply the changes.\n")

        print("Read everything and understand the risks of entering this program.\n")

        print("Report any bugs and leave any suggestions and feedback.\n")

        print("==INSTRUCTIONS==")
        print("Use your keyboard and type prompts which are on the window. For example, '1' key on your keyboard corresponds to option 1, '2' corresponds to option 2, etc...\n")

        print("Type the option you want in the prompt, then hit ENTER on your keyboard.\n")

        print("Instead of exiting the window, select 'Exit + Clean up' in main menu to clean up all the temporary files made by the program, otherwise those temporary files won't be deleted.\n")

        print("Open the Win11PerformanceApp_settings.ini file to change any settings.\n")

        print("==TEMP FILES==")
        print("This program will save temporary files to the folder specified in the Win11PerformanceApp_settings.ini file. DO NOT touch them while the program is running. They are safe to delete once you have exited the program. You can also select the 'Exit + Clean up' option to delete them for you.\n")

        print("==CHECK FOR UPDATES==")
        config = configparser.ConfigParser()
        config.read('Win11PerformanceApp_settings.ini')
        if config.getboolean('Initial', 'update_check'):
            try:
                response = requests.get(API_URL)

                if response.status_code == 200:
                    release_data = response.json()
                    latest_tag_name = release_data['tag_name']

                    if str(version) != latest_tag_name:
                        print("!! NEW UPDATE AVAILABLE. VISIT THE GITHUB PAGE TO UPDATE !!\n")
                        print("You are running version : v" + str(version))
                        print("The latest version is : v" + str(latest_tag_name) + "\n")
                    else:
                        print("You have the latest version of the program.\n")
                        print("You are running version : v" + str(version))
                        print("The latest version is : v" + str(latest_tag_name) + "\n")
                else:
                    print(f'ERROR! Failed to check for update.')

            except requests.exceptions.RequestException as e:
                print(f'ERROR! Failed to check for update.')
        else:
            print("!! UPDATE CHECK IS DISABLED IN Win11PerformanceApp_settings.ini !!\n")
            print("You are running version : v" + str(version) + "\n")

        print("==AGREEMENT==")
        print("!! This program will now make changes to your PC !!\n")
        agreement = input("Type 'Y' if you agree you are responsible for everything that happens [Y] : ").lower()

        if agreement == 'y':
            os.system('cls')
            main_menu.menu()
        else:
            os.system('cls')
            print('\n')

else:
    print("Welcome to Windows 11 Performance Application - Python Edition by 123keelos")
    print("https://github.com/Mr123keelos/Win11PerformanceApp-Python\n")
    print("ERROR! Please re-run the application as administrator.")
    input("Press ENTER to exit...")
