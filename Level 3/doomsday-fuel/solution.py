from __future__ import division
import numpy as np
import fractions
def convertMatrix(transMatrix):
    probMatrix = []

    for i in range(len(transMatrix)):
        row = transMatrix[i]
        newRow = []
        rowSum = sum(row)

        if all([v == 0 for v in row]):
            for j in row:
                newRow.append(0)
            newRow[i] = 1
            probMatrix.append(newRow)

        else:
            for j in row:
                if j == 0:
                    newRow.append(0)
                else:
                    newRow.append(float(j/rowSum))
            probMatrix.append(newRow)
    return probMatrix

def terminalStateFilter(matrix):
    terminalStates = []

    for row in range(len(matrix)):

        if all(x == 0 for x in matrix[row]):
            terminalStates.append(True)

        else:
            terminalStates.append(False)
            
    return terminalStates

def orderMatrix(probMatrix,terminalStates):
    I_list = []
    newMatrix = []
    for i,item in enumerate(terminalStates):
        if item == True:
            newMatrix.append(probMatrix[i])
            I_list.append(i)
    for i in range(len(probMatrix)):
        if i not in I_list:
            newMatrix.append(probMatrix[i])
            
    latestMatrix = []        
    for i,col in enumerate(zip(*newMatrix)):
        if i in I_list:
            latestMatrix.append(col)
            
    for i,col in enumerate(zip(*newMatrix)):
        if i not in I_list:
            latestMatrix.append(col)
            
    orderedMatrix = [[latestMatrix[j][i] for j in range(len(latestMatrix))] for i in range(len(latestMatrix[0]))]
    return orderedMatrix

def getRQ(orderedMatrix,count):    
    a = np.array(orderedMatrix)
    I = np.matrix(a[:count,:count])
    R = np.matrix(a[count:,:count])
    Q = np.matrix(a[count:,count:])
    
    return I,R,Q

def calculateF(Q):
    I = np.identity(len(Q))
    
    I = np.array(I)
    Q = np.array(Q)
    
    I = np.subtract(I,Q)
    
    F = np.linalg.inv(I)
    
    return F
    
    
    
def solution(m):

    if len(m) == 1:
        return [1, 1]

    probMatrix = convertMatrix(m)  
    terminalStates = terminalStateFilter(m)
    orderedMatrix = orderMatrix(probMatrix,terminalStates)
    count = terminalStates.count(True)
    I,R,Q = getRQ(orderedMatrix,count)
    F = calculateF(Q)
    FR = np.dot(F,R)
    FR = np.array(FR)
    a = list(FR[0])
    
    numerators = []
    for i in a:
            numerator = fractions.Fraction(float(i)).limit_denominator().numerator
            numerators.append(numerator)
    
    denominators = []
    for i in a:
            denominator = fractions.Fraction(float(i)).limit_denominator().denominator
            denominators.append(denominator)
            
    factors = [np.lcm.reduce(denominators) / x for x in denominators]
    numeratorsTimesFactors = [a * b for a, b in zip(numerators, factors)]
    
    answerlist = []
    for i in numeratorsTimesFactors:
            answerlist.append(i)
    answerlist.append(np.lcm.reduce(denominators))
    
    return list(map(int, answerlist))
