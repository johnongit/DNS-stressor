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
   pip install dnspython scapy
   ```

## Usage

The `dns_stressor.py` script takes the following parameters:

- `server`: The IP address of the target DNS server.
- `qps`: The number of queries per second to generate.
- `record`: The DNS record to resolve (e.g., "example.com").
- `duration`: The duration of the load generation in seconds.
- `source_ip`: The source IP address to use for the DNS queries.

To run the script, use the following command:

```
sudo python dns_stressor.py <server> <qps> <record> <duration> <source_ip>
```

Replace `<server>`, `<qps>`, `<record>`, `<duration>`, and `<source_ip>` with the appropriate values.

**Note:** The script requires root privileges to modify the source IP address of the DNS queries.

## Example

Here's an example usage of the script:

```
sudo python dns_stressor.py 192.168.1.100 100 example.com 60 192.168.1.200
```

This example generates a load of 100 DNS queries per second for 60 seconds towards the DNS server located at IP address 192.168.1.100, resolving the record "example.com". The DNS queries will use the source IP address 192.168.1.200.

## Logging

The script includes logging of the number of queries sent per second. The log messages are displayed in the console during the execution of the script.

## Contributing

Contributions to this project are welcome. If you would like to make improvements or fix any issues, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Suggested repository title: `dns-load-generator`

This README.md file provides an overview of the project, installation instructions, usage guidelines, an example usage, information about logging and contributing, and the project license.

Feel free to customize the content based on your project's specific details.
