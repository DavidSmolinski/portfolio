import re
import os

print("Programmer = David Smolinski\n"
      "Coolant Modifier\n"
      "Instructions in instructions.txt must be obeyed.\n")

might_be_steve = input('Enter the first letter of your first name.\n')

steve = False

if might_be_steve.lower() == 's':
    possibly_steve = input('Hi Steve. Enter the letter "Y" if you are Steve or "N" if you are not.\n')
    if possibly_steve.lower() == 'y':
        steve = True

if steve is False:
    source_path = os.listdir('to_change/')

    # regular expression objects for g code words
    m8 = re.compile(r'[Mm](08|8)')  # any M08
    m9 = re.compile(r'[Mm](09|9)')
    g43 = re.compile(r'[Gg]43')
    g28 = re.compile(r'[Gg]28')
    # any Z word (such as Z5.5)
    z = re.compile(r'[Zz](\d*\.\d*)')

    m8_z_value = input('Enter the Z value for M08 (coolant on).\n')
    m8_z_value = float(m8_z_value)
    m9_z_value = input('Enter the Z value for M09 (coolant off).\n')
    m9_z_value = float(m9_z_value)

    for file in source_path:
        input_file = 'to_change/' + file #the path of the .txt file to change
        print("processing" + file)
        with open(input_file, 'r') as to_change:
            #a list of the lines in the input .txt file
            file_data = to_change.readlines()
        output_file = 'changed/' + file
        with open(output_file, 'w') as changed:
            changed_list = [] #will contain a list of the lines in the output .txt file
            i = 0
            file_data_length = len(file_data)
            new_m9_line = False

            while i < file_data_length - 1:
                if g28.search(file_data[i + 1]) is not None:  # g28 was found on the next line.
                    file_data[i + 1] = m9.sub('', file_data[i + 1])  # Remove m9 from the next line.
                    # m9 was found on this line.
                    if m9.search(file_data[i]) is not None:
                        # z was found.
                        if z.search(file_data[i]) is not None:
                            file_data[i] = m9.sub('', file_data[i])  # Remove m9.
                            # Replace the Z word with the new Z and M09 words (ex. Z5.5 M09)
                            file_data[i] = z.sub('Z' + str(m9_z_value) + ' M09', file_data[i])
                        else:
                            file_data[i] = m9.sub('', file_data[i])
                            new_m9_line = True
                    else:
                        new_m9_line = True
                elif g43.search(file_data[i]) is not None:
                    file_data[i] = m8.sub('', file_data[i])
                    file_data[i] = z.sub('Z' + str(m8_z_value) + ' M08', file_data[i])
                else:
                    file_data[i] = m8.sub('', file_data[i])
                    file_data[i] = m9.sub('', file_data[i])

                if new_m9_line is True:
                    changed_list.append(file_data[i])
                    changed_list.append('Z' + str(m9_z_value) + ' M09\n')
                    new_m9_line = False
                else:
                    changed_list.append(file_data[i])
                i += 1
            changed_list.append(file_data[file_data_length - 1])

            for element in changed_list:
                changed.write(element)
    print('Done. new Z values: for M08: ' + str(m8_z_value) + ' for M09: ' + str(m9_z_value))
