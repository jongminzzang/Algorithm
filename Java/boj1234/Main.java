package boj1234;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int [][] arr = new int[4][4001];

        String[] sl;
        for (int i = 0; i < N; i++){
            sl = br.readLine().split(" ");
            for (int j = 0; j < 4; j++) {
                arr[j][i] = Integer.parseInt(sl[j]);
            }
        }

        // Map<Integer, Integer> m1 = new HashMap<>();
        Map<Integer, Integer> m2 = new TreeMap<>();
        Map<Integer, Integer> m1 = new TreeMap<>();

        for (int i = 0; i <N; i++) {
            for (int j = 0; j < N; j++) {

                if (m1.containsKey(arr[0][i] + arr[1][j])){
                    m1.put(arr[0][i] + arr[1][j], m1.get(arr[0][i] + arr[1][j])+1);
                }
                else {
                    m1.put(arr[0][i] + arr[1][j], 1);
                }

                if (m2.containsKey(arr[2][i] + arr[3][j])){
                    m2.put(arr[2][i] + arr[3][j], m2.get(arr[2][i] + arr[3][j])+1);
                }
                else {
                    m2.put(arr[2][i] + arr[3][j], 1);
                }

            }
        }

        int answer = 0;
        for (Integer x : m1.keySet()){
            answer += m1.get(x) * m2.getOrDefault(-x, 0);
        }
        System.out.println(answer);
    }
}
