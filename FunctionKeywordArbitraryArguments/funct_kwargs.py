"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/5/2020
This program tests the use of *args and **kwargs
"""


def average_scores(*args, **kwargs):
    """
    This function calculates the average of whatever is in the parameters
    :param args:
    :param kwargs:
    :return:
    """
    sums = 0
    for x in args:
        sums = sums + x

    avg = sums / len(args)  # calculates the average score
    average_score = avg

    student_name, course_name = kwargs

    print("Results:", "Average Score =", average_score,'Name =', student_name,  "Course =", course_name)

if __name__ == '__main__':
    average_scores(9, 8, 10, 9, student_name='E', course_name="Python")
    average_scores(5, 4, 1, 2, student_name='L', course_name="Math")
    average_scores(13, 9, 15, 12, student_name='M', course_name="History")
