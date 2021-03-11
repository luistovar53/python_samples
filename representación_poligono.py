from shapely.geometry import Point, Polygon
import roboticaaerea as ra

p1 = (1, 0)
p2 = (0, 2)
p3 = (-1, 0)

poli = Polygon([p1, p2, p3])

ra.plotPolygons([poli])
