import rhinoscriptsyntax as rs


def main(filename):
    f = open(filename, 'r')
    lines = f.read().split("\n")
    for i in range(len(lines)):
        pts = []
        points = lines[i].split(",")
        for j in range(len(points)):
            pt = points[j].split(" ")
            pts.append([float(pt[0]), float(pt[1]), float(pt[2])])
        rs.AddCurve(pts, 1)

main("../output.csv")