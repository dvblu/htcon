Subprocess Ping Script
This Python script demonstrates how to use the subprocess module to perform ping operations on one or more hosts. It allows you to check the reachability of hosts (either by hostname or IP address) from the command line.

Prerequisites
Python installed on your system (version 3.x)
Basic understanding of Python programming language
Usage
Run the Script:

Save the script to a file, for example, ping_hosts.py.
Open a terminal or command prompt.
Navigate to the directory containing the script.
Run the script using the command:
css
Copy code
python ping_hosts.py [host1] [host2] ...
Replace [host1] [host2] ... with the hosts you want to ping. You can provide multiple hosts separated by spaces.
Follow the Instructions:

If you don't provide hosts as command-line arguments, the script will prompt you to enter hosts.
Enter hosts separated by spaces and press Enter.
View Results:

The script will ping each provided host and display the results.
If a host is reachable, it will print a success message. If not, it will print a failure message.
Example
Copy code
python ping_hosts.py example.com 192.168.1.1
Script Explanation
The script defines a ping_host function that uses the subprocess.run() function to execute the ping command and check the reachability of a host.
If the script is run directly (not imported as a module), it checks if hosts are provided as command-line arguments. If not, it prompts the user to enter hosts.
The script then iterates over each host, pings it using the ping_host function, and prints the results.
Finally, it prints an overall summary of reachability, highlighting successful and failed pings.
Note: This script is for demonstration purposes and may need adjustments based on your specific requirements or environment.
