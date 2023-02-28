package boj9251;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static char[] str1;
    static char[] str2;

    static int ans;

    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str1 = (" " + br.readLine()).toCharArray();
        str2 = (" " + br.readLine()).toCharArray();

        dp = new int[str1.length][str2.length];

        for (int i = 1; i < str1.length; i++) {
            for (int j = 1; j < str2.length; j++) {

                // 비교하는 마지막 char가  같은 경우
                if (str1[i] == str2[j]){
                    dp[i][j] = dp[i-1][j-1]+1;
                }
                // 비교하는 마지막 char가 다른 경우
                else{
                    if (dp[i-1][j] > dp[i][j-1]){
                        dp[i][j] = dp[i-1][j];
                    }else{
                        dp[i][j] = dp[i][j-1];
                    }
                }
            }
        }

        System.out.println(dp[str1.length-1][str2.length-1]);
    }
}

