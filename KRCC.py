import numpy as np
from scipy.stats import kendalltau
from scipy.special import comb
import math

x =  [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 5.0, 0.0, 4.0, 2.0, 3.0, 7.0, 14.0, 14.0, 25.0, 15.0, 12.0, 12.0, 12.0, 11.0, 12.0, 10.0, 14.0, 20.0, 8.0, 12.0, 30.0, 4.0, 3.0, 10.0, 10.0, 17.0, 1.0, 7.0, 11.0, 7.0, 11.0, 11.0, 6.0, 6.0, 7.0, 6.0, 8.0]
y = [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 15.0, 25.0, 1.0, 44.0, 26.0, 85.0, 82.0, 65.0, 38.0, 25.0, 9.0, 17.0, 17.0, 23.0, 24.0, 53.0, 42.0, 161.0, 117.0, 130.0, 236.0, 282.0, 411.0, 322.0, 340.0, 314.0, 271.0, 229.0, 225.0, 219.0, 165.0, 269.0, 257.0, 234.0, 242.0, 184.0, 152.0, 197.0, 153.0]

if len(x) == len(y):
    n = len(x)

    # default scipy is tau_b
    krcc = kendalltau(x, y)
    
    # https://github.com/mmhs013/pyMannKendall this also finds the tau and mann-kendall score but it doesnt do what we want
    
    print("KRCC =", krcc[0])

    # The two-sided p-value for a hypothesis test whose null hypothesis is an absence of association, tau = 0
    print("p value =", krcc[1])

else:
    print("inconsistent number of points in x and y")