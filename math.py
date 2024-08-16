import statistics
from statistics import median
from statistics import mode
from statistics import variance
from statistics import stdev
from fractions import Fraction as fr
import scipy.stats as stats

li = [1,2,3,4,5,6,7,8,9]
#fraction
lifr = (fr(1,2),fr(3,5),fr(4,9),fr(9,8),fr(9,8))
negative_sample = (-3,-5,-7,-5,-9,-8)
negative_float_sample  = (-4.3,-5.6,-7.6,-9.6)
#mean
print("The Average/'MEAN' of list value is : ",end="")
print(statistics.mean(li))

#Harmonic Mean """The harmonic mean is a type of average, 
# a measure of the central location of the data. 
# It is often appropriate when averaging quantities which are rates or ratios, for example speeds. For example:"""
#
#Suppose an investor purchases an equal value of shares in each of three companies, 
# with P/E (price/earning) ratios of 2.5, 3 and 10. What is the average P/E ratio 
# for the investor’s portfolio?
print("The HARMONIC MEAN of the data-set is %s" %(statistics.harmonic_mean(li)))


#Median """Middle Number"""
print("MEDIAN of data-set lifr is % s" % (median(lifr)))

#Median Low """for even numbers a float""" """For odd numbers the low median out of the 2"
print("LOW MEDIAN of the data-set is % s " % (statistics.median_low(lifr)))

#Median High """for even numbers a float""" """For odd numbers the high median out of the 2"
print("HIGH MEDIAN of the data-set is %s " % (statistics.median_high(lifr)))

#Medain Grouped """Return the median of grouped continuous data, 
# calculated as the 50th percentile, using interpolation."""
print("MEDIAN GROUPED of data-set is %s" %(statistics.median_grouped(lifr)))

#Mode """Highest freqency"""
print("MODE of data-set is %s" %(mode(lifr)))

#Range ""The Differecne between the Largest data value and smalles data value
Maximum = max(lifr)
Minimum = min(lifr)
Range = Maximum-Minimum
print("MAXIMUM = {}, MINIMUM = {} and RANGE = {}".format(Maximum, Minimum, Range))

#Variance """The average squared deviation from the mean"
"""It is defined as an average squared deviation from the mean.
It is calculated by finding the difference between every data point and 
the averagewhich is also known as the mean, squaring them, adding all of them, and 
then dividing by the number of data points present in our data set."""
print("VARIANCE of data-set is %s " % (variance(lifr)))

#Standard Deviation
"""It is defined as the square root of the variance. It is calculated by finding the Mean, 
then subtracting each number from the Mean which is also known as the average, and squaring the result. 
Adding all the values and then dividing by the no of terms followed by the square root."""
print("The STANDAR DEVIATION of data-set is %s " % (stdev(lifr)))

#Population Variance """Used to calculate population variance of data"
print("The POPULATION VARIANCE of data is: ",end="")
print(statistics.pvariance(lifr))

#zscore - The z-score is a score that measures how many standard deviations a data point is away 
# from the mean. 
# The z-score allows us to determine how usual or unusual a data point is in a distribution. 

lifr_floats = [float(f) for f in lifr]

zscores = stats.zscore(lifr_floats)
print('Here are the zscores %s' %(zscores))