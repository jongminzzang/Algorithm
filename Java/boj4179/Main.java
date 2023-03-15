package boj4179;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    static String s[];
    static int R, C;
    static char[][] m;

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    static boolean isEdge(int x, int y){
        if (x == 0 || y == 0 || x == R-1 || y == C-1) return true;
        else return false;
    }

    static boolean isIn(int x, int y){
        if (x >= 0 && y >= 0 && x < R && y < C) return true;
        else return false;
    }

    static class Node{
        boolean isFire;
        int x;
        int y;
        int time;


        public Node(boolean isFire, int x, int y, int time) {
            this.isFire = isFire;
            this.x = x;
            this.y = y;
            this.time = time;
        }

        @Override
        public String toString() {
            return "Node{" +
                    "isFire=" + isFire +
                    ", x=" + x +
                    ", y=" + y +
                    ", time=" + time +
                    '}';
        }
    }


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        s = br.readLine().split(" ");
        R = Integer.parseInt(s[0]);
        C = Integer.parseInt(s[1]);

        m = new char[R][];

        for (int i = 0; i < R; i++) {
            m[i] = br.readLine().toCharArray();
        }
        Queue<Node> queue = new LinkedList<>();
        int sx = -1;
        int sy = -1;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (m[i][j] == 'F'){
                    queue.add(new Node(true, i, j, 0));
                }
                if (m[i][j] == 'J'){
                    sx = i;
                    sy = j;
                }
            }
        }
        queue.add(new Node(false, sx, sy, 0));

        Node t = null;
        int tx, ty;
        boolean ans = false;
        while (!queue.isEmpty()){

            t = queue.poll();
            // System.out.println(t);
            tx = t.x;
            ty = t.y;
            if (t.isFire){
                for (int i = 0; i < 4; i++) {
                    if (isIn(tx+dx[i], ty+dy[i]) && m[tx+dx[i]][ty+dy[i]]=='.'){
                        m[tx+dx[i]][ty+dy[i]] = 'F';
                        queue.add(new Node(true, tx+dx[i], ty+dy[i], t.time+1));

                    }
                }
            }
            else {
                // 가장 자리인지 검사해서 맞다면 답 return
                if (isEdge(t.x, t.y)) {
                    ans = true;
                    break;
                }

                // 아니면 옆으로 이동하는데 불이면 안됨
                else {
                    for (int i = 0; i < 4; i++) {
                        if (isIn(tx+dx[i], ty+dy[i]) && m[tx+dx[i]][ty+dy[i]]=='.') {
                            m[tx+dx[i]][ty+dy[i]] = 'J';
                            queue.add(new Node(false, tx + dx[i], ty + dy[i], t.time + 1));
                        }
                    }
                }

            }
        }
        if (ans){
            System.out.println(t.time+1);
        }
        else{
            System.out.println("IMPOSSIBLE");
        }



    }
}