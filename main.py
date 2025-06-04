# main.py
from navigator import FileNavigator

def main():
    nav = FileNavigator(".")

    while True:
        print(f"\n📁 Current Directory: {nav.current_path}")
        print("1. List Files")
        print("2. Change Directory")
        print("3. Go Back")
        print("4. Search File")
        print("5. Show Tree")
        print("6. Exit")
        
        choice = input("Choose: ")

        if choice == "1":
            items = nav.list_dir()
            for item in items:
                print(" -", item)
        elif choice == "2":
            folder = input("Enter folder name: ")
            nav.change_dir(folder)
        elif choice == "3":
            nav.go_back()
        elif choice == "4":
            query = input("Search query: ")
            results = nav.search(query)
            for r in results:
                print("🧭", r)
        elif choice == "5":
            nav.show_tree()
        elif choice == "6":
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
