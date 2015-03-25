#!/usr/bin/python
import re

file="./darkKnight_screenplay.txt"
count=0
### a little massaging of the data specifically for this screenplay ###
manual_remove=['PULLING THE PINS.','TRAPPING THE PURPLE THREAD...','SCANNER.',
	'OFFICER RACHEL DAWES.','OFFERS HIS OWN WRISTS TO THE OFFICERS',
	'OVER A BARREL.','CORRECTIONS OFFICERS.', 'DETONATOR.','SIRENS.',
	'BEHIND HIM IS A LARGE PHOTOGRAPH OF DENT SMILING.']
bad_text=[" \(CONT'D\)"," \(O.S.\)"]

##### detect character edges #####
edges={}
with open(file) as f:
   script = f.readlines()
   scene={}
   for row in script:
	row=re.sub('</TT>.*<TT>','',row)
        count+=1

        #### detect a scene & flush the previous edges ####
	if re.match('^ *\d',row) and re.search('\d *$',row):
	  for i in scene:
	    for j in scene:
	  	if i!=j: print "\"%s\",\"%s\"" % (i,j)
	  scene = {}
	  #print "SCENE",row.rstrip()
	     
        #### identify the characters ####
	text = re.sub('^ *','',row.strip());
	for a in bad_text:
	  text = re.sub(a,'',text)
	char=1
	for x in text:
	  if not x.isupper() and x!=' ' and x!='.': 
	    char=0
	    break
	if char==1 and text not in manual_remove and len(text)>1:
	  if text not in scene: scene[text]=0
	  scene[text]+=1

