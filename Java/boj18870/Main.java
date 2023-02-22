package boj18870;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main {

    static int N;
    static String s[];
    static Set<Integer> set = new HashSet();
    static int valarr[];

    public static void main(String[] args) throws IOException {
        StringBuffer sb = new StringBuffer();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        s = br.readLine().split(" ");

        valarr = new int[N];
        int t;
        for (int i = 0; i < N; i++) {

            t = Integer.parseInt(s[i]);
            valarr[i] = t;
            if (!set.contains(t)){
                set.add(t);
            }
        }

        Integer[] arr = set.toArray(new Integer[0]);
        Arrays.sort(arr);

        int idx;
        for (int i = 0; i < N; i++) {
            idx = Arrays.binarySearch(arr, valarr[i]);
            sb.append(idx).append(" ");
        }
        System.out.println(sb.toString());
    }
}


