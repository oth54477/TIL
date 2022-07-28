import java.util.Scanner;

public class Main {
    
   public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    long A = in.nextLong();
    long B = in.nextLong();

    System.out.println(Math.abs(A-B));

    in.close();
   } 
}
