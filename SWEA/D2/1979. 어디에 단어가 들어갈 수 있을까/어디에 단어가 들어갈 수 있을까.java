import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
    static int[][] map;
    static int k;
    static int N;

    public static int check(int idx, String start) {
        int ret = 0;
        int vad = 0;

        if ("row".equals(start)) {
            for (int i = 0; i < N; i++) {
                if (map[idx][i] == 1) {
                    vad++;
                    continue;
                }

                if (vad == k) {
                    ret++;
                }
                vad = 0;
            }
            if (vad == k) {
                ret++;
            }
        } else {
            for (int i = 0; i < N; i++) {
                if (map[i][idx] == 1) {
                    vad++;
                    continue;
                }
                if (vad == k) {
                    ret++;
                }
                vad = 0;
            }
            if (vad == k) {
                ret++;
            }
        }

        return ret;
    }

    public static void main(String args[]) throws Exception
	{
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        sc.nextLine();

        for (int t = 1; t < tc + 1; t++) {
            N = sc.nextInt();
            k = sc.nextInt();

            map = new int[N][N];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    map[i][j] = sc.nextInt();
                }
            }

            int cnt = 0;

            for (int i = 0; i < N; i++) {
                cnt += check(i, "row"); // 행 순회
                cnt += check(i, "col"); // 열 순회
            }

            System.out.println("#"+t+" "+cnt);
        }
    }
}
		


