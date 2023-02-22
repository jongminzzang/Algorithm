package boj27468;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();


        int q = n / 4;
        int r = n % 4;

        int t;
        if (r == 3){
            for (int i = 0; i < q; i++) {
                t = i*4;
                sb.append((t+1) + " " + (t+3) + " " + (t+2) + " " + (t+4) + " ");
            }
            sb.append((n-2) + " " + n + " " + (n-1));
        }
        else{
            for (int i = 0; i < q; i++) {
                t = i*4;
                sb.append(t+1 + " " + (t+2) + " " + (t+4) + " " + (t+3) + " ");
            }
            if (r == 1){
                sb.append(n);
            } else if (r == 2) {
                sb.append((n-1) + " "+ n);
            }
        }
        System.out.println("YES");
        System.out.println(sb.toString());
    }
}
