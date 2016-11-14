import os
import glob
import re

def parse_all_files(resultVar):
    for filename in glob.iglob('*.txt'):

        with open(filename, "r") as handler:  
            for line in handler:
    
                if resultVar in line.lower():

                    digits = re.findall(r'\d', line)
                    result = ''.join(digits)

                    strategy, num, arena, seed = os.path.basename(filename).split('_')

                    yield dict(strategy=strategy, num=num, arena=arena, seed=seed, result=int(result))

def build_dict_sorted(field, resultVar):
   parsed_dict = parse_all_files(resultVar)
   return sorted(parsed_dict, key=lambda k: k[field])
   
def printFinalResultForField(field, resultVar):
    dictList = build_dict_sorted(field, resultVar)
    
    finalDict = {}
    finalDictList = []
    count = 0
    
    for d in dictList:
        if not finalDict:
            finalDict[field] = d[field]
    
        if resultVar in finalDict:
            if d[field] == finalDict[field]:
                count = count + 1
                finalDict[resultVar] = int(finalDict[resultVar]) + int(d[resultVar])
            else:
                finalDict['average'] = round(float(finalDict[resultVar]) / float(count), 2)
                finalDictList.append(finalDict)
                count = 1
                finalDict = {}
                finalDict[field] = d[field]
                finalDict[resultVar] = int(d[resultVar])
        else:
            count = count + 1
            finalDict[resultVar] = int(d[resultVar])
    finalDict['average'] = round(float(finalDict[resultVar]) / float(count), 2)
    finalDictList.append(finalDict)
    print(finalDictList)
    
printFinalResultForField('arena', 'result')
printFinalResultForField('strategy', 'result')