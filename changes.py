class ChangeLog:
    def __init__(self):
        self.changes = []

    def add_change(self, version, date, description):
        change_entry = {
            "version": version,
            "date": date,
            "description": description
        }
        self.changes.append(change_entry)

    def display_changes(self):
        for change in self.changes:
            print(f"Version: {change['version']}")
            print(f"Date: {change['date']}")
            print(f"Description: {change['description']}\n")


if __name__ == "__main__":
    changelog = ChangeLog()
    changelog.add_change("1.0.0", "2023-01-10", "Initial release of the pizza ordering chatbot.")
    changelog.add_change("1.1.0", "2023-02-15", "Added support for multiple pizza sizes.")
    changelog.add_change("1.2.0", "2023-03-01", "Implemented user authentication for order history.")
    changelog.add_change("1.3.0", "2023-03-20", "Improved natural language understanding for better order processing.")
    changelog.add_change("1.4.0", "2023-04-10", "Added payment integration and order confirmation feature.")
    changelog.display_changes()
