from math import e


class DataManager:
    def __init__(self):
        self.data = {}

    def save_new_entry(self):
        try:
            # Get and validate ID
            while True:
                try:
                    id_input = input("Enter ID: ").strip()
                    if not id_input:
                        print("ID cannot be empty. Please try again.")
                        continue

                    if str(id_input) in self.data:
                        overwrite = input(
                            f"ID {id_input} already exists, Overwrite it? (y/n): "
                        ).lower()
                        if overwrite != "y":
                            print("Entry cancelled.")
                            return
                    break
                except ValueError as e:
                    print(f"Invalid ID: {e}. Please try again.")

            # Get and validate name
            while True:
                try:
                    name_input = input("Enter Name: ").strip()
                    if not name_input:
                        print("Name cannot be empty. Please try again.")
                        continue
                    break
                except ValueError as e:
                    print(f"Invalid name: {e}. Please try again.")

            # Get and validate age
            while True:
                try:
                    age_input = input("Enter Age: ").strip()
                    if not age_input:
                        print("Age cannot be empty. Please try again.")
                        continue
                    age = int(age_input)
                    if age > 150 or age < 0:
                        print("Age must be between 0 and 150. Please try again.")
                        continue
                    break
                except ValueError as e:
                    print(f"Invalid age: {e}. Please try again.")

            # Save entry
            self.data[str(id_input)] = {"name": name_input, "age": age}

            print(f"\n ID [{id_input}] saved successfully")

        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def search_by_id(self):
        try:
            id_input = input("Please enter the ID you want to look for: ").strip()
            if not id_input:
                print("ID cannot be empty.")
                return

            if not id_input.isnumeric() or int(id_input) <= 0:
                print("ID must be a positive integer.")
                return

            if str(id_input) in self.data.keys():
                entry = self.data[str(id_input)]
                print(f"\n Entry found:")
                print(f"ID: {id_input}")
                print(f"Name: {entry['name']}")
                print(f"Age: {entry['age']}")
            else:
                print(f" No entry found with ID: {id_input}")

        except ValueError as e:
            print(f"Invalid ID: {e}")
        except Exception as e:
            print(f"Error during search: {e}")

    def print_ages_average(self):
        if not self.data:
            print("No entries found. Database is empty.")
            return

        ages = [entry["age"] for entry in self.data.values()]
        avg_age = sum(ages) / len(ages)
        print(f"Average age: {avg_age}")

    def print_all_names(self):
        if not self.data:
            print("No entries found. Database is empty.")
            return

        # names = [entry["name"] for entry in self.data.items()]
        names = [entry["name"] for entry in self.data.values()]

        for i, name in enumerate(names):
            print(f"{i}. {name}")

    def print_all_ids(self):
        if not self.data:
            print("No entries found. Database is empty.")
            return

        ids = [entry_id for entry_id in self.data.keys()]
        for i, entry_id in enumerate(ids, 1):
            entry = self.data[str(entry_id)]
            print(f"{i}. ID: {entry_id}")

    def print_all_entries(self):
        if not self.data:
            print("No entries found. Database is empty.")
            return

        for index, (entry_id, entry) in enumerate(self.data.items()):
            print(f"{index}. ID: {entry_id}")
            print(f"   Name: {entry['name']}")
            print(f"   Age: {entry['age']}")

    def print_entry_by_index(self):
        if not self.data:
            print("No entries found. Database is empty.")
            return

        try:
            index_input = input("Enter index number: ").strip()
            if not index_input:
                print("Index cannot be empty.")
                return

            index = int(index_input)
            if index < 0 or index >= len(self.data):
                print(f"Index must be between 0 and {len(self.data) - 1}.")
                return
            entry_id, entry = list(self.data.items())[index]
            print(f"ID: {entry_id}")
            print(f"Name: {entry['name']}")
            print(f"Age: {entry['age']}")

        except ValueError:
            print("Index must be a valid number.")
        except Exception as e:
            print(f"Error: {e}")

    def display_menu(self):
        print("1.  Save a new entry")
        print("2.  Search by ID")
        print("3.  Print ages average")
        print("4.  Print all names")
        print("5.  Print all IDs")
        print("6.  Print all entries")
        print("7.  Print entry by index")
        print("8. Exit")
        print("Please enter your choice: ", end="")

    def run(self):
        while True:
            try:
                self.display_menu()
                choice = input().strip()

                if choice == "1":
                    self.save_new_entry()
                elif choice == "2":
                    self.search_by_id()
                elif choice == "3":
                    self.print_ages_average()
                elif choice == "4":
                    self.print_all_names()
                elif choice == "5":
                    self.print_all_ids()
                elif choice == "6":
                    self.print_all_entries()
                elif choice == "7":
                    self.print_entry_by_index()
                elif choice == "8":
                    break
                else:
                    print(f" Invalid choice: '{choice}'. Please select 1-8.")

                # Pause before showing menu again (except for exit)
                if choice != "8":
                    input("\nPress Enter to continue...")

            except KeyboardInterrupt:
                print("\n\n  Program interrupted by user.")
                print(" Goodbye!")
                break
            except Exception as e:
                print(f" Unexpected error: {e}")
                print("The program will continue...")


def main():
    manager = DataManager()
    manager.run()


if __name__ == "__main__":
    main()
