package boj11401;

import java.util.Scanner;

public class Main {

    static int mul[];
    static int div[];


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();

        if (2*K > N){
            K = N-K;
        }

        mul = new int[K];
        div = new int[K];

        for (int i = 0; i < N+1; i++) {
            mul[i] = N-i;
        }

        for (int i = 0; i < K+1; i++){
            div[i] = K-i;
        }



    }
}
