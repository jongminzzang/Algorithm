import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static char map[][];
    static char[] check = new char[26];
    static int[] dx = {1,0,-1,0};
    static int[] dy = {0,1,0,-1};
    static int R, C;
    static int answer;

    public static void dfs(int x, int y, int depth){
        if (depth > answer){
            answer = depth;
        }

        int tx, ty;
        for (int i = 0; i < 4; i++) {
            tx = x + dx[i];
            ty = y + dy[i];

            if (tx >= 0 && ty >= 0 && tx < R && ty < C) {
                if (check[map[tx][ty] - 'A'] == 0) {
                    check[map[tx][ty] - 'A'] = 1;
                    dfs(tx, ty, depth + 1);
                    check[map[tx][ty] - 'A'] = 0;
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s = br.readLine().split(" ");
        R = Integer.parseInt(s[0]);
        C = Integer.parseInt(s[1]);

        map = new char[R][];

        for (int i = 0; i < R; i++) {
            char[] newArr = new char[C];
            String t = br.readLine();
            map[i] = t.toCharArray();
        }

        check[map[0][0]-'A'] = 1;
        dfs(0,0, 1);
        System.out.println(answer);
    }
}