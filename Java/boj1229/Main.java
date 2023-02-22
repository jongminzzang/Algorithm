package boj1229;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int[] h = new int[1000];
    static int[] dp = new int[1000001];

    public static void main(String[] args) throws IOException {

        // N 입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N + 1; i++) {
            dp[i] = 7;
        }

        // 육각수 배열 h 채우기
        h[0] = 1;
        dp[1] = 1;
        for (int i = 1; i < 1000; i++) {
            h[i] = h[i - 1] + 4 * i + 1;
            if (h[i] > 1000000) break;
            dp[h[i]] = 1;
        }

        // dp 테이블 채우기
        for (int i = 0; i < N+1; i++) {

            for (int j = 0; j < 1000; j++) {
                if (i - h[j] < 1) {
                    break;
                } else {
                    dp[i] = Math.min(dp[i], dp[i - h[j]] + 1);
                }
            }
        }

        System.out.println(dp[N]);
    }
}
