def build_scale(scale,index_start_s,notes,scale_result):
	scale_index = 0
	for i in range(len(scale)-1):
		scale_index += scale[i]
		if scale_index + index_start_s > 11:
			scale_index = scale_index - 12
		scale_result.append(notes[index_start_s+scale_index])

def build_chord(interval,index_start_c,notes,chord_result):
	scale_index = 0

	for i in range(len(interval)):
		scale_index += interval[i]
		if scale_index + index_start_c >11:
			scale_index = scale_index - 12
		chord_result.append(notes[index_start_c+scale_index])

def converter(minor,major,interval_maj,interval_min):

	for i in range(8):
		minor[i] = int(minor[i])
		major[i] = int(major[i])
	for i in range(3):
		interval_maj[i] = int(interval_maj[i])
		interval_min[i] = int(interval_min[i])




def order_major(scale_result):

	repeats = [('A','A#'),('D','Db'),('Gb','G'),('C','C#'),('F','F#')]
	replace = ['Bb','C#','F#','B#','E#']
	for i in range(6):
	
		if (scale_result[i] in repeats[0])  and (scale_result[i+1] in repeats[0]):
			print("in 1")
			scale_result.remove(scale_result[i+1])
			scale_result.insert(i+1,replace[0])
	
		elif (scale_result[i] in repeats[1])  and (scale_result[i+1] in repeats[1]):
			print("in 2")
			scale_result.remove(scale_result[i+1])
			scale_result.insert(i+1,replace[1])

		elif (scale_result[i] in repeats[2])  and (scale_result[i+1] in repeats[2]):
			print("In 3")
			scale_result.remove(scale_result[i+1])
			scale_result.insert(i+1,replace[2])
		
		elif (scale_result[i] in repeats[3])  and (scale_result[i+1] in repeats[3]):
			print("in 4")
			scale_result.remove(scale_result[i])
			scale_result.insert(i,replace[3])

		elif (scale_result[i] in repeats[4])  and (scale_result[i+1] in repeats[4]):
			scale_result.remove(scale_result[i])
			scale_result.insert(i,replace[4])
			scale_result.remove(scale_result[6])
			scale_result.insert(6,'B#')

		


def order_minor(scale_result):

	repeats = [('A','A#',),('D','Db',),('Gb','G'),('Bb','Bb')]
	replace = ['Bb','C#','F#','B#','E#','A']

	
	for i in range(6):
	
		if (scale_result[i] in repeats[0])  and (scale_result[i+1] in repeats[0]):
			print("in 1")
			print(scale_result[i])
			print(scale_result[i+1])
			scale_result.remove(scale_result[i+1])
			scale_result.insert(i+1,replace[0])
	
		elif (scale_result[i] in repeats[1])  and (scale_result[i+1] in repeats[1]):
			print("in 2")
			scale_result.remove(scale_result[i])
			scale_result.insert(i,replace[1])

		elif (scale_result[i] in repeats[2])  and (scale_result[i+1] in repeats[2]):
			print("in 3")
			scale_result.remove(scale_result[i])
			scale_result.insert(i,replace[2])

		elif (scale_result[i] in repeats[3])  and (scale_result[i+1] in repeats[3]):
			print(4)
			scale_result.remove(scale_result[i])
			scale_result.insert(i,replace[5])

	


		

def build_harmony(scale_result,harmony_triad,harmony_seventh):
	loop_triad = scale_result*2
	loop_seventh = scale_result*3
	for i in range(len(scale_result)):
		harmony_triad.append([loop_triad[i],loop_triad[i+2],loop_triad[i+4]])
	for i in range(len(scale_result)):
		harmony_seventh.append([loop_seventh[i],loop_seventh[i+2],loop_seventh[i+4],loop_seventh[i+6]])
	return harmony_triad, harmony_seventh; 



	




	
