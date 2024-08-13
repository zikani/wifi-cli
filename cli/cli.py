import argparse
from wifi_manager import (scan_networks, connect_to_network, current_connection_info, delete_network_profile,
                          monitor_signal_strength, run_speed_test, run_traceroute, set_dns_servers, 
                          create_wifi_hotspot, log_signal_strength, backup_network_settings, log_event, 
                          reset_network_adapter, list_network_profiles, prioritize_network_profile, 
                          load_config, save_config, setup_logging, update_default_config)

def main():
    parser = argparse.ArgumentParser(description="Wi-Fi Manager CLI")
    parser.add_argument('command', choices=[
        'scan', 'connect', 'info', 'delete', 'monitor', 'speed', 'traceroute', 
        'dns', 'hotspot', 'log', 'backup', 'reset', 'list', 'prioritize', 'update'
    ], help="Command to execute")
    parser.add_argument('--ssid', help="SSID for connection or hotspot")
    parser.add_argument('--password', help="Password for connection or hotspot")
    parser.add_argument('--dns1', help="Primary DNS server")
    parser.add_argument('--dns2', help="Secondary DNS server")
    parser.add_argument('--destination', help="Destination for traceroute")
    parser.add_argument('--config', help="Configuration file", default='config.json')
    
    args = parser.parse_args()

    config = load_config(args.config)
    setup_logging(config.get('log_file', 'wifi_manager.log'))
    
    if args.command == 'scan':
        scan_networks()
    elif args.command == 'connect':
        connect_to_network(args.ssid, args.password)
    elif args.command == 'info':
        current_connection_info()
    elif args.command == 'delete':
        delete_network_profile(args.ssid)
    elif args.command == 'monitor':
        monitor_signal_strength()
    elif args.command == 'speed':
        run_speed_test()
    elif args.command == 'traceroute':
        run_traceroute(args.destination)
    elif args.command == 'dns':
        set_dns_servers(args.dns1, args.dns2)
    elif args.command == 'hotspot':
        create_wifi_hotspot(args.ssid, args.password)
    elif args.command == 'log':
        log_signal_strength()
    elif args.command == 'backup':
        backup_network_settings()
    elif args.command == 'reset':
        reset_network_adapter()
    elif args.command == 'list':
        list_network_profiles()
    elif args.command == 'prioritize':
        prioritize_network_profile(args.ssid)
    elif args.command == 'update':
        update_default_config(args.ssid, args.password)
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
