import numpy as np
from scipy.stats import kendalltau
from scipy.special import comb
import math

def krcc_test(x, y):
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

if __name__ == "__main__":
    krcc_test( [1,2.2,6,4,5,5.8,7,8,9,10,11,12,13.9,14,15,16,17,18,21,20], [1,4,3,4,5,6,9.4,8,9,11.2,11,12,13,14,3,16,17,18,19,17])