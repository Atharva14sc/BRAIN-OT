from collections import defaultdict

class PortScanDetector:

    def __init__(self):
        self.destination_ports = defaultdict(set)

    def update(self, packet_info):

        src_ip = packet_info["source_ip"]

        if packet_info["destination_port"] is not None:
            self.destination_ports[src_ip].add(
                packet_info["destination_port"]
            )

    def is_scanning(self, src_ip):

        if len(self.destination_ports[src_ip]) > 10:
            return True

        return False