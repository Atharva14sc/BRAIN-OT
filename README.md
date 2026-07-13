# BRAIN-OT
### Behavioral Risk-Aware Adaptive Industrial Network Defense Platform

## 🚧 Project Status

**Status:** Under Development (Prototype Phase)

Expected Completion: December 2026

An Adaptive Industrial Cyber Defense Platform that continuously monitors industrial devices, detects cyber threats, evaluates behavioral trust using the Behavioral Adaptive Trust Index (BATI), and autonomously responds to security incidents in Industrial Control Systems (ICS) and Operational Technology (OT) environments.

## 📖 Project Overview

BRAIN-OT (Behavioral Risk-Aware Adaptive Industrial Network Defense Platform) is a cybersecurity platform designed to enhance the security of Industrial Control Systems (ICS) and Operational Technology (OT) environments through continuous monitoring, intelligent threat detection, adaptive trust evaluation, and automated incident response.

Unlike traditional Intrusion Detection Systems (IDS) that primarily generate alerts based on predefined signatures or anomalies, BRAIN-OT continuously evaluates the behavioral trustworthiness of industrial devices using the **Behavioral Adaptive Trust Index (BATI)**. BATI continuously computes a dynamic trust score using multiple behavioral indicators, allowing trust to evolve over time rather than relying on binary attack detection.

By combining industrial device monitoring, AI-assisted anomaly detection, adaptive trust scoring, automated response mechanisms, and a Security Operations Center (SOC) dashboard, BRAIN-OT provides a practical and intelligent cyber defense solution suitable for modern industrial environments.

## 🎯 Problem Statement

Industrial Control Systems (ICS) and Operational Technology (OT) are increasingly connected to enterprise networks and the Internet, making them increasingly vulnerable to cyber threats such as malware, insider attacks, unauthorized access, and protocol-based attacks.

Most existing Intrusion Detection Systems (IDS) focus on identifying known attack signatures or detecting isolated anomalies. While effective in generating alerts, these systems often lack continuous trust evaluation, adaptive decision-making, and automated response capabilities. Security analysts are therefore required to manually interpret alerts, verify device behavior and determine the appropriate response.

As industrial environments continue to expand, relying solely on static detection mechanisms becomes increasingly insufficient. There is a need for an intelligent cybersecurity platform capable of continuously evaluating behavioral trust, dynamically adapting trust levels, and autonomously responding to potential threats, while minimizing human intervention. 


## 💡 Novel Contribution

Unlike conventional Intrusion Detection Systems (IDS) that primarily detect attacks and generate alerts, BRAIN-OT introduces the **Behavioral Adaptive Trust Index (BATI)**—a lightweight adaptive trust evaluation model that continuously measures the trustworthiness of industrial devices using multiple behavioral indicators.

Rather than making binary security decisions based solely on detected attacks, BATI enables continuous trust evolution, allowing the platform to perform adaptive, context-aware, and automated cyber defense in Industrial Control Systems (ICS) and Operational Technology (OT) environments.

## 🎯 Project Objectives

The primary objectives of BRAIN-OT are:

- Develop and implement the "Behavioral Adaptive Trust Index (BATI)" to continuously evaluate the trustworthiness of industrial devices based on their behavioral characteristics.

- Detect suspicious device behavior through AI-assisted anomaly detection and network intrusion detection techniques.

- Automate incident response by dynamically applying security actions based on the calculated trust level of monitored devices.

- Provide an intuitive Security Operations Center (SOC) dashboard for real-time visualization of device status, trust evolution, alerts, and security events.

- Develop a modular, lightweight, and scalable cybersecurity platform suitable for industrial environments and future research.

## 🚀 Core Features

### 🔍 Industrial Device Monitoring
Continuously monitors industrial devices, network traffic, and communication behavior within Industrial Control Systems (ICS) and Operational Technology (OT) environments.

### 🛡️ Intrusion Detection
Identifies suspicious activities and potential cyber threats using network-based intrusion detection techniques and behavioral analysis.

### 🤖 AI-Assisted Anomaly Detection
Applies machine learning techniques to distinguish normal operational behavior from anomalous activities and emerging cyber threats.

### ⭐ Behavioral Adaptive Trust Index (BATI)
Continuously evaluates the trustworthiness of industrial devices by analyzing anomaly scores, communication confidence, protocol consistency, attack history, and recovery behavior to produce dynamic trust scores.

### ⚡ Automated Incident Response
Automatically executes appropriate mitigation actions such as alert generation, device isolation, communication blocking, or access restriction based on BATI-driven risk assessment.

### 📊 Security Operations Center (SOC) Dashboard
Provides a centralized dashboard for monitoring device status, trust evolution, alerts, security events, and overall industrial network health in real time.

## 🏗️ System Architecture

BRAIN-OT follows a modular architecture designed specifically for Industrial Control Systems (ICS) and Operational Technology (OT) environments.

The overall workflow is illustrated below:

Industrial Devices
        ↓
VVM801 Edge Device
        ↓
Monitoring Layer
        ↓
Intrusion Detection
        ↓
Behavioral Adaptive Trust Index (BATI)
        ↓
Decision Engine
        ↓
Automated Response
        ↓
SOC Dashboard

The BATI Engine serves as the core intelligence of the platform by continuously evaluating behavioral trust based on multiple parameters. Instead of making binary security decisions, BATI dynamically updates trust scores, enabling adaptive and context-aware cybersecurity responses.

## 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python 3.13 |
| Machine Learning | Scikit-learn |
| Network Analysis | Scapy |
| Dashboard | Flask |
| Database | SQLite |
| Version Control | Git & GitHub |
| Development Environment | Visual Studio Code |
| Industrial Communication | Modbus TCP (Simulation), VVM801 |
| Operating System | Windows 11 |

## 📁 Repository Structure

```text
BRAIN-OT/
│
├── assets/                      # Images, diagrams, logos, screenshots, and project media
│   ├── diagrams/
│   ├── images/
│   ├── logos/
│   ├── screenshots/
│   └── videos/
│
├── datasets/                    # Datasets for AI training, testing, and simulations
│
├── docs/                        # Project documentation
│   ├── proposal/
│   ├── literature-review/
│   ├── report/
│   ├── presentation/
│   └── diagrams/
│
├── hardware/                    # VVM801 integration and hardware-related files
│
├── journal/                     # Weekly development logs and progress tracking
│
├── research/                    # Research work and paper analysis
│   ├── papers/
│   ├── notes/
│   ├── comparisons/
│   └── research-gap/
│
├── scripts/                     # Utility and automation scripts
│
├── src/                         # Source code
│   ├── config/                  # Configuration files
│   ├── dashboard/               # Security Operations Center (SOC) Dashboard
│   ├── detection/               # Intrusion Detection Module
│   ├── engine/                  # BATI Engine and Trust Evaluation
│   ├── monitoring/              # Industrial Device Monitoring
│   ├── response/                # Automated Incident Response
│   └── utils/                   # Common helper functions
│
├── testing/                     # Testing, evaluation, and validation
│
├── .gitignore
├── CONTRIBUTING.md
├── README.md
├── requirements.txt
└── TODO.md
```

## 📅 Development Roadmap

| Phase | Description | Status |
|--------|-------------|:------:|
| Phase 1 | Project Planning, Literature Review, Repository Setup | ✅ Completed |
| Phase 2 | Industrial Device Monitoring Module | ⏳ Planned |
| Phase 3 | Intrusion Detection & AI-Assisted Anomaly Detection | ⏳ Planned |
| Phase 4 | Behavioral Adaptive Trust Index (BATI) Engine | ⏳ Planned |
| Phase 5 | Decision Engine & Automated Response | ⏳ Planned |
| Phase 6 | SOC Dashboard Development | ⏳ Planned |
| Phase 7 | VVM801 Hardware Integration | ⏳ Planned |
| Phase 8 | Testing, Evaluation & Final Demonstration | ⏳ Planned |

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Atharva14sc/BRAIN-OT.git
```

Navigate to the project directory:

```bash
cd BRAIN-OT
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```powershell
.venv\Scripts\activate
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

## 🔮 Future Scope

Future enhancements of BRAIN-OT may include:

- Support for additional industrial communication protocols.
- Explainable AI (XAI) for trust score interpretation.
- Deployment in cloud-based industrial environments.
- Advanced visualization and analytics within the SOC dashboard.
- Experimental validation and optimization of the Behavioral Adaptive Trust Index (BATI).

## 👨‍💻 Authors

**Atharva More**
**Tanisha Bhangare**
**Aanvii Kotlaapure**

Final Year B.E. Electronics & Telecommunication Engineering

Cyber Security (Honours)

Shah and Anchor Kutchhi Engineering College (SAKEC)

Mumbai, India

## 📄 License

This project is licensed under the MIT License.

See the LICENSE file for more details.

## 🙏 Acknowledgements

The authors would like to thank the faculty members of Shah and Anchor Kutchhi Engineering College for their guidance and support throughout the development of this project.

The project is inspired by recent research in Industrial Control System (ICS) cybersecurity, adaptive trust management, and AI-assisted intrusion detection.

## 📢 Disclaimer

BRAIN-OT is an academic research and development project created for educational and research purposes. The platform is intended to demonstrate adaptive cybersecurity concepts for Industrial Control Systems (ICS) and Operational Technology (OT) environments.
