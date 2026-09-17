import sys
import os

# ----------------------------------
# Add ML Folder To Python Path
# ----------------------------------

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

SRC_DIR = os.path.dirname(CURRENT_DIR)

ML_DIR = os.path.join(SRC_DIR, "ml")

sys.path.append(ML_DIR)

# ----------------------------------
# Imports
# ----------------------------------

from scapy.all import sniff

from packet_parser import parse_packet
from packet_logger import log_packet

from monitoring_statistics import (
    update_statistics,
    display_statistics,
    statistics
)

from device_tracker import DeviceTracker
from bati_engine import BATIEngine

from threat_decision_engine import ThreatDecisionEngine

# ----------------------------------
# Startup Banner
# ----------------------------------

print("Starting BRAIN-OT Packet Capture...")
print("BATI MODULE LOADED")
print("THREAT DECISION ENGINE LOADED")
print("TEST VERSION 5")

# ----------------------------------
# Initialize Components
# ----------------------------------

tracker = DeviceTracker()

bati = BATIEngine()

decision_engine = ThreatDecisionEngine()

# ----------------------------------
# Packet Processing Function
# ----------------------------------

def process_packet(packet):

    # ------------------------------
    # Parse Packet
    # ------------------------------

    packet_info = parse_packet(packet)

    if packet_info is None:
        return

    # ------------------------------
    # Update Statistics
    # ------------------------------

    update_statistics(packet_info)

    # ------------------------------
    # Update Device Tracker
    # ------------------------------

    tracker.update(packet_info)

    # ------------------------------
    # BATI Analysis
    # ------------------------------

    score, status, reasons = bati.calculate_score(
        packet_info
    )

    # ------------------------------
    # ML Disabled For Now
    # ------------------------------

    threat_type = "normal"

    # ------------------------------
    # Decision Engine
    # ------------------------------

    decision = decision_engine.evaluate(
        bati_score=score,
        bati_status=status,
        threat_type=threat_type,
        anomaly_detected=False
    )

    # ------------------------------
    # Log Packet
    # ------------------------------

    log_packet(
        packet_info,
        score,
        status,
        reasons
    )

    # ------------------------------
    # Display Results
    # ------------------------------

    print("\n===================================")

    print("Source IP        :", packet_info["source_ip"])
    print("Destination IP   :", packet_info["destination_ip"])

    print("Protocol         :", packet_info["protocol"])

    print("Source Port      :", packet_info["source_port"])
    print("Destination Port :", packet_info["destination_port"])

    print("Packet Length    :", packet_info["packet_length"])

    print("-----------------------------------")

    print("BATI Score       :", score)
    print("BATI Status      :", status)

    if reasons:

        print(
            "BATI Reasons     :",
            ", ".join(reasons)
        )

    else:

        print(
            "BATI Reasons     : None"
        )

    print("-----------------------------------")

    print("ML Threat Type   :", threat_type)

    print(
        "Final Verdict    :",
        decision["status"]
    )

    print(
        "Confidence       :",
        str(decision["confidence"]) + "%"
    )

    if decision["reasons"]:

        print(
            "AI Reasons       :",
            ", ".join(decision["reasons"])
        )

    print("===================================")

    # ------------------------------
    # Threat Alert
    # ------------------------------

    if decision["status"] in [
        "SUSPICIOUS",
        "HIGH RISK",
        "CRITICAL"
    ]:

        print("\n" + "=" * 50)

        print("🚨🚨 BRAIN-OT ALERT 🚨🚨")

        print(
            "Source IP        :",
            packet_info["source_ip"]
        )

        print(
            "Destination IP   :",
            packet_info["destination_ip"]
        )

        print(
            "Verdict          :",
            decision["status"]
        )

        print(
            "Confidence       :",
            str(decision["confidence"]) + "%"
        )

        if decision["reasons"]:

            print(
                "Reasons          :",
                ", ".join(decision["reasons"])
            )

        print("=" * 50)

    # ------------------------------
    # Periodic Statistics
    # ------------------------------

    if statistics["total_packets"] % 20 == 0:

        display_statistics()

        tracker.display()

# ----------------------------------
# Start Packet Capture
# ----------------------------------

sniff(
    filter="ip",
    prn=process_packet,
    store=False
)