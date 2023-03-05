package boj13144;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    static String[] s;
    static int[] arr = new int[100001];
    static int size = 0;
    static long ans = 0;
    static int N = 0;


    public static void main(String[] args) throws IOException {
        Arrays.fill(arr, -1);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        s = br.readLine().split(" ");

        int k, t;
        for (int i = 0; i < N; i++) {

            k = Integer.parseInt(s[i]);

            // 처음 나온 수
            if (arr[k] == -1){
                arr[k] = i;
                size += 1;
            }

            // 이전에 나왔던 수
            else{
                t = i - arr[k];
                arr[k] = i;
                if (t <= size){
                    size = t;
                }
                else{
                    size += 1;
                }
            }
            ans += size;
        }
        System.out.println(ans);
    }
}