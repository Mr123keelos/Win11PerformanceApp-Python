import os
import webbrowser
import main_menu
import configparser

def usefulwebsite():
    while True:
        print("==USEFUL WEBSITES==\n"
              "[1] r/OptimizedGaming : Subreddit for optimized settings for games\n"
              "[2] Nexus Mods : Mods for games, search for your specific game as there could be performance enhancing mods\n"
              "[3] PC Gaming Wiki : Troubleshooting and performance tips\n"
              "[4] ...back to Main Menu")

        usefulwebsite_choice = input("\nEnter a number: ")

        if usefulwebsite_choice == '1':
            os.system('cls')
            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            browser_open = config.getboolean('Useful Software', 'browser_open')
            if browser_open:
                webbrowser.open("https://www.reddit.com/r/OptimizedGaming/", new=2)
            else:
                print("")

        elif usefulwebsite_choice == '2':
            os.system('cls')
            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            browser_open = config.getboolean('Useful Software', 'browser_open')
            if browser_open:
                webbrowser.open("https://www.nexusmods.com/", new=2)
            else:
                print("")

        elif usefulwebsite_choice == '3':
            os.system('cls')
            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            browser_open = config.getboolean('Useful Software', 'browser_open')
            if browser_open:
                webbrowser.open("https://www.pcgamingwiki.com/wiki/Home", new=2)
            else:
                print("")

        elif usefulwebsite_choice == '4':
            os.system('cls')
            main_menu.menu()

        else:
            os.system('cls')
            print("INVALID! Please try again...\n")
