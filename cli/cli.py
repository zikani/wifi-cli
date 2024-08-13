from wifi_manager import (scan_networks, connect_to_network, current_connection_info, delete_network_profile,
                          monitor_signal_strength, run_speed_test, run_traceroute, set_dns_servers, 
                          create_wifi_hotspot, log_signal_strength, backup_network_settings, log_event, 
                          reset_network_adapter, list_network_profiles, prioritize_network_profile, load_config, save_config, setup_logging)

def main():
    config = load_config()
    setup_logging(config.get('log_file', 'wifi_manager.log'))
    log_event("Wi-Fi manager started.")
    while True:
        print("\nWi-Fi Manager")
        print("1. Scan for networks")
        print("2. Connect to a network")
        print("3. Show current connection info")
        print("4. Delete a network profile")
        print("5. Monitor signal strength")
        print("6. Run speed test")
        print("7. Run traceroute")
        print("8. Set DNS servers")
        print("9. Create Wi-Fi hotspot")
        print("10. Log signal strength")
        print("11. Backup network settings")
        print("12. Reset network adapter")
        print("13. List network profiles")
        print("14. Prioritize a network profile")
        print("15. Update configuration")
        print("16. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            scan_networks()
        elif choice == '2':
            ssid = input("Enter SSID (or press Enter to use default): ")
            password = input("Enter Password (or press Enter to use default): ")
            connect_to_network(ssid or None, password or None)
        elif choice == '3':
            current_connection_info()
        elif choice == '4':
            ssid = input("Enter SSID of the profile to delete: ")
            delete_network_profile(ssid)
        elif choice == '5':
            monitor_signal_strength()
        elif choice == '6':
            run_speed_test()
        elif choice == '7':
            destination = input("Enter the destination (e.g., google.com): ")
            run_traceroute(destination)
        elif choice == '8':
            dns1 = input("Enter the primary DNS server: ")
            dns2 = input("Enter the secondary DNS server: ")
            set_dns_servers(dns1, dns2)
        elif choice == '9':
            ssid = input("Enter the SSID for the hotspot: ")
            password = input("Enter the password for the hotspot: ")
            create_wifi_hotspot(ssid, password)
        elif choice == '10':
            log_signal_strength()
        elif choice == '11':
            backup_network_settings()
        elif choice == '12':
            reset_network_adapter()
        elif choice == '13':
            list_network_profiles()
        elif choice == '14':
            ssid = input("Enter the SSID to prioritize: ")
            prioritize_network_profile(ssid)
        elif choice == '15':
            default_ssid = input("Enter default SSID (leave blank to keep current): ")
            default_password = input("Enter default Password (leave blank to keep current): ")
            config = load_config()
            if default_ssid:
                config['default_ssid'] = default_ssid
            if default_password:
                config['default_password'] = default_password
            save_config(config)
            print("Configuration updated.")
        elif choice == '16':
            log_event("Wi-Fi manager exited.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
