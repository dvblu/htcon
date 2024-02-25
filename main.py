import sys
import subprocess

# Color codes for formatting
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
NC = '\033[0m'  # No Color

# Function to ping a host (either hostname or IP address)
def ping_host(host):
    try:
        # Use the 'ping' command to check the reachability of the host
        result = subprocess.run(["ping", "-n", "4", host], capture_output=True, text=True)
        print(f"Pinging {host} with 32 bytes of data:")
        print(result.stdout)
        return result.returncode == 0  # Return True if the host is reachable, False otherwise
    except Exception as e:
        # Handle any errors that may occur during ping
        print(f"{RED}An error occurred while pinging {host}. Error: {e}{NC}")
        return False

if __name__ == "__main__":
    # Check if hosts are provided as command-line arguments
    if len(sys.argv) > 1:
        hosts = sys.argv[1:]
    else:
        # Prompt the user to enter hosts if not provided as arguments
        hosts_input = input("Enter hosts separated by space: ")
        hosts = hosts_input.split()

    # Initialize lists to track failed pings
    failed_pings = []

    # Iterate over each host and ping it
    for host in hosts:
        # Ping the host
        reachable = ping_host(host)
        if not reachable:
            failed_pings.append(host)

        # Add a newline for better readability between each set of pings
        print()

    # Print overall reachability summary with color
    if not failed_pings:
        if len(hosts) == 1:
            print(f"{GREEN}Host {hosts[0]} is reachable.{NC}")  # Green color
        else:
            print(f"{GREEN}All hosts are reachable.{NC}")  # Green color
    else:
        print(f"{RED}Failed to reach the following hosts:{NC}")  # Red color
        for host in failed_pings:
            print(f"{RED}{host}{NC}")
