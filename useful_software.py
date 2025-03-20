import os
import webbrowser
import main_menu
import configparser


def usefulsoftware():
    while True:
        print("==USEFUL SOFTWARE==\n"
              "[1] NVCleanstall\n"
              "[2] Windows Debloat Script\n"
              "[3] InSpectre\n"
              "[4] Rufus\n"
              "[5] Nvidia App/Control Panel Settings\n"
              "[6] ...back to Main Menu\n")

        usefulsoftware_choice = input("\nEnter a number : ")

        if usefulsoftware_choice == '1':
            os.system('cls')
            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            browser_open = config.getboolean('Useful Software', 'browser_open')
            if browser_open:
                webbrowser.open("https://www.techpowerup.com/download/techpowerup-nvcleanstall/", new=2)
            else:
                print("")
            print("-----------------\n")
            print("LINK - https://www.techpowerup.com/download/techpowerup-nvcleanstall/\n")
            print("NVCleanstall installs debloated nvidia GPU drivers on your PC\n")
            print("1] Download the latest game ready driver here using the manual search - https://www.nvidia.com/en-us/drivers/\n"
                  "2] Open NVCleanstall\n"
                  "3] Select 'Use drivers files on disk' and navigate it to the game ready driver you downloaded in Step 1\n"
                  "4] Click Next\n"
                  "5] Under Select Components to Install, select PhysX and Nvidia App\n"
                  "6] You will be prompted asking you if you want to install the other required components, select Yes then click next and wait for the app to finish unpacking the installer.\n"
                  "7] Under Installation Tweaks CHECK/ENABLE the following:\n"
                  "- Disable Installer Telemetry & Advertising\n"
                  "- Unattended Express Installation\n"
                  "    - Allow automatic reboot, if needed\n"
                  "- Perform a Clean Installation\n"
                  "- Disable Multiplane Overlay (if you do not use this feature)\n"
                  "- Disable Ansel (if you do not use this feature)\n"
                  "- Show Expert Tweaks\n"
                  "    - Disable Driver Telemetry\n"
                  "    - Disable NVIDIA HD Audio device sleep timer\n"
                  "    - Enable Message Signaled Interrupts\n"
                  "        - Interrupt Policy - Default\n"
                  "        - Interrupt Priority - Default\n"
                  "    - Disable HDCP\n"
                  "- Rebuild digital signature (if 'Disable Driver Telemetry' is DISABLED, this option will not appear)\n"
                  "    - Use method compatible with Easy-Anti-Cheat\n"
                  "    - Automatically accept the 'driver unsigned' warning\n")
            print("9] Click Next\n"
                  "10] Select Install and wait until it finishes\n"
                  "11] Done! You have to do this everytime there is a new driver update. NVCleanstall has a 'Use previous settings' button so you do not have to change your settings all over again. After an update, your Nvidia Control Panel settings will be reset so be sure to fix that.\n")
            print("-----------------\n")

        elif usefulsoftware_choice == '2':
            os.system('cls')
            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            browser_open = config.getboolean('Useful Software', 'browser_open')
            if browser_open:
                webbrowser.open("https://github.com/Sycnex/Windows10Debloater", new=2)
            else:
                print("")
            print("-----------------\n")
            print("LINK - https://github.com/Sycnex/Windows10Debloater\n")
            print("Uninstalls bloatware that comes packaged with Windows, reducing RAM usage, CPU usage and freeing up storage space. Works on Windows 11 24H2\n"
                  "\nFollow the instructions on the github page\n")
            print("-----------------\n")

        elif usefulsoftware_choice == '3':
            os.system('cls')
            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            browser_open = config.getboolean('Useful Software', 'browser_open')
            if browser_open:
                webbrowser.open("https://www.grc.com/inspectre.htm", new=2)
            else:
                print("")
            print("-----------------\n")
            print("LINK - https://www.grc.com/inspectre.htm\n")
            print("Disables Meltdown and Spectre protection for increased performance but at the cost of lower security.\n\n"
                  "1] Open the .exe as ADMIN and click on 'Disable Meltdown Protection' and 'Disable Spectre Protection'\n"
                  "2] Reboot your PC\n"
                  "3] Done! If you want to re-enable, open the software again and click enable on both protections\n")
            print("-----------------\n")

        elif usefulsoftware_choice == '4':
            os.system('cls')
            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            browser_open = config.getboolean('Useful Software', 'browser_open')
            if browser_open:
                webbrowser.open("https://rufus.ie/en/", new=2)
            else:
                print("")
            print("-----------------\n")
            print("LINK - https://rufus.ie/en/\n")
            print("Rufus is a utility that helps format and create bootable USB flash drives.\n"
                  "When creating a new bootable drive, Rufus allows you to change some settings in the Windows User Experience. CHECK/ENABLE all of the following:\n"
                  "    - Remove requirement for 4GB+ RAM, Secure Boot and TPM 2.0\n"
                  "    - Remove requirement for an online Microsoft account\n"
                  "    - Disable data collection (Skip privacy questions)\n"
                  "    - Disable BitLocker automatic device encryption\n"
                  "    ...you can check the rest if you want\n")
            print("-----------------\n")

        elif usefulsoftware_choice == '5':
            os.system('cls')
            print("-----------------\n")
            print("Nvidia App > Graphics > Global Settings:\n"
                  "    - RTX HDR : <preference, but keep in mind there is a performance hit with this enabled>\n"
                  "    - Low Latency Mode : OFF, for smoothness. ON/ULTRA for least latency (*needs per-game testing as ON/ULTRA can cause stuttering*)\n"
                  "    - Max Frame Rate : [monitor refresh rate] - 3. Ex. 144hz = 141, 240hz = 237, etc...\n"
                  "    - Power Management Mode : Prefer maximum performance OR Adaptive, needs per-machine testing as max performance could reduce FPS due to high temp and load.\n"
                  "    - Preferred Refresh Rate : Highest available\n"
                  "    - Vertical Sync : On\n"
                  "    ...all else leave at default or change to your liking.\n")
            print("Manage 3D Settings:\n"
                  "    - Antialising Gamma Correction : OFF\n"
                  "    - Preferred Refresh Rate : Highest available\n"
                  "    ...all else leave at default or change to your liking. We already changed the other settings in Nvidia App\n")
            print("Nvidia App > System > Displays\n"
                  "    - G-SYNC:\n"
                  "        - On, Fullscreen\n")
            print("Nvidia App > System > Performance\n"
                  "    - Automatic tuning : <preference, I personally have it OFF>\n"
                  "    - Voltage maximum (%) : 0%\n"
                  "    - Power maximum (%) : 125% (...or highest available)\n"
                  "    - Temperature target (C) : 88 (...or highest available)\n"
                  "    - Fan speed target (%) : Automatic\n")
            print("-----------------\n")

        elif usefulsoftware_choice == '6':
            os.system('cls')
            main_menu.menu()

        else:
            os.system('cls')
            print("INVALID! Please try again...\n")
