#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int x,y;
    string numbers[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    cin >> x >> y;
    for(int i = x; i <= y; i++) {
        if(i <= 9) {
            cout << numbers[i - 1] << endl;
        }
        else if(i % 2 == 0) {
            cout << "even" << endl;
        }
        else {
            cout << "odd" << endl;
        }
    }
    return 0;
}