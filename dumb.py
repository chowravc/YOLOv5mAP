import glob
import shutil

wrong = './wrong/*.txt'

right = './source/'
output = './YOLO_files_ground_truth/'

wrongs = glob.glob(wrong)

for file in wrongs:

	wrongfileName = file.split('\\')[-1]
	rightfileName = glob.glob(right+'*'+wrongfileName)[0].split('\\')[-1]
	dest = output + rightfileName
	shutil.copyfile(file, dest)