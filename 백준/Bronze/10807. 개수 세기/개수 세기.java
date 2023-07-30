import java.util.Scanner;

public class Main {	
			
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

    	// 입력받을 숫자 갯수
	    int n = sc.nextInt();
    	// 찾으려고 하는 정수 v
        int[] array = new int[n];
		for(int i= 0; i < n; i++) {
			array[i] = sc.nextInt();
		}

	    int v = sc.nextInt();

        int cnt = 0; // 배열 
		
		for(int i= 0; i < n; i++) {
			if(v == array[i]) {
				cnt++;
			}
		}
        
		System.out.print(cnt);
	}

}
