from django.shortcuts import render
from sb_admin2.models import PanelTabsTest
def home(request,page=""):
	paneltest = PanelTabsTest.objects.all()
	return render(request,(page if page else "index") + ".html",{"tabs":paneltest})
