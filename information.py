import main_menu
import os


def info():
    while True:
        print("Welcome to Windows 11 Performance Application - Python Edition by 123keelos\n")

        print("==TO-DO List==\n"
              "- Disable Search Indexing\n"
              "- Disable High Precision Event Timer in Device Manager (could cause performance issues, needs testing)\n"
              "- Disable Fast Startup\n"
              "- Enable storage sense\n"
              "- Defragment your HDD (skip if on SSD)\n"
              "- Change to Windows High Performance (needs testing, sometimes it makes no difference and will make your PC run at higher CPU load)\n"
              "- C: > Properties > UNCHECK 'Allow files on this drive to have contents indexed in addtion to file properties' (disables search indexing)\n"
              "- Enable Variable refresh rate\n"
              "- Privacy Settings within Windows 11\n"
              "- Advanced System Settings > Performance > Settings...\n"
              "- Turn off Programs and Features\n"
              "- Sound Scheme\n")

        print("==Programs and Features==\n"
              "1] Open Control Panel\n"
              "2] Search for Programs and Features\n"
              "3] Find 'Turn Windows Features on or off'\n"
              "4] Uncheck the following :\n"
              "    - Internet Explorer 11 (if you use another browser)\n"
              "    - Media Features > Windows Media Player (if you have another media player)\n"
              "    - Microsoft Print to PDF (if you do not use this feature)\n"
              "    - Print and Document Service (if you do not print)\n"
              "    - Remote Differential Compression API Support\n"
              "    - Work Folders Client\n\n")

        print("==Uninstall Bloatware==\n"
              "1] Go to Apps & Features in Windows\n"
              "2] Uninstall any apps you do not use\n"
              "2] We cannot uninstall every single app so we will use a special software for that. This can be found in the 'Useful Software' section\n")

        print("==CHECKLISTS==\n"
              "- Keep Windows updated\n"
              "- Make sure to update GPU drivers often\n"
              "- Physically clean your PC\n"
              "- Check for motherboard BIOS updates and its drivers/tools\n")

        run_yes_success = input("Type 'Y' to return to the main menu : ").lower()

        if run_yes_success == 'y':
            os.system('cls')
            main_menu.menu()
        else:
            os.system('cls')
