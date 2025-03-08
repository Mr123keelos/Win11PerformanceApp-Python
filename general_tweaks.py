import os
import time
import subprocess
import main_menu
import configparser


def general_tweaks():
    while True:
        print("==GENERAL TWEAKS==\n"
              "[1] Install Automatic Temp Folder Cleaner\n"
              "[2] Install Task Scheduler Tweaks\n"
              "[3] ...back to Main Menu\n")

        generaltweaks_choice = input("\nEnter a number : ")

        if generaltweaks_choice == '1':
            os.system('cls')

            startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
            batch_file_name = 'auto-temp-cleaner-123keelos.bat'
            batch_content = """
del /s /q /f %localappdata%\\Temp\\*.*
del /s /q /f %temp%
del /s /q /f %Windir%\\Temp\\*.*
del /s /q /f %Windir%\\Prefetch\\*.*
del /s /q /f %Windir%\\SoftwareDistribution\\Download\\*.*
del /s /q /f %Windir%\\SoftwareDistribution\\Download\\*.*
            """

            batch_file_path = os.path.join(startup_folder, batch_file_name)
            with open(batch_file_path, 'w') as batch_file:
                batch_file.write(batch_content)

            command = [
                "schtasks", "/create",
                "/tn", batch_file_name,
                "/tr", f'"{batch_file_path}"',
                "/sc", "onlogon",
                "/rl", "highest",
                "/f"
            ]

            try:
                subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except subprocess.CalledProcessError as e:
                print(f"ERROR : {e}")

            print("SUCCESS! Automatic Temp Folder Cleaner has been installed in '%appdata%\Microsoft\Windows\Start Menu\Programs\Startup'. The .bat file will run every time you reboot your PC.\n")
            print("-----------------\n")

        elif generaltweaks_choice == '2':
            os.system('cls')

            config = configparser.ConfigParser()
            config.read('settings.ini')
            temp_file_folder = config.get('Temporary Files', 'temp_file_folder')

            script_file_path = os.path.join(temp_file_folder, 'Win11PerformanceApp_123keelos','task-scheduler-tweaks.bat')
            os.makedirs(os.path.dirname(script_file_path), exist_ok=True)
            script_content = r"""schtasks /Change /TN "\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser" /DISABLE
schtasks /Change /TN "\Microsoft\Windows\Application Experience\MareBackup" /DISABLE
schtasks /Change /TN "\Microsoft\Windows\Application Experience\PcaPatchDbTask" /DISABLE
schtasks /Change /TN "\Microsoft\Windows\Application Experience\SdbinstMergeDbTask" /DISABLE
schtasks /Change /TN "\Microsoft\Windows\Application Experience\StartupAppTask" /DISABLE

schtasks /Change /TN "\Microsoft\Windows\Autochk\Proxy" /DISABLE

schtasks /Change /TN "\Microsoft\Windows\Customer Experience Improvement Program\Consolidator" /DISABLE
schtasks /Change /TN "\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip" /DISABLE

schtasks /Change /TN "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector" /DISABLE
schtasks /Change /TN "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver" /DISABLE

schtasks /Change /TN "\Microsoft\Windows\Feedback\Siuf\DmClient" /DISABLE

schtasks /Change /TN "\Microsoft\Windows\Location\Notifications" /DISABLE

schtasks /Change /TN "\Microsoft\Windows\Maps\MapsUpdateTask" /DISABLE
schtasks /Change /TN "\Microsoft\Windows\Maps\MapsToastTask" /DISABLE
                            """

            with open(script_file_path, 'w') as file:
                file.write(script_content)

            config = configparser.ConfigParser()
            config.read('settings.ini')
            program_delay = config.getfloat('Initial', 'program_delay')
            time.sleep(program_delay)

            subprocess.run(['cmd', '/c', 'start', 'cmd', '/c', script_file_path], shell=True)

            print("SUCCESS! Task scheduler tweaks have been enabled\n")
            print("-----------------\n")

        elif generaltweaks_choice == '3':
            os.system('cls')
            main_menu.menu()

        else:
            os.system('cls')
            print("INVALID! Please try again...\n")
