import six 

def return_numer_and_title(**tag_kwargs):
	title = tag_kwargs.get('title') if isinstance(tag_kwargs.get('title'),six.string_types) else ""
	number = str(tag_kwargs.get('number')) if isinstance(tag_kwargs.get('number'), int) else raise_an_exception("You must pass number argoument!")
	return (number,title)

def raise_an_exception(text):
	raise Exception(text)