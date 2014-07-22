from django import template
import six
from ..html import render_tag, render_fa_icon,render_bs_icon, render_panel

register = template.Library()
loadjstoo = [False,False,False]

@register.simple_tag
def sb_admin_loadjs(flot=None,allyes=None):
	urls = []
	if flot or allyes:
		urls.append('//www.flotcharts.org/javascript/jquery.flot.min.js')
	if loadjstoo[0]:
		urls.append('//cdn.datatables.net/1.10.1/js/jquery.dataTables.js')
		urls.append('//cdn.datatables.net/plug-ins/be7019ee387/integration/bootstrap/3/dataTables.bootstrap.js')
	if loadjstoo[2]:
		urls.append('//cdn.jsdelivr.net/bootstrap.metismenu/1.1.0/js/metismenu.min.js')
	if loadjstoo[1]:
		urls.append('//cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js')
		urls.append('http://startbootstrap.com/templates/sb-admin-2/js/plugins/morris/morris.min.js')
	urls.append('http://startbootstrap.com/templates/sb-admin-2/js/sb-admin-2.js')
	scripts = []
	for url in urls:
		scripts.append('<script src="{0}"></script>'.format(url))
	return "".join(scripts)

@register.simple_tag
def sb_admin_loadcss(datatables=None,morris=None,socialbuttons=None,timeline=None,metismenu=None,allyes=None):
	urls = []
	if datatables or allyes:
		loadjstoo[0] = True
		urls.append('//cdn.datatables.net/1.10.1/css/jquery.dataTables.css')
		urls.append('//cdn.datatables.net/plug-ins/be7019ee387/integration/bootstrap/3/dataTables.bootstrap.css')
	if socialbuttons or allyes:
		urls.append('//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css')
		urls.append('http://lipis.github.io/bootstrap-social/bootstrap-social.css')
	if morris or allyes:
		loadjstoo[1] = True
		urls.append('http://cdn.oesmith.co.uk/morris-0.5.1.css')
	if metismenu or allyes:
		loadjstoo[2] = True
		urls.append('//cdn.jsdelivr.net/bootstrap.metismenu/1.1.0/css/metismenu.min.css')
	if timeline or allyes:
		urls.append('http://startbootstrap.com/templates/sb-admin-2/css/plugins/timeline.css')
	urls.append('http://startbootstrap.com/templates/sb-admin-2/css/sb-admin-2.css')

	scripts = []
	for url in urls:
		scripts.append('<link href="{0}" rel="stylesheet">'.format(url))
	return "".join(scripts)
	'''
	implementare anche l'import di css 
	'''

@register.simple_tag
def sb_panel(ptype="default",title="Default Panel",text='',footer=''):
	return render_panel(ptype,title,text,footer)

@register.simple_tag
def sb_panel_notify(content,icon,iconsize,iconmode,ptype="primary",comment="View Details",link="#"):
	icon = render_tag("div",{"class":"col-xs-3"},sb_icon(icon=icon,size=iconsize,mode=iconmode))
	content = render_tag("div",{"class":"col-xs-9 text-right"},content)
	header = render_tag("div",{"class":"row"},icon+" "+content) # don't disturb render_tag when copy-paste is enough
	comment = render_tag("span",{"class":"pull-left"},comment) + '<span class="pull-right"><i class="fa fa-arrow-circle-right"></i></span><div class="clearfix"></div>'
	footer = render_tag("a",{"href":link if isinstance(link,six.string_types) else "#"},comment)
	import pdb; pdb.set_trace()
	return sb_panel(ptype,header,None,footer)
@register.simple_tag
def sb_icon(icon,size="",fw=False,li=False,border=False,pull="",spin="",rotate="",inverse=False,stack=0,mode="fa"):
	if mode == "fa":
		return render_fa_icon(icon,size,fw,li,border,pull,spin,rotate,inverse,stack)
	elif mode == "bs":
		return render_bs_icon(icon)
	else:
		raise Exception("mode must be 'fa' or 'bs'")

