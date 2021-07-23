from pprint import pprint
from itertools import product

def left(pos):
    return (pos[0], pos[1]-1)

def right(pos):
    return (pos[0], pos[1]+1)

def up(pos):
    return (pos[0]-1, pos[1])

def down(pos):
    return (pos[0]+1, pos[1])

def argmin(dic):
    min_ = float('+inf')
    for k, v in dic.items():
        if v <= min_:
            min_ = v
            argmin_ = k
    return argmin_, min_

def solution(M, source=(0,0), sink=None):
    """
    Modified version of Dijkstra's algorithm

    Instead of populating one distance for each position i,j,
    we populate two quantities: one distance assuming
    we didn't use our "wall credit" yet and one distance assuming we did.

    walls (i.e. i,j such that M[i][j] = 1) will always have an
    infinite first distance but can receive a finite second distance
    if their parent is accessible without using the wall credit.

    The final answer is the shortest of the two distances
    for the sink position
    """
    if sink is None:
        sink = (len(M)-1, len(M[0])-1)

    # initialize distances to the source to +inf
    # except for the source itself

    # each position is associated with a list containing
    # two distances:
    # 1. minimum distance to source, having NOT used our wall credit yet
    # 2. minimum distance to source, having used our wall credit

    dist =\
        [
            [
                [float('+inf'), float('+inf')]\
                for _ in range(len(M[0]))
            ]\
            for _ in range(len(M))
        ]

    dist[source[0]][source[1]] = [0, 0]

    # the prev table contains the previous position of a given position
    # this is used to backtrack and retrieve the min path from the sink
    # to source node once we have computed the min distance

    # again, we use two values:
    # one that assumes we haven't used the wall credit yet
    # one that assumes we have used the wall credit already
    prev = [[[None, None] for _ in range(len(M[0]))] for _ in range(len(M))]

    # initialize dicionary of unvisited nodes
    # each pos is represented twice (wall credit used/not used)
    all_pos = product(range(len(M)), range(len(M[0])), [0,1])
    unvisited = {(i,j,k): dist[i][j][k] for i,j,k in all_pos}

    while len(unvisited) > 0:
        # update unvisited dict to reflect the updated distances
        unvisited = {(i,j,k): dist[i][j][k] for i,j,k in unvisited.keys()}
        key, curr_dist = argmin(unvisited)
        curr_pos = (key[0], key[1])  # current position
        is_credit_used = key[2]
        del unvisited[key]

        next_positions = [fn(curr_pos) for fn in (left, right, up, down)]

        for pos in next_positions:
            # check whether the new pos is within the map boundaries
            impossible_pos = (pos[0] < 0 or pos[0] >= len(M))\
                          or (pos[1] < 0 or pos[1] >= len(M[0]))

            if impossible_pos:
                continue

            for use_credit in [0, 1]:
                if (pos[0], pos[1], use_credit) not in unvisited:
                    # we already visited pos_
                    # under the use_credit (yes/no) assumption
                    continue
                elif M[pos[0]][pos[1]] == 0:  # didn't visit pos_ & not a wall
                    #  only update current scenario (credit was used or not)
                    if is_credit_used == use_credit:
                        new_dist = curr_dist + 1

                        if new_dist < dist[pos[0]][pos[1]][use_credit]:
                            # assign new distance and new parent position
                            dist[pos[0]][pos[1]][use_credit] = new_dist
                            prev[pos[0]][pos[1]][use_credit] = curr_pos

                elif M[pos[0]][pos[1]] == 1:  # it's a wall!
                    if use_credit != 1:
                        # first distance stays +inf if
                        # we do not use the credit
                        continue
                    else:
                        # what would be the distance to this new position
                        # if we hadn't already used the credit?
                        dist_without_using_credit =\
                            1 + dist[curr_pos[0]][curr_pos[1]][0]

                        # Is it better than the case where we use it for
                        # the first time?
                        if dist_without_using_credit < dist[pos[0]][pos[1]][1]:
                            # update distance and parent position
                            dist[pos[0]][pos[1]][1] = dist_without_using_credit
                            prev[pos[0]][pos[1]][1] = curr_pos

    return 1 + min(dist[sink[0]][sink[1]])


if __name__ == '__main__':
    with open('testcases.txt', 'r') as f:
        text = f.read()

    lines = text.strip().split('\n')

    testcase = []
    for i, line in enumerate(lines):
        if len(line) > 0:
            testcase.append([int(char) for char in line.strip('\n')])
        if len(line) == 0 or i == len(lines) - 1:
            print('\nTestcase:\n')
            pprint(testcase)
            print('\nMinimum distance:\n')
            print(solution(testcase))
            testcase = []
