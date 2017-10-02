/*
 * Create the function factorial here
 */
function factorial(n) {
    let result = n;
    n -= 1;
    while (n > 0) {
        result *= n;
        n -= 1;
    }
    return result;
}