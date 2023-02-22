package boj6588;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;

public class Main {

    static int n;

    static boolean[] arr = new boolean[1000001];

    static int count = 0;
    static int[] prime = new int[1000001];


    public static void main(String[] args) throws IOException {

        int k;
        for (int i = 3; i < 1000001; i++) {
            if (arr[i] == true){
                ;
            }
            else{
                prime[count] = i;
                count += 1;
                k = 2;
                while (i*k < 1000000){
                    arr[i*k] = true;
                    k ++;
                }
            }
        }


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();


        while (true){
            n = Integer.parseInt(br.readLine());
            if (n == 0){
                break;
            }

            for (int i = 0; i < count; i++) {
                if (!arr[n-prime[i]]){
                    sb.append(n).append(" = ").append(prime[i]).append(" + ").append(n-prime[i]).append("\n");
                    break;
                }
            }
        }

        System.out.print(sb.toString());

    }
}
