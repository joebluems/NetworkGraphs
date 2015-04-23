#!/usr/bin/python

import csv
import re

file="./avengers_screenplay.txt"

identities={}
identities["PEPPER"]="PEPPER POTTS"
identities["BARTON"]="HAWKEYE/BARTON"
identities["CLINT BARTON"]="HAWKEYE/BARTON"
identities["HAWKEYE"]="HAWKEYE/BARTON"
identities["TONY"]="IRON MAN/TONY"
identities["IRON MAN"]="IRON MAN/TONY"
identities["NATASHA"]="BLACK WIDOW/NATASHA"
identities["BLACK WIDOW"]="BLACK WIDOW/NATASHA"
identities["BANNER"]="HULK/BANNER"
identities["HULK"]="HULK/BANNER"
identities["STEVE"]="CAPTAIN AMERICA/STEVE"
identities["CAPTAIN AMERICA"]="CAPTAIN AMERICA/STEVE"

manual_remove=["THE AVENGERS","INTERCUTS","STEVE TONY","TONY STEVE","NATASHA BANNER","MONTAGE","THE AVENGERS.",
	"I WILL NOT BE BULLIED...","PUNY GOD."]

##### detect character edges #####
edges={}
with open(file) as f:
   script = f.readlines()
   scene={}
   for row in script:

        #### detect a scene & flush the previous edges ####
	if row.startswith('INT') or row.startswith('EXT'):
	     if len(scene)>1:
		#print scene
		for i in scene:
		  for j in scene:
		  	if i!=j: print "\"%s\",\"%s\"" % (i,j)
	     scene = {}
	     
        #### identify the characters ####
	if row.startswith(' ') and "CUT TO" not in row:
	     text = re.sub(' \(V.O.\)','',re.sub(" \(CONT'D\)",'',re.sub('^	*','',row.strip())));
	     char=1
	     for x in text:
		if not x.isupper() and x not in [' ','.','#'] and not x.isdigit(): 
		  char=0
		  break
	     if char==1 and text not in manual_remove:
		if text in identities: text=identities[text]
		if text not in scene: scene[text]=0
		scene[text]+=1

