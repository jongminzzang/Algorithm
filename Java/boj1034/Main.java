package boj1034;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class Main {


    static String map[][];
    static String smap[];
    static int answer = 0;



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s[] = br.readLine().split(" ");
        int N = Integer.parseInt(s[0]);
        int M = Integer.parseInt(s[1]);

        smap  = new String[N];
        map = new String[N][];

        String t;
        for (int i = 0; i < N; i++) {
            t = br.readLine();
            smap[i] = t;
            map[i] = t.split("");
        }

        int K = Integer.parseInt(br.readLine());

        int zero = 0;
        int same = 0;

        for (int i = 0; i < N; i++) {
            zero = 0;
            same = 0;
            for (int j = 0; j < M; j++) {
                if (map[i][j].equals("0")){
                    zero += 1;
                }
            }
            if (zero <= K && zero%2==K%2){
                same = 1;
                for (int j = i + 1; j < N; j++) {
                    if (smap[i].equals(smap[j])) same += 1;
                }
                answer = Integer.max(answer, same);
            }
        }

        System.out.println(answer);
    }

}
