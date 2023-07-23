import numpy as np
import math as m


def main(radius, step, amplitude, bulge = 0, layerheight = .2):

	count = int(radius/step)
	count = count + count%4 + 1
	if ((count-1)/4) % 2 == 1:
		print("adjust")
		count = count + 4
	contours = []

	for n in range(10):

		pt = []
		pts = []

		amp = amplitude

		for i in range(count):
			
			pt = np.array([m.cos(2 * m.pi * i/(count-1)), m.sin(2 * m.pi * i/(count-1)), 0])
			nxt = np.array([m.cos(2 * m.pi * (i+1)/(count-1)), m.sin(2 * m.pi * (i+1)/(count-1)), 0])
			prev = np.array([m.cos(2 * m.pi * (i-1)/(count-1)), m.sin(2 * m.pi * (i-1)/(count-1)), 0])
			
			if i%4 == 0:
				amp = -amp
				r = radius
				pt = pt*r
			elif i%4 == 1:
				r = radius + amp/2
				tan = prev - pt
				pt = pt*r + tan/np.linalg.norm(tan)*bulge 
			elif i%4 == 2:
				r = radius + amp
				pt = pt*r
			elif i%4 == 3:
				r = radius + amp/2
				tan = nxt - pt
				pt = pt*r + tan/np.linalg.norm(tan)*bulge

			pt[2] = n*layerheight
			pts.append(list(pt))

		contours.append(pts)


	f = open("output.csv", "w")

	for n in range(len(contours)):
		for i in range(len(contours[n])):
			pt = contours[n][i]
			f.write(str(pt[0]) + " " + str(pt[1]) + " " + str(pt[2]))
			if i < len(contours[n]) - 1:
				f.write(",")
		if n < len(contours) - 1:
			f.write("\n")

	f.close()


main(100, .2, 2, bulge = 2)