// 문자열 두개를 주고 문자열1의 문자가 문자열2의 문자와 같은 개수 중 최대값

package swea4865;

import java.util.Scanner;

public class swea4865 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int tc = sc.nextInt();
        sc.nextLine();

        for (int t = 0; t < tc; t++) {
            String str1 = sc.nextLine();
            String str2 = sc.nextLine();
            String check = "";


            int ans = 0;

            for (int i = 0; i < str1.length(); i++) {

                char a = str1.charAt(i);

                if (check.contains(String.valueOf(a))) {
                    continue;
                }

                check += a;

                int cnt = 0;


                for (int j = 0; j < str2.length(); j++) {
                    if (str2.charAt(j) == a) {
                        cnt++;
                    }

                if (cnt > ans) {
                    ans = cnt;
                }

                }
            }
            System.out.println("#"+t+" "+ans);

        }
    }
}
