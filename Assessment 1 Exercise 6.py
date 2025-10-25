def main():
    CORRECT_PASSWORD = "r1ane1s4vr6y"
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        pwd = input("Enter password: ").strip()
        if pwd == CORRECT_PASSWORD:
            print("Access granted. Correct password entered.")
            return
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts remaining.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")

if __name__ == "__main__":
    main()