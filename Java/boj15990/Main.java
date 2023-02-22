package boj15990;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int[][] arr = new int[3][100001];

    public static void main(String[] args) throws IOException {

        arr[0][1] = 1;
        arr[0][2] = 0;
        arr[0][3] = 1;

        arr[1][2] = 1;
        arr[1][3] = 1;

        arr[2][3] = 1;

        for (int i = 4; i < 100001; i++) {
            arr[0][i] = (arr[1][i-1] + arr[2][i-1]) % 1000000009;
            arr[1][i] = (arr[0][i-2] + arr[2][i-2]) % 1000000009;
            arr[2][i] = (arr[0][i-3] + arr[1][i-3]) % 1000000009;
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n, k, t;
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            k = Integer.parseInt(br.readLine());
            t = (arr[0][k] + arr[1][k]) % 1000000009;
            t = (t + arr[2][k]) % 1000000009;
            sb.append(t).append("\n");
        }

        System.out.print(sb.toString());
    }
}
