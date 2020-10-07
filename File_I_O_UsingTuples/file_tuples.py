"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/6/2020
This program writes student names and test scores to a file,
then reads the info on a .txt file
"""

def write_to_file(*names_and_scores):
    """
    This function opens a file, writes to a line, then closes the file
    :param names_and_scores:
    :return:
    """
    with open('student_info.txt', 'a') as outfile:
        outfile.write(str(names_and_scores))
        outfile.write("\n")


def get_student_info(**kwargs):
    """
    This function takes a kwarg (name) as a parameter, gathers score data from the
    user, and places that data in the write_to_file function
    :param kwargs:
    :return:
    """
    scores = ()
    index = 0
    while True:
        scores = scores + (input("Please enter your test scores (-1 to stop): "),)
        if scores[-1] == '-1':
            print("=" * 40)  # a divider between function calls
            break

    names = kwargs
    write_to_file(names, scores)


def read_from_file():
    """
    This function reads a file line by line
    :return:
    """
    with open('student_info.txt', 'r') as file:
        read_data = file.read()
        print(read_data)


if __name__ == '__main__':
    get_student_info(name="Elijah Morishita")
    get_student_info(name="John McClain")
    get_student_info(name="John Connor")
    get_student_info(name="David Hayter")
    read_from_file()
    input('Press any key to end')
