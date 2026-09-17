statistics = {
    "total_packets": 0,
    "tcp_packets": 0,
    "udp_packets": 0,
    "icmp_packets": 0,
    "other_packets": 0
}


def update_statistics(packet_info):

    statistics["total_packets"] += 1

    if packet_info["protocol"] == "TCP":
        statistics["tcp_packets"] += 1

    elif packet_info["protocol"] == "UDP":
        statistics["udp_packets"] += 1

    elif packet_info["protocol"] == "ICMP":
        statistics["icmp_packets"] += 1

    else:
        statistics["other_packets"] += 1


def display_statistics():

    print("\n")
    print("========== NETWORK STATISTICS ==========")
    print("Total Packets :", statistics["total_packets"])
    print("TCP Packets   :", statistics["tcp_packets"])
    print("UDP Packets   :", statistics["udp_packets"])
    print("ICMP Packets  :", statistics["icmp_packets"])
    print("Other Packets :", statistics["other_packets"])
    print("========================================")