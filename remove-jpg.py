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
    
    size_of_deleted, count_of_deleted = DeleteJpgInOneFolder(args["WorkDir"], args["R"], args["Raw"], args["Delete"], args["Verbose"])

    if args["Verbose"] > 0:
        if args["Delete"]:
            print("We deleted " + str(count_of_deleted) + " files. " + str(size_of_deleted / 1024 / 1024) + " Mb freed.")
        else:
            print("We are supposed to delete " + str(count_of_deleted) + " files. To free " + str(size_of_deleted / 1024 / 1024) + " Mb.")
        



def DeleteJpgInOneFolder(WorkDir, Recursive, RawFilesExt, isDelete, Verbose):
    """
    Deletes (if isDelete is True) all the .JPG files in WorkDir directory if there are corresponding RAW files exist. 
    It works recusevely if Recursive is True.

    Returns sum of sizes of deleted files
    """
    import os

    # ok. let's check if WorkDir exists
    if not os.path.isdir(WorkDir):
        print("Err:"+WorkDir+" does not exist")
        quit(2)
    
    local_size_of_deleted = 0
    local_count_of_deleted = 0
    local_files_to_be_removed = []
    
    # the WorkDir exists let's have a list of files in the directory
    list_of_files = os.listdir(WorkDir)

    if Verbose > 2: print("DEB: list of files to delete - ", list_of_files)

    for f in list_of_files: 
        if os.path.isdir(os.path.join(WorkDir,f)) and Recursive:
            temp_size_of_deleted, temp_count_of_deleted = DeleteJpgInOneFolder(
                os.path.join(WorkDir, f), Recursive, RawFilesExt, isDelete, Verbose)

            local_size_of_deleted += temp_size_of_deleted
            local_count_of_deleted += temp_count_of_deleted

        else:
            # f - not a folder. lets check if is has a .jpg extention
            temp_name, temp_ext = os.path.splitext(f)
            if Verbose > 2:
                print ("DEB: ext - " + temp_ext)
            if temp_ext.upper() in [".JPG", ".JPEG"]:
                # ok. this .jpg file is a possible candidate to be removed
                # let's check if there is a corresponding RAW file in the dir

                if Verbose > 2:
                    print("DEB: join temp_name + RawFilesExt - ", os.path.join(WorkDir, temp_name + RawFilesExt))

                if os.path.exists(os.path.join(WorkDir, temp_name + RawFilesExt)):
                    # looks like we have a pair JPG and RAW file
                    # add this file name to list of files to be deleted to deal with them later
                    local_files_to_be_removed.append(f)
    
    if Verbose > 2:
        print("DEB: list of files to be removed: ", local_files_to_be_removed)

    # now we have a list of files to be removed located in the list 'local_files_to_be_removed'
    # lest go though the list and try to remove these files from the WorkDir
    for f in local_files_to_be_removed:
        # before deleting the file let's get it's info for our statistics
        temp_file_name = os.path.join(WorkDir, f)
        temp_file_size = os.path.getsize(temp_file_name)
        try:
            if isDelete:
                os.remove(temp_file_name)
            
            if Verbose > 1:
                print("deleted - ", temp_file_name)
            
            local_size_of_deleted += temp_file_size
            local_count_of_deleted += 1
        except OSError as myerror:
            print("Err: could not delete " + temp_file_name)
    
    return local_size_of_deleted, local_count_of_deleted


if __name__ == '__main__':
    main()

