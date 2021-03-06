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

class webForm:
    """ Custom Form class
        Build to store extracted values of a http form """
    def __init__(self,method="POST",name=None):
        """ Constructor
            <str> method Method used by the form
            <str> name Name attribute of the form """
        self.method=method
        self.name=name
        self.controls=[]
    def __str__(self):
        """ String builder for this class"""
        return "Form name : "+str(self.name)+", formMethod : "+str(self.method)+" Inputs :"+str(self.controls)
    def __repr__(self):	
        """ Printed when you interact with an instance of this class"""
        return self.__str__()
    def show(self):
        """ Print a nice description of the form"""
        print("Form name : "+str(self.name)+", formMethod : "+str(self.method))
        for webCtrl in self.controls:
            print("* "+str(webCtrl))
    def addControl(self,Control):
        """ Add a webControl to the controls list member
            <webControl> Control Instance of a webControl class"""
        self.controls.append(Control)

class webControl:
    """ Custom Control/Input class
        Build to store extracted input infos from a http form """
    def __init__(self,type="text",name=None,value=None):
        """ Constructor
            <str> type Type used of the input field
            <str> name Name attribute of the input field 
            <str> value Value attribute of the input field"""
        self.type=type
        self.name=name
        self.value=value
    def __str__(self):
        """ String builder for this class"""
        return "(Type : "+str(self.type)+") InputName : "+str(self.name)+" Value : "+str(self.value)
    def __repr__(self):
        """ Printed when you interact with an instance of this class"""
        return self.__str__()


def usage():
    """Help for the user"""
    print("""
        Maybe you should try:
            > urlOpen(myUrl)
            > listInfos()


        You could have a look to :
        help(nav) 	// Provide the nav.br mechanize browser
        help(open) 	// Open an url with the browser
        help(listInfos)	// List usefull infos
                help(displayForms)
                help(listLinks)

        _____ optional _____
        help(listForms)
        help(listControls)
        help(printControlInfo)

        _____ comprehensive documentation  ____
        help(MechanizedPython) 
        h() 			// Do the same thing

        """)

def h():
    """ Display the help for this script"""
    help(MechanizedPython)

def urlOpen(url, data=None, timeout=10):
    """Open an url with the nav static browser"""
    res=nav.br.open(url,data,timeout)

	
def printFormInfo(form,formIndex=-1):
    """Print Form informations"""
    if formIndex!=-1:
        print("Code to get the form : "+"list(nav.br.forms())["+str(formIndex)+"]")
    print form
	
def listForms():
    """List Forms from the visited page"""
    i=0
    formList=[]
    for form in nav.br.forms():
        mForm=webForm(form.method,form.name)
        formList.append(mForm)
        i+=1
        print("")
    return formList

def listControls(form):
    """List Controls/Inputs from the visited page"""
    ctrlList=[]
    for control in form.controls:
        mControl=webControl(control.type,control.name,control.value)
        ctrlList.append(mControl)
    return ctrlList

def displayForms():
    """Display forms infos in a page using the static Browser object, you have to call urlOpen(url) first. """
    i=0
    formList=[]
    for form in nav.br.forms():
        mForm=webForm(form.method,form.name)
        nav.br.form = list(nav.br.forms())[i]
        mForm.controls=listControls(form)
        formList.append(mForm)
        i+=1
        print("")
    return formList

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
    """ Main code """
    code.interact("Python "+str(sys.version_info.major)+"."+str(sys.version_info.minor)+" is running."+"Try usage() to get some useful information about this interactive script",local=locals())



