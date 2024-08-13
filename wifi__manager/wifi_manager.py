import subprocess
import csv
import datetime
import json
import logging
import time

# Configure logging
def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(message):
    logging.error(message)
    print(f"Error: {message}")

def log_info(message):
    logging.info(message)
    print(f"Info: {message}")

def load_config(filename='config.json'):
    with open(filename, 'r') as file:
        return json.load(file)

def save_config(config, filename='config.json'):
    with open(filename, 'w') as file:
        json.dump(config, file, indent=4)

def scan_networks():
    log_info("Scanning for available networks...")
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'networks'], capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to scan networks: {e}")

def connect_to_network(ssid=None, password=None):
    config = load_config()
    ssid = ssid or config.get('default_ssid')
    password = password or config.get('default_password')
    
    if not ssid or not password:
        log_error("SSID and password must be provided.")
        return

    profile = f"""
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>{ssid}</name>
        <SSIDConfig>
            <SSID>
                <name>{ssid}</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>{password}</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>
    """
    try:
        with open(f'{ssid}.xml', 'w') as file:
            file.write(profile)
        subprocess.run(['netsh', 'wlan', 'add', 'profile', f'filename={ssid}.xml'], check=True)
        subprocess.run(['netsh', 'wlan', 'connect', f'name={ssid}'], check=True)
        log_info(f"Attempting to connect to {ssid}...")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to connect to the network: {e}")

def current_connection_info():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to retrieve current connection info: {e}")

def delete_network_profile(ssid):
    try:
        subprocess.run(['netsh', 'wlan', 'delete', 'profile', f'name={ssid}'], check=True)
        log_info(f"Deleted profile for {ssid}")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to delete profile for {ssid}: {e}")

def monitor_signal_strength():
    try:
        while True:
            result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if "Signal" in line:
                    signal_strength = line.split(":")[1].strip()
                    print(f"Current Signal Strength: {signal_strength}")
            time.sleep(5)
    except KeyboardInterrupt:
        log_info("Stopping signal strength monitoring.")

def run_speed_test():
    try:
        print("Pinging google.com to test network speed...")
        result = subprocess.run(['ping', 'google.com', '-n', '5'], capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to run speed test: {e}")

def run_traceroute(destination):
    try:
        result = subprocess.run(['tracert', destination], capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to run traceroute to {destination}: {e}")

def set_dns_servers(dns1, dns2):
    try:
        subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'dnsservers', 'Wi-Fi', f'static', dns1, 'primary'], check=True)
        subprocess.run(['netsh', 'interface', 'ipv4', 'add', 'dnsservers', 'Wi-Fi', dns2, 'index=2'], check=True)
        log_info(f"Set DNS servers to {dns1} and {dns2}.")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to set DNS servers: {e}")

def create_wifi_hotspot(ssid, password):
    try:
        subprocess.run(['netsh', 'wlan', 'set', 'hostednetwork', f'mode=allow', f'ssid={ssid}', f'key={password}'], check=True)
        subprocess.run(['netsh', 'wlan', 'start', 'hostednetwork'], check=True)
        log_info(f"Wi-Fi hotspot {ssid} created and started.")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to create Wi-Fi hotspot {ssid}: {e}")

def log_signal_strength():
    with open('signal_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'SSID', 'Signal Strength'])

        while True:
            result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ssid = "Unknown"
            for line in result.stdout.splitlines():
                if "SSID" in line:
                    ssid = line.split(":")[1].strip()
                if "Signal" in line:
                    signal_strength = line.split(":")[1].strip()
                    writer.writerow([timestamp, ssid, signal_strength])
            time.sleep(5)

def backup_network_settings(backup_file="network_backup.txt"):
    with open(backup_file, 'w') as file:
        result = subprocess.run(['netsh', 'wlan', 'show', 'all'], capture_output=True, text=True)
        file.write(result.stdout)
        log_info(f"Network settings backed up to {backup_file}.")

def log_event(event):
    with open('wifi_event_log.txt', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {event}\n")
        log_info(f"Logged event: {event}")

def reset_network_adapter():
    try:
        subprocess.run(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=disable'], check=True)
        time.sleep(2)
        subprocess.run(['netsh', 'interface', 'set', 'interface', 'name="Wi-Fi"', 'admin=enable'], check=True)
        log_info("Network adapter reset successfully.")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to reset network adapter: {e}")

def list_network_profiles():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True)
        profiles = [line.split(":")[1].strip() for line in result.stdout.splitlines() if "All User Profile" in line]
        print("Available Network Profiles:")
        for profile in profiles:
            print(profile)
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to list network profiles: {e}")

def prioritize_network_profile(ssid):
    try:
        subprocess.run(['netsh', 'wlan', 'set', 'profile', f'name={ssid}', 'priority=1'], check=True)
        log_info(f"Network profile {ssid} prioritized.")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to prioritize network profile {ssid}: {e}")
