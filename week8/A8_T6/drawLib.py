from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle


def drawSquare(PDwg: Drawing, left, top, sideLength, color, strokeColor) -> None:
    rect = Rect(
        insert=(left, top),
        size=(sideLength, sideLength),
        fill=color,
        stroke=strokeColor
    )
    PDwg.add(rect)
    return None


def drawCircle(PDwg: Drawing, centerX, centerY, radius, color, stroke) -> None:
    circle = Circle(
        center=(centerX, centerY),
        r=radius,
        fill=color,
        stroke=stroke
    )
    PDwg.add(circle)
    return None


def saveSvg(PDwg, filename):
    svg_text = PDwg.tostring()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_text)
