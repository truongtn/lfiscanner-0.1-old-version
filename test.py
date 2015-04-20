import getopt
import sys



print 'ARGV      :', sys.argv[1:]

options, remainder = getopt.getopt(sys.argv[1:], 'o:v')


for opt, arg in options:
    if opt in ('-o', '--output'):
        print arg





