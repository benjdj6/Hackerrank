import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        String max = "";
        String min = "";
        for (int i = k; i <= s.length(); i++) {
            String curr = s.substring(i - k, i);
            if (curr.compareTo(max) > 0) {
                max = curr;
            }
            if (min == "" || curr.compareTo(min) < 0) {
                min = curr;
            }
        }
        System.out.println(min);
        System.out.println(max);
    }
}