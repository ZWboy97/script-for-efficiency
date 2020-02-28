import docx
from docx import Document
import xlwt
import os
import os.path

# 修改这两个参数
workspace_dir = "W:\\WorkPlace\\Python\\word_handler\\"  # 批处理文件所在的目录
excel_file_name = "result.xls"  # 输出的Excel的文件名


# 表格中的读取的内容可能有很多换行啥的，去掉
def formate_string(raw_string):
    result = raw_string.strip().replace(' ', '').replace(
        '\n', '').replace('\t', '').replace('\r', '').strip()  # 表格中有回车，去掉
    return result


# 从文档表格中读取内容，table为表格变量，x，y为内容在表格中的坐标
def get_content_from_table(table, x, y):
    content = table.cell(x, y).text
    return formate_string(content)


# 从文档中提取需要的信息，需要增删字段，改这里就可以
# 返回一个list，对应excel中的一行
def get_info_cell_from_docx(docx_path):
    document = Document(docx_path)
    tables = document.tables
    info_table = tables[0]
    name = get_content_from_table(info_table, 0, 0)
    sex = get_content_from_table(info_table, 0, 2)
    date = get_content_from_table(info_table, 3, 4)
    result_table = tables[1]
    les_length = get_content_from_table(result_table, 5, 1)
    les_fuqiang_length = get_content_from_table(result_table, 6, 1)
    les_jing_xi_max_pressure = get_content_from_table(result_table, 12, 1)
    les_jing_xi_min_pressure = get_content_from_table(result_table, 13, 1)
    les_can_yu_average_pressure = get_content_from_table(result_table, 14, 1)
    les_song_chi_rate = get_content_from_table(result_table, 16, 1)
    ues_jing_xi_average_pressure = get_content_from_table(result_table, 21, 1)
    ues_can_yu_average_pressure = get_content_from_table(result_table, 22, 1)
    cell_list = [
        name, sex, date, les_length,
        les_fuqiang_length,
        les_jing_xi_max_pressure,
        les_jing_xi_min_pressure,
        les_can_yu_average_pressure,
        les_song_chi_rate,
        ues_jing_xi_average_pressure,
        ues_can_yu_average_pressure
    ]
    return cell_list


# 将最终的N个List一次性存储到一个Excel文件中
def save_data_to_excel(header, data, excel_path):
    # 创建了一个Excel文件
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('result', cell_overwrite_ok=True)
    # 设置表头
    i = 0
    for k in header:
        sheet.write(0, i, k)
        i = i + 1

    # 数据写入excel
    row = 1  # 第二行开始
    for value in data:
        col = 0
        for col in range(0, len(value)):
            sheet.write(row, col, value[col])
        row = row + 1
    # 最后，将以上操作保存到指定的Excel文件中
    book.save(excel_path)
    print('\n处理成功，导出Excel路径为：'+excel_path)
    return


# 读取目录下，以.docx结尾的文件，返回文件列表
def get_docx_file_list(dir_path):
    file_list = []
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            if ".docx" in filename:
                file_list.append(filename)
    return file_list


# 遍历文件列表，一次从每个文件中提取信息，最终返回这些信息的list
def get_result_list_from_docx_files(dir_path, docx_file_list):
    result_list = []
    for file_name in docx_file_list:
        path = dir_path + "\\" + file_name
        print('\n正在操作文件：' + path)
        result = get_info_cell_from_docx(path)
        print('提取信息结果：' + str(result)+"\n")
        result_list.append(result)
    return result_list


# 启动处理
def main():
    dir_path = workspace_dir
    docx_file_list = get_docx_file_list(dir_path)
    print('There are '+str(len(docx_file_list)) +
          ' .docx file in dir ' + dir_path)
    result_list = get_result_list_from_docx_files(dir_path, docx_file_list)
    header = ['姓名', '性别', '日期',
              'LES总长度', 'LES腹腔长度', 'LES静息压Max',
              'LES静息压Min', '残余压平均值', '松弛率',
              'UES残余压', 'UES静息压']
    print('提取数据如下：\n')
    print(header)
    for result in result_list:
        print(result)
    excel_path = workspace_dir + excel_file_name
    save_data_to_excel(header, result_list, excel_path)
    return


main()
