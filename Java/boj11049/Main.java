package boj11049;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int N;
    static int[] x = new int[500];
    static int[] y = new int[500];

    static int[][] dp = new int[501][501];

    static int multi(int n, int m, int k){
        return n*m*k;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());


        String[] s;
        for (int i = 0; i < N; i++) {
            s = br.readLine().split(" ");
            x[i] = Integer.parseInt(s[0]);
            y[i] = Integer.parseInt(s[1]);
        }

        for (int i = 0; i < N - 1; i++) {
            dp[i][i+1] = x[i]*x[i+1]*y[i+1];
        }


        int t;
        // diff = i;   dp[x][x+i] ==> x에서 x+i 까지의 구간에서의 min
        for (int i = 2; i < N; i++) {
            // start = j;  dp[j][j+i]를 구해주는 것이 목표
            for (int j = 0; i+j < N; j++) {
                dp[j][j+i] = 0x7fffffff;
                for (int k = 0; k < i; k++) {
                    t = dp[j][j+k] + dp[j+k+1][j+i] + x[j]*y[j+k]*y[j+i];
                    if (dp[j][j+i] > t)
                        dp[j][j+i] = t;
                }
            }
        }
        System.out.println(dp[0][N-1]);
    }
}
