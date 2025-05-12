# Power Usage Monitoring Script

import os
import subprocess
import sqlite3
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Configuration
DB_PATH = 'power_usage.db'
ALERT_THRESHOLD = 300  # Watts
CHECK_INTERVAL = 60  # Seconds
EMAIL = 'your-email@example.com'

# Function to initialize the database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS power_usage (
                        timestamp TEXT,
                        device TEXT,
                        power_watts REAL
                    )''')
    conn.commit()
    conn.close()

# Function to get power usage using IPMI
def get_power_usage(device):
    try:
        result = subprocess.check_output(['ipmitool', '-I', 'lanplus', '-H', device, '-U', 'admin', '-P', 'password', 'sensor'], encoding='utf-8')
        for line in result.split('\n'):
            if 'Power' in line:
                return float(line.split('|')[1].strip())
    except Exception as e:
        print(f'Error collecting data from {device}: {e}')
    return None

# Function to send alert email
def send_alert(device, power):
    msg = MIMEText(f'High power usage detected on {device}: {power} Watts')
    msg['Subject'] = 'Power Usage Alert'
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    with smtplib.SMTP('smtp.example.com') as server:
        server.send_message(msg)

# Monitoring loop
def monitor():
    devices = ['192.168.1.100', '192.168.1.101']  # Replace with actual IP addresses
    while True:
        for device in devices:
            power = get_power_usage(device)
            if power:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f'{timestamp} - {device} - {power} Watts')
                conn = sqlite3.connect(DB_PATH)
                cursor = conn.cursor()
                cursor.execute('INSERT INTO power_usage VALUES (?, ?, ?)', (timestamp, device, power))
                conn.commit()
                conn.close()
                if power > ALERT_THRESHOLD:
                    send_alert(device, power)
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    init_db()
    monitor()
