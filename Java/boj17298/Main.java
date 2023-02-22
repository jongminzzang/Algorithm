package boj17298;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    static class Node{
        int idx;
        int val;

        public Node(int idx, int val){
            this.idx = idx;
            this.val = val;
        }
    }
    static Stack<Node> stack = new Stack<>();
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String s[] = br.readLine().split(" ");

        int arr[] = new int[s.length];
        for (int i = 0; i < s.length; i++) {
            arr[i] = Integer.parseInt(s[i]);
        }

        int t;
        Node n;
        for (int i = 0; i < s.length; i++) {
            t = arr[i];
            while (!stack.empty() && t > stack.peek().val){
               n = stack.pop();
               arr[n.idx] = t;
            }
            stack.push(new Node(i, arr[i]));
        }

        for (Node x : stack){
            arr[x.idx] = -1;
        }

        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]).append(" ");
        }
        System.out.print(sb);
    }
}
