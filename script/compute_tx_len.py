'''
This program computes the transcript genomic length (i.e exon + intron). Develop with Python 3.

Author: M2 Bioinfo, AMU
Usage:
  $ python compute_tx_len.py
'''


import re

def write_tx_genomic_len(input_file):
    '''
    This functions takes a GTF file as input,
    computes transcript genomic sizes and write the result to
    STDOUT.
    '''

    # These dictionnaries will store
    # the most 5' and most 3' exon coordinates (values)
    # for each transcript (key).
    tx_starts = dict()
    tx_ends = dict()

    file_handler = open(input_file)

    for line in file_handler:
        token = line.split("\t")
        start = int(token[3])
        end = int(token[4])
        tx_id = re.search('transcript_id "([^"]+)"', token[8]).group(1)

        if tx_id not in tx_starts:

            tx_starts[tx_id] = start
            tx_ends[tx_id] = end

        else:
            if start < tx_starts[tx_id]:

                tx_starts[tx_id] = start

            if end > tx_ends[tx_id]:

                tx_ends[tx_id] = end

    for tx_id in tx_starts:
        genomic_len = tx_ends[tx_id] - tx_starts[tx_id] + 1
        print(tx_id + "\t" + str(genomic_len))

if __name__ == '__main__':
    write_tx_genomic_len("../gtf/simple.gtf")
