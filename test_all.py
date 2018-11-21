import os, sys
import lists

test_group = None
if len(sys.argv) > 1:
	test_group = sys.argv[1]
else:
	print ('Please provide a valid argument!')
	exit()

if test_group == 'list_comp':
	module_methods = [method for method in dir(lists) if method[0] != '_']
	
	for method_name in module_methods:
		os.system('python test.py %s' % method_name)
else:
	print ('TODO')
