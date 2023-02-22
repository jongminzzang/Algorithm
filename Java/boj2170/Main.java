package boj2170;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    static int N;
    static class Line{
        int start;
        int end;

        Line(int start, int end){
            this.start = start;
            this.end = end;
        }
    }


    static int sumLines(Line[] lines){
        int ret = 0;
        Line t = lines[0];

        for (int i = 1; i < lines.length; i++) {

            // 1. 다음 점의 시작점이 현재의 끝 점 보다 크다.
            if (lines[i].start > t.end){
                ret += t.end - t.start;
                t = lines[i];
            }
            // 2. 다음 점의 끝 점이 현재의 끝 점 보다 작다
            else if (lines[i].end < t.end) {
                ;
            }
            // 3. 다음 점의 시작점이 현재의 끝 점 보다는 작고
            //    다음 점의 끝점이 현재의 끝 점 보다는 크다.
            else {
                t.end = lines[i].end;
            }
        }
        ret += (t.end-t.start);

        return ret;
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        Line[] lines = new Line[N];

        String[] s;
        for (int i = 0; i < N; i++) {
           s = br.readLine().split(" ");
           lines[i] = new Line(Integer.parseInt(s[0]), Integer.parseInt(s[1]));
        }

        // 정렬
        Arrays.sort(lines, (x, y)->x.start-y.start);

        System.out.println(sumLines(lines));
    }
}
