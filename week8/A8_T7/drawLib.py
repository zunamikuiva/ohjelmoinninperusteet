from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon
import math

def drawSquare(PDwg: Drawing, left, top, sideLength, color, strokeColor) -> None:
    PDwg.add(Rect(insert=(int(left), int(top)),
                 size=(int(sideLength), int(sideLength)),
                 fill=color,
                 stroke=strokeColor))

def drawCircle(PDwg: Drawing, centerX, centerY, radius, color, stroke) -> None:
    PDwg.add(Circle(center=(int(centerX), int(centerY)),
                     r=int(radius),
                     fill=color,
                     stroke=stroke))

def drawHexagon(PDwg: Drawing, centerX, centerY, apothem, fill, stroke) -> None:
    circumradius = apothem / math.cos(math.radians(30))
    points = []
    angles = [30, 90, 150, 210, 270, 330]
    for angle in angles:
        rad = math.radians(angle)
        x = centerX + circumradius * math.cos(rad)
        y = centerY - circumradius * math.sin(rad) 
        points.append((round(x), round(y)))
    PDwg.add(Polygon(points=points, fill=fill, stroke=stroke))

def saveSvg(PDwg: Drawing, filename) -> None:
    svg_text = PDwg.tostring()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_text)
