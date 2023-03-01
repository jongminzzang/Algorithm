package boj1956;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static String[] s;

    static int V, E;
    static int a, b, c;

    static int[][] m;
    static int ans = 4000001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        s = br.readLine().split(" ");
        V = Integer.parseInt(s[0]);
        E = Integer.parseInt(s[1]);

        m = new int[V][V];

        // 초기 값 설정
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                m[i][j] = 4000001;
            }
        }

        // 값 대입
        for (int i = 0; i < E; i++) {
            s = br.readLine().split(" ");
            a = Integer.parseInt(s[0])-1;
            b = Integer.parseInt(s[1])-1;
            c = Integer.parseInt(s[2]);
            m[a][b] = c;
        }

        // 플로이드 알고리즘
        // i번 정점을 거친다고 가정
        for (int i = 0; i < V; i++) {
            // j번 정점에서 시작하는 값
            for (int j = 0; j < V; j++) {
                // k번 정점이 목적지
                for (int k = 0; k < V; k++) {
                    if (m[j][k] > m[j][i] + m[i][k]){
                        m[j][k] = m[j][i] + m[i][k];
                    }
                }
            }
        }


        // 정답 찾기
        for (int i = 0; i < V; i++) {
            if (m[i][i] < ans){
                ans = m[i][i];
            }
        }


        if (ans == 4000001){
            System.out.println(-1);
        }else {
            System.out.println(ans);
        }
    }

}
