import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        char[] arr = A.toCharArray();
        /* Enter your code here. Print output to STDOUT. */
        String answer = "Yes";
        for(int i = 0; i < arr.length / 2; i++) {
            if(arr[i] != arr[arr.length - i - 1]) {
                answer = "No";
                break;
            }
        }
        System.out.println(answer);
    }
}