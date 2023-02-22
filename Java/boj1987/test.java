package boj1987;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class test {
    static int R, C;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static char[][] board;
    static boolean[][] visited;
    static int[][] count;
    static HashSet<Character> set;
    public static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        board = new char[R][C];
        visited = new boolean[R][C];
        count = new int[R][C];
        set = new HashSet<>();
        result = 1;

        for (int i = 0; i < R; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < C; j++) {
                board[i][j] = tmp.charAt(j);
            }
        }

        count[0][0] = 1;

        set.add(board[0][0]);
        dfs(0, 0);

        System.out.println(result);
    }

    public static void dfs(int p1, int p2) {
        //visited[p1][p2] = true;
        for (int i = 0; i < 4; i++) {
            int x = p1 + dx[i];
            int y = p2 + dy[i];
            if(0 <= x && x < R && 0 <= y && y < C) {
                if(!set.contains(board[x][y])) {
                    set.add(board[x][y]);
                    count[x][y] = count[p1][p2] + 1;
                    if (result < count[x][y]){
                        result = count[x][y];
                    }
                    dfs(x, y);
                    set.remove(board[x][y]);
                }
            }
        }
    }
}