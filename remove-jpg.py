# the 'main' function begins here
def main():
    
    # import the necessary packages
    import argparse
    import os
    import textwrap
 
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser(prog='Remove-jpg',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\
         Info:
             If you chose to save both RAW and .JPG file in your camera both files will be copied to Lightroom storage. At this moment you 
             probably don't need these .JPG files anymore and they could be deleted safely. 

             This utility is used to remove unnecessary .JPG files from Photoshop Lightroom storage. If there are both RAW and JPG files are
             in you directory - the .JPG file will be deleted.
             
         '''))
    ap.add_argument("-w", "--WorkDir", required=False, default=os.getcwd(), help="working directory. Default - current dir")
    ap.add_argument("-r", "--R", required=False, action="store_true", help="Set this flag if you need to work recursively")
    ap.add_argument("-o", "--Raw", required=False, default=".ARW", help="Raw file type. Something lile .CR2 (Canon) or .ARW (Sony). .ARW by default")
    ap.add_argument("-d", "--Delete", required=False, action = "store_true", help="Should we really delete .JPG files. Default - no.")
    ap.add_argument("-v", "--Verbose", required=False, default = 0, action = "count", help="Add this argument to see more log and debug info. Default - no.")

    args = vars(ap.parse_args())
    # print(args)
    if args["Verbose"] > 1:
        print('DEBUG: WorkDir ', args["WorkDir"])
        print('DEBUG: Raw ', args["Raw"])
        print('DEBUG: Recurcively? ', args["R"])
        print('DEBUG: Delete? ', args["Delete"])
    
    DeleteJpgInOneFolder(args["WorkDir"], args["R"], args["Raw"], args["Delete"], args["Verbose"])

def DeleteJpgInOneFolder(WorkDir, Recursive, RawFilesExt, isDelete, Verbose):
    """
    Deletes (if isDelete is True) all the .JPG files in WorkDir directory if there are corresponding RAW files exist. 
    It works recusevely if Recursive is True.
    """
    import os

    # ok. let's check if WorkDir exists
    if not os.path.isdir(WorkDir):
        print("Err:"+WorkDir+" does not exist")
        quit(2)
    
    # the WorkDir exists let's have a list of files in the directory
    list_of_files = os.listdir(WorkDir)

    print(list_of_files)

    # for f in list_of_files:
    #    if 

if __name__ == '__main__':
    main()

