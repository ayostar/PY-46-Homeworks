import os


def merge_files(incoming_directory):

    files = os.listdir(incoming_directory)
    text_files = filter(lambda x: x.endswith('.txt'), files)
    text_files_list = list(text_files)
    print(f'В папкe {incoming_directory} находятся такие файлы с расширением *.txt: {text_files_list}')
    files_keys_lines_var1_text_var2 = {}

    for txt_file in text_files_list:
        with open((incoming_directory + '/' + txt_file), encoding = 'utf-8') as file:
            files_keys_lines_var1_text_var2[file.name] = [sum(1 for line in open(file.name, 'rt')), file.read()]
    sorting_by_number_of_lines = sorted(files_keys_lines_var1_text_var2.items(), key=lambda item: item[1])
    result_dict = dict(sorting_by_number_of_lines)

    with open((incoming_directory + '/merged_file.txt'), 'w') as merged_file:
        for keys, values in result_dict.items():
            merged_file.write(keys + '\n')
            for value in values:
                merged_file.write(str(value) + '\n')

    with open((incoming_directory + '/merged_file.txt'), 'r') as merged_file:
        return print(merged_file.read())


merge_files('/Users/artemstarodubtsev/PycharmProjects/pythonProject/Files')