import sys, getopt
sys.path.append('../')
from config import *
sys.path.append('lib/attack/')
from exportfile import *
sys.path.append('lib/crawler/')
from  gethref import *
from  getdata import *
from phpaccept import *
from urlparse import urlparse
sys.path.append('lib/attack/')
from makelinkattack import *
sys.path.append('lib/attack/')
from makelinkquery import *
from xacdinhfilename import *
sys.path.append('lib/scan/')
from scan import *
sys.path.append('controller/')
from attackController import *
def main(argv):
   
   try:
      opts, args = getopt.getopt(argv,"u:h")
   except getopt.GetoptError:
      print '-h for help'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print "-u: URL with GET parameter = a file you know"
         print "example: http://localhost/test/?file=abc.php"
         sys.exit()
         
      elif opt == '-u':
        attackController(arg)
      
   
banner="\n\n\n\n\n\n\n\n\n                            LFISCANNER\nAuthor: truongtn \na.k.a truongpro\nHome:http://truongtn.wordpress.com\n\n\n\n\n"


                                                             
                                                             


print banner
if __name__ == "__main__":
   main(sys.argv[1:])
