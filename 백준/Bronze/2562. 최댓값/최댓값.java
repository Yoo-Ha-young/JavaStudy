import java.util.Scanner;


public class Main {		

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);

		
		int[] array = new int[9];
		
		for(int i= 0; i < array.length; i++) {
			array[i] = sc.nextInt();
		}
			
		int maxNum = 0;
		int position = 0;

		for(int i= 0; i < array.length; i++) {			

			if(maxNum < array[i]) {
				maxNum = array[i];
				position = i+1;
			}
		}
	
		System.out.println(maxNum);
		System.out.println(position);

	}
		
}
