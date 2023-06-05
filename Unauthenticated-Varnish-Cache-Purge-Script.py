import sys
import subprocess

# Read subdomains from the text file
subdomains_file = "subdomains.txt"

try:
    with open(subdomains_file, "r") as file:
        # Read the lines from the file and strip any leading or trailing whitespace
        # Ignore empty lines
        subdomains = [line.strip() for line in file if line.strip()]
except IOError:
    print("Subdomains file '{}' not found.".format(subdomains_file))
    sys.exit(1)

vulnerabilities_detected = False  # Flag to track if any vulnerabilities are detected

for subdomain in subdomains:
    url = "https://{}.com/".format(subdomain)
    # Construct the curl command with --insecure flag to disable SSL certificate verification
    command = "curl --insecure -X PURGE {}".format(url)
    
    try:
        # Execute the curl command and capture the output
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        # Decode the output from bytes to string
        output = output.decode("utf-8")
        
        # Check if the output contains "status": "ok"
        if "status\": \"ok\"" in output:
            vulnerabilities_detected = True
            # Print the "VULNERABILITY DETECTED" message in red color
            print("\033[91mVULNERABILITY DETECTED in subdomain:", subdomain, "\033[0m")
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during the curl command execution
        print("Error executing curl command for subdomain {}: {}".format(subdomain, e.output.decode("utf-8")))

if not vulnerabilities_detected:
    # Print the "NO Unauthenticated Varnish Cache Purge VULNERABILITY" message in blue color
    print("\033[94mNO Unauthenticated Varnish Cache Purge VULNERABILITY\033[0m")
