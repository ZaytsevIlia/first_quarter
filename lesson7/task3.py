import os
import shutil

folder = r'my_project\templates'

for root, dir, files in os.walk('my_project'):
    for item in files:
        if item.lower().endswith('.html'):
            if os.path.exists(folder):

                if os.path.exists(os.path.join(folder, os.path.split(root)[1])):
                    shutil.copyfile(os.path.join(root, item), os.path.join(folder,
                                                                           os.path.join(os.path.split(root)[1], item)))
                else:
                    os.makedirs(os.path.join(folder, os.path.split(root)[1]))
                    shutil.copyfile(os.path.join(root, item), os.path.join(folder,
                                                                           os.path.join(os.path.split(root)[1], item)))
            else:
                os.makedirs(folder)
                os.makedirs(os.path.join(folder, os.path.split(root)[1]))
                shutil.copyfile(os.path.join(root, item), os.path.join(folder,
                                                                       os.path.join(os.path.split(root)[1], item)))
