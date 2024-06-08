import datetime

def display_entries(entries):
    if not entries:
        print("No entries in the diary.")
    else:
        for entry in entries:
            print(f"Date: {entry['date']}")
            print(f"Title: {entry['title']}")
            print(f"Content: {entry['content']}\n")

def add_entry(entries):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = input("Enter the title of your entry: ")
    content = input("Write your entry: ")
    entries.append({"date": date, "title": title, "content": content})
    print("Entry added.")

def search_entries(entries):
    search_term = input("Enter a keyword to search: ").lower()
    found_entries = [entry for entry in entries if search_term in entry['title'].lower() or search_term in entry['content'].lower()]
    if not found_entries:
        print("No entries found matching your search term.")
    else:
        display_entries(found_entries)

def diary_app():
    entries = []
    while True:
        print("\nDiary Options:")
        print("1. View all entries")
        print("2. Add a new entry")
        print("3. Search entries")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_entries(entries)
        elif choice == '2':
            add_entry(entries)
        elif choice == '3':
            search_entries(entries)
        elif choice == '4':
            print("Exiting the diary application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

diary_app()

