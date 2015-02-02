#!/usr/bin/python2
# coding: utf-8

import mechanize
import sys
import code
import MechanizedPython

class nav:
	"""Class nav
		Providing a static mechanize.Browser object
	"""
	
	""" Static Browser """
	br=mechanize.Browser()
	
	"""Local test page"""
	test="http://127.0.0.1/form.php"

def usage():
	"""Help for the user"""
	print("""You could have a look to :
		help(nav)
		help(open) 
		help(listInfos)
			help(displayForms)
			help(listLinks)

		_____ optional _____
		help(listForms)
		help(listControls)
		help(printControlInfo)

		_____ comprehensive documentation  ____
		help(MechanizedPython) for all infos
		""")

def open(url, data=None, timeout=10):
	"""Open an url with the nav static browser"""
	res=nav.br.open(url,data,timeout)


def printControlInfo(control):
	""" print the information about a control/input"""
	print("Type : "+str(control.type)+",InputName : "+str(control.name))
	try:
		print("Value : "+str(nav.br[control.name]))
	except:
		pass
	
def _printFormInfo(form,formIndex=-1):
	"""Print Form informations"""
	if formIndex!=-1:
		print("Code to get the form : "+"list(nav.br.forms())["+str(formIndex)+"]")
	print("Form name : "+str(form.name)+", formMethod : "+str(form.method))
	
def listForms():
	"""List Forms from the visited page"""
	i=0
	for form in nav.br.forms():
		_printFormInfo(form,i)
                i+=1
		print("Form name : "+str(form.name))
		print("")

def listControls(form):
	"""List Controls/Inputs from the visited page"""
	for control in form.controls:
		printControlInfo(control)

def displayForms():
	"""Display forms infos in a page using the static Browser object, you have to call open(url) first. """
	i=0
	for form in nav.br.forms():
		_printFormInfo(form,i)
		i+=1
		nav.br.form = list(nav.br.forms())[0]
		listControls(form)
		print("")

def listLinks():
	"""Lists links form the nav.br object (current page)"""
	for link in nav.br.links():
    		print("text: '"+str(link.text)+"' -> "+str(link.url))

def getLinks():
	"""Return a list of mechanize.Links from the nav.br object (current page)"""
	listOfLinks=[]
	for link in nav.br.links():
		listOfLinks.append(link)
	return listOfLinks

def listInfos():
	""" Display usefull info for current page """
	print("==== Forms ====")
	print("")
	displayForms()
	print("==== Links ====")
	print("")
	listLinks()	

if __name__=="__main__":
	code.interact("Python "+str(sys.version_info.major)+"."+str(sys.version_info.minor)+" is running."+"Try usage() to get some useful information about this interactive script",local=locals())


