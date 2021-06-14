# when creating diatonic harmonies we can just add major or minor thirds 
# from the root and the second note. The choice of interval is simple.
# chose an interval that keeps you in the parent scale. 
# For example C D E F G A B is the Cmaj Scale. The ii chord is Dmin
# A minor 3rd brings us to F and a major 3rd brings us to A 

import scale_modules as sm
import turtle
import random 
import math

def draw_board(fret,string_lable,FONT_NOTES):
	fret.speed(200)
	# creating board outline 
	for i in range(2):
		fret.forward(150)
		fret.right(90)
		fret.forward(200)
		fret.right(90)

	# creating frets
	for i in range(4):
		fret.goto(0,-40*(i+1))
		fret.pendown()
		fret.forward(150)
		fret.penup()

	fret.penup()
	fret.goto(0,0)
	fret.right(90)

	# creatong strings 
	for i in range(4):
		fret.goto(30*(i+1),0)
		fret.pendown()
		fret.forward(200)
		fret.penup()
	
	# labeling strings

	letters = ['E','A','D','G','B','E']
	for i in range(len(letters)):
		string_lable.penup()
		string_lable.goto(30*i,40)
		string_lable.write(letters[i],font = FONT_NOTES)


# unix pipelines
def INSTRUCTIONS():
	print("<< THE SCALE CONSTRUCTOR PROGRAM >>\n")
	print("USER INPUT HELP")
	print("---------------\n")
	print("<<<< Aspects of program >>>>\n")
	print("ASPECT 1")
	print("--------\n")
	print("Aspect 1 allows you to build a scale, and chord, then harmonize the scale.\n")
	print("HOW TO USE ASPECT 1")
	print("-------------------\n")
	print("Aspect 1 will progmpt you for a scale type. Its important to check your spelling.")
	print("Then it will prompt you for a specific note to build a scale around.")
	print("Then it will prompt you for a note to build a cord around.\n")
	print("LIST OF SCALE TYPES")
	print("-------------------\n")
	print("Major, Minor, Dorian, Phyrgian, Lydian, Mixolydian, Locrian, Pentatonic(M),Pentatonic(m)\n")
	print("------------------------------------------------------------------------------------------")
	print("------------------------------------------------------------------------------------------\n")
	print("ASPECT 2")
	print("--------\n")
	print("Aspect 2 of the program builds a visual representation of chord on a fretboard diagram.\n")
	print("HOW to USE ASPECT 2")
	print("-------------------\n")
	print("Aspect 2 will prompt you for a note to build your visual chord around")
	print("Then aspect 2 will guide you through chosing your desired chord position and version (if available)\n")
	print("ENJOY :):)\n")


	print("INFO FOR ASPECT 1")
	print("Replacement Scales\n")
	print("---> = use \n")
	print("D#(maj) ---> Eb(maj) ")
	print("A#(maj) ---> Bb(maj) ")
	print("G#(maj) ---> Ab(maj) ")
	print("C#(maj) ---> Db(maj) ")
	print("\n")
	print("INFO FOR ASPECT 2")
	print("Visual chords available\n")
	print("-----------------------")
	print("Visual chords are only available in major variations\n")
	print("Chords available: C, D , E , F, G ")

# scale choice 
def get_scale_type():
	s_types = ['Major','Minor','Dorian','Phyrgian','Lydian','Mixolydian','Locrian','Pentatonic(M)','Pentatonic(m)']
	scale_type = 0
	while True:
		scale_type = input("Please enter choice for scale type: ")
		print("\n")
		if scale_type in s_types:
			break
		else:
			print("Not a valid scale type\n")

	return scale_type

# getting key for scale construction 
def get_key(mj,mn):
	key = ' '
	while True:
		key = input("Please enter key to start with: ")
		print("\n")
		if key in mj or key  in mn:
			break
		else:
			print("Not a valid key\n")

	return key
# getting key for chord construction 
def get_key_2(mj,mn):
	key_2 = ' '
	while True:
		key_2 = input("Please enter tonic note for chord: ")
		print("\n")
		if key_2 in mj or key_2 in mn:
			break
		else:
			print("Not a valid choice\n")

	return key_2

def get_key_3(mj,mn):
	while True:
		key_3 = input("Please Enter note to build chord around: ")
		if key_3 in mj or key_3 in mn:
			break
		else:
			print("Not a valid choice\n")

	return key_3

# formatting scale output 
def format_scale(scale_type,scale_result,key):
	print("The " + key , " "+ scale_type," Scale is \n" )
	for item in scale_result:
		print(item, end = ' ')
	print("\n")

# formating chord output 
def format_chord(scale_type,chord_result,key_2):
	print( key_2 , " "+ scale_type," is \n" )
	for item in chord_result:
		print(item, end = ' ')
	print("\n")

# formatiting harmonization output
def format_harmony(key,scale_type,scale_result,harmony_triad,harmony_seventh,harmonization_order):
	print("The harmonization of the " + key, " "+ scale_type," Scale in triad chords is \n")
	ho_index = 0
	sc_index = 0

	for item in harmony_triad:
		print(scale_result[sc_index], harmonization_order[ho_index])
		ho_index += 1
		sc_index += 1
		for note in item:
			print(note, end = ' ')
		print('\n')

	print("The harmonization of the " + key, " "+ scale_type," Scale in seventh chords is \n")
	ho_index = 0
	sc_index = 0
	for item in harmony_seventh:
		print(scale_result[sc_index], harmonization_order[ho_index], "7")
		ho_index += 1
		sc_index += 1
		for note in item:
			print(note, end = ' ')
		print('\n')

# adding note(s) that arent contained in major list E#, F##, Preserves ordering 
def alt_major(key,scale_result):
	if key == 'F#':
		scale_result.remove('F')
		scale_result.insert(6,'E#')
	elif key == 'G#':
		scale_result.remove('F')
		scale_result.insert(5,'E#')
		scale_result.remove('G')
		scale_result.insert(6,'F##')

def alt_minor(key,scale_result):
	if key == 'Ab':
		scale_result.remove('B')
		scale_result.insert(2,'Cb')
		scale_result.remove('E')
		scale_result.insert(5,'Fb')
	elif key == 'Eb':
		scale_result.remove('B')
		scale_result.insert(5,'Cb')

	elif key == 'D#':
		scale_result.remove('F')
		scale_result.insert(2,'E#')

# changing notes list if key selection isnt in current list major --> minor
def is_flats(key,check_flats,minor_notes):
	if key in check_flats:
		notes = minor_notes
		index_start_s = notes.index(key)
		return key

# changing notes list if key selections isnt in current list minor --> major
def is_sharps(key,check_sharps,major_notes):
	if key in check_sharps:
		notes = major_notes
		index_start_s = notes.index(key)
		return key

def get_fret(fret_pos):
	while True:
		try:
			fret = int(input("PLease enter fret position: "))
			if fret in fret_pos:
				break
			else:
				print("NOT a valid fret starting point ")
		except ValueError:
			print("Not valid type")


	return fret

		
	




def main():

	wn = turtle.Screen()
	
	# turtle for drawing fretboard
	fret = turtle.Turtle()
	fret.hideturtle()
	
	# turtle for drawing notes on fretboard
	string_lable = turtle.Turtle()
	string_lable.hideturtle()
	string_lable.color('black')
	FONTSIZE_N = 16
	FONT_NOTES = ('Arial', FONTSIZE_N, 'normal')
	letters = ['e','A','D','G','B','E']
	

	# turtle for drawing note positions
	dot = turtle.Turtle()
	dot.hideturtle()

	# turtle for drawing barre line
	line = turtle.Turtle()
	line.pencolor('green')
	line.hideturtle()

	
	

	with open("outfile.txt") as file:
		
		members = file.readlines(); # adding each line of file to a list

		# making each element of 'members' list into a list itself; previously they were str
		major_notes = list(members[0].replace("\n","").split(',')) 
		minor_notes = list(members[1].replace("\n","").split(','))
		major = list(members[2].replace("\n","").split(','))
		minor = list(members[3].replace("\n","").split(','))
		interval_maj = list(members[4].replace("\n","").split(','))
		interval_min = list(members[5].replace("\n","").split(','))

		
		
		#converting str objects in major, minor, and dorian into int objects
		sm.converter(minor,major,interval_maj,interval_min)
			
		print("\n")
		INSTRUCTIONS()
		print("\n")
		draw_board(fret,string_lable,FONT_NOTES)

	cont_0 = 'y'
	while cont_0 == 'y':
		
		# initializing nut positions
		E_pos = [(0,10)]
		A_pos = [(30,10)]
		D_pos = [(60,10)]
		G_pos = [(90,10)]
		B_pos = [(120,10)]
		e_pos = [(150,10)]
	
		pos = [E_pos,A_pos,D_pos,G_pos,B_pos,e_pos]

		# adding positions to each list
		j = 1
		for l in range(6):
			for i in range(6):
				pos[l].append(((30*l),(-20*j)))
				j+= 2
			j = 1
		
		# chord data 
		chords_major = {('C',1):[[(E_pos[0],'X'),(A_pos[3],'B'),(D_pos[2],'B'),(B_pos[1],'B'),(G_pos[0],'R'),(e_pos[0],'R')],[(E_pos[0],'X'),(A_pos[3],'B'),(D_pos[2],'B'),(G_pos[0],'R'),(B_pos[1],'B'),(e_pos[3],'B')]],
						('C',3):[[(A_pos[1],'B'),(D_pos[3],'B'),(G_pos[3],'B'),(B_pos[3],'B'),(e_pos[1],'B')]], ('C',10):[[(D_pos[1],'B'),(G_pos[3],'B'),(B_pos[4],'B'),(e_pos[3],'B')]],
						('C',8):[[(E_pos[1],'B'),(A_pos[3],'B'),(D_pos[3],'B'),(G_pos[2],'B'),(e_pos[1],'B')]],
						('C',5):[[(E_pos[4],'B'),(A_pos[3],'B'),(D_pos[1],'B'),(B_pos[1],'B'),(e_pos[4],'B')]],
						('D',1):[[(E_pos[0],'X'),(A_pos[0],'X'),(D_pos[0],'R'),(G_pos[2],'B'),(B_pos[3],'B'),(e_pos[2],'B')]],
						('D',5):[[(A_pos[1],'B'),(D_pos[3],'B'),(G_pos[3],'B'),(B_pos[3],'B'),(e_pos[1],'B')]],
						('D',10):[[(E_pos[1],'B'),(A_pos[3],'B'),(D_pos[3],'B'),(G_pos[2],'B'),(e_pos[1],'B')]],
						('D',7):[[(E_pos[4],'B'),(A_pos[3],'B'),(D_pos[1],'B'),(B_pos[1],'B'),(e_pos[4],'B')]],
						('E',1):[[(E_pos[0],'R'),(A_pos[2],'B'),(D_pos[2],'B'),(G_pos[1],'B'),(B_pos[0],'R'),(e_pos[0],'R')]],
						('E',2):[[(E_pos[0],'X'),(A_pos[0],'X'),(D_pos[1],'B'),(G_pos[3],'B'),(B_pos[4],'B',(e_pos[3],'B'))]],
						('E',4):[[(E_pos[0],'X'),(A_pos[4],'B'),(D_pos[3],'B'),(G_pos[1],'B'),(B_pos[2],'B'),(e_pos[1],'B')]],
						('E',7):[[(A_pos[1],'B'),(D_pos[3],'B'),(G_pos[3],'B'),(B_pos[3],'B'),(e_pos[1],'B')]],
						('E',12):[[(E_pos[1],'B'),(A_pos[3],'B'),(D_pos[3],'B'),(G_pos[2],'B'),(e_pos[1],'B')]],
						('F',1):[[(E_pos[1],'B'),(A_pos[3],'B'),(D_pos[3],'B'),(G_pos[2],'B'),(e_pos[1],'B')]],
						('F',3):[[(E_pos[0],'X'),(A_pos[0],'X'),(D_pos[1], 'B'),(G_pos[3],'B'),(B_pos[4],'B'),(e_pos[3],'B')]],
						('F',5):[[(E_pos[0],'X'),(A_pos[4],'B'),(D_pos[3],'B'),(G_pos[1],'B'),(B_pos[2],'B'),(e_pos[1],'B')]],
						('F',8):[[(A_pos[1],'B'),(D_pos[3],'B'),(G_pos[3],'B'),(B_pos[3],'B'),(e_pos[1],'B')]],
						('G',1):[[(E_pos[3],'B'),(A_pos[2],'B'),(D_pos[0],'R'),(G_pos[0],'R'),(B_pos[0],'R'),(e_pos[3],'B')]],
						('G',3):[[(E_pos[0],'B'),(A_pos[3],'B'),(D_pos[3],'B'),(G_pos[2],'B',),(e_pos[1],'B')]],
						('G',5):[[(E_pos[0],'X'),(A_pos[0],'X'),(D_pos[1],'B'),(G_pos[3],'B'),(B_pos[4],'B'),(e_pos[3],'B')]]}
		
		chords_minor = {'E':[[(E_pos[0],'R'),(A_pos[2],'B'),(D_pos[2],'B'),(G_pos[0],'R'),(B_pos[0],'R'),(e_pos[0],'R')]]}
		
		aspect = int(input("Enter which aspect of the program you'd like to use: "))
	  	
	  	# user choses type of scale they would like to build
		if aspect == 1: 
			cont_1 = 'y' 
			while cont_1 == 'y':
				# creating list objects for use
				scale_result = []
				chord_result = []
				harmony_triad = []
				harmony_seventh = []
				harmonization_order= ['Maj','min','min','Maj','Maj','min','dim']
				check_flats = ['Ab','Bb','Db','Eb','Gb']
				check_sharps = ['A#','C#','D#','F#','G#']
				scale_type = get_scale_type()

				if scale_type == 'Major':
					notes = major_notes 
					scale = major
					interval = interval_maj

					# getting key to build scale around 
					key = get_key(major_notes,minor_notes)
					key_2 = get_key_2(major_notes,minor_notes)
					
					#changing notes list if necessary 
					if key in check_flats:
						notes = minor_notes

					index_start_s = notes.index(key)
					index_start_c = notes.index(key_2)

					# building scale
					sm.build_scale(scale,index_start_s,notes,scale_result)
					
					# adding notes that cant be accesed from major notes list
					alt_major(key,scale_result)

					# making sure the scale is in alphabetical order 
					sm.order_major(scale_result)

					# formating output 
					format_scale(scale_type,scale_result,key)

					# building harmonies
					sm.build_harmony(scale_result,harmony_triad,harmony_seventh)
					
					# formating output 
					format_harmony(key,scale_type,scale_result,harmony_triad,harmony_seventh,harmonization_order)

					# building chord
					sm.build_chord(interval,index_start_c,notes,chord_result)

					# formating output
					format_chord(scale_type,chord_result,key_2)

					


							
				elif scale_type == 'Minor':
					notes = minor_notes
					scale = minor
					interval = interval_min
					chords = chords_minor

					# getting key to buld scale and chord
					key = get_key(major_notes,minor_notes)
					key_2 = get_key_2(major_notes,minor_notes)
					
					# changing note list if necessary
					if key in check_sharps:
						notes = major_notes

					# setting index for the looping through notes 
					index_start_s = notes.index(key)
					index_start_c = notes.index(key_2)

					# building scale and chord 
					sm.build_scale(scale,index_start_s,notes,scale_result)
					# swappng notes that arent incldued in minor notes list
					alt_minor(key,scale_result)
					
					sm.build_chord(interval,index_start_c,notes,chord_result)


					# ordering scale
					sm.order_minor(scale_result)

					# formating scale  and chord 
					format_scale(scale_type,scale_result,key)
					format_chord(scale_type,chord_result,key_2)



				
				elif scale_type == 'Dorian':
					notes = minor_notes
					scale = minor
					minor[5] = 2
					minor[6] = 1
					key = get_key(major_notes,minor_notes)
					index_start = notes.index(key)
					sm.build_scale(scale,index_start,notes,scale_result)
					format_scale(scale_type,scale_result,key)


				elif scale_type == 'Phyrgian':
					notes = minor_notes
					scale = minor
					minor[1]= 1
					minor[2] = 2
					key = get_key(major_notes,minor_notes)
					index_start = notes.index(key)
					sm.build_scale(scale,index_start,notes,scale_result)
					format_scale(scale_type,scale_result,key)
				
				elif scale_type == 'Lydian':
					notes = major_notes
					scale = major
					major[3] = 2
					major[4] = 1
					key = get_key(major_notes,minor_notes)
					index_start = notes.index(key)
					sm.build_scale(scale,index_start,notes,scale_result)
					format_scale(scale_type,scale_result,key)

				elif scale_type == 'Mixolydian':
					notes = major_notes
					scale = major
					major[6] = 1
					major[7] = 2
					key = get_key(major_notes,minor_notes)
					index_start = notes.index(key)
					sm.build_scale(scale,index_start,notes,scale_result)
					format_scale(scale_type,scale_result,key)

				elif scale_type == 'Locrian':
					notes = minor_notes
					scale = minor
					minor[1] = 1
					minor[2] = 2
					minor[5] = 2
					minor[4] = 1
					key = get_key(notes)
					index_start = notes.index(key)
					sm.build_scale(scale,index_start,notes,scale_result)
					format_scale(scale_type,scale_result,key)

				# Remember list changes length after pop so need to update index choice

				elif scale_type == 'Pentatonic(M)':
					notes = major_notes
					scale = major
					major.pop(4)
					major.pop(6)
					major[3] = 3
					key = get_key(notes)
					index_start = notes.index(key)
					sm.build_scale(scale,index_start,notes,scale_result)
					format_scale(scale_type,scale_result,key)


				elif scale_type == 'Pentatonic(m)':
					notes = minor_notes
					scale = minor
					minor.pop(2)
					minor.pop(5)
					minor[1] = 3
					minor[4] = 3
					key = get_key(notes)
					index_start = notes.index(key)
					sm.build_scale(scale,index_start,notes,scale_result)
					format_scale(scale_type,scale_result,key)

				else:
					print("DO NOTHING")

				cont_1 = input("Would you like to build another scale(y/n): ")

		elif aspect == 2:
			cont_2 = 'y'
			while cont_2 == 'y':
				dot.clear()
				line.clear()
				key_3 = get_key_3(major_notes,minor_notes)
				print("\n")
				print("< Fret Position info >\n")
				print("C Major Fret Positions: 1,3,5,10")
				print("D Major Fret Positions: 1,5,7,10 ")
				print("E Major Fret Positions: 1,2,4,7,12")
				print("F major Fret Positions: 1,3,5,8")
				print("G major Fret Positions: 1,3,5")
				print("\n")
				fret_pos = [1,2,3,4,5,7,8,10,12]

			
				fret = get_fret(fret_pos)
				print("\n")

				print("When picking a chord version in the next step, you'll select an option based on")
				print("the number of chord versions there are for your chosen fret position which will be given")
				print("to you. For example if youd like to pick the second version of a Cmaj chord in fret ")
				print("position 1, you'd enter 2 as your chord version choice \n")
					

				## Need to add while loop 
				# building chord visual 
				print("\n")
				KEY = (key_3,fret)
				num_choices = len(chords_major[KEY])
				print("There are ", num_choices ,"choice(s) starting at fret", fret)
				print("\n")
				choice = int(input("Please enter chord version choice as integer (1,2.....): "))
				print("\n")
				dot.penup()
				dot.goto(-20,-20)
				dot.pendown()
				dot.write(fret, font = ('Arial',15,'normal'))
				barre_list = []

				for i in range(len(chords_major[KEY][choice-1])):
					if chords_major[KEY][choice-1][i][1] == 'X':
						dot.penup()
						dot.goto(chords_major[KEY][choice-1][i][0])
						dot.pendown()
						dot.write('X',font = ('Arial',10,'normal'))
						barre_list.append(chords_major[KEY][choice-1][i][0])
					elif chords_major[KEY][choice-1][i][1] == 'B':
						dot.penup()
						dot.goto(chords_major[KEY][choice-1][i][0])
						dot.pendown()
						dot.dot(10,'black')
						barre_list.append(chords_major[KEY][choice-1][i][0])
					elif chords_major[KEY][choice-1][i][1] == 'R':
						dot.penup()
						dot.goto(chords_major[KEY][choice-1][i][0])
						dot.pendown()
						dot.dot(10,'red')
						barre_list.append(chords_major[KEY][choice-1][i][0])

				# code for selcting which chord takes a barre and drawing it
				barre = []
				for i in range(len(barre_list)):
					if barre_list[i][1] == -20:
						barre.append(barre_list[i])
						if len(barre) > 1:
							distance = (barre[1][0] - barre[0][0])
			
							line = turtle.Turtle()
							line.pencolor('green')
							line.hideturtle()
							line.pensize(7)
							line.penup()
							line.goto(barre[0])
							line.pendown()
							line.forward(distance)

				cont_2 = input("Would you like to build another chord (y/n): ")

		#formatting output scale(s) + chord(s)
		cont_0 = input("Would you like to pick a different aspect of the program(y/n): ")
		print("\n")
	print("OK BYE :) ")
		


if __name__ == '__main__':
	main()














