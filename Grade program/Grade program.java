import java.io .*;
import java.util.Scanner;

class GFG {
    public static void main(String[] args)
    {
        while (true){
            Scanner num = new Scanner(System.in);
            System. out.println("1. Convert marks.");
            System.out.println("2. Exit.");
            System. out.print("Choose option(1 or 2): ");
            int input = num.nextInt();
            if (input == 1){
                System. out.print("Enter marks: ");
                int marks = num.nextInt();
                if (marks >= 90 && marks <= 100) {
                    System. out. println("The grade for " + marks + " is A.");
                    System.out.println("");
                }
                else if (marks >= 87 && marks <= 89){
                    System. out. println("The grade for " + marks + " is A -. ");
                    System.out.println("");
                }
                else if (marks >= 84 && marks <= 86){
                    System. out. println("The grade for " + marks + " is B+.");
                    System.out.println("");
                }
                else if (marks >= 80 && marks <= 83){
                    System. out. println("The grade for " + marks + " is B.");
                    System.out.println("");
                }
                else if (marks >= 77 && marks <= 79){
                    System. out. println("The grade for " + marks + " is B -. ");
                    System.out.println("");
                }
                else if (marks >= 74 && marks <= 76){
                    System. out. println("The grade for " + marks + " is C+.");
                    System.out.println("");
                }
                else if (marks >= 70 && marks <= 73){
                    System. out. println("The grade for " + marks + " is C.");
                    System.out.println("");
                }
                else if (marks >= 67 && marks <= 69){
                    System. out. println("The grade for " + marks + " is C -. ");
                    System.out.println("");
                }
                else if (marks >= 64 && marks <= 66){
                    System. out. println("The grade for " + marks + " is D+.");
                    System.out.println("");
                }
                else if (marks >= 62 && marks <= 63){
                    System. out. println("The grade for " + marks + " is D.");
                    System.out.println("");
                }
                else if (marks >= 60 && marks <= 61){
                    System. out. println("The grade for " + marks + " is D -. ");
                    System.out.println("");
                }
                else if (marks >= 0 && marks <= 59){
                    System. out. println("The grade for " + marks + " is F.");
                    System.out.println("");
                }
                else{
                    System.out.println("Invalid input!");
                    System.out.println("");
                }

            else if (input == 2){
                System. out.println("Goodbye!");
                break;
            }
            else{
                System.out.println("Invalid input.");
                System.out.println("");  }
            }
        }
    }
}