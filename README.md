# Power Usage Monitoring Script

## Description

This script monitors the power consumption of servers using IPMI. It records data in a SQLite database and sends alert emails when power usage exceeds a specified threshold.

## Features

* Tracks power consumption using IPMI.
* Stores historical data in a SQLite database.
* Sends alert emails if power usage exceeds a set threshold.
* Supports multiple devices.
* Runs on a scheduled interval.

## Prerequisites

* Python 3.x
* IPMItool installed
* SMTP server credentials
* SQLite3

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/power-usage-monitoring.git
   cd power-usage-monitoring
   ```

2. Install required packages:

   ```bash
   pip install smtplib
   ```

3. Edit the script to update the following:

   * IP addresses of the devices to monitor.
   * IPMI credentials (username, password).
   * SMTP server settings for sending alerts.

## Usage

Run the script:

```bash
python power_usage_monitoring.py
```

## Configuration

* Update the following variables in the script:

  * `DB_PATH` - Path to the SQLite database.
  * `ALERT_THRESHOLD` - Power consumption limit in Watts.
  * `CHECK_INTERVAL` - Time interval between checks (in seconds).
  * `EMAIL` - Email address for sending alerts.

## Troubleshooting

* Ensure IPMItool is correctly configured and accessible.
* Check for firewall rules blocking IPMI or SMTP ports.
* Verify SMTP settings and credentials.

## License

MIT License
