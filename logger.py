import serial
import csv
import os
from datetime import datetime

PORT = "COM12"
BAUD = 9600
OUTPUT_FILE = "C:/Users/admin/OneDrive/Desktop/air_quality_data.csv"

headers = ["timestamp", "millis", "temperature_C", "humidity_pct", "gas_level", "quality"]
file_exists = os.path.isfile(OUTPUT_FILE)

with open(OUTPUT_FILE, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(headers)

print("Logging started... Press Ctrl+C to stop")

with serial.Serial(PORT, BAUD, timeout=2) as ser:
    while True:
        try:
            line = ser.readline().decode("utf-8").strip()
            print("RAW:", repr(line))
            if not line or "," not in line or "millis" in line:
                continue
            parts = line.split(",", 4)
            if len(parts) < 5:
                continue
            row = [datetime.now().isoformat()] + parts
            print(row)
            with open(OUTPUT_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(row)
        except KeyboardInterrupt:
            print("Logging stopped.")
            break
        except Exception as e:
            print("Error:", e)