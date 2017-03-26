class Student(Person):

    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNum, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNum
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = sum(self.scores)
        avg = avg / len(self.scores)
        grade = 'F'
        if avg >= 90:
            grade = 'O'
        elif avg >= 80:
            grade = 'E'
        elif avg >= 70:
            grade = 'A'
        elif avg >= 55:
            grade = 'P'
        elif avg >= 40:
            grade = 'D'
        else:
            grade = 'T'
        return grade
