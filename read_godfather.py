#!/usr/bin/python

import csv
import re

file="./godfather_screenplay.txt"
count=0
manual_remove=["THE GODFATHER","MY POSITION CANNOT AFFORD TO BE","I LOVE YOU.","OK."]

##### detect character edges #####
edges={}
with open(file) as f:
   script = f.readlines()
   scene={}
   for row in script:
	count+=1
	#if count<100: 

        #### detect a scene & flush the previous edges ####
	if row.startswith('INT') or row.startswith('EXT'):
	     if len(scene)>1:
		#print scene
		for i in scene:
		  for j in scene:
		  	if i!=j: print "\"%s\",\"%s\"" % (i,j)
	     scene = {}
	     
        #### identify the characters ####
	if row.startswith('	'):
	     text = re.sub(' \(O.S.\)','',re.sub('^	*','',row.strip()));
	     char=1
	     for x in text:
		if not x.isupper() and x!=' ' and x!='.': 
		  char=0
		  break
	     if char==1 and text not in manual_remove:
		if text not in scene: scene[text]=0
		scene[text]+=1

