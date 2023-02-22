package boj7517;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static int M;
    private static int N;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        M  = Integer.parseInt(s[0]);
        N = Integer.parseInt(s[1]);

        int x = 0;
        int y = 0;
        int[] xArr = new int[N];
        int[] yArr = new int[N];


        for (int i = 0; i < N; i++) {
            s = br.readLine().split(" ");
            xArr[i] = Integer.parseInt(s[0]);
            yArr[i] = Integer.parseInt(s[1]);

            x += xArr[i];
            y += yArr[i];
        }
        System.out.println(x + " " + y);
        int xAvg = (int) (((double) x/N) + 0.5);
        int yAvg = (int) (((double) y/N) + 0.5);
        xAvg = 5;
        yAvg = 5;
        long answer = 0;
        int xt = 0;
        int yt = 0;
        System.out.println(xAvg + " " + yAvg);
        for (int i = 0; i < N; i++) {
            xt = xArr[i] - xAvg;
            yt = yArr[i] - yAvg;
            System.out.println(xt + " " + yt);
            if (xt < 0) {
                answer -= xt;
            }
            else{
                answer += xt;
            }
            if (yt < 0){
                answer -= yt;
            }
            else {
                answer += yt;
            }
        }
        System.out.println(answer);
    }
}
