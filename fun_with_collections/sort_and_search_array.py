"""
Author: Elijah Morishita
elmorishita@dmacc.edu
10/7/2020
This program gathers numeric input from a user, and places it into a array as a string,
it also gives the user a chance to search for an index within the array they created,
and finally it sorts the array in numeric order.
"""


def get_input():
    """
    This function gathers numeric user input and converts it to a string, then returns it.
    It also gives the user an option to search the array and sort the array.
    :return: user_input
    """

    end_loop = True  # Used to stop the loop for user input
    while end_loop:
        try:
            user_input = str(float(input("Please enter a number: ")))
            end_loop = False  # The loop breaks once the user has entered valid input
        except():
            print("Invalid input, please try again.")

    return user_input


def search_array(user_input):
    """
    This function gathers user input to pick an index, or -1 if their desired index isn't available
    :param user_input:
    :return: choice
    """
    end_loop = True  # Used to stop the loop for user input
    while end_loop:
        try:
            choice = int(float(input("Which index would you like to search for (1-3, or -1 if not found): ")))
            if choice > len(user_input) or choice == 0 or choice < -2:
                print("Invalid INDEX, please try again")
                continue
            end_loop = False  # The loop breaks once the user has entered valid input
        except():
            print("Invalid input, please try again.")
    return choice


def sort_array(user_input):
    """
    This function sorts the array and then returns it to keep the main function cleaner
    :param user_input:
    :return: user_input
    """
    user_input.sort()
    return user_input  # added a return statement for a cleaner looking main function


def make_array():
    """
    This function places the return of get_input() into a array, then returns the array
    :return: user_input
    """
    user_input = [0, 0, 0]  # initialized a array

    for x in range(0, 3):
        user_input[x] = get_input()

    index = search_array(user_input) - 1  # subtracting one for index sake
    if index != -1:
        print("You've chosen index #", (index + 1), ", which is ", user_input[index], "on the array")

    return sort_array(user_input)


if __name__ == '__main__':

    print("And the final results (sorted) are...", make_array())
