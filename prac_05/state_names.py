CODE_TO_NAME = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania"}
print(CODE_TO_NAME)

short_state = input("Enter short state: ").upper()
while short_state != "":
    if short_state in CODE_TO_NAME:
        print(short_state, "is", CODE_TO_NAME[short_state])
    else:
        print("Invalid short state")
    short_state = input("Enter short state: ").upper()