import os

# 主路径
path = 'F:\\pyData\\ppt'
files = set(os.listdir(path))

# 计数器
num = 0




def normal_ppt(path):
	files = set(os.listdir(path))
	for file in files:
		# 提取压缩文件名和文件类型
		fname,fename=os.path.splitext(file)
		if fename in ['.zip', '.rar']:
			# 将压缩包解压至以自身为名字的文件夹里
			filesname = os.path.join(path, fname)
			# print(filesname)
			if not os.path.exists(filesname):
				os.makedirs(filesname)

			# 压缩文件原全地址
			filename = os.path.join(path, file)

			# 去除文件名里的空格
			New_filename = filename.replace(' ', '')
			os.rename(filename, New_filename)
			cmd3 = '7z x %s -o%s' % (New_filename, filesname)
			if os.system(cmd3) == 0:
				os.remove(New_filename)

				# 防止局部全局变量出错
				global num
				num += 1
				try:
					new_files =set(os.listdir(filesname))
				except :
					print(New_filename)
				for new in new_files:
					f_new,fn_new = os.path.splitext(new)

					# 提取出来的文件
					new_file = os.path.join(filesname, new)

					# 去除杂乱文件
					if fn_new in ['.html', '.url', '.link']:
						os.remove(new_file)

# 遍历每一个大类
for file in files:

	# 大类
	bclass = os.path.join(path, file)
	ppt_files = set(os.listdir(bclass))
	for ppt_file in ppt_files:

		# 小类
		sclass = os.path.join(bclass, ppt_file)
		normal_ppt(sclass)
print('转换成功，共%d个文件' %(num, ))