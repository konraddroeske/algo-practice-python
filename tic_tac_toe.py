# DumbTicTacToe
#
# Two dumb computers are playing a game of tic-tac-toe. They really don't bother using
# advanced logic or heuristic in order to play a better move, so they just take a
# random move.

# Given a state in the tic-tac-toe game, your task is to determine the statistical chances
# of the current computer on to win. The state of the game is given by a 3x3 string
# matrix consisting of 'x','o' and '?' for not yet filled fields. The winner is the
# one which makes three of his marks in a single row, column or a diagonal.

# Example:
# Given {"x?o","xo?","???"}
#
# the map is:
# x?o
# xo?
# ???
#
# Since the number of played moves is 4, the next computer is the one with 'x'. He can
# place an 'x' on each of the 5 available places. The bottom left field makes him a
# winner, while the other four resume the game. Next, the 'o'
# computer can play one of the 4 remaining fields in each of the four states that the
# 'x' computer can leave to him.
# And so on ...
#
# In this example, the chances for the 'x' computer to win are 44.6%
#
# Your task is to fetch all the possible game outcomes, and return the chances of winning
# for the current computer in percentages (the percentages are half rounded up with one
# decimal place). If there is a winner in some step,
# and still some remaining empty fields, these fields are not played in that state.

# Map legend:
# 'x' - represents a marked field by the 'x' computer
# 'o' - represents a marked field by the 'o' computer
# '?' - represents a not yet filled field

# Input parameters:
#   map - a String[], representing the current game state

# Constraints:
#   - map will have exactly three element
#   - each element of map will consist of exactly three characters
#   - each character will be either 'x','o' or '?'
#   - there will be at least one character different than '?'
#   - the input will be correct, valid and without any winner present at the moment

# Return value:
#   The chances of the current computer to win, expressed in percentages
# Class Name:
#   DumbTicTacToe
#
# Method signature:
#   public String getChances(String[] map)

# Test Case 1:
#   getChances({"x?o","xo?","???"}) = "44.6%"
#
# Test Case 2:
#   getChances({"oox","xx?","?ox"}) = "0.0%"
#
# Test Case 3:
#   getChances({"?oo","oxx","oxx"}) = "100.0%"
#
# Test Case 4:
#   getChances({"ox?","x?o","xxo"}) = "100.0%"
#
# Test Case 5:
#   getChances({"ox?","???","?xo"}) = "44.6%"
#
# Test Case 6:
#   getChances({"???","???","??x"}) = "28.5%"
#
# Test Case 7:
#   getChances({"xox","o?x","?xo"}) = "0.0%"
#
# Test Case 8:
#   getChances({"x?x","o?x","oxo"}) = "0.0%"
#
# Test Case 9:
#   getChances({"xx?","x?o","?o?"}) = "22.2%"
#
# Test Case 10:
#   getChances({"??x","?x?","o??"}) = "26.9%"
