package programmers.findRaod;

import java.util.*;

class Node {

    static ArrayList<Integer> preOrder = new ArrayList();
    static ArrayList<Integer> postOrder = new ArrayList();

    int x;
    int y;
    int val;
    Node left;
    Node right;

    Node (int x, int y, int val){
        this.x = x;
        this.y = y;
        this.val = val;
    }

    @Override
    public String toString(){
        return "(" + this.x + " " + this.y + " " + val + ")";
    }

    void add(Node n){
        Node t = this;
        while (true){
            // 내 자식 노드 인 경우
            if (t.y + 1 == n.y){
                if (t.x > n.x){
                    t.left = n;
                }
                else{
                    t.right = n;
                }
                break;
            }
            // 더 밑으로 내려가야하는 경우 -> t 갱신
            else{
                if (t.x > n.x){
                    t = t.left;
                }
                else{
                    t = t.right;
                }
            }
        }
    }

    void preOrderFunc() {
        preOrder.add(this.val);
        if (this.left != null) this.left.preOrderFunc();
        if (this.right != null) this.right.preOrderFunc();
    }
    void postOrderFunc() {
        if (this.left != null) this.left.postOrderFunc();
        if (this.right != null) this.right.postOrderFunc();
        postOrder.add(this.val);
    }
}


class Solution {
    public int[][] solution(int[][] nodeinfo) {

        int N = nodeinfo.length;
        Node[] nodeArr = new Node[N];

        int y = 0;
        int[] t;
        for (int i = 0; i < N; i++){
            t = nodeinfo[i];
            nodeArr[i] = new Node(t[0], t[1], i+1);
        }
        
        // y값 기준으로 정렬
        Arrays.sort(nodeArr, (a, b)->b.y-a.y);

        Node root = nodeArr[0];
        
        // y값을 1씩 증가하는 방향으로 수정
        // Node.add()를 편하게 하기 위해서
        root.y = 100001;
        int h = 100001;
        int k = root.y;
        for (int i = 1; i < N; i++){
            if (nodeArr[i].y != k){
                h += 1;
                k = nodeArr[i].y;
            }
            nodeArr[i].y = h;
        }

        // 트리 완성
        for (int i = 1; i < N; i++){
            root.add(nodeArr[i]);
        }

        // preOrder, postOrder 함수 실행
        root.preOrderFunc();
        root.postOrderFunc();

        
        int[][] answer = new int[2][N];
        for (int i = 0; i < N; i++){
            answer[0][i] = Node.preOrder.get(i);
            answer[1][i] = Node.postOrder.get(i);
        }

        return answer;
    }
}
