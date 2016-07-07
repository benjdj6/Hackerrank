import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Stack<Long> max = new Stack<Long>();
        Stack<Long> main = new Stack<Long>();
        while(n>0) {
            int query = sc.nextInt();
            if(query == 1) {
                long newVal = sc.nextInt();
                main.push(newVal);
                if(max.empty()) {
                    max.push(newVal);
                }
                else if(newVal >= max.peek()) {
                    max.push(newVal);
                }
            }
            else if(query == 2) {
                if(!main.empty()) {
                    long temp = main.pop();
                    if(max.peek() == temp) {
                        max.pop();
                    }    
                }
                else {
                    while(!max.empty()) {
                        max.pop();
                    }
                }
            }
            else if(query == 3) {
                if(!max.empty()) {
                    System.out.println(max.peek());
                }
            }
            n--;
        }
    }
}