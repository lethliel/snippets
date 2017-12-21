#!/usr/bin/python3

from urlgrabber import urlopen
from urlgrabber.grabber import URLGrabber
from urlgrabber.mirror import MirrorGroup

fo = urlopen('http://localhost')
data = fo.read()
print(data)

gr = URLGrabber()
mg = MirrorGroup(gr, ['http://localhost2/',
                      'http://me.myself/'])
mg.urlgrab('test.txt')
