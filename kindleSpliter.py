import os

output_folder = os.path.join('output')

if not os.path.exists(output_folder):
	os.mkdir(output_folder)

title_filename = os.path.join(output_folder,' ! titleAll.txt')

with open('My Clippings.txt','r') as clipping_file:
	line = clipping_file.readlines()
	titleline = set()
	for i in range( len(line) ):
		if line[i] == '==========\n':
			titleline.add(line[i-4])

with open(title_filename,'w') as title_file:
	for i in titleline:
		title_file.write(i)
					
for x in titleline:
	x2 = x.decode('utf-8')
	filename = os.path.join(output_folder, x2.strip() +'.txt')
	with open(filename,'w') as out_file:
		with open('My Clippings.txt','r') as clipping_file:
			line = clipping_file.readlines()
			for i in range( len(line) ):
				if x == line[i]:
					out_file.write(line[i+1])
					out_file.write(line[i+2])
					out_file.write(line[i+3])
					out_file.write(line[i+4])