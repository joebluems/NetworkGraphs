#!/usr/bin/python

import csv
import re

file="./wiz_oz_screenplay.txt"
count=0
manual_remove=["MARVEL","ACCLAIMED BY","GROUP","ALL TOGETHER","ALL OF GROUP","... I ....","BOTH","THE THREE"]


##### detect character edges #####
edges={}
with open(file) as f:
   script = f.readlines()
   scene={}
   for row in script:
	count+=1
	#if count<100: 

        #### detect a scene & flush the previous edges ####
	if row.startswith('MLS') or row.startswith('LS') or row.startswith('ELS'):
	     if len(scene)>1:
		for i in scene:
		  for j in scene:
			pass
		  	if i!=j: print "\"%s\",\"%s\"" % (i,j)
	     scene = {}
	     
        #### identify the characters ####
	if row.startswith('	'):
	     text = re.sub(' o.s.','',re.sub('^	*','',row.strip()));
	     char=1
	     for x in text:
		if not x.isupper() and x!=' ' and x!='.': 
		  char=0
		  break
	     if char==1 and text not in manual_remove:
		if text=="AUNTIE EM": text="AUNT EM"
		if text=="PROFESSOR MARVEL": text="PROFESSOR"
		if "AND" not in text:
		   if text not in scene: scene[text]=0
		   scene[text]+=1
		else: 
		   ent = text.split(' AND ')
		   for g in ent:
		     if g not in scene: scene[g]=0
		     scene[g]+=1

