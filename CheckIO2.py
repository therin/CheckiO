from turtle import *
'''
setup (width=200, height=200, startx=0, starty=0)

speed ("slow") # important! turtle is intolerably slow otherwise
tracer (False)    # This too: rendering the 'turtle' wastes time

for i in range(200):
    forward(i)
    right(90.5)

done()


BOOL CrossLine(long x1, long y1, long x2, long y2, long x3, long y3, long x4, long y4, long &x, long &y) {
long    dx1 = x2 - x1;
long    dy1 = y2 - y1;
long    dx2 = x4 - x3;
long    dy2 = y4 - y3;
    x = dy1 * dx2 - dy2 * dx1;
    if(!x || !dx2)
        return
            false;
    y = x3 * y4 - y3 * x4;
    x = ((x1 * y2 - y1 * x2) * dx2 - y * dx1) / x;
    y = (dy2 * x - y) / dx2;
    return
        ((x1 <= x && x2 >= x) || (x2 <= x && x1 >= x)) && ((x3 <= x && x4 >= x) || (x4 <= x && x3 >= x));
}

Input: Four lists with coordinates, each one is a list of x and y coordinates - W1, W2, A, B - Integers.
Output: Hits the wall or not, True or False
'''

from math import sqrt
 
 
class Point(object):
    """A point in 2D space.
    """
 
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
 
    def __repr__(self):
        return "Point(%r, %r)" % (self.x, self.y)
 
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
 
    def dist(self, b):
        """Distance between point A (this point) and another point B.
 
        http://en.wikipedia.org/wiki/Euclidean_distance
        """
        distance = sqrt((b.x - self.x) ** 2 + (b.y - self.y) ** 2)
        return distance
 
    def between(self, a, c):
        """Point B (this point) is between two other points A and C, if
        the distance AB added to the distance BC is equal to the
        distance AC.
 
        http://en.wikipedia.org/wiki/Line_segment
        """
        return approx_equal(self.dist(c) + self.dist(a), a.dist(c))
 
 
class Line(object):
    """A line in 2D space.
    """
 
    def __init__(self, start, end):
        self.start = start
        self.end = end
 
    def __repr__(self):
        return "Line(%r, %r)" % (self.start, self.end)
 
    def intersect(self, l2):
        """Return the intersection point P if the lines L1 and L2 intersect,
        or None if they don't.
 
        http://en.wikipedia.org/wiki/Line-line_intersection
        """
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        x3, y3 = l2.start.x, l2.start.y
        x4, y4 = l2.end.x, l2.end.y
 
        px_nom = det(det(x1, y1, x2, y2), det(x1, 1, x2, 1),
                    det(x3, y3, x4, y4), det(x3, 1, x4, 1))
        py_nom = det(det(x1, y1, x2, y2), det(y1, 1, y2, 1),
                    det(x3, y3, x4, y4), det(y3, 1, y4, 1))
 
        denom = det(det(x1, 1, x2, 1), det(y1, 1, y2, 1),
                    det(x3, 1, x4, 1), det(y3, 1, y4, 1))
 
        if denom == 0:
            # No intersection
            return None
        else:
            # Intersection
            px = px_nom / denom
            py = py_nom / denom
            return Point(px, py)
 
 
def approx_equal(a, b):
    """Test two floats for equality with a tolerance.
    """
    tolerance = 1e-14
    return abs(a - b) < tolerance
 
 
def det(a, b, c, d):
    """Determinant of a 2x2 matrix.
 
    http://en.wikipedia.org/wiki/Determinant
    """
    return a * d - b * c
 
 
def bullet_hits_wall(bullet, wall):
    """Determines if a bullet defined by a line between points A and B hits a wall
    from W1 to W2.
 
    The bullet hits the wall if:
    - lines AB and W1W2 intersect at point P
    - P lies on the wall (W1W2)
    - P lies on the ray from A trough B
 
    Edge case: Bullet ray hitting W1W2 straight on
    """
    # Cover bullet hitting one of the end points of the wall straight on
    if bullet.end.between(bullet.start, wall.start) or \
       bullet.end.between(bullet.start, wall.end):
        return True
 
    # Determine intersection point
    p = bullet.intersect(wall)
    print "P: %r" % p
    if p is not None:
        on_wall = p.between(wall.start, wall.end)
        on_bullet_ray = bullet.end.between(bullet.start, p) or \
                        p.between(bullet.start, bullet.end)
        return on_wall and on_bullet_ray
    return False
 
 
def checkio(data):
    w1, w2, a, b = data
    w1 = Point(w1[0], w1[1])
    w2 = Point(w2[0], w2[1])
    a = Point(a[0], a[1])
    b = Point(b[0], b[1])
    bullet = Line(a, b)
    wall = Line(w1, w2)
    print "Bullet: %s" % bullet
    print "Wall:   %s" % wall
    hit = bullet_hits_wall(bullet, wall)
    print hit and "Hit!" or "Miss!"
    print
    return hit
  

#print checkio([[0,0], [0,2], [5,1], [3,1]])
print checkio([[0, 0], [0, 2], [3, 1], [5, 1]])
#print checkio([[0, 0], [2, 2], [6, 0], [3, 1]])
#print checkio([[6, 0], [5, 5], [4, 0], [5, 6]])
#print checkio([[0, 0], [1, 1], [3, 3], [2, 2]])
#print checkio([[0, 0], [1, 1], [3, 2], [2, 1]])