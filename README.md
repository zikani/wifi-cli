# WiFi-CLI Manager

`wifi-cli` is a command-line interface tool for managing Wi-Fi connections and settings on Windows. It provides a range of features for network scanning, connection management, signal monitoring, and more.

## Features

- Scan for available Wi-Fi networks
- Connect to a Wi-Fi network
- Show current connection information
- Delete network profiles
- Monitor signal strength
- Run speed tests
- Perform traceroute
- Set DNS servers
- Create and manage Wi-Fi hotspots
- Log signal strength
- Backup and reset network settings
- Prioritize and list network profiles

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/zikani/wifi-cli.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd wifi-cli
   ```

3. **Install the Package**

   ```bash
   pip install .
   ```

## Usage

The wifi-cli tool is used via the command line. Here is the basic syntax:

   ```bash
   wifi-cli <command> [options]
   ```

### Example Commands

- Scan for networks:
   ```bash
   wifi-cli scan
   ```

- Connect to a network:
   ```bash
   wifi-cli connect --ssid <SSID> --password <PASSWORD>
   ```

- Update default configuration:
   ```bash
   wifi-cli update --ssid <SSID> --password <PASSWORD>
   ```

### Running as a Module

You can also run `wifi-cli` as a Python module using the `-m` flag:

   ```bash
   python -m wifi-cli <command> [options]
   ```

Example:
   ```bash
   python -m wifi-cli scan
   ```

### Running as a Script

Alternatively, you can run `wifi-cli` as a script directly:

   ```bash
   python path/to/wifi-cli <command> [options]
   ```

Example:
   ```bash
   python path/to/wifi-cli scan
   ```

This `README.md` provides a comprehensive guide to using the `wifi-cli` tool, including installation instructions, detailed usage examples, configuration options, and troubleshooting tips.

