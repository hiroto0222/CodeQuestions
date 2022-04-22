import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        sc.close();

        int ans = (int)Math.floor(Math.log(N) / Math.log(2));
        System.out.println(ans);
    }
}