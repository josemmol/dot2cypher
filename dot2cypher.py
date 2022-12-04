#!/home/jmmol/anaconda3/envs/my_env/bin/python
##############################################################################

##############################################################################
# PYTHON CODE BEGINS HERE

import os
import sys
import errno
import getopts
import pydot


##############################################################################
# GLOBALS

SCRIPTNAME = os.path.basename(__file__)

class opts:
    files = []
    output = ""
    input= ""
    help = False


##############################################################################
# USAGE

def usage():
    """\
Usage: {SCRIPTNAME} [option] [file]
Example script to show how to use object-oriented getopts.py.
Options:
  -i <file>, --input-dot=<file>    Input dot file
  -o <file>, --output-cypher=<file>   Output cypher file
  -h, --help                   Show help screen (this screen)
"""

    print(usage.__doc__.format(**globals()))

##############################################################################
# dot2cypher
def dot2cypher(dotfile,cypherfile):
	graphs = pydot.graph_from_dot_file(dotfile)
	graph = graphs[0]

	f= open(cypherfile,"w+")
	f.write('CREATE \r\n')
	for n in graph.get_nodes():
		print(n.get_name(),n.get_label())
		f.write('(n'+n.get_name().strip('"').replace('-','')+': python_package {name:\''+n.get_name()+'\'}),\r\n')
	for e in graph.get_edge_list():
		print("origen: ",e.get_source())
		print("desti: ",e.get_destination())
		f.write('(n'+e.get_source().strip('"').replace('-','')+')-[:dependency {label:\''+e.get_label()+'\'}]->(n'+e.get_destination().strip('"').replace('-','')+'),\r\n')
	f.write('\r\n')
	f.write('\r\n')
	f.close()


def main():
	ofs = sys.stdout
	errcount = 0

	getopt = getopts.getopts(sys.argv, {
		"h": 0         , "help"   : 0,
		"o": 1         , "output" : 1,
		"i": 1         , "input"  : 1
	})

	for c in getopt:
		if   c in ("-")           : opts.files.append(getopt.optarg)
		elif c in ("h", "help")   : opts.help = True
		elif c in ("o", "output-cypher") : opts.output  = getopt.optarg
		elif c in ("i", "input-dot")  : opts.input   = getopt.optarg
		else: errcount += 1

	if(errcount > 0):
		eprint("")
		eprint("Type '%s --help' for help" % sys.argv[0])
		sys.exit(1)

	# Help screen
	if(opts.help):
		usage()
		sys.exit(0)

	print ('Input dot file is "', opts.input)
	print ('Output cypher file is "', opts.output)


	if not os.path.exists(opts.input):
		eprint("")
		eprint("File %s not exist" % opts.input)
		sys.exit(1)
        
	try:
		dot2cypher(opts.input, opts.output)
	except:
		eprint("Input file is not format dot")
	
def eprint(text):
    sys.stderr.write("%s\n" % text)

if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print("")
        sys.exit(errno.EOWNERDEAD)
