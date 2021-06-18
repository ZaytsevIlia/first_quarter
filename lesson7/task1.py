import os


def make_root_folder(name_folder):
    try:
        os.mkdir(name_folder)
    except FileExistsError:
        print(f'Папка {name_folder} уже существует.')
        quit()


def make_folder(name_folder, name_dir):
    try:
        os.mkdir(f'{name_folder}//{name_dir}')
    except FileExistsError:
        print(f'Папка {name_dir} уже существует.')


root_folder = 'my_project'
name_dir1 = 'settings'
name_dir2 = 'mainapp'
name_dir3 = 'adminapp'
name_dir4 = 'authapp'

make_root_folder(root_folder)
make_folder(root_folder, name_dir1)
make_folder(root_folder, name_dir2)
make_folder(root_folder, name_dir3)
make_folder(root_folder, name_dir4)

