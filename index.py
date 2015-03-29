

# variable that stores all entered keywords into a list.
keywords = []

# allows the user to enter a keyword 
def enter_keyword(keyword):
	keyword_list = keywords
	keyword_list.append(keyword)
	print "Keyword List"
	print keyword_list
	print "Enter the definition:"
	enter_defintion(raw_input('> '))

# variable that stores all entered defintions into a list.
definitions = []

# allows the user to enter the definition for the term.
def enter_defintion(definition):
	definition_list = definitions
	definition_list.append(definition)
	print "Definition List"
	print definition_list
	print "Enter an example:"
	enter_example(raw_input('> '))

# variable that stores all entered definitions into a list.
examples = []

# allows the user to enter an example for the term.
def enter_example(example):
	example_list = examples
	example_list.append(example)
	print "Example List"
	print example_list
	start()

#def printing everything in order

# this starts the entry.
def start():
	# enter a term?
	print "Do you want to enter a term?"

	choice = raw_input('> ')
	if choice == 'yes':
		print "Please enter your term:"
		enter_keyword(raw_input('> '))
	elif choice == 'no':
		print "Keywords"
		print keywords
		print "Definitions"
		print definitions
		print "Examples"
		print examples
	else:
		print "ok thank you anyway"

start()
	



