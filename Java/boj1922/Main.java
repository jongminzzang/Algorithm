package boj1922;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;

public class Main {

    static int N, M;
    static String[] s;
    static int a, b, c;


    static class Node implements Comparable<Node>{

        int y; // 도착지
        int v; // 비용

        Node(int y, int v){
            this.y = y;
            this.v = v;
        }

        @Override
        public String toString() {
            return "y : " + y + " v : " + v;
        }

        @Override
        public int compareTo(Node o) {
            return this.v - o.v;
        }
    }

    static int[] arr;
    static ArrayList<Node>[] edges;

    static PriorityQueue<Node> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        arr = new int[N+1];
        edges = new ArrayList[N+1];
        for (int i = 0; i < N + 1; i++) {
            edges[i] = new ArrayList<Node>();
        }

        for (int i = 0; i < M; i++) {
            s = br.readLine().split(" ");
            a = Integer.parseInt(s[0]);
            b = Integer.parseInt(s[1]);
            c = Integer.parseInt(s[2]);

            edges[a].add(new Node(b, c));
            edges[b].add(new Node(a, c));

        }

//        for (ArrayList<Node> x :
//                edges) {
//            for (Node t :
//                    x) {
//                System.out.println(t);
//            }
//            System.out.println();
//        }

        int answer = 0;
        int count = 1;
        arr[1] = 1;

        for (Node x: edges[1]) {
            pq.add(x);
        }

        Node t;
        while (count < N){
            t = pq.poll();

            if (arr[t.y] == 0){
                answer += t.v;
                arr[t.y] = 1;
                for (Node x: edges[t.y]) {
                    pq.add(x);
                }
                count += 1;
            }
        }
        System.out.println(answer);
    }
}
