
I love taking pictures with my Sony A7RIII. It is an awesome camera. But. If you want to share the picture out of it wirelessly you need to have jpg file. On the other hand I definitely use RAW files in any other case. And when I import the photos to lightroom it takes both of the files - jpg and raw one. I have found that I spent something about 10-15% of my storage to sotore the unnecessary jpg files!

The main idea

The script checks the directory and finds all the jpg files which have corresponding raw files and only then deletes them! Recursively. 

 
Usage: Remove-jpg [-h] [-w WORKDIR] [-r] [-o RAW] [-d] [-v]

Optional arguments:
  -h, --help            show this help message and exit
  -w WORKDIR, --WorkDir WORKDIR
                        working directory. Default - current dir
  -r, --R               Set this flag if you need to work recursively
  -o RAW, --Raw RAW     Raw file type. Something lile .CR2 (Canon) or .ARW(Sony). .ARW by default
  -d, --Delete          Should we really delete .JPG files. Default - no.
  -v, --Verbose         Add this argument to see more log and debug info. Default - no.