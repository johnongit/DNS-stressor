# DNS Load Generator

A Python script to generate a controlled load of DNS queries towards a specified server, based on the provided parameters. It is designed to help in sizing and testing DNS servers by simulating a controlled query load.

## Prerequisites

- Python 3.x
- `dnspython` library
- `scapy` library

## Installation

1. Clone this GitHub repository:
   ```
   git clone https://github.com/johnongit/DNS-stressor.git
   ```

2. Navigate to the project directory:
   ```
   cd DNS-stressor
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.tx
   ```

## Usage

The `dns_stressor.py` script takes the following parameters:

- `server`: The IP address of the target DNS server.
- `qps`: The number of queries per second to generate.
- `record`: The DNS record to resolve (e.g., "example.com").
- `duration`: The duration of the load generation in seconds.
- `--source-ips-file`: (Optional) A file containing a list of source IP addresses to use for the DNS queries. Each IP address should be on a separate line.

To run the script, use the following command:

```
sudo python dns_stressor.py <server> <qps> <record> <duration> [--source-ips-file <file>]
```

Replace <server>, <qps>, <record>, <duration>, and optionally <file> with the appropriate values.

**Note:** The script requires root privileges to modify the source IP address of the DNS queries.

## Example

Here's an example usage of the script:

```
sudo python dns_stressor.py 192.168.1.100 100 example.com 60 --source-ips-file source_ips.txt
```

This example generates a load of 100 DNS queries per second for 60 seconds towards the DNS server located at IP address 192.168.1.100, resolving the record "example.com". The DNS queries will use the source IP addresses specified in the file "source_ips.txt".

## Additional Information

This domain is used for illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission. More information is available at http://example.com.

## Logging

The script includes logging of the number of queries sent per second. The log messages are displayed in the console during the execution of the script.

## Contributing

Contributions to this project are welcome. If you would like to make improvements or fix any issues, feel free to submit a pull request.

