package boj2458;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {


    static List<Integer>[] arr;
    static int N, M;

    static Queue<Integer> q = new LinkedList<>();
    static int[] visit;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s[] = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);

        visit = new int[N+1];
        arr = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) {
            arr[i] = new ArrayList<>();
        }

        int a, b;
        for (int i = 0; i < M; i++) {
            s = br.readLine().split(" ");
            arr[Integer.parseInt(s[1])].add(Integer.parseInt(s[0]));
        }

        for (int i = 1; i < N+1; i++) {
            if (arr[i].size() == 0){
                q.add(i);
            }
        }

        int t, answer = 0;
        while (!q.isEmpty()){
            if(q.size() ==1){
                answer += 1;
            }
            t = q.poll();
            for(Integer x :arr[t]){
                if (visit[x] == 0){
                    visit[x] = 1;
                    q.add(x);
                }
            }
        }

        System.out.println(answer);
    }

}
