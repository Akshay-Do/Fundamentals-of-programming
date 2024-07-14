import area
while True:
    print("1. Calculate area of circle")
    print("2. Calculate area of rectangle")
    print("3. Calculate area of triangle")
    print("4. Exit")
    choice = int(input("Enter your choice(1-4): "))

    if choice == 1:
        radius = int(input("Enter the radius: "))
        circle_area = area.calculate_circle_area(radius)
        print("Area of cricle with radius", radius, "is:", circle_area)
        print("")

    elif choice == 2:
        length = int(input("Enter the length: "))
        width = int(input("Enter the width: "))
        rectangle_area = area.calculate_rectangle_area(length,width)
        print("Area of rectangle with length", length,"and width", width, "is:", rectangle_area)
        print("")

    elif choice == 3:
        base = int(input("Enter the base: "))
        height = int(input("Enter the height: "))
        triangle_area = area.calculate_triangle_area(base,height)
        print("Area of triangle with base", base,"and height", height, "is:", triangle_area)
        print("")

    elif choice >4 or choice < 1:
        print("Invalid choice")
        print("")

    elif choice == 4:
        print("Goodbye!")
        break
    
