from django.http import HttpResponse

import os
import sys
import commands
import urllib
import ftplib
import io

#urllib.urlretrieve('ftp://username:password@server/path/to/file', 'file')
#urllib.urlretrieve('ftp://username:password@server/path/to/file', 'file')
#urllib.urlretrieve('ftp://username:password@server/path/to/file', 'file')
#urllib.urlretrieve('ftp://username:password@server/path/to/file', 'file')
#urllib.urlretrieve('ftp://username:password@server/path/to/file', 'file')
#urllib.urlretrieve('ftp://username:password@server/path/to/file', 'file')

def index(request):
    x = str(request.GET['x'])
    ret = urllib.urlopen('ftp://'+un+':'+pw+'@ftp.freecluster.eu/htdocs/id/'+x+'/cmd.txt').read()
    return HttpResponse(ret)
def save(request):
    x = str(request.GET['x'])
    c = str(request.GET['c'])
    session = ftplib.FTP('ftp.freecluster.eu',un,pw)
    session.storbinary('STOR /htdocs/id/'+x+'/cmd.txt',io.BytesIO(c))
    session.quit()
    return HttpResponse()
