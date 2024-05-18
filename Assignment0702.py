# Author: Barini Simhadri
# Date: 29-02-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/AP-TXOEefe4

import random
import math

class Point:
    def __init__(self, x, y):
        """Initialize the Point with x and y coordinates."""
        self.x = x
        self.y = y

class Ellipse:
    def __init__(self, center, focal_point, long_axis_width):
        """
        Initialize the Ellipse with center point, focal point, and width of the long axis.

        Args:
            center (Point): Center point of the ellipse.
            focal_point (Point): Focal point of the ellipse.
            long_axis_width (float): Width of the long axis of the ellipse.
        """
        self.center = center
        self.focal_point = focal_point
        self.long_axis_width = long_axis_width
        self.short_axis_width = math.dist([center.x, center.y], [focal_point.x, focal_point.y]) / 2

def is_inside_ellipse(point, ellipse):
    """
    Check if a point is inside an ellipse.

    Args:
        point (Point): The point to check.
        ellipse (Ellipse): The ellipse to check against.

    Returns:
        bool: True if the point is inside the ellipse, False otherwise.
    """
    distance_to_center = math.dist([point.x, point.y], [ellipse.center.x, ellipse.center.y])
    distance_to_focal_points = (math.dist([point.x, point.y], [ellipse.focal_point.x, ellipse.focal_point.y]),
                                math.dist([point.x, point.y], [ellipse.center.x, ellipse.center.y]))
    return (distance_to_center <= ellipse.long_axis_width / 2) and (sum(distance_to_focal_points) <= ellipse.long_axis_width)

def computeOverlapOfEllipses(e1, e2, num_samples=10000):
    """
    Compute the area of overlap between two ellipses using Monte Carlo simulation.

    Args:
        e1 (Ellipse): The first ellipse.
        e2 (Ellipse): The second ellipse.
        num_samples (int): Number of random points to sample for Monte Carlo simulation.

    Returns:
        float: Estimated area of overlap between the two ellipses.
    """
    count = 0
    for _ in range(num_samples):
        x = random.uniform(min(e1.center.x - e1.long_axis_width, e2.center.x - e2.long_axis_width),
                          max(e1.center.x + e1.long_axis_width, e2.center.x + e2.long_axis_width))
        y = random.uniform(min(e1.center.y - e1.long_axis_width, e2.center.y - e2.long_axis_width),
                          max(e1.center.y + e1.long_axis_width, e2.center.y + e2.long_axis_width))
        point = Point(x, y)
        if is_inside_ellipse(point, e1) and is_inside_ellipse(point, e2):
            count += 1

    total_area = (e1.long_axis_width * e1.short_axis_width * math.pi) + (e2.long_axis_width * e2.short_axis_width * math.pi)
    overlap_area = (count / num_samples) * total_area
    return overlap_area

# Simple Case: Two ellipses - one surrounding the other
p1 = Point(2, 3)
p2 = Point(2, 3)
e1 = Ellipse(p1, p2, 4)
e2 = Ellipse(p1, p2, 2)
overlap = computeOverlapOfEllipses(e1, e2)
print("Overlap Area (Simple Case):", overlap)

# More Complicated Case: Two ellipses with different centers and sizes
p3 = Point(0, 0)
p4 = Point(4, 0)
e3 = Ellipse(p3, p4, 6)
e4 = Ellipse(p1, p2, 3)
overlap = computeOverlapOfEllipses(e3, e4)
print("Overlap Area (Complicated Case):", overlap)
