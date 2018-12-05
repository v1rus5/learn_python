import os, sys
import lists, generators, more, advanced

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

elif test_group == 'genexp':
	module_methods = [method for method in dir(generators) if method[0] != '_']

	for method_name in module_methods:
		os.system('python test.py %s' % method_name)

elif test_group == 'more':
	module_methods = [method for method in dir(more) if method[0] != '_']

	for method_name in module_methods:
		os.system('python test.py %s' % method_name)

elif test_group == 'advanced':
	module_methods = [method for method in dir(advanced) if method[0] != '_']

	for method_name in module_methods:
		os.system('python test.py %s' % method_name)

else:
	print ('TODO')
