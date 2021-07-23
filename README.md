# dijkstra-with-a-shortcut
A modified version of Dijkstra's algorithm in which we're allowed to take down a wall. I solved this problem as part of the Google foobar challenge and thought my solution was worth sharing.

## Problem description

You have a map, with an entry and exit. The map is represented as a matrix of 0s and 1s, where 0s are passable spaces and 1s are impassable walls. The entry is at the top left (0,0) and the exit is at the bottom right (w-1,h-1).

Write a function `solution(map)` that generates the length of the shortest path from the entry to the exit, where you are allowed to remove one wall. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

## Some examples:
Map:
```
000000
111110
000000
011111
011111
000000
```

Answer: 11

Map:
```
000000
111110
100000
011111
011111
000000
```

Answer: 21

Map:
```
010
001
100
110


Answer: 6

## Using the script
To test the testcases, simply run the script

```python
python dijkstra_with_a_shortcut.py
```
