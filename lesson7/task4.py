import os

folder = r'C:\Users\Admin\PycharmProjects\firstquarter\lesson7\some_data'
file_dict = {}

files_100 = [item.name for item in os.scandir(folder) if item.stat().st_size < 100]
files_1000 = [item.name for item in os.scandir(folder) if item.stat().st_size > 100 and item.stat().st_size < 1000]
files_10000 = [item.name for item in os.scandir(folder) if item.stat().st_size > 1000 and item.stat().st_size < 10000]
files_100000 = [item.name for item in os.scandir(folder) if
                item.stat().st_size > 10000 and item.stat().st_size < 100000]

file_dict['100'] = len(files_100)
file_dict['1000'] = len(files_1000)
file_dict['10000'] = len(files_10000)
file_dict['100000'] = len(files_100000)

print(file_dict)
