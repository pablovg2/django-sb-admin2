import six 

def return_numer_and_title(**tag_kwargs):
	title = tag_kwargs.get('title') if isinstance(tag_kwargs.get('title'),six.string_types) else ""
	number = str(tag_kwargs.get('number')) if isinstance(tag_kwargs.get('number'), int) else raise_an_exception("You must pass number argoument!")
	return (number,title)

def raise_an_exception(text):
	raise Exception(text)

def not_blank_and_string(variable,key="variable"):
	if not variable or not isinstance(variable,six.string_types):
		raise_an_exception(key+" must be a string and not blank")
	else:
		return variable