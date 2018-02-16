import sys, os
import urllib

CWD = os.getcwd()       # Current user's work directory

def get_imm():
  if not os.path.isfile(CWD+"/imm.py"):
    print "Download imm to {}".format(CWD)
    imm_file = urllib.URLopener()
    imm_file.retrieve("https://raw.githubusercontent.com/rmilovanov/imm/master/imm.py", CWD+"/imm.py")
  else:
    print "Imm already exists"

def main():
  get_imm()


if __name__ == '__main__':
  main()
