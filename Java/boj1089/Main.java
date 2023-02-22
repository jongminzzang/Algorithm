package boj1089;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    static char light[][] = {
            "###...#.###.###.#.#.###.###.###.###.###".toCharArray(),
            "#.#...#...#...#.#.#.#...#.....#.#.#.#.#".toCharArray(),
            "#.#...#.###.###.###.###.###...#.###.###".toCharArray(),
            "#.#...#.#.....#...#...#.#.#...#.#.#...#".toCharArray(),
            "###...#.###.###...#.###.###...#.###.###".toCharArray()
    };


    static char[][] tower;

    static List<Integer> available(int start){
        List<Integer> l= new ArrayList<>();

        boolean b = true;
        int t = 0;

        for (int i = 0; i < 10; i++) {
            b = true;
            for (int j = 4*i; j < 4*i+3; j++) {
                for (int k = 0; k < 5; k++) {
                    if (light[k][j] == '.' && tower[k][start+j%4] == '#'){
                        b = false;
                        break;
                    }
                }
                if (b == false) break;
            }
            if (b == true) l.add(i);
        }
        return l;
    }


    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        tower = new char[5][];

        for (int i = 0; i < 5; i++) {
            tower[i] = br.readLine().toCharArray();
        }

        double answer = 0;
        List<Integer> arr;
        List<List <Integer>> arrmap = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            arrmap.add(available(4*i));
        }


        int count = 0;
        double darr[] = new double[N];
        for (int i = 0; i < N; i++) {
            if(arrmap.get(i).size()==0){
                answer = -1;
                break;
            }
            else{
                for (int j = 0; j < arrmap.get(i).size(); j++) {
                    darr[i] += arrmap.get(i).get(j);
                }
                darr[i] = darr[i]/arrmap.get(i).size();
            }
        }

        if (answer == -1){
            System.out.println(answer);
        }
        else {
            for (int i = 0; i < N; i++) {
                answer += darr[i]*(Math.pow(10, N-i-1));
            }
            System.out.println(String.format("%.7f", answer));
        }

    }

}
