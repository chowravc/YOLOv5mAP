import glob
import os

def main():
	files = glob.glob('./dat_files_ground_truth/*.dat')

	for file in files:

		fileName = file.split('\\')[-1][:-3] + 'txt'

		outFile = './mAP/input/ground-truth/' + fileName

		dims = (1104, 800) # Image dimensions

		print('Converting file ' + fileName)

		readFile = open(file, 'r')
		writeFile = open(outFile, 'w')

		lines = readFile.read().split('\n')

		for line in lines:
			if len(line) != 0:

				v = line.split(' ')

				inXC = int(float(v[1]))
				inYC = int(float(v[2]))

				semiW = 5 # BBox size = 11
				semiH = 5 #

				# Outputs in mAP format: <class_name> <left> <top> <right> <bottom> [<difficult>]

				inClass = '0'

				left = str(inXC - semiW)
				top = str(inYC + semiH)
				right = str(inXC + semiW)
				bottom = str(inYC - semiH)

				outLine = inClass + ' ' + left + ' ' + top + ' ' + right + ' ' + bottom + '\n'
				writeFile.write(outLine)

		readFile.close()
		writeFile.close()

if __name__ == '__main__':
	main()