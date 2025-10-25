def main():
    print("Count up 0 to 50:")
    for i in range(0, 51):
        print(i)

    print("\nCount down 50 to 0:")
    for i in range(50, -1, -1):
        print(i)

    print("\nCount up 30 to 50:")
    for i in range(30, 51):
        print(i)

    print("\nCount down 50 to 10 by 2:")
    for i in range(50, 9, -2):
        print(i)

    print("\nCount up 100 to 200 by 5:")
    for i in range(100, 201, 5):
        print(i)

if __name__ == "__main__":
    main()
