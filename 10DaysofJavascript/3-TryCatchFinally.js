/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    let res = "";
    try {
        res = s.split("");
        res = res.reverse();
        res = res.join("");
    }
    catch (e) {
        console.log(e.message);
        console.log(s);
    }
    console.log(res);
}