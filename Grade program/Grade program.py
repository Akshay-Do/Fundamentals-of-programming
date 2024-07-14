while True:
    print("1. Convert marks.")
    print("2. Exit.")
    uinput = int(input("Choose option (1 or 2): "))
    if uinput == 1:
        marks = int(input("Enter marks: "))
        if marks > 100 and marks < 0:
            print("Invalid marks")
            print("")
        elif marks >= 90 and marks <= 100:
            print(f"The grade for {marks} is A.")
            print("")
        elif marks >= 87 and marks <= 89:
            print(f"The grade for {marks} is A -. ")
            print("")
        elif marks >= 84 and marks <= 86:
            print(f"The grade for {marks} is B+.")
            print("")
        elif marks >= 80 and marks <= 83:
            print(f"The grade for {marks} is B.")
            print("")
        elif marks >= 77 and marks <= 79:
            print(f"The grade for {marks} is B -. ")
            print("")
        elif marks >= 74 and marks <= 76:
            print(f"The grade for {marks} is C+.")
            print("")
        elif marks >= 70 and marks <= 73:
            print(f"The grade for {marks} is C.")
            print("")
        elif marks >= 67 and marks <= 69:
            print(f"The grade for {marks} is C -. ")
            print("")
        elif marks >= 64 and marks <= 66:
            print(f"The grade for {marks} is D+.")
            print("")
        elif marks >= 62 and marks <= 63:
            print(f"The grade for {marks} is D.")
            print("")
        elif marks >= 60 and marks <= 61:
            print(f"The grade for {marks} is D -. ")
            print("")
        elif marks >= 0 and marks <= 59:
            print(f"The grade for {marks} is F.")
            print("")

    elif uinput == 2:
        print("Goodbye!")
        break
