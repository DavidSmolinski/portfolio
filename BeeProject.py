'''
David Smolinski
Project Purpose: to show some of my Python and Excel abilities
This text file gets processed:
https://usda.mannlib.cornell.edu/usda/current/BeeColonies/BeeColonies-08-01-2018.txt
See the first print() function for the full purpose and instructions.
'''

import xlsxwriter  # This writes to Excel.

# Prints the purpose and instructions
print(
    "Program written by: David Smolinski\n Project Purpose: to show that David can do the following with Python and Excel\n - Grab data from a .txt file.\n - Clean the data.\n - Put it in Excel.\n - Make visuals, and use Excel tools.\n\n Requirements: Have the xlsxwriter module, in the right location. Use the proper file paths. The program is written specifically for BeeColonies-08-01-2018.txt\n\n")
y_or_n = input('Enter "y" to use default file names and paths. Otherwise, enter "n".\n')

xlsxfile = "BeeTable.xlsx"  # default output
bee_text = "BeeColonies-08-01-2018.txt"  # default input

# Decides which I/O file paths to use, ends program if user fails the first prompt
if y_or_n.lower() != 'y':
    if y_or_n.lower() == 'n':
        bee_text = input('Enter the correct .txt file name or path.\n')
        xlsxfile = input('Enter the correct .xlsx file name or path.\n')
    else:
        print("wrong input")
        quit()

# makes Excel file
workbook = xlsxwriter.Workbook(xlsxfile)
worksheet = workbook.add_worksheet()

# opens .txt file in read mode
bee_txt = open(bee_text, "r")


# Make a string a list based on the delimiter '  '. Remove blank elements, and clean it.

# input = string, output = row in Excel
# line_in = a line from the table (string)
# row determines Excel row
def clean_line(line_in, row):
    def bad_element(element): # Return false for bad elements.
        if element == ' \n':
            return False
        else:
            return True

    line_list = line_in.split('  ') # makes string line_in a list, delimiter = '  '
    line_list = list(filter(bad_element, line_list)) # deletes elements when bad_element returns false
    line_list = list(filter(None, line_list)) # deletes empty elements

    i = 0 # index of element in line_list
    while i < len(line_list):
        line_list[i] = line_list[i].strip(':') # strips outer bad characters in element
        line_list[i] = line_list[i].strip('.')
        line_list[i] = line_list[i].strip() # strips blanks
        if line_list[i] == '(Z)' or line_list[i] == '-': # The original table should have used 0.
            line_list[i] = '0'
        line_list[i] = line_list[i].replace(",", "") # "," gone
        if i > 0: # make numbers ints
            line_list[i] = int(line_list[i])
        worksheet.write(row, i, line_list[i]) # write Excel value in row row, column i
        i += 1 #next list element


in_Alabama = False
in_Other_States = False
line_index = 1

# Go to Alabama.
while not in_Alabama:
    line = bee_txt.readline() # read a line from text file, auto increment
    in_Alabama = line.startswith("Alab")
    if in_Alabama == True:
        clean_line(line, line_index) # cleans line, puts in Excel, row = line_index
        line_index += 1

# Go to Other States.
while not in_Other_States:
    line = bee_txt.readline()
    in_Other_States = line.startswith("Other S")
    blank_start = line.startswith(" ") #ignore blank lines
    if not blank_start:
        clean_line(line, line_index)
        line_index += 1

# Excel row starting at cell 0,0
worksheet.write_row(0, 0, ['State', 'Number of Colonies on 1/1/17', 'Maximum Colonies', 'Lost Colonies', '% Lost',
                           'Colonies Added', 'Colonies Renovated', '% Renovated'])
worksheet.write_row(line_index, 0,
                    ['United States', '=SUM(B2:B' + str(line_index) + ')', '=SUM(C2:C' + str(line_index) + ')',
                     '=SUM(D2:D' + str(line_index) + ')', '=AVERAGE(E2:E' + str(line_index) + ')',
                     '=SUM(F2:F' + str(line_index) + ')', '=SUM(G2:G' + str(line_index) + ')',
                     '=AVERAGE(H2:H' + str(line_index) + ')'])

# defines green background
good_survival = workbook.add_format({'bg_color': '#00FF00'})

# from cell (1,4) to (line_index,4) decide whether cells are green
worksheet.conditional_format(1, 4, line_index, 4, {'type': 'cell',
                                                   'criteria': '<=',
                                                   'value': 5,
                                                   'format': good_survival})
worksheet.write(line_index + 1, 0, '', good_survival) #green cell

worksheet.write(line_index + 1, 1, 'Cells with % loss <=5 are green')
worksheet.set_column(0, 8, 13) #width 13 from column 0 to 8

bee_txt.close()
workbook.close()