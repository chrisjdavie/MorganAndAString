'''
Hackerrank run test file

Created on 2 Jan 2016

@author: chris
'''
from src import solver

num = 'AE'
inputFname  = 'data/Input' + num + '.txt'
outputFname = 'data/Output'+ num + '.txt'

inputStrings = []
with open(inputFname,'rb') as f:
    for line in f:
        inputStrings.append(line.strip())
    
solverOutput = solver(inputStrings[1:])

for solverLine in solverOutput:
    print solverLine

# with open(outputFname,'rb') as f:
#     for testLine, solverLine in zip(f, solverOutput):
#         print testLine == solverLine
#         if testLine != solverLine:
#             print testLine
#             print solverLine
    