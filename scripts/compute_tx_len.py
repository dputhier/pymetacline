transcriptStart = dict()
transcriptEnd = dict()

import re

fileHandler = open("../pymetacline/data/gtf/simple.gtf", "r")

for line in fileHandler:
    Token = line.split("\t")  
    start = int(Token[3]) # le début de l'élément courant
    end = int(Token[4]) # la fin de l'élément courant
    # L'identifiant du transcrit
    txID = re.search('transcript_id "([^"]+)"', Token[8]).group(1)

    if txID not in transcriptStart:

        transcriptStart[txID] = start
        transcriptEnd[txID] = end

    else:
        if start < transcriptStart[txID]: 

            transcriptStart[txID] = start

        if end > transcriptEnd[txID]:

            transcriptEnd[txID] = end

            
for txID in transcriptStart:

    print(txID + "\t" + str(transcriptEnd[txID] - transcriptStart[txID] + 1))
