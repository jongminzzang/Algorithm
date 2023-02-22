package boj10830;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int[][] multiple(int[][] a, int[][] b, int N){
        int[][] ret = new int[N][N];
        int t;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                t = 0;
                for (int k = 0; k < N; k++) {
                    t += a[i][k] * b[k][j];
                }
                if (t >= 1000){
                    t = t%1000;
                }
                ret[i][j] = t;
            }
        }

        return ret;
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s[] = br.readLine().split(" ");
        int N = Integer.parseInt(s[0]);
        Long B = Long.parseLong(s[1]);

        String b = Long.toBinaryString(B);

        int arr[][][] = new int[b.length()][N][N];

        for (int i = 0; i < N; i++) {
            s = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                arr[0][i][j] = Integer.parseInt(s[j])%1000;
            }
        }

        for (int i = 1; i < b.length(); i++){
            arr[i] = multiple(arr[i-1], arr[i-1], N);
        }



        int answer_arr[][] = arr[b.length()-1];

        for (int i = 1; i < b.length(); i++) {
            if (b.charAt(i) == '1'){
                //System.out.println(i);
                answer_arr = multiple(answer_arr, arr[b.length()-1-i], N);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(answer_arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
