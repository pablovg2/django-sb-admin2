from django.db import models

# Create your models here.
class PanelTabsTest(models.Model):
	tabname = models.CharField(max_length=30)
	tabtitle = models.CharField(max_length=100)
	content = models.TextField()
	def __str__(self):
		return "Name: '"+self.tabname+"' ,Title: '"+self.tabtitle+"'"