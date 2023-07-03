class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        if start.x == end.x:
            self.slope = float("inf")
            self.y_intercept = float("inf")
        else:
            self.slope = (end.y - start.y) / (end.x - start.x)
            self.y_intercept = end.y - self.slope * end.x

    def is_vertical(self) -> bool:
        return self.slope == float("inf")

    def get_y_from_x(self, x: float):
        if self.is_vertical():
            return float("inf")
        return self.slope * x + self.y_intercept


def is_between_nums(start: float, middle: float, end: float) -> bool:
    if start > end:
        return end <= middle and middle <= start
    else:
        return start <= middle and middle <= end


def is_between_points(start: Point, middle: Point, end: Point) -> bool:
    return is_between_nums(start.x, middle.x, end.x) and is_between_nums(start.y, middle.y, end.y)


def find_intersection(start1: Point, end1: Point, start2: Point, end2: Point) -> Point:
    line1: Line = Line(start1, end1)
    line2: Line = Line(start2, end2)

    # If lines are parallel, then their infinite lines must have same
    # intercept. If so, check start/end of one is on the other line
    if line1.slope == line2.slope:
        if line1.y_intercept != line2.y_intercept:
            return None
        if is_between_points(start1, start2, end1):
            return start2
        elif is_between_points(start1, end2, end1):
            return end2
        elif is_between_points(start2, start1, end2):
            return start1
        elif is_between_points(start2, end1, end2):
            return end1
        else:
            return None
    x: float = None
    if line1.is_vertical() or line2.is_vertical():
        x = line1.start.x if line1.is_vertical() else line2.start.x
    else:
        x = (line2.y_intercept - line1.y_intercept) / (line1.slope - line2.slope)

    y: float = line2.get_y_from_x(x) if line1.is_vertical() else line1.get_y_from_x(x)

    intersection = Point(x, y)
    if is_between_points(start1, intersection, end1) and is_between_points(start2, intersection, end2):
        return intersection
    return None


if __name__ == "__main__":
    intersection = find_intersection(Point(1,1), Point(100, 100), Point(1, 100), Point(100, 1))
    print(intersection.x, intersection.y)
