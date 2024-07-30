import java.util.Scanner;
import java.util.Random;

public class j {
    public static void main(String[] args) {

        int user, count = 1;
        
        Random rand = new Random();
        int number = rand.nextInt(100) + 1;
        System.out.println(number);

        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter Number : ");
        user = sc.nextInt();
        
        do {
            if (user < number) {
                System.out.println("Enter A Higher Value :");
                user = sc.nextInt();
                count += 1;
            } else if (user > number) {
                System.out.println("Enter A Lower Value :");
                user = sc.nextInt();
                count += 1;
            }
        } while (user != number);

        System.out.println("You Won With " + count + " Times");

        sc.close();
    }
}