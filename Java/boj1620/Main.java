package boj1620;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s[] = br.readLine().split(" ");

        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);

        String[] arr = new String[n+1];
        Map<String, Integer> map = new HashMap<>();


        String t;
        for (int i = 1; i < n+1; i++) {
            t = br.readLine();
            arr[i] = t;
            map.put(t, i);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            t = br.readLine();
            if (t.charAt(0) < 'A'){
                sb.append(arr[Integer.parseInt(t)]).append("\n");
            }
            else {
                sb.append(map.get(t)).append("\n");
            }
        }

        System.out.print(sb.toString());
    }
}
