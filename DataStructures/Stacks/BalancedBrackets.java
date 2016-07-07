import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        char[] sol = {'{', '}', '[', ']', '(', ')'};
        for(int a0 = 0; a0 < t; a0++){
            Stack<Character> para = new Stack<Character>();
            String s = in.next();
            Boolean bal = true;
            for(int i=0; i < s.length(); i++) {
                if(para.isEmpty() && (s.charAt(i) == '}' || s.charAt(i) == ']' || s.charAt(i) == ')')) {
                    bal = false;
                    break;
                }
                else if(s.charAt(i) == ')' && para.peek() == '(') {
                    para.pop();
                }
                else if(s.charAt(i) == ']' && para.peek() == '[') {
                    para.pop();
                }
                else if(s.charAt(i) == '}' && para.peek() == '{') {
                    para.pop();
                }
                else if(para.isEmpty() || s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{') {
                    para.push(s.charAt(i));
                }
                else {
                    bal = false;
                    break;
                }
            }
            if(para.isEmpty() && bal) {
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }
        }
    }
}