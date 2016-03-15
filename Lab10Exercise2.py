"""

Lab10Exercise2.py

"""

from random_module_randrange_function_as_module import*

def AskNumberOfTurns():

    while True:
        number_turns_input = raw_input("Please enter the number of turns for both players: ")
        try:
            number_turns = int(number_turns_input)
            return number_turns
        except ValueError:
            print "You have not entered an integer value for number of turns."
            continue

def ReturnPointsForBoolean(boolean):

    if boolean == True:
        return 2
    else:
        return 1

def TotalPoints(points_list):

    total = 0

    for points in points_list:
        total = total + points

    return total

def PrintResults(points_list_1, points_list_2):

    points_list_1_total = TotalPoints(points_list_1)
    points_list_2_total = TotalPoints(points_list_2)

    print "Player 1 points are:", points_list_1, "and the total for Player 1 is:", points_list_1_total
    print "Player 2 points are:", points_list_2, "and the total for Player 2 is:", points_list_2_total

def PlayGame():

    turn = 1
    player_1_points = []
    player_2_points = []

    number_turns = AskNumberOfTurns()
    while turn <= number_turns:
        player_1 = TossCoins()
        player_1_points.append(ReturnPointsForBoolean(player_1))
        player_2 = TossCoins()
        player_2_points.append(ReturnPointsForBoolean(player_2))
        turn = turn + 1
        
    print player_1_points
    PrintResults(player_1_points, player_2_points)

PlayGame()
