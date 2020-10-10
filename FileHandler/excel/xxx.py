import openpyxl

# （时间，存量和增速）
data = []

def load_data(file_name):
    wb = openpyxl.load_workbook('F:\视频图片\文档\数据统计\社会融资存量\\'+file_name+'.xlsx', read_only=True)
    print(wb)
    cur_sheet = wb.active  # 获取默认打开的Sheet
    wb.close()
    print(cur_sheet)
    # print(cur_sheet['B9'].value)

load_data('2016')

