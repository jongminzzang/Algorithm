import java.util.*;


/*
시간복잡도 : N^2LogN
a, b 고정(N^2) -> x=b+1 고정 ->  y 이분 탐색(logN)
*/

class Solution1 {
    public int solution(int[] cookie) {
        int answer = 0;
        int cookie_len = cookie.length;
        
        int[] sum = new int[cookie_len+1];
        Arrays.fill(sum, 0);

        for (int i = 0; i < cookie_len; i++) {
            sum[i+1] = sum[i] + cookie[i];
        }


        int a, b;
        int t;
        int l, r, m;
        for (int i = 0; i < cookie_len; i++) {
            b = i;
            for (a = 0; a < b; a++) {
                t = sum[b]-sum[a];
                l = b;
                r = cookie_len;
                while (l <= r) {
                    m = (l+r)/2;
                    if (t == sum[m] - sum[b]){
                        if (t > answer) {
                            answer = t;
                        }
                        break;
                    } else if (t < sum[m] - sum[b]) {
                        r = m-1;
                    } else {
                        l = m+1;
                    }
                }
            }
        }

        return answer;
    }
}
