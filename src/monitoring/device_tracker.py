from collections import defaultdict

class DeviceTracker:

    def __init__(self):
        self.devices = defaultdict(
            lambda: {
                "packets": 0,
                "protocols": set()
            }
        )

    def update(self, packet_info):

        src_ip = packet_info["source_ip"]
        protocol = packet_info["protocol"]

        self.devices[src_ip]["packets"] += 1
        self.devices[src_ip]["protocols"].add(protocol)

    def display(self):

        print("\n")
        print("========== DISCOVERED DEVICES ==========")

        for ip, data in self.devices.items():

            protocols = ", ".join(data["protocols"])

            print(f"\nIP Address : {ip}")
            print(f"Packets    : {data['packets']}")
            print(f"Protocols  : {protocols}")

        print("========================================")
        print("========================================")