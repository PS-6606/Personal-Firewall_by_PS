import json
from collections import Counter

STATS_FILE = "stats.json"
LOG_FILE = "logs.txt"


def generate_report():

    try:

        with open(
            STATS_FILE,
            "r"
        ) as file:

            stats = json.load(file)

    except:

        stats = {
            "total_connections": 0,
            "allowed_connections": 0,
            "blocked_connections": 0,
            "no_rule_connections": 0
        }

    try:

        with open(
            LOG_FILE,
            "r"
        ) as file:

            logs = file.readlines()

    except:

        logs = []

    ports = []

    for line in logs:

        try:

            port = (
                line.split("|")[1]
                .strip()
                .replace(
                    "Port ",
                    ""
                )
            )

            ports.append(port)

        except:

            pass

    print(
        "\n========== SECURITY REPORT =========="
    )

    print(
        f"Total Connections: "
        f"{stats['total_connections']}"
    )

    print(
        f"Allowed Connections: "
        f"{stats['allowed_connections']}"
    )

    print(
        f"Blocked Connections: "
        f"{stats['blocked_connections']}"
    )

    print(
        f"No Rule Connections: "
        f"{stats['no_rule_connections']}"
    )

    print(
        f"\nBlocked Attempts Logged: "
        f"{len(logs)}"
    )

    if ports:

        most_targeted = (
            Counter(ports)
            .most_common(1)[0][0]
        )

        print(
            f"Most Targeted Port: "
            f"{most_targeted}"
        )

    else:

        print(
            "Most Targeted Port: None"
        )

    print(
        "\nRecent Blocked Connections:"
    )

    for line in logs[-5:]:

        print(
            line.strip()
        )