import csv
import os
import sys

usage = '''For any two csv files (equal column size), remove one header, and combine them to a new csv file.

Usage: python merge_two_csv.py <file_1.csv> <file_2.csv> <out.csv>'''

def merge_two_csv(file_1, file_2, file_out):

    try:
        csv_1 = csv.reader(open(file_1))
        csv_2 = csv.reader(open(file_2))

        for line in csv_1:
            head_1 = line
            break

        for line in csv_2:
            head_2 = line
            break

        if head_1 != head_2:
            print "Error: two csv files have different columns\n"
            exit(-1)
        else:
            csvwriter = csv.writer(open(file_out, 'wb'))
            csvwriter.writerow(head_1)

            for line in csv_1:
                csvwriter.writerow(line)

            for line in csv_2:
                csvwriter.writerow(line)

            return 1

    except IOError:
        print "Error: %s %s files open error\n" %(file_1, file_2)


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print usage
        exit()
    else:
        if merge_two_csv(sys.argv[1], sys.argv[2], sys.argv[3]) == 1:
            print "Successfully merged to %s\n" %(sys.argv[3])

