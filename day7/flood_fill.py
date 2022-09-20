"""
733. Flood Fill

An image is represented by an m x n integer
grid image where image[i][j] represents the
pixel value of the image.

You are also given three integers sr, sc, and color.
You should perform a flood fill on the image
starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel,
plus any pixels connected 4-directionally to the starting
pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels
(also with the same color), and so on.
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1:

>>> floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)
[[2,2,2],[2,2,0],[2,0,1]]

Explanation: From the center of the image with
position (sr, sc) = (1, 1) (i.e., the red pixel),
all pixels connected by a path of the same color as
the starting pixel (i.e., the blue pixels) are colored with
the new color.
Note the bottom corner is not colored 2, because it is not
4-directionally connected to the starting pixel.

Example 2:

>>> floodFill([[0,0,0],[0,0,0]],0,0,0)
[[0,0,0],[0,0,0]]

Explanation: The starting pixel is already colored 0,
so no changes are made to the image.

"""

import doctest
from typing import List


def floodFill(
    self, image: List[List[int]], sr: int, sc: int, color: int
) -> List[List[int]]:
    """
    Solution Idea:
    """
    if image is None or image[sr][sc] == color:
        return image
    fill(image, sr, sc, image, image[sr][sc], color)
    return image


def fill(
    image: List[List[int]], sr: int, sc: int, initial_color: int, color: int
):
    # check out of bound
    if (
        sr < 0
        or sr >= len(image)
        or sc < 0
        or sc >= len(image[0])
        or image[sr][sc] != initial_color
    ):
        return
    image[sr][sc] = color
    fill(image, sr + 1, sc, initial_color, color)  # down
    fill(image, sr - 1, sc, initial_color, color)  # up
    fill(image, sr, sc - 1, initial_color, color)  # left
    fill(image, sr, sc + 1, initial_color, color)  # right


doctest.testmod()
