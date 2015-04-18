import sys, getopt

def main(argv):
   
   try:
      opts, args = getopt.getopt(argv,"ao:hbg")
   except getopt.GetoptError:
      print '-h for help'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print "-a: Automatic detect & exploit mode"
         print "-m: Manual exploit
         sys.exit()
         
      elif opt == '-b':
         print 'Day la huong dan'
      elif opt == '-a':
         print 'Day la huong dan1'
      elif opt == '-g':
         print 'Day la huong dan2'
        
      
   
banner ="day la banner :v"
print banner
if __name__ == "__main__":
   main(sys.argv[1:])
