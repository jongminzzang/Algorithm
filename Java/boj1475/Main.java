package boj1475;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int[] arr = new int[10];

        int t;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '6' || s.charAt(i) == '9'){
                if (arr[6]==arr[9]){
                    arr[6] += 1;
                }
                else{
                    arr[9] += 1;
                }
            }
            else{
                arr[(int) (s.charAt(i)-'0')] += 1;
            }
        }
        System.out.println(Arrays.stream(arr).max().getAsInt());
    }
}
