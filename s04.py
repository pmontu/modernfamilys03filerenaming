import os
os.chdir("F:/Downloads/tv7/Modern Family Season 04 HDTV XviD")
import glob
fns = glob.glob("*.*")
fns.pop(24)
fns.pop(24)

fns2 = ["Bringing Up Baby",
"Schooled",
"Snip",
"The Butler's Escape",
"Open House of Horrors",
"Yard Sale",
"Arrested",
"Mistery Date",
"When a Tree Falls",
"Diamond in the Rough",
"New Year's Eve",
"Party Crasher",
"Fulgencio",
"A Slight at the Opera",
"Heart Broken",
"Bad Hair Day",
"Best Men",
"The Wow Factor",
"The Future Dunphys",
"Flip Flop",
"Career Day",
"My Hero",
"Games People Play",
"Goodnight Gracie"]

i=0
while(i<24):
	s = fns[i].split('.')
	n = "MF"+s[2]+"."+fns2[i]+".avi"
	print("renamed\n"+fns[i]+"\n"+n+"\n\n")
	os.rename(fns[i],n)
	i+=1