from images import *
import sys
import subprocess

dirToProcess = sys.argv[1]

def transform_photo(photo_filename):
	img0 = PIL.Image.open(photo_filename)
	img0 = np.float32(img0)
	# showarray(img0/255.0)
	render_deepdream(tf.square(T('mixed4c')), img0, 'transformed/'+photo_filename)
	return True


#photos_to_transform = ['pilatus800.jpg']

print dirToProcess
photos_to_transform = subprocess.check_output("ls " + dirToProcess , shell=True)
photos_to_transform = str(photos_to_transform).split("\n")
print photos_to_transform
print len(photos_to_transform)

for photo in photos_to_transform:
	transform_photo(photo)
