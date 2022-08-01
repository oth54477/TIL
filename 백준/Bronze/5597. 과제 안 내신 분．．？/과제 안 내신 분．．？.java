import java.util.Scanner;
import java.util.Arrays;

public class Main{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int arr[] = new int[28];
        
        for (int i=0; i<28; i++) {
            arr[i] = in.nextInt();
        }
        in.close();
        
        Arrays.sort(arr);
        int k = 1;
        for (int j=0; j<28; j++) {
			if (arr[j] != k) {
                System.out.println(k);
                j--;
            }
            

            k++;
            
        }
        if (k == 29) {
            System.out.println(29);
            System.out.println(30);
        } else if ( k == 30) {
            System.out.println(30);
        }
    }
}