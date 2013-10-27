import glob
import os
fn = glob.glob("*.*")
fn.pop(24)
fn.pop(24)
print(fn)
i=6
while(i<24):
	s1 = fn[i-1].split('.')
	s2 = fn[i].split('.')
	new = s1[0]+"."+s1[1]+"."+s1[2]+"."+s2[3]+"."+s1[4]
	print(fn[i-1]+" to "+new)
	os.rename(fn[i-1],new)
	i+=1
	print("renamed "+str(i)+" to "+str(i-1)+"\n")	