'''
create / read and resize excel using pd

'''
import pandas as pd
files_path = '/Users/mkhan11/Documents/development/data'

def export_to_excel(files_path, file_name):
    print("Expoting initiated....")
    excel_data_df = pd.read_excel(files_path + '/' +file_name, sheet_name="Sheet1", index_col=0)
    # excel_data_df = pd.read_excel(files_path + '/' +file_name, sheet_name="Sheet1")
    print(f"data content of file---{file_name}-- is below")
    print('######################')
    print(excel_data_df)
    print('######################')
    from_file_columns = ["ID", "Name", "Marks", "Grade"]
    master_file = 'MarksData.xlsx'
    print(f"==writing to master file== ---{master_file}")
    print(files_path + '/' + master_file)
    # status = excel_data_df.to_excel(files_path + '/' + master_file, columns=from_file_columns, index=False)
    # with pd.ExcelWriter(files_path + '/' + master_file, mode="a", if_sheet_exists="overlay") as writer:
    #     excel_data_df.to_excel(writer,header=True, index=False)

    with pd.ExcelWriter(files_path + '/' + master_file, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
        excel_data_df.to_excel(writer, sheet_name="Sheet1", header=False, startrow=writer.sheets["Sheet1"].max_row, index=False)
    return 1


# file_one = "Athena01-01-2023.xlsx"
# print(export_to_excel(files_path, file_one))

def generate_file_names():
    file_prefix = "Athena"
    starting_month = 7
    ending_month = 8
    days_limit = 5
    suffix = "-2023.xlsx"
    files_list = []
    for str_month in range(starting_month, ending_month + 1):
        for day in range(1, days_limit + 1):
            day = '0' + str(day) if day <= 9 else day
            if int(str_month) <= 9:
                month = '0' + str(str_month)
                f = file_prefix + str(month) + '-' + str(day) + suffix
                files_list.append(f)
    # for index, file in enumerate(files_list):
    #     if index == 31:
    #         print()
    #         print()
    #     print(file)
    return files_list

def read_file_from_files_lake(files_path):
    files = generate_file_names()
    print('===reading files.....')
    print('=== files names.....', files)
    for file_name in files:
        print(f"for file----->{file_name}")
        if os.path.isfile(files_path + '/' + file_name):
            print(f"{file_name}--->True")
            export_to_excel(files_path, file_name)
    return True


# print(read_file_from_files_lake(files_path="/Users/mkhan11/Documents/development/data"))


# generate_file_names()

def create_sample_files():
    marks_data = pd.DataFrame({'ID': {0: 23, 1: 43, 2: 12,
                                    3: 13, 4: 67, 5: 89,
                                    6: 90, 7: 56, 8: 34},
                            'Name': {0: 'Ram', 1: 'Deep',
                                    2: 'Yash', 3: 'Aman',
                                    4: 'Arjun', 5: 'Aditya',
                                    6: 'Divya', 7: 'Chalsea',
                                    8: 'Akash' },
                            'Marks': {0: 89, 1: 97, 2: 45, 3: 78,
                                        4: 56, 5: 76, 6: 100, 7: 87,
                                        8: 81},
                            'Grade': {0: 'B', 1: 'A', 2: 'F', 3: 'C',
                                        4: 'E', 5: 'C', 6: 'A', 7: 'B',
                                        8: 'B'}})

    files_list = generate_file_names()
    # print(d)
    # file_name =  'Athena07-01-2023.xlsx'
    for abs_file_name in files_list:
        abs_file_name = os.path.join(files_path, abs_file_name)
        # print(abs_file_name)
        marks_data.to_excel(abs_file_name)
    print('DataFrame is written to Excel File successfully.')
    return None