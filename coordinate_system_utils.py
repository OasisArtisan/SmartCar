import numpy


def rotate_points(points, o, theta):
    """
    Convenience method that rotates multiple points around another point\n
    Format for points: ((x1,y1),(x2,y2),(x3,y3))
    """
    return tuple([rotate_point(p, o, theta) for p in points])
    pass


def rotate_point(p, o, theta):
    """Rotates a point about another point"""
    x = numpy.cos(theta) * (p[0]-o[0]) - numpy.sin(theta) * (p[1]-o[1]) + o[0]
    y = numpy.sin(theta) * (p[0] - o[0]) + numpy.cos(theta) * (p[1] - o[1]) + o[1]
    return x, y


def get_mbbox(points):
    """
    Computes the minimum oriented bounding box\n
    Format for points: ((x1,y1),(x2,y2),(x3,y3))
    """
    points = points + (points[0],)
    lowest_bbox = None
    lowest_area = None
    for i in range(len(points)-1):
        p = points[i+1]
        o = points[i]
        theta = get_angle(p, o)
        nps = rotate_points(points, o, -theta)
        bbox = get_sbbox(nps)
        area = get_area(bbox)
        if lowest_area is None or area < lowest_area:
            bbox = rotate_points(bbox, o, theta)
            lowest_bbox = bbox
            lowest_area = area
    return lowest_bbox


def get_angle(p, o):
    """
    Calculates the angle the point makes with an origin
    The angle is in radians counter clock wise from the positive x-axis
    """
    x = p[0] - o[0]
    y = p[1] - o[1]
    # Check if the point lies on an axis
    if x == 0 and y == 0:
        return 0
    if x == 0:
        if y > 0:
            return numpy.pi * 1/2
        else:
            return numpy.pi * 3/2
    elif y == 0:
        if x > 0:
            return 0
        else:
            return numpy.pi

    theta = numpy.arctan(abs(y) / abs(x))

    # Check the point's quarter
    if x > 0 and y > 0:  # 1st
        return theta
    elif x < 0 and y > 0:  # 2nd
        return numpy.pi - theta
    elif x < 0 and y < 0:  # 3rd
        return numpy.pi + theta
    else:  # 4th
        return numpy.pi*2 - theta


def get_sbbox(points):
    """
    Computes the straight un oriented bounding box\n
    Format for points: ((x1,y1),(x2,y2),(x3,y3))
    """
    p = tuple(zip(*points))
    xmax = max(p[0])
    xmin = min(p[0])
    ymax = max(p[1])
    ymin = min(p[1])
    return (xmin, ymin), (xmin, ymax), (xmax, ymax), (xmax, ymin)


def get_centeroid(points):
    """
    Returns the centeroid of a cluster of points\n
    Format for points: ((x1,y1),(x2,y2),(x3,y3))\n
    """
    points = tuple(zip(*points))
    x = sum(points[0])/len(points[0])
    y = sum(points[1]) / len(points[1])
    return x, y


def get_visual_center():
    pass


def get_shapes_intersections(shape1, shape2) :
    """
    Returns the intersection points of the 2 shapes\n
    Format for shapes: ((x1,y1),(x2,y2),(x3,y3))\n
    """
    shape1 = shape1 + (shape1[0],)
    shape2 = shape2 + (shape2[0],)
    # Start with a line from the first shape then go through all
    # the lines in the other shape and see if there is an intersection.
    for i in range(len(shape1)-1):
        for j in range(len(shape2) - 1):
            # Use cramer's rule to get the intersection
            pass


def get_lines_intersections(line1, line2):
    """
    Calculates the intersecting points of the two infinite straight lines
    Line format: ((x1,y1),(x2,y2))
    """
    x1 = line1[0][0]
    x2 = line1[1][0]
    y1 = line1[0][1]
    y2 = line1[1][1]
    x3 = line2[0][0]
    x4 = line2[1][0]
    y3 = line2[0][1]
    y4 = line2[1][1]
    det = (y2-y1) * (x3-x4) - (x1-x2) * (y4-y3)
    if  det == 0:
        return None
    xdet = (x1*y2-y1*x2) * (x3-x4) - (x1-x2) * (x3*y4-y3*x4)
    ydet = (y2-y1) * (x3*y4-y3*x4) - (x1*y2-y1*x2) * (y4-y3)
    return xdet/det, ydet/det


def get_lines_segments_intersections(line1, line2):
    pass


def is_inside(inner_points,outer_points):
    """
    Returns True if all the inner_points are enclosed by the outer_points' shape\n
    Format for points: ((x1,y1),(x2,y2),(x3,y3))
    """
    pass


def get_line_length(point1, point2):
    pass


def get_area(points):
    """
    Calculates the area of an arbitary polygon using the shoelace formula\n
    Format for points: ((x1,y1),(x2,y2),(x3,y3))\n
    """
    points = points+(points[0],)
    sum = 0
    x, y = zip(*points)
    for i in range(len(points)-1):
        sum += x[i]*y[i+1] - y[i] * x[i+1]
    return 0.5*abs(sum)
