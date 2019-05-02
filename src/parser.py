#!/usr/bin/env python

# We can't get this script's return value
# But we can get stdout and use redirect(or pipeline)

import yaml
import subprocess
import sys

def main():
#if len(sys.argv) != 3:
#    print("usage : python parser.py assign_num student_num");
#    return -1
    assign_num = sys.argv[1]
    student_num = sys.argv[2]

# Load point information to points array.
    points = []
    with open("init.yml", 'r') as stream:
        try:
            prob_info = yaml.safe_load(stream)
            tc = prob_info['test_cases']
            for t in tc:
                points.append(t['points'])
        except yaml.YAMLError as exc:
            print(exc)

# Make parsed result of dmoj-judge
# It will print as follow 
# total_get_score / total_score
    a = subprocess.check_output(["dmoj-cli", "-c", "config.yml", "--no-ansi", "submit", assign_num, "C", "students/" + assign_num + "/" + student_num + ".c" ])
    sp = a.split()

    i = 2
    seq = 1
    total = sum(points)
    total_get = 0
    while True:
        if "Self" in sp[i]:
            i = i + 3
            continue
        if "Running" in sp[i]:
            i = i + 10
            continue
        if seq > len(points):
            break
        if int(sp[i]) == seq:
            if sp[i+1] == "AC":
                total_get = total_get + points[seq-1]
            seq = seq + 1
            i = i + 8


    print(str(total_get) + " / " +  str(total))

# I think it is better to insert data into database here

# It means that this script will be run when be executed directly 
if __name__ == '__main__':
    main()
