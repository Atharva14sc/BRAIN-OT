class BATIEngine:

    def __init__(self):

        self.high_risk_ports = {

            # IT Services
            21: ("FTP Service", 15),
            23: ("TELNET Service", 30),
            135: ("RPC Service", 20),
            139: ("NETBIOS Service", 25),
            445: ("SMB Service", 40),
            3389: ("RDP Service", 30),

            # OT / ICS Services
            502: ("MODBUS TCP", 25),
            102: ("SIEMENS S7", 25),
            44818: ("ETHERNET/IP", 25),
            20000: ("DNP3", 25)
        }

    def calculate_score(self, packet_info):

        score = 100
        reasons = []

        protocol = packet_info.get("protocol") or "Other"
        packet_length = packet_info.get("packet_length") or 0
        destination_port = packet_info.get("destination_port") or 0
        source_ip = packet_info.get("source_ip") or ""
        destination_ip = packet_info.get("destination_ip") or ""

        # High Risk Service Detection

        if destination_port in self.high_risk_ports:

            service_name, penalty = self.high_risk_ports[destination_port]

            score -= penalty
            reasons.append(service_name)

        # Unknown Protocol

        if protocol == "Other":

            score -= 15
            reasons.append("Unknown Protocol")

        # Very Large Packet

        if packet_length > 1500:

            score -= 10
            reasons.append("Abnormally Large Packet")

        # Industrial Protocol Monitoring

        industrial_ports = {
            502: "MODBUS",
            102: "SIEMENS S7",
            44818: "ETHERNET/IP",
            20000: "DNP3"
        }

        if destination_port in industrial_ports:

            score -= 10
            reasons.append(
                f"ICS Traffic ({industrial_ports[destination_port]})"
            )

        # External Access To OT Service

        internal_source = (
            source_ip.startswith("10.")
            or source_ip.startswith("192.168.")
            or source_ip.startswith("172.")
        )

        internal_destination = (
            destination_ip.startswith("10.")
            or destination_ip.startswith("192.168.")
            or destination_ip.startswith("172.")
        )

        if (
            not internal_source
            and internal_destination
            and destination_port in industrial_ports
        ):

            score -= 30
            reasons.append(
                "External Access To OT Service"
            )

        # Dangerous IT Services

        dangerous_ports = [
            21,
            23,
            445,
            3389
        ]

        if destination_port in dangerous_ports:

            score -= 15
            reasons.append(
                "Sensitive Service Exposure"
            )

        # Score Bounds

        score = max(score, 0)

        # Classification

        if score >= 90:

            status = "TRUSTED"

        elif score >= 75:

            status = "MONITOR"

        elif score >= 50:

            status = "SUSPICIOUS"

        else:

            status = "CRITICAL"

        return score, status, reasons