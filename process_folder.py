#!/usr/bin/env python
#

# import modules used here -- sys is a very standard one
import sys, os, argparse, logging
import imm

CWD = os.getcwd()       # Current user's work directory

# Gather our code in a main() function
def main(args):

  folder = args.folder
  output_folder = folder + "_square_preview"
  print output_folder
  if not os.path.isdir(output_folder):
    os.makedirs(output_folder)

  files = imm.get_files_names_in_folder(args.folder)
  for f in files:
    if imm.is_valid_image(folder+"/"+f):
      print "Processing {}".format(f)
      o_file = output_folder + "/" + os.path.splitext(f)[0]+ "_spw"+".jpg"
      imm.put_into_rect(folder+"/"+f, o_file, 460, 460)
      print o_file


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  parser = argparse.ArgumentParser(
                                    description = "Does a thing to some stuff.",
                                    epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
                                    fromfile_prefix_chars = '@' )
  # TODO Specify your real parameters here.
  parser.add_argument(
                      "-f",
                      "--folder",
                      help = "Folder with your materials",
                      default=CWD)
  parser.add_argument(
                      "-o",
                      "--output_folder",
                      help="increase output verbosity",
                      action="store_true")
  args = parser.parse_args()

  main(args)
