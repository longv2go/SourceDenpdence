#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os
import os.path

rootdir = "."

for dirpath, dirnames, filenames in os.walk(rootdir):
	for dirname in dirnames:
		print "dirpath: " + dirpath
		print "dirname: " + dirname

	for filename in filenames:
		print "dirpath: " + dirpath
		print "full path: " + os.path.join(dirpath, filename)

