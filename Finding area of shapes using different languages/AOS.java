import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);
    String shape;
    
    System.out.println("Enter shape(circle,rectangle,triangle):"); 
    shape = myObj.nextLine();   
  
    switch(shape){
        case "circle":
            System.out.println("Enter the radius: ");
            double radius = myObj.nextDouble();
            double area = 3.1416 * radius * radius;
            System.out.println("The area of the circle is " + area);
            break;
        case "rectangle":
            System.out.println("Enter the length: ");
            double length = myObj.nextDouble();
            System.out.println("Enter the width: ");
            double width = myObj.nextDouble();
            double area2 = length * width;
            System.out.println("The area of the rectangle is " + area2);
            break;
        case "triangle":
            System.out.println("Enter the base: ");
            double base = myObj.nextDouble();
            System.out.println("Enter the height: ");
            double height = myObj.nextDouble();
            double area3 = 0.5 * base * height;
            System.out.println("The area of the triangle is " + area3);
            break;
    }
  }
}