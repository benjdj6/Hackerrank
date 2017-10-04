function getGrade(score) {
    let grade;
    // Fun solution without explicit if-else
    let i = 0;
    let letters = ['F','E','D','C','B','A'];
    while (score > 5) {
        score -= 5;
        i += 1;
    }
    grade = letters[i];
    return grade;
}