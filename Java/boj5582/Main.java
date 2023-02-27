package boj5582;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static char[] str1;
    static char[] str2;
    static int[][] m;
    static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        str1 = br.readLine().toCharArray();
        str2 = br.readLine().toCharArray();

        m = new int[str1.length][str2.length];



        for (int i = 0; i < str1.length; i++) {
            for (int j = 0; j < str2.length; j++) {

                if (str1[i] == str2[j]){

                    if (i==0 || j==0){
                       m[i][j] = 1;
                   }
                   else {
                       m[i][j] = m[i - 1][j - 1] + 1;
                   }

                   // 정답 갱신
                   if (m[i][j] > ans){
                       ans = m[i][j];
                   }
                }
            }
        }
        System.out.println(ans);
    }
}
