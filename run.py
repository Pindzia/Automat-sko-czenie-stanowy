#!/usr/bin/python2
__author__ = 'Pindzia&Piolun'

import sys
import re


def loader():
    tab = []
    end_states = []
    #with open(sys.argv[1], 'r') as ufoporno:
    for line in sys.stdin:
        same = False
        corrected = line.rstrip().split()
        if len(corrected) == 3:
            if corrected[0] != "#":
                for inc in tab:
                    if inc['x'] == corrected[0] and inc['y'] == corrected[2]:
                        if inc['var'] != corrected[1]:
                            print "NON-DETERMINISTIC"
                            return
                        else:
                            same = True
                            break
                if same:
                    continue
                else:
                    lib = {'x': corrected[0], 'var': corrected[1], 'y': corrected[2]}
                    tab += [lib]
        elif len(corrected) == 1:
            end_states += corrected
    with open(sys.argv[1], 'r') as examples:
        for word in examples:
            corrected = word.rstrip()
            status = "0"
            iterator = 0
            #fit = False
            for symbol in corrected:
                iterator = iterator + 1
                fit = False
                for inc in tab:
                    if inc['y'] == symbol and inc['x'] == status:
                        #print "WESZLEM!"
                        status = inc['var']
                        fit = True
                        break
                if not fit:
                    break
            var_yes = False
            for st in end_states:
                if len(corrected) == iterator and st == status and fit == True:
                    var_yes = True
            if var_yes:
                print "YES" + " " + corrected
            else:
                print "NO" + " " + corrected

loader()
