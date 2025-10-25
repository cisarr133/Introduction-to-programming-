names = ["Cesar", "Jyace", "Riane", "Wil", "Smith", "Angkol"]

def main():
    search = input("Enter name to search (press Enter to search for 'Angkol'): ").strip()
    if not search:
        search = "Angkol"

    
    for idx, name in enumerate(names):
        if name.lower() == search.lower():
            print(f"{search} found at index {idx}.")
            break
    else:
        print(f"{search} not found in the list.")

if __name__ == "__main__":
    main()