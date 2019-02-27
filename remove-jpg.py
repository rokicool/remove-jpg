# the 'main' function begins here
def main(WorkDir, Raw, R):
    print 'DEBUG: WorkDir', WorkDir
    print 'DEBUG: Raw', Raw
    print 'DEBUG: Recurcively?', R
    
# import the necessary packages
import argparse
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-w", "--WorkDir", required=True, help="working directory. Default - current dir")
ap.add_argument("-r", "--R", required=False, action="store_true", help="Set this flag if you need to work recursively")

ap.add_argument("-o", "--Raw", required=False, default=".ARW", help="Raw file type. Something lile .CR2 (Canon) or .ARW (Sony). .ARW by default")

args = vars(ap.parse_args())
print dir(args)

if __name__ == '__main__':
    main(args["WorkDir"], args["Raw"], args["r"])


# display a friendly message to the user
print("Working directory is {}!".format(args["WorkDir"]))

