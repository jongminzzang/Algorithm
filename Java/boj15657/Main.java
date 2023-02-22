package boj15657;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    static int[] arr;
    static List<Integer> answer = new ArrayList<>();
    static int N, M;
    static StringBuilder sb = new StringBuilder();
    static void func(int nowIdx, int depth){
        if (depth == M){
            for (int x : answer){
                sb.append(x).append(' ');
            }
            sb.append('\n');
        }


        else{
            for (int i = nowIdx; i < N; i++) {
                answer.add(arr[i]);
                func(i, depth+1);
                answer.remove(answer.size()-1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s[] = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);

        s = br.readLine().split(" ");
        arr = new int[s.length];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(s[i]);
        }

        Arrays.sort(arr);

        func(0, 0);
        System.out.print(sb);
    }
}
