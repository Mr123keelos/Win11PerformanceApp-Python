import os
import main_menu
import configparser
import time
import subprocess


def reg_tweaks():
    while True:
        print("==REGISTRY TWEAKS==\n"
              "[1] Disable GameDVR and XBOX Services\n"
              "[2] Disable Useless Window Services and Settings\n"
              "[3] Disable Windows Defender and Protection Settings\n"
              "[4] Disable Windows Telemetry and Data Collection\n"
              "[5] Disable Microsoft Copilot\n"
              "[6] ...back to Main Menu\n")

        regtweaks_choice = input("\nEnter a number : ")

        if regtweaks_choice == '1':
            os.system('cls')

            print("SUCCESS! GameDVR and XBOX Services have been DISABLED. Please select 'YES' when you get a registry prompt\n")

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            temp_file_folder = config.get('Temporary Files', 'temp_file_folder')

            script_file_path = os.path.join(temp_file_folder, 'Win11PerformanceApp_123keelos', '1_XBOX-Services.reg')
            os.makedirs(os.path.dirname(script_file_path), exist_ok=True)
            script_content = """Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\System\GameConfigStore]
"GameDVR_Enabled"=dword:00000000
"GameDVR_FSEBehaviorMode"=dword:00000002
"GameDVR_HonorUserFSEBehaviorMode"=dword:00000000
"GameDVR_DXGIHonorFSEWindowsCompatible"=dword:00000001
"GameDVR_EFSEFeatureFlags"=dword:00000000

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\GameDVR]
"AppCaptureEnabled"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\GameDVR]
"AllowGameDVR"=dword:00000000

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XblGameSave]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XboxNetApiSvc]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XboxGipSvc]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XblAuthManager]
"Start"=dword:00000004
            """

            with open(script_file_path, 'w') as file:
                file.write(script_content)

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            program_delay = config.getfloat('Initial', 'program_delay')
            time.sleep(program_delay)

            subprocess.call(['regedit', script_file_path])

        elif regtweaks_choice == '2':
            os.system('cls')

            print("SUCCESS! Useless Windows services and settings have been DISABLED. Please select 'YES' when you get a registry prompt\n")

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            temp_file_folder = config.get('Temporary Files', 'temp_file_folder')

            script_file_path = os.path.join(temp_file_folder, 'Win11PerformanceApp_123keelos', '2_Windows-Services.reg')
            os.makedirs(os.path.dirname(script_file_path), exist_ok=True)
            script_content = """Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\BITS]
"Start"=dword:00000003

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\lfsvc]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\DiagTrack]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\QWAVE]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\GraphicsPerfSvc]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\stisvc]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PcaSvc]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MapsBroker]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MMCSS]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsMediaPlayer]
"PreventLibrarySharing"=dword:00000001

[HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\CloudContent]
"DisableSoftLanding"=dword:00000001
"DisableWindowsSpotlightFeatures"=dword:00000001
"DisableWindowsConsumerFeatures"=dword:00000001
"DisableTailoredExperiencesWithDiagnosticData"=dword:00000001

[HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\CloudContent]
"DisableTailoredExperiencesWithDiagnosticData"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power]
"HibernateEnabledDefault"=dword:00000000
"HibernateEnabled"=dword:00000000

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power]
HiberBootEnabled"=dword:00000000

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications]
"GlobalUserDisabled"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Spooler]
"Start"=dword:00000003

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PrintNotify]
"Start"=dword:00000003
            """

            with open(script_file_path, 'w') as file:
                file.write(script_content)

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            program_delay = config.getfloat('Initial', 'program_delay')
            time.sleep(program_delay)

            subprocess.call(['regedit', script_file_path])

        elif regtweaks_choice == '3':
            os.system('cls')

            print("SUCCESS! Windows Defender and protection settings have been DISABLED. Please select 'YES' when you get a registry prompt\n")

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            temp_file_folder = config.get('Temporary Files', 'temp_file_folder')

            script_file_path = os.path.join(temp_file_folder, 'Win11PerformanceApp_123keelos', '3_Windows-Defender.reg')
            os.makedirs(os.path.dirname(script_file_path), exist_ok=True)
            script_content = """Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender]
"DisableAntiSpyware"=dword:00000001
"PUAProtection"=dword:00000000

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard]
"EnableVirtualizationBasedSecurity"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection]
"DisableBehaviorMonitoring"=dword:00000001
"DisableOnAccessProtection"=dword:00000001
"DisableScanOnRealtimeEnable"=dword:00000001
"DisableRealtimeMonitoring"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Antimalware\Real-Time Protection]
"DisableScanOnRealtimeEnable"=dword:00000001
"DisableOnAccessProtection"=dword:00000001

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management]
"FeatureSettingsOverride"=dword:00000003
"FeatureSettingsOverrideMask"=dword:00000003

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\MpEngine]
"MpEnablePus"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Policy Manager]
"DisableScanningNetworkFiles"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge]
"SmartScreenPuaEnabled"=dword:00000000

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity]
"Enabled"=dword:00000000
"Enable"=dword:00000000

;Lines below produce an error, so I edited them off. Trying to find a fix

;[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Spynet]
;"SpyNetReporting"=dword:00000000 
;"SubmitSamplesConsent"=dword:00000000

;[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Sense]
;"Start"=dword:00000004 

;[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer]
;"SmartScreenEnabled"="Off"

;[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Edge\SmartScreenEnabled]
;@=dword:00000000 

;[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdNisSvc]
;"Start"=dword:00000004

;[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WinDefend]
;"Start"=dword:00000004

;[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WTDS\Components]
;"ServiceEnabled"=dword:00000000 

;[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy]
;"VerifiedAndReputablePolicyState"=dword:00000000
            """

            with open(script_file_path, 'w') as file:
                file.write(script_content)

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            program_delay = config.getfloat('Initial', 'program_delay')
            time.sleep(program_delay)

            subprocess.call(['regedit', script_file_path])

        elif regtweaks_choice == '4':
            os.system('cls')

            print("SUCCESS! Windows telemetry and data collection have been DISABLED. Please select 'YES' when you get a registry prompt\n")

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            temp_file_folder = config.get('Temporary Files', 'temp_file_folder')

            script_file_path = os.path.join(temp_file_folder, 'Win11PerformanceApp_123keelos', '4_Windows-Data-Collection.reg')
            os.makedirs(os.path.dirname(script_file_path), exist_ok=True)
            script_content = """Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DataCollection]
"AllowDesktopAnalyticsProcessing"=dword:00000000
"AllowDeviceNameInTelemetry"=dword:00000000
"MicrosoftEdgeDataOptIn"=dword:00000000
"AllowWUfBCloudProcessing"=dword:00000000
"AllowUpdateComplianceProcessing"=dword:00000000
"AllowCommercialDataPipeline"=dword:00000000
"AllowTelemetry"=dword:00000000
"DisableOneSettingsDownloads"=dword:00000001
"DoNotShowFeedbackNotifications"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\DataCollection]
"AllowTelemetry"=dword:00000000
"DoNotShowFeedbackNotifications"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization]
"DODownloadMode"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\WiFi\AllowWiFiHotSpotReporting]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\WiFi\AllowAutoConnectToWiFiSenseHotspots]
"value"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Personalization\Settings]
"AcceptedPrivacyPolicy"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager]
"ContentDeliveryAllowed"=dword:00000000
"OemPreInstalledAppsEnabled"=dword:00000000
"PreInstalledAppsEnabled"=dword:00000000
"PreInstalledAppsEverEnabled"=dword:00000000
"SilentInstalledAppsEnabled"=dword:00000000
"SystemPaneSuggestionsEnabled"=dword:00000000
"SubscribedContentEnabled"=dword:00000000
"SubscribedContent-338387Enabled"=dword:00000000
"SubscribedContent-338388Enabled"=dword:00000000
"SubscribedContent-338389Enabled"=dword:00000000
"SubscribedContent-353698Enabled"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo]
"Enabled"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Feeds]
"EnableFeeds"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\AdvertisingInfo]
"DisabledByGroupPolicy"=dword:00000001

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\ContentDeliveryManager]
"SubscribedContent-338393Enabled"=dword:00000000
"SubscribedContent-353694Enabled"=dword:00000000
"SubscribedContent-353696Enabled"=dword:00000000

[HKEY_CURRENT_USER\Software\Policies\Microsoft\InputPersonalization]
"RestrictImplicitInkCollection"=dword:00000001
"RestrictImplicitTextCollection"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\InputPersonalization]
"RestrictImplicitInkCollection"=dword:00000001
"RestrictImplicitTextCollection"=dword:00000001

[HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\HandwritingErrorReports]
"PreventHandwritingErrorReports"=dword:00000001

[HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\HandwritingErrorReports]
"PreventHandwritingErrorReports"=dword:00000001

[HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\TabletPC]
"PreventHandwritingDataSharing"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\TabletPC]
"PreventHandwritingDataSharing"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\InputPersonalization]
"AllowInputPersonalization"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore]
"HarvestContacts"=dword:00000000

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Siuf\Rules]
"NumberOfSIUFInPeriod"=dword:00000000

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\SearchSettings]
"IsDynamicSearchBoxEnabled"=dword:00000001
"IsMSACloudSearchEnabled"=dword:00000000
"IsAADCloudSearchEnabled"=dword:00000000
"IsDeviceSearchHistoryEnabled"=dword:00000001

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search]
"DisableSearchBoxSuggestions"=dword:00000001
"BingSearchEnabled"=dword:00000000
"DeviceHistoryEnabled"=dword:00000000
"HistoryViewEnabled"=dword:00000000
"IsWindowsHelloActive"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search]
"ConnectedSearchPrivacy"=dword:00000003
"AllowSearchToUseLocation"=dword:00000000
"EnableDynamicContentInWSB"=dword:00000000
"ConnectedSearchUseWeb"=dword:00000000
"DisableWebSearch"=dword:00000001
"PreventRemoteQueries"=dword:00000001
"AlwaysUseAutoLangDetection"=dword:00000000
"AllowIndexingEncryptedStoresOrItems"=dword:00000000
"ConnectedSearchUseWebOverMeteredConnections"=dword:00000000
"AllowCloudSearch"=dword:00000000
"DoNotUseWebResults"=dword:00000001

[HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\SearchCompanion]
"DisableContentFileUpdates"=dword:00000001

[HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\SQMClient\Windows]
"CEIPEnable"=dword:00000000

[HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\AppCompat]
"AllowTelemetry"=dword:00000000
"DisableInventory"=dword:00000001
"DisablePCA"=dword:00000001

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Privacy]
"TailoredExperiencesWithDiagnosticDataEnabled"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft]
"AllowNewsAndInterests"=dword:00000000

[HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows NT\CurrentVersion\Software Protection Platform]
"NoGenTicket"=dword:00000001

[HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\System]
"EnableActivityFeed"=dword:00000000
"PublishUserActivities"=dword:00000000
"UploadUserActivities"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge]
"EnableMediaRouter"=dword:00000000

[HKEY_CURRENT_USER\Software\Policies\Microsoft\Edge]
"ReadAloudEnabled"=dword:00000000
            """

            with open(script_file_path, 'w') as file:
                file.write(script_content)

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            program_delay = config.getfloat('Initial', 'program_delay')
            time.sleep(program_delay)

            subprocess.call(['regedit', script_file_path])

        elif regtweaks_choice == '5':
            os.system('cls')

            print("SUCCESS! Microsoft Copilot has been DISABLED. Please select 'YES' when you get a registry prompt\n")

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            temp_file_folder = config.get('Temporary Files', 'temp_file_folder')

            script_file_path = os.path.join(temp_file_folder, 'Win11PerformanceApp_123keelos', '5_Microsoft-Copilot.reg')
            os.makedirs(os.path.dirname(script_file_path), exist_ok=True)
            script_content = """Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsCopilot]
"TurnOffWindowsCopilot"=dword:00000001

[HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\WindowsCopilot]
"TurnOffWindowsCopilot"=dword:00000001

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced]
"ShowCopilotButton"=dword:00000000
            """

            with open(script_file_path, 'w') as file:
                file.write(script_content)

            config = configparser.ConfigParser()
            config.read('Win11PerformanceApp_settings.ini')
            program_delay = config.getfloat('Initial', 'program_delay')
            time.sleep(program_delay)

            subprocess.call(['regedit', script_file_path])

        elif regtweaks_choice == '6':
            os.system('cls')
            main_menu.menu()

        else:
            os.system('cls')
            print("INVALID! Please try again...\n")
