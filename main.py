from firewall import (
    load_rules,
    firewall_check,
    view_rules
)

from report import generate_report


def main():

    rules = load_rules()
    print("\n===================================")
    print("      PERSONAL FIREWALL")        
    print("===================================")
    print("1. Check Port")
    print("2. View Firewall Rules")
    print("3. Generate Security Report")
    print("4. Exit")
    while True:

        choice = input(
            "\nChoose an option: "
        )

        if choice == "1":

            firewall_check(rules)

        elif choice == "2":

            view_rules(rules)

        elif choice == "3":

            generate_report()

        elif choice == "4":

            print(
                "\nFirewall shutting down..."
            )

            break

        else:

            print(
                "Invalid option."
            )


if __name__ == "__main__":
    main()