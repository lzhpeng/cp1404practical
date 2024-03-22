def main():
    guitars = []

    print("My guitars!")

    while True:
        name = input("Name (leave blank to finish): ").strip()
        if not name:
            break

        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(guitars(name, year, cost))
        print(f"{name} added.")

    guitars.append(guitars("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(guitars("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars :( Quick, go and buy one!")


if __name__ == "__main__":
    main()
