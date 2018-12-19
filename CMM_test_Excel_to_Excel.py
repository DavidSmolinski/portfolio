import xlsxwriter  # This writes to Excel.
import xlrd  # This reads from to Excel.

# input Excel file
input_path = "test input.xlsx"
input_workbook = xlrd.open_workbook(input_path)
input_worksheet = input_workbook.sheet_by_index(0)

# output Excel file
output_path = 'test output.xlsx'
workbook = xlsxwriter.Workbook(output_path)
worksheet = workbook.add_worksheet()

nums = []

for i in range(1, input_worksheet.nrows):
    inp = input_worksheet.cell_value(i, 0)
    if inp != "":
        nums.append(inp)

nums_max = max(nums)
nums_min = min(nums)
nums_length = len(nums)
nums_abs = []
multiples_of_5 = []

worksheet.write_row(0, 0, ['numbers', 'absolute values', 'multiples of 5', 'max', 'min'])
worksheet.write_column(1, 0, nums)

blue_max = workbook.add_format({'bg_color': '#99CCFF'})
orange_min = workbook.add_format({'bg_color': 'FF9900'})

worksheet.conditional_format(1, 0, nums_length, 0, {'type': 'cell',
                                                    'criteria': '==',
                                                    'value': nums_max,
                                                    'format': blue_max})
worksheet.conditional_format(1, 0, nums_length, 0, {'type': 'cell',
                                                    'criteria': '==',
                                                    'value': nums_min,
                                                    'format': orange_min})

for num in nums:
    nums_abs.append(abs(num))
    if num != 0 and num % 5 == 0:
        multiples_of_5.append(num)

worksheet.write_column(1, 1, nums_abs)
worksheet.write_column(1, 2, multiples_of_5)
worksheet.write(1, 3, nums_max, blue_max)
worksheet.write(1, 4, nums_min, orange_min)

worksheet.set_column(0, 8, 14) #width 13 from column 0 to 8

workbook.close()
