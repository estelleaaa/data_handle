import xlrd, xlwt

# 读取excel
# 参数 filename： excel文件路径
# 参数 formatting_info：是否读取格式信息， 仅对.xls文件有用， 如果是.xlsx需要转存为.xls文件（改后缀名没用）
workbook = xlrd.open_workbook(r'./打卡.xls', formatting_info=True)
# 获取第一个表单
sheet = workbook.sheets()[0]
print(sheet)
# 获取所有的有效的行数
nrows = sheet.nrows
# 用来保存读取到的信息的列表
li = []
# 用来保存读取到的信息的列数
length = 0
# 用来判断是否进入正式的逻辑， 也就是姓名那一行
is_start = False
# 用来保存这个月的星期数， [1, 2, 3 ..., 30]
date_li = []
# 是否是夏令时
weather = 0
# 夏令时的默认加班时间点
default_end = '21:30'
# 夏令时日常组的默认加班时间点
esp_end = '16:30'
if weather:
	# 冬令时的默认加班时间点
	default_end = '21:00'
	# 冬令时的日常组默认加班时间点
	esp_end = '17:00'
# 将时间都处理成整数， 用来比较排序， 如09:38转为938
end_time = int(default_end.replace(':', ""))
esp_time = int(esp_end.replace(':', ""))
# 标注行数， 防止在姓名那一行就直接进入加班逻辑判断
row_tag = 0
# 保存合计加班数
total_nums = 0
# 保存是否结束
is_end = False
# 对整张excel表进行遍历
for r_index in range(nrows):
	# 获取当前行的值
	row = sheet.row_values(r_index)
	# 保存是否加班的列， 例如第7列
	tag_li = []
	# 保存这一行加班的数量
	nums = 0

	# 如果第1列的值是姓名， 则说明开始进入正式的逻辑处理部分， 记录下当前行， 将开始标志置为True， 读取这个月的日期
	if row[0] == '姓名' and not is_start:
		row_tag = r_index
		is_start = True
		date_li = row[5:-1]

	# 如果开始正式逻辑了， 但是第1列或者第2列没有值 且 第1列或者第17列不是’合计’则不再往下进行（对应开头或者结尾那些空列）， 如果要加最后的合计部分可以再加统计逻辑， 在li后面再补一列
	if is_start and ((not (row[0] and row[1])) and row[0] != '合计'):
		if not row[16]:
			continue
	# 如果第17列或者第1列是合计， 则逻辑应该结束
	if (row[16] == '合计' or row[0] == '合计') and not is_end:
		is_end = True
	# 如果开始正式逻辑了且还没结束， 正式进入统计
	elif is_start and not is_end:
		# 获取他是哪个考勤组的
		group = row[1]
		# 获取他的打卡时间点
		time_li = row[5:-1]
		# 遍历打卡信息， 对每天的打卡进行处理
		for i in range(len(time_li)):
			# 获取他的加班时间点
			cmp_time = esp_time if group == '日常组' and date_li[i] == '六' else end_time
			# 如果是在姓名那一列则直接跳出去，不能处理这行
			if row_tag == r_index:
				break
			# 获取某天的打卡时间记录
			time_str = time_li[i]
			# 如果为空， 说明没有打卡， 直接跳过
			if not time_str:
				continue
			# 将时间按照这行进行分割， 然后去掉左右的空字符， 取前5个字符， 替换掉里面的:， 再转为整数
			time_str_li = [int(x.strip()[:5].replace(':', '')) for x in time_str.split('\n')]
			# 如果加班到凌晨， 以6点为界， 将凌晨的时间加上24小时
			if 0 <= time_str_li[-1] < 600:
				time_str_li[-1] += 2400
			# 对时间进行排序
			time_str_li.sort(key=lambda x:x)
			# 如果上班时间不超过8小时， 不算加班， 直接跳过
			if time_str_li[-1] - time_str_li[0] < 800:
				continue
			# 如果上班结束时间大于加班时间点， 将这一列的列数加入到保存加班列信息的列表里面， 并且加班数加1
			if time_str_li[-1] > cmp_time:
				tag_li.append(5 + i)
				nums += 1

	# 获取此张表最大的长度
	if not length:
		length = len(row)
	# 保存每行的单元格
	row_li = []
	# 存单元格的变量
	cell = None
	# 对每列进行遍历
	for col_index in range(length):
		# 获取当前行、列对应的单元格， 如果当前列在加班标识里， 改变它的背景颜色属性
		cell = sheet.cell(r_index, col_index)
		xfx = sheet.cell_xf_index(r_index, col_index)
		xf = workbook.xf_list[xfx]
		if col_index in tag_li:
			xfx = sheet.cell_xf_index(r_index, col_index)
			xf = workbook.xf_list[xfx]
			xf.background.pattern_colour_index = 16
		# 将单元格添加到行单元格数组中
		row_li.append(cell)
	else:
		# 遍历过后， 将加班数更新到最后一个单元格中, 并统计进合计
		if is_start and row_tag != r_index:
			cell.value = int(nums)
			total_nums += nums
	# 将各行单元格添加到列表中用于写excel
	li.append(row_li)
else:
	# 更新合计
	row = li[-1]
	row[-1].value = total_nums

# 准备写入
wb = xlwt.Workbook()
w_sheet = wb.add_sheet('打卡时间')

# 对列表进行遍历
for r_index in range(len(li)):
	# 取出一行单元格
	cells = li[r_index]
	# 对该行的列进行遍历
	for c_index in range(len(cells)):
		# 获取单元格
		cell = cells[c_index]
		# 根据之前默认的和改变过的颜色信息， 更新颜色
		xfx = sheet.cell_xf_index(r_index, c_index)
		xf = workbook.xf_list[xfx]
		pattern = xlwt.Pattern()
		pattern.pattern = xlwt.Pattern.SOLID_PATTERN
		pattern.pattern_back_colour = 65 - xf.background.background_colour_index
		pattern.pattern_fore_colour = 65 - xf.background.pattern_colour_index
		style = xlwt.XFStyle()
		style.pattern = pattern
		# 写表
		w_sheet.write(r_index, c_index, cell.value, style)
# 保存
wb.save('9月打卡.xls')
# cell = sheet.cell(8, 7)
# xfx = sheet.cell_xf_index(8, 7)
# xf = workbook.xf_list[xfx]