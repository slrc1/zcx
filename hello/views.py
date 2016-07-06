from django.http import HttpResponse
pw = '12345nadeen'
un = 'fceu_17699664'

import os
import sys
import commands
import urllib
import ftplib

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
