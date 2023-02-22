package boj7576;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;


public class Main {

    static class Pos{
        public int x;
        public int y;

        Pos(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    static int N, M;
    static String[] s;
    static int[][] m;

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    static boolean check(int tx, int ty){
        if (tx > -1 && ty > -1 && tx < N && ty <M && m[tx][ty] == 0) return true;
        else return false;
    }

    static LinkedList<Pos> posList = new LinkedList<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = br.readLine().split(" ");

        M = Integer.parseInt(s[0]);
        N = Integer.parseInt(s[1]);

        m = new int[N][M];
        int numTomato = N*M;

        for (int i = 0; i < N; i++) {
            s = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                m[i][j] = Integer.parseInt(s[j]);
                if (m[i][j] == -1){
                    numTomato -= 1;
                }
                else if (m[i][j] == 1){
                    numTomato -= 1;
                    posList.add(new Pos(i, j));
                }
            }
        }

        Pos t;
        int tx, ty;
        int answer = 1;
        while (!posList.isEmpty()){
            t = posList.poll();
            for (int i = 0; i < 4; i++) {
                tx = t.x + dx[i];
                ty = t.y + dy[i];

                if (check(tx,ty)){
                    numTomato -= 1;
                    m[tx][ty] = m[t.x][t.y] + 1;
                    if (m[tx][ty] > answer){
                        answer = m[tx][ty];
                    }
                    posList.add(new Pos(tx, ty));
                }
            }

            if (numTomato == 0){
                break;
            }
        }

        if (numTomato == 0){
            System.out.println(answer-1);
        }
        else{
            System.out.println(-1);
        }

    }
}
