package boj16139;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int[][] m = new int[26][200001];
    static int N;
    static String[] strings;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String s = br.readLine();

        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < 26; j++) {
                m[j][i+1] = m[j][i];
            }
            m[s.charAt(i)-'a'][i+1] += 1;
        }


        char t;
        int x, y;
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            strings = br.readLine().split(" ");
            t = (char) (strings[0].charAt(0)-'a');
            x = Integer.parseInt(strings[1]);
            y = Integer.parseInt(strings[2]);

            sb.append(m[t][y+1] - m[t][x]).append("\n");
        }
        System.out.println(sb.toString());
    }
}
