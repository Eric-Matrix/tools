#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import os
import struct

"""
	python str16_bin_convert.py file(can include path)
"""
#input file 

#output file

def Str16_to_binFile(inputpath, outpath):
	with open(inputpath, 'r') as f:
		str_buffer = f.read()
		#print(str_buffer)
	with open(outpath,'wb') as f1:
		j = 0
		while(j < len(str_buffer) -1):
			a = str_buffer[j:j+2]
			j+=2
			#print(a)
			b = int("0x"+a, 16)
			f1.write(struct.pack('B', b))

def binFile_to_Str16(inputpath, outpath):
	buffer = []
	Str16 = ''
	with open(inputpath, 'rb') as f:
		buffer = f.read()
		print(type(buffer))
		for i in buffer:
			#获取每个字节并转换成十进制数字
			b = struct.unpack('B', i)[0]
			#16进制转换
			c = hex(b)
			#将16进制数字去掉0X
			d = str(c[2:]).upper()
			if(len(d)) == 1: #如果不足2位，前面需要补0
				d = '0'+ d
			Str16 = Str16 + d
			
	#print(Str16)
	with open(outpath, 'w') as f:		
		f.write(Str16)
			
if __name__ == '__main__':
	print('-' * 80)
	print('Usage python 16str_bin_convert.py input_file_path ')
	print('python 16str_bin_convert.py ./a.bin：意思是把a.bin中二进制按字节转换成相同的字符串！')
	print('python 16str_bin_convert.py ./a.txt: 意思是把txt中的字符串转成相同的二进制文件！')
	print('例如：二进制文件内容是 "0x9D 0x2F  0x0D...."，转换成字符串是9D2F0D...')
	print('输出文件在同一路径下')
	print('-' * 80)
	if(len(sys.argv) < 2):
		print('请检查参数！')
	else:
		input_file_path = sys.argv[1]
		filepath, tempFileName = os.path.split(sys.argv[1])
		filename, extension = os.path.splitext(tempFileName)

		if(filepath == ''):
			filepath = filepath + '.'
		print(filepath)

		if(extension ==  '.bin'):
			output_file = filepath + '/' + filename + '.txt'
			binFile_to_Str16(input_file_path, output_file)
			print('输出文件：' + output_file + 'finshed!')
		elif(extension == '.txt'):
			output_file = filepath + '/' + filename + '.bin'
			print(output_file)
			Str16_to_binFile(input_file_path, output_file)
			print('输出文件：' + output_file + 'finshed!')
		

	
	
	

	


