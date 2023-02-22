package boj1991;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {


    static char[] left = new char[26];
    static char[] right = new char[26];

    static String[] s;
    static char rt, l, r;

    static StringBuilder sb = new StringBuilder();


    static String preOrder(int k){
        sb.append((char) ('A'+k));
        if (left[k] != 0){
            preOrder((int) left[k]);
        }
        if (right[k] != 0){
            preOrder((int) right[k]);
        }
        return sb.toString();
    }
    static String inOrder(int k){
        if (left[k] != 0){
            inOrder((int) left[k]);
        }
        sb.append((char) ('A'+k));
        if (right[k] != 0){
            inOrder((int) right[k]);
        }
        return sb.toString();
    }
    static String postOrder(int k){
        if (left[k] != 0){
            postOrder((int) left[k]);
        }
        if (right[k] != 0){
            postOrder((int) right[k]);
        }
        sb.append((char) ('A'+k));
        return sb.toString();
    }



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        // input -> tree
        for (int i = 0; i < N; i++) {
            s = br.readLine().split(" ");
            rt = s[0].charAt(0);
            l = s[1].charAt(0);
            r = s[2].charAt(0);
            if (l != '.'){
                left[(int) (rt-'A')] = (char) (l-'A');
            }
            if (r != '.'){
                right[(int) (rt-'A')] = (char) (r-'A');
            }
        }

        System.out.println(preOrder(0));
        sb.setLength(0);
        System.out.println(inOrder(0));
        sb.setLength(0);
        System.out.println(postOrder(0));
    }
}
