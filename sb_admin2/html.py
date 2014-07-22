import six

def render_tag(tag="div",attrs="",content=""):
	
	if not isinstance(attrs,dict) and not None:
		raise Exception("The attrs parameter is not a dictionary " + str(attrs))
	attributes = ""
	for key in attrs:
		attributes += str(key)+'="{0}"'.format(attrs[key])
	tag = tag if isinstance(tag,six.string_types) else ""
	content = content if isinstance(content,six.string_types) else ""
	return '<{tag} {attrs}> {content} </{tag}>'.format(
		tag=tag,
		attrs=attributes,
		content=content
		)
	
def render_panel(ptype="default",title="Default Panel",text='',footer=''):
	if not isinstance(ptype,six.string_types):
		raise TemplateSyntaxError("You must pass a string to type parameter!")
	header = render_tag("div",{"class":"panel-heading"},title if isinstance(title,six.string_types) else "")
	
	content = render_tag(attrs={"class":"panel-body"},content=text if isinstance(text,six.string_types) else "")
	pfooter = render_tag(attrs={"class":"panel-footer"},content=footer if isinstance(footer,six.string_types) else "")
	return render_tag(attrs={"class":"panel panel-{0}".format(ptype)},content=" ".join((header,content if text != None else "",pfooter)))

def render_fa_icon(icon,size="",fw=False,li=False,border=False,pull="",spin="",rotate="",inverse=False,stack=0):
	if not isinstance(icon,six.string_types):
		raise Exception("icon must be a string")
	attribute = "fa fa-{0} ".format(icon)
	attribute += "fa-{0}x ".format(size) if size else "" + "fa-fw " if fw else "" + "fa-li " if li  else "" + "fa-border " if border else ""  + "pull-{0} ".format(pull) if pull else ""  + "fa-spin " if spin  else ""  + "fa-inverse " if inverse  else "" 
	
	if rotate.isnumeric and rotate:
		attribute += "fa-rotate-"+str(rotate)
		
	elif isinstance(rotate,six.string_types) and rotate:
		attribute += "fa-flip-"+rotate

	if stack > 0 and stack < 3:
		attribute += "fa-stack-{0}x".format(stack)

	return render_tag("i",{"class":attribute},"")

def render_bs_icon(icon):
	if not isinstance(icon,six.string_types):
		raise Exception("icon must be a string")
	import pdb; pdb.set_trace() 
	return render_tag("span",{"class":"glyphicon glyphicon-{0}".format(icon)},"")