from scapy.all import IP, TCP, UDP, ICMP


def parse_packet(packet):

    if not packet.haslayer(IP):
        return None

    protocol = "Other"
    source_port = None
    destination_port = None

    if packet.haslayer(TCP):
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif packet.haslayer(UDP):
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif packet.haslayer(ICMP):
        protocol = "ICMP"

    packet_info = {
        "source_ip": packet[IP].src,
        "destination_ip": packet[IP].dst,
        "protocol": protocol,
        "source_port": source_port,
        "destination_port": destination_port,
        "packet_length": len(packet)
    }

    return packet_info