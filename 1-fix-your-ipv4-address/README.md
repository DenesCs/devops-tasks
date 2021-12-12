# Fix your IPv4 address

## Task

Write a shell script (use bash) to query your current public IP-address. Then calculate a "fixed" IP- address by incrementing each octet by one, eg. 1.2.3.4 -> 2.3.4.5
Print both the original and the fixed IP-address to stdout, eg.
My current IP-address is 74.125.133.27My fixed IP-address is 75.126.134.28 You may use http://checkip.amazonaws.com to get your IPv4 address
Verify the script using shellcheck to make sure it follows best practices, ie. shellcheck your-script.sh should provide no errors or warning.

## Solution

### Run bash script

```bash
➜  1-fix-your-ipv4-address git:(main) ✗ ./calculate_ip.sh 
My current IP-address is 193.16.224.10My fixed IP-address is 194.17.225.11
```
