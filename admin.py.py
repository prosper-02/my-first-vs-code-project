import json

DATA_FILE = "data.txt"


def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)


def add_item(category, item):
    data = load_data()
    if category not in data:
        data[category] = []
    data[category].append(item)
    save_data(data)
    print(f"Added '{item}' to '{category}'.")


def list_items(category):
    data = load_data()
    if category in data:
        items = data[category]
        print(f"Items in '{category}':")
        for item in items:
            print(f"- {item}")
    else:
        print(f"No items found in '{category}'.")


def search_item(item):
    data = load_data()
    found = False
    for category, items in data.items():
        if item in items:
            found = True
            print(f"Found '{item}' in '{category}'.")
    if not found:
        print(f"No results found for '{item}'.")


def view_category(category):
    data = load_data()
    if category in data:
        items = data[category]
        print(f"Items in '{category}':")
        for item in items:
            print(f"- {item}")
    else:
        print(f"No items found in '{category}'.")


def delete_item(category, item):
    data = load_data()
    if category in data:
        items = data[category]
        if item in items:
            items.remove(item)
            save_data(data)
            print(f"Deleted '{item}' from '{category}'.")
            return
    print(f"Item '{item}' not found in '{category}'.")


def main():
    while True:
        print("Welcome to the Admin CLI Program!")
        print("1. Add item")
        print("2. List items")
        print("3. Search item")
        print("4. View category")
        print("5. Delete item")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter the category: ")
            item = input("Enter the item: ")
            add_item(category, item)
        elif choice == "2":
            category = input("Enter the category: ")
            list_items(category)
        elif choice == "3":
            item = input("Enter the item to search for: ")
            search_item(item)
        elif choice == "4":
            category = input("Enter the category to view: ")
            view_category(category)
        elif choice == "5":
            category = input("Enter the category: ")
            item = input("Enter the item to delete: ")
            delete_item(category, item)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()