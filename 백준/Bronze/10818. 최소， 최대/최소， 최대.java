import java.util.Scanner;


public class Main {		

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // 수열 갯수
		int[] a = new int[n];		

		for(int i= 0; i < n; i++) {
			a[i] = sc.nextInt();
		}

		int min = a[0];
		int max = a[0];
			
		
		for(int i= 0; i < n; i++) {			
			if(min > a[i]) {
				min = a[i];
			}
		}

		for(int i= 0; i < n; i++) {			
			if(max < a[i]) {
				max = a[i];
			}
		}
		
		System.out.println(min + " " + max);
			
	}
		
}
