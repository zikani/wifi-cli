from .wifi_manager import (scan_networks, connect_to_network, current_connection_info, delete_network_profile,
                           monitor_signal_strength, run_speed_test, run_traceroute, set_dns_servers, 
                           create_wifi_hotspot, log_signal_strength, backup_network_settings, log_event, 
                           reset_network_adapter, list_network_profiles, prioritize_network_profile)
import json
import logging

def setup_logging(log_file):
    logging.basicConfig(filename=log_file,
                        level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Logging setup complete.')

def load_config(config_file='config.json'):
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        # Return a default configuration if the file does not exist
        return {
            'default_ssid': '',
            'default_password': '',
            'log_file': 'wifi_manager.log'
        }
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse config file: {e}")
        return {}

def save_config(config, config_file='config.json'):
    try:
        with open(config_file, 'w') as file:
            json.dump(config, file, indent=4)
    except IOError as e:
        logging.error(f"Failed to save config file: {e}")

def update_default_config(ssid=None, password=None):
    config = load_config()
    if ssid:
        config['default_ssid'] = ssid
    if password:
        config['default_password'] = password
    save_config(config)
