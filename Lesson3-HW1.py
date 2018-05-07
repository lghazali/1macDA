import math
from statistics import pvariance, pstdev, mean, median, mode
import statistics


l = [15, 4, 3, 8, 15, 22, 7, 9, 2, 3, 3, 12, 6]


l.sort()
n = len(l)
lmedian = median(l)
q1 = median(l[:6])
q3 = median(l[7:])
lmean = mean(l)
lmode = mode(l)
iqr = q3 - q1
lrange = l[len(l)-1]-l[0]
lvariance = pvariance(l)
lstdev = pstdev(l)
lmin = min(l)
lmax = max(l)


print("Ordered Values: " + str(l))
print("n: " + str(n))
print("Median: " + str(lmedian))
print("Q1: " + str(q1))
print("Q3: " + str(q3))
print("Mean: " + str(lmean))
print("Mode: " + str(lmode))
print("IQR: " + str(iqr))
print("Range: " + str(lrange))
print("Variance: " + str(lvariance))
print("Standard Deviation: " + str(lstdev))
print("Minimum: " + str(lmin))
print("Maximum: " + str(lmax))
