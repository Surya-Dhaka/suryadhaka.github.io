import sys 
import os
from PIL import Image  

def JPGtoPNGconverter(JPG_file, PNG_file):
	source_path = '/Users/suryadhaka/Documents/' + JPG_file
	destination_path = '/Users/suryadhaka/Documents/' + PNG_file

	if os.path.exists(destination_path):
		print('this folder exists :)')
	else:
		os.makedirs(destination_path)

	def converter(file_paths):
		with Image.open(file_paths) as img:
			base_name = os.path.splitext(os.path.basename(file_paths))[0]
			new_file_name = base_name + '.png'
			final_destination = os.path.join(destination_path, new_file_name)
			img.save(final_destination)

	for pokemon in os.listdir(source_path):
		file_path = os.path.join(source_path, pokemon)
		if os.path.isfile(file_path) and file_path.lower().endswith('.jpg'):
			converter(file_path)
			
print(os.getcwd() )