package boj15486;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    static int N;
    static String[] s;

    static int answer = 0;
    static int maxBefore = 0;

    static int[] day;
    static int[] fee;

    static int[] dp;




    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        day = new int[N+1];
        fee = new int[N+1];
        dp = new int[N+1];


        for (int i = 0; i < N; i++) {
            s = br.readLine().split(" ");
            day[i] = Integer.parseInt(s[0]);
            fee[i] = Integer.parseInt(s[1]);
        }

        // day, fee, nextday;
        int d, f, nd;

        for (int i = 0; i < N; i++) {

            if (dp[i] > maxBefore){
                maxBefore = dp[i];
            }
            else{
                dp[i] = maxBefore;
            }

            d = day[i];
            nd = d + i;
            if (nd > N){
                continue;
            }
            if (dp[nd] < dp[i] + fee[i]){
                dp[nd] = dp[i] + fee[i];
                if (dp[nd] > answer) {
                    answer = dp[nd];
                }
            }
        }


        System.out.println(answer);
    }

}
