import re
import os

print("Programmer = David Smolinski\n"
      "This is for programs with a .txt (text) file type.\n"
      "For all tools, this sets where the coolant turns on, and adds M08 if it's missing.\n"
      "It does nothing with M09.\n"
      "It changes Z and adds M08 on the G43 lines. example: G43 H01 Z2. M08\n"
      "Important: not for files with ;")

might_be_steve = input('Enter the first letter of your first name.\n')

steve = False

if might_be_steve.lower() == 's':
    possibly_steve = input('Hi Steve. Enter the letter "Y" if you are Steve or "N" if you are not.\n')
    if possibly_steve.lower() == 'y':
        steve = True

if steve == False:
    source_path = os.listdir('to_change/')
    m8 = re.compile(r'[Mm](08|8)')
    g43 = re.compile(r'[Gg]43')
    z = re.compile(r'[Zz].*')
    has_semi = re.compile(r'.*;')
    z_value = input('Enter the Z value (including "."\n')

    for file in source_path:
        input_file = 'to_change/' + file
        print("processing" + file)
        with open(input_file, 'r') as to_change:
            file_data = to_change.readlines()
        output_file = 'changed/' + file
        with open(output_file, 'w') as changed:
            for element in file_data:

                if g43.search(element) is None:
                    element = m8.sub('', element)
                elif has_semi.search(element) is None:
                    element = z.sub('Z' + str(z_value) + ' M08\n', element)
                else:
                    element = z.sub('Z' + str(z_value) + ' M08;\n', element)
                changed.write(element)
