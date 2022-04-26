import csv
import re


def get_data(file_names):
    main_data = {'Изготовитель системы': [], 'Название ОС': [], 'Код продукта': [], 'Тип системы': []}
    for file_name in file_names:
        with open(file_name, 'r', encoding='windows-1251') as file:
            file_content = file.read()
            for k, v in main_data.items():
                v.append(re.search(fr'{k}:\s*([^\r\n]+)', file_content).group(1).strip())
    os_prod_list = main_data['Изготовитель системы']
    os_name_list = main_data['Название ОС']
    os_code_list = main_data['Код продукта']
    os_type_list = main_data['Тип системы']
    main_data = list(main_data.keys())
    return main_data, os_prod_list, os_name_list, os_code_list, os_type_list


def write_to_csv(file_names, report_file):
    main_data, os_prod_list, os_name_list, os_code_list, os_type_list = get_data(file_names)
    csv_writer = csv.writer(report_file, quoting=csv.QUOTE_NONNUMERIC)
    csv_writer.writerow(main_data)
    for row in zip(os_prod_list, os_name_list, os_code_list, os_type_list):
        csv_writer.writerow(row)


with open('task_1/main_data.csv', 'w', encoding='windows-1251') as report_file:
    write_to_csv(
        [
            'task_1/info_1.txt',
            'task_1/info_2.txt',
            'task_1/info_3.txt'
        ],
        report_file
    )
