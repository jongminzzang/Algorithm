package boj11728;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n, m;
    static int[] l1, l2;
    static String[] s;

    public static void main(String[] args) throws IOException {
        long beforeTime = System.currentTimeMillis();

        System.setIn(new FileInputStream("test.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        m = Integer.parseInt(s[1]);

        l1 = new int[n];
        l2 = new int[m];


        s = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            l1[i] = Integer.parseInt(s[i]);
        }
        s = br.readLine().split(" ");
        for (int i = 0; i < m; i++) {
            l2[i] = Integer.parseInt(s[i]);
        }

        StringBuilder sb = new StringBuilder();
        int k1 = 0;
        int k2 = 0;

        while (true){
            if (k1 == n){
                while (k2 < m){
                    sb.append(l2[k2]).append(" ");
                    k2 += 1;
                }
                break;
            } else if (k2 == m) {
                while (k1 < n){
                    sb.append(l1[k1]).append(" ");
                    k1 += 1;
                }
                break;
            }
            else{
                if (l1[k1] < l2[k2]){
                    sb.append(l1[k1]).append(" ");
                    k1 += 1;
                }
                else{
                    sb.append(l2[k2]).append(" ");
                    k2 += 1;
                }
            }
        }
        // System.out.println(sb.toString());
        long afterTime = System.currentTimeMillis();
        long secDiffTime = (afterTime - beforeTime); //두 시간에 차 계산
        System.out.println("시간차이(m) : "+secDiffTime);
    }
    
}
