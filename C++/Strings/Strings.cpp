#include <iostream>
#include <string>
using namespace std;

int main() {
    // Complete the program
    string a, b;
    cin >> a >> b;
    cout << a.size() << " " << b.size() << endl;
    cout << a + b << endl;
    char tmp = b[0];
    b[0] = a[0];
    a[0] = tmp;
    cout << a << " " << b;
    return 0;
}