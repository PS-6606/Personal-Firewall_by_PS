import json
from datetime import datetime

RULES_FILE = "rules.json"
STATS_FILE = "stats.json"
LOG_FILE = "logs.txt"

PORT_SERVICES = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    135: "RPC",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    587: "SMTP Submission",
    993: "Secure IMAP",
    995: "Secure POP3",
    1433: "Microsoft SQL Server",
    1434: "SQL Monitor",
    3306: "MySQL",
    3389: "Remote Desktop Protocol",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "Alternative HTTP",
    8443: "Alternative HTTPS"
}


def load_rules():

    with open(RULES_FILE, "r") as file:
        return json.load(file)


def load_stats():

    try:

        with open(STATS_FILE, "r") as file:
            return json.load(file)

    except:

        return {
            "total_connections": 0,
            "allowed_connections": 0,
            "blocked_connections": 0,
            "no_rule_connections": 0
        }


def save_stats(stats):

    with open(STATS_FILE, "w") as file:
        json.dump(stats, file, indent=4)


def check_port(port, rules):

    if port in rules["blocked_ports"]:
        return "BLOCKED"

    elif port in rules["allowed_ports"]:
        return "ALLOWED"

    else:
        return "NO RULE"


def log_connection(port, action):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(LOG_FILE, "a") as file:

        file.write(
            f"{timestamp} | Port {port} | {action}\n"
        )


def firewall_check(rules):

    stats = load_stats()

    try:

        port = int(
            input(
                "\nEnter Port Number: "
            )
        )

    except ValueError:

        print(
            "Invalid port number."
        )
        return

    result = check_port(
        port,
        rules
    )

    service = PORT_SERVICES.get(
        port,
        "Unknown Service"
    )

    print(
        f"\nPort {port} ({service}): {result}"
    )

    stats["total_connections"] += 1

    if result == "ALLOWED":

        stats["allowed_connections"] += 1

    elif result == "BLOCKED":

        stats["blocked_connections"] += 1

        log_connection(
            port,
            result
        )

    else:

        stats["no_rule_connections"] += 1

    save_stats(stats)


def view_rules(rules):

    print(
        "\n===== FIREWALL RULES ====="
    )

    print("\nAllowed Ports:")

    for port in rules["allowed_ports"]:

        service = PORT_SERVICES.get(
            port,
            "Unknown Service"
        )

        print(
            f"{port} ({service})"
        )

    print("\nBlocked Ports:")

    for port in rules["blocked_ports"]:

        service = PORT_SERVICES.get(
            port,
            "Unknown Service"
        )

        print(
            f"{port} ({service})"
        )