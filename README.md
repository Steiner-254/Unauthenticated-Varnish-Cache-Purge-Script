# Unauthenticated Varnish Cache Purge Vulnerability Check

This Python script allows you to check for vulnerabilities in a list of subdomains using the `curl` command. It specifically checks for unauthenticated Varnish Cache Purge vulnerabilities.

## Prerequisites

- Python 3.x
- `curl` command-line tool

## Getting Started

1. Clone the repository or download the `subdomain_vulnerability_check.py` script.

2. Create a text file named `subdomains.txt` in the same directory as the script.

3. Add the subdomains to be checked, each on a new line, in the `subdomains.txt` file. Example:

4. Open a terminal or command prompt and navigate to the directory where the script is located.

5. Run the script using the following command:
$ python subdomain_vulnerability_check.py


6. The script will execute the `curl` command for each subdomain and check for vulnerabilities. If a vulnerability is detected, it will be displayed in red color. If no vulnerabilities are found, a message will be displayed in blue color.

Note: Make sure you have the necessary permissions to execute the script and that the `curl` command is available in your system's PATH.

## Example Output

Here's an example output of running the script:

VULNERABILITY DETECTED in subdomain: subdomain1
VULNERABILITY DETECTED in subdomain: subdomain3
NO Unauthenticated Varnish Cache Purge VULNERABILITY
