package boj1103;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    static int N, M;
    static char map[][];
    static int int_map[][];
    static int dx[] = {0, 1, 0, -1};
    static int dy[] = {1, 0, -1, 0};

    static class Pos{
        char x;
        char y;
        int depth;

        public Pos(char x, char y, int depth){
            this.x = x;
            this.y = y;
            this.depth = depth;
        }
    }
    static Deque<Pos> d;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s[] = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);
        map = new char[N][];
        int_map = new int[N][M];

        for (int i = 0; i < N; i++) {
            map[i] = br.readLine().toCharArray();
        }

        d = new ArrayDeque<Pos>();
        d.add(new Pos((char) 0,(char) 0, 1 ));

        Pos t;
        char k;
        char tx, ty;
        int ttx, tty;
        int answer = 0;
        while (!d.isEmpty()){
            t = d.pollFirst();
            if (t.depth > answer){
                answer = t.depth;
            }
            if (t.depth > N*M){
                answer = -1;
                break;
            }
            k = (char)(map[t.x][t.y] - '0');
            tx = t.x;
            ty = t.y;
            for (int i = 0; i < 4; i++) {

                ttx = tx + dx[i]*k;
                tty = ty + dy[i]*k;
                // System.out.println("ttx : " + (int)ttx + " tty : " + (int)tty);

                if (ttx >= 0 && ttx < N && tty >= 0 && tty < M){
                    if (map[ttx][tty] != 'H'){
                        if (int_map[ttx][tty] < t.depth) {
                            int_map[ttx][tty] = t.depth;
                            d.add(new Pos((char) ttx, (char) tty, t.depth + 1));
                        }
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
