#!/usr/bin/env python
#
# Solution Template for Corey's Party
# 
# Australian Informatics Olympiad 2014
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of friends.
N = None

# M is the number of friendships.
M = None

# A is the number of guests each guest must already know.
A = None

# B is the number of guests each guest must not already know.
B = None

# Open the input and output files.
input_file = open("partyin.txt", "r")
output_file = open("partyout.txt", "w")

# Read the values of N, M, A and B from the input file. 
input_line = input_file.readline().strip()
N, M, A, B = map(int, input_line.split())

# Number of freindships for each person
numFriends = {x+1 : 0 for x in range(N)}

# Friends of each person
friends = {x+1 : [] for x in range(N)}

# Read in the friendships.
for i in xrange(0, M):
    input_line = input_file.readline().strip()
    x, y = map(int, input_line.split())
    numFriends[x] += 1
    numFriends[y] += 1
    friends[x] = friends[x] + [y]
    friends[y] = friends[y] + [x]
    # TODO: We do not do anything with the values that are being read in. It is
    # up to you to process or store them.

# TODO: This is where you should compute your solution and store it into the
# variable answer.
answer = N

madeRemov = True

while madeRemov:
    madeRemov = False
    for person in numFriends.keys():
        x = numFriends[person]
        if x < A or x >= answer-B:
            for friend in friends[person]:
                numFriends[friend] -= 1
            answer -= 1
            del numFriends[person]
            madeRemov = True

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
