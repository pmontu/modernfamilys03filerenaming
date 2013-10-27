print("modern family name changer")
import glob
filenames = glob.glob("f:/downloads/tv7/modernfamilys03/*.*")
filenames2 = ["f:/downloads/tv7/modernfamilys03/Modern.Family.S03E01.Dude Ranch",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E02.When Good Kids Go Bad",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E03.Phil on Wire",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E04.Door to Door",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E05.Hit and Run",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E06.Go Bullfrogs!",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E07.Treehouse",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E08.After the Fire",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E09.Punkin Chunkin",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E10.Express Christmas",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E11.Lifetime Supply",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E12.Egg Drop",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E13.Little Bo Bleep",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E14.Me Jealous",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E15.Aunt Mommy",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E16.Virgin Territory",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E17.Leap Day",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E18.Send Out the Clowns",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E19.Election Day",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E20.The Last Walt",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E21.Planes, Trains and Cars",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E22.Disneyland",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E23.Tableau Vivant",
"f:/downloads/tv7/modernfamilys03/Modern.Family.S03E24.Baby on Board"]
import os
i=0
print(str(len(filenames)))
while(i<24):
	ext = filenames[i][-4:]
	fr = filenames[i]
	to = filenames2[i]+ext
	print(fr+" to "+to+"\n")
	i+=1
	os.rename(fr,to)
	print("renamed "+str(i))