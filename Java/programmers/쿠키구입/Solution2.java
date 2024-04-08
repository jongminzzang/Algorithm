import java.util.*;

/*
  시간복잡도 : N^2
  b = x 고정(N) -> a는 b에서 0으로, y는 -> x에서 cookie_len으로 투 포인터
*/

class Solution {
    public int solution(int[] cookie) {
        int answer = 0;
        int cookie_len = cookie.length;
        
        int[] sum = new int[cookie_len+1];
        Arrays.fill(sum, 0);

        for (int i = 0; i < cookie_len; i++) {
            sum[i+1] = sum[i] + cookie[i];
        }

        int l, r;
        for (int b = 0; b < cookie_len; b++) {
            l = b;
            r = b;
            while (true) {
                if (l == -1 || r == cookie_len+1) break;
                else if (sum[b] - sum[l] == sum[r] - sum[b]) {
                    if (sum[b] - sum[l] > answer) {
                        answer = sum[b] - sum[l];
                    }
                    r++;
                }
                else if (sum[b] - sum[l] > sum[r] - sum[b]) r++;
                else l--;
            }
        }

        return answer;
    }
}
