
if(0):
    def extract_lines(input_file, output_file):
        unique_chars = set()
        unique_lines = []

        with open(input_file, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                line = lines[i]
                if '@' in line:
                    unique_chars.add('@')
                    if i + 1 <len(lines):
                        unique_lines.append(lines[i+1])
                        break


        with open(output_file,'w') as f:
            f.writelines(unique_lines)

    input_file = "input.txt"
    output_file = "output.txt"

    extract_lines(input_file, output_file)

if(0):
    def extract_lines(input_file, output_file):
        lines_to_write = []
        append_next_line = False

        with open(input_file, 'r') as f:
            for line in f:
                if '@' in line:
                    append_next_line = True
                elif append_next_line:
                    lines_to_write.append(line)
                    append_next_line = False

        with open(output_file,'w') as f:
            f.writelines(lines_to_write)

    input_file = "input.txt"
    output_file = "output.txt"

    extract_lines(input_file, output_file)


if(0):


    def extract_lines(input_file, output_file):
        lines_to_write = []
        append_next_line = False
        append_line = False
        between_lines = False


        with open(input_file, 'r') as f:
            for line in f:
                if '@' in line:
                    append_next_line = True
                elif append_next_line:
                    lines_to_write.append(line)
                    append_next_line = False

                if '*-' in line and '-*' in line:  #if '@%' in line and '%@' in line:
                    start_index = line.index('*-')#@%
                    end_index = line.index('-*')#%@
                    lines_to_write.append(line[start_index + 2:end_index] + '\n')
                elif '*-' in line: #elif '@%' in line:
                    append_line = True
                    start_index = line.index('*-') #start_index = line.index('@%')
                    lines_to_write.append(line[start_index + 2:])
                elif append_line:
                    lines_to_write.append(line)
                    if '-*' in line:  #if '%@' in line:
                        append_line = False


#               if line.startswith('@%') and line.endswith('%@\n'):
#                   lines_to_write.append(line[2:-3] + '\n')
#                elif line.startswith('@%'):
#                    append_line = True
#                    lines_to_write.append(line[2:])
#                elif append_line:
#                    lines_to_write.append(line)
#                    if line.endswith('%@\n'):
#                        append_line = False

        with open(output_file,'w') as f:
            f.writelines(lines_to_write)

    input_file = "input.cpp"#input.txt
    output_file = "output.txt"

    extract_lines(input_file, output_file)

#if(0):
    #import os  # module os needs to be imported to have files in a folder to be extracted

#    def extract_lines(input_file, output_file):
#        lines_to_write = []
#        append_next_line = False
#        append_line = False

if(1):
    def show():
        print("DONE EXTRACTION")

    def clean_output(lines):
        cleaned_lines = []
        for line in lines:
            cleaned_line = line.replace('-*','')
            cleaned_lines.append(cleaned_line)
        return cleaned_lines

    def extract_lines(input_file, output_file):
        lines_to_write = []
        append_next_line = False
        append_line = False
        between_lines = False


        with open(input_file, 'r') as f:
            for line in f:
#                if '@' in line:
#                    append_next_line = True
#                elif append_next_line:
#                    lines_to_write.append(line)
#                    append_next_line = False

                if '*-' in line and '-*' in line:  #if '@%' in line and '%@' in line:
                    start_index = line.index('*-')#@%
                    end_index = line.index('-*')#%@
                    lines_to_write.append(line[start_index + 2:end_index] + '\n')
                elif '*-' in line: #elif '@%' in line:
                    append_line = True
                    start_index = line.index('*-') #start_index = line.index('@%')
                    lines_to_write.append(line[start_index + 2:])
                elif append_line:
                    lines_to_write.append(line)
                    if '-*' in line:  #if '%@' in line:
                        append_line = False

        cleaned_lines = clean_output(lines_to_write)

        with open(output_file,'w') as f:
            f.writelines(cleaned_lines)#lines_to_write

    input_file = "input.cpp"#input.txt
    output_file = "output.txt"

    extract_lines(input_file, output_file)



show()





