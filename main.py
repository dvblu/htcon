import subprocess
import sys

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
        print(f"An error occurred while pinging {host}. Error: {e}")
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
            print(f"\033[92mHost {hosts[0]} is reachable.\033[0m")  # Green color
        else:
            print("\033[92mAll hosts are reachable.\033[0m")  # Green color
    else:
        print("\033[91mFailed to reach the following hosts:\033[0m")  # Red color
        for host in failed_pings:
            print(f"\033[91m{host}\033[0m")
