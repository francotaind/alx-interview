island perimeter
================

## Description

You are given a map in form of a two-dimensional integer grid where 1 represents
land and 0 represents water. Grid cells are connected horizontally/vertically
(not diagonally). The grid is completely surrounded by water, and there is
exactly one island (i.e., one or more connected land cells). The island doesn't
have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and
height don't exceed 100. Determine the perimeter of the island.

Example:

```
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
```

## Solution

The solution is pretty simple. We just need to iterate over the grid and check
if the current cell is a land cell. If it is, we add 4 to the perimeter around
the cell and check if the adjacent cells are land cells. If they are, We
decrement the perimeter by 1. We do this for all the cells in the grid around
the current cell. The final perimeter is the sum of all the perimeters around
the land cells.

The time complexity of this solution is O(n^2) where n is the number of cells
inside
