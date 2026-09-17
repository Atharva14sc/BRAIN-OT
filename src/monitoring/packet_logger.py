import csv
import os
from datetime import datetime

# ==================================
# LOG DIRECTORY SETUP
# ==================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "packets.csv")


# ==================================
# PACKET LOGGER
# ==================================

def log_packet(packet_info, score, status, reasons):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.isfile(LOG_FILE)

    with open(
        LOG_FILE,
        mode="a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # Create CSV header if file is new
        if not file_exists:

            writer.writerow([
                "Timestamp",
                "Source IP",
                "Destination IP",
                "Protocol",
                "Source Port",
                "Destination Port",
                "Packet Length",
                "BATI Score",
                "Status",
                "Reasons"
            ])

        # Write packet row
        writer.writerow([
            timestamp,
            packet_info.get("source_ip"),
            packet_info.get("destination_ip"),
            packet_info.get("protocol"),
            packet_info.get("source_port"),
            packet_info.get("destination_port"),
            packet_info.get("packet_length"),
            score,
            status,
            "; ".join(reasons) if reasons else ""
        ])