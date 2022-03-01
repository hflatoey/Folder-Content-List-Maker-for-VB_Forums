# -*- coding: utf-8 -*-
'''
CODE
'''

import os
import contextlib
import glob
from threading import Thread
import shutil
import difflib

#Make config file if missing
if not os.path.isfile(os.path.abspath('config.ini')):
    file_name = 'config.ini'
    f = open(file_name, 'a')
    f.write('[main]' + "\n")
    f.write('folder1_path = ' + "\n")
    f.write('folder2_path = ' + "\n")
    f.write('folder3_path = ' + "\n")
    f.write('folder4_path = ' + "\n")
    f.write('folder5_path = ' + "\n")
    f.write('folder6_path = ' + "\n")
    f.write('folder7_path = ' + "\n")
    f.write('check1 = off' + "\n")
    f.write('check2 = off' + "\n")
    f.write('check3 = off' + "\n")
    f.write('check4 = off' + "\n")
    f.write('check5 = off' + "\n")
    f.write('check6 = off' + "\n")
    f.write('check7 = off' + "\n")
    f.close()
    
#Make folders if missing
folder_temp_path = 'temp_files'
isExist = os.path.exists(folder_temp_path)
if not isExist:
    os.makedirs(folder_temp_path)
  
folder_temp_diff_path = 'temp_files/diff'
isExist = os.path.exists(folder_temp_diff_path)
if not isExist:
    os.makedirs(folder_temp_diff_path)
    
folder_temp_new_path = 'temp_files/new'
isExist = os.path.exists(folder_temp_new_path)
if not isExist:
    os.makedirs(folder_temp_new_path)
    
folder_temp_new_path = 'temp_files/bbcode_size'
isExist = os.path.exists(folder_temp_new_path)
if not isExist:
    os.makedirs(folder_temp_new_path)
    
folder_temp_original_path = 'temp_files/original'
isExist = os.path.exists(folder_temp_original_path)
if not isExist:
    os.makedirs(folder_temp_original_path)
    
#Make empty text files for first time run
if not os.path.isfile(os.path.abspath('temp_files/diff/folder1.txt')):
    file_name = 'temp_files/diff/folder1.txt'
    f = open(file_name, 'w')
    f.write('probably a better way to do this...also this text will go away after the 2nd run')
    f.close()
    
if not os.path.isfile(os.path.abspath('temp_files/diff/folder2.txt')):
    file_name = 'temp_files/diff/folder2.txt'
    f = open(file_name, 'w')
    f.write('probably a better way to do this...also this text will go away after the 2nd run')
    f.close()
    
if not os.path.isfile(os.path.abspath('temp_files/diff/folder3.txt')):
    file_name = 'temp_files/diff/folder3.txt'
    f = open(file_name, 'w')
    f.write('probably a better way to do this...also this text will go away after the 2nd run')
    f.close()
    
if not os.path.isfile(os.path.abspath('temp_files/diff/folder4.txt')):
    file_name = 'temp_files/diff/folder4.txt'
    f = open(file_name, 'w')
    f.write('probably a better way to do this...also this text will go away after the 2nd run')
    f.close()
    
if not os.path.isfile(os.path.abspath('temp_files/diff/folder5.txt')):
    file_name = 'temp_files/diff/folder5.txt'
    f = open(file_name, 'w')
    f.write('probably a better way to do this...also this text will go away after the 2nd run')
    f.close()
    
if not os.path.isfile(os.path.abspath('temp_files/diff/folder6.txt')):
    file_name = 'temp_files/diff/folder6.txt'
    f = open(file_name, 'w')
    f.write('probably a better way to do this...also this text will go away after the 2nd run')
    f.close()
    
if not os.path.isfile(os.path.abspath('temp_files/diff/folder7.txt')):
    file_name = 'temp_files/diff/folder7.txt'
    f = open(file_name, 'w')
    f.write('probably a better way to do this...also this text will go away after the 2nd run')
    f.close()
    
folder_content_list_file = 'temp_files/all_lists_full.txt'
folder_content_list_file1 = 'temp_files/original/folder1.txt'
folder_content_list_file2 = 'temp_files/original/folder2.txt'
folder_content_list_file3 = 'temp_files/original/folder3.txt'
folder_content_list_file4 = 'temp_files/original/folder4.txt'
folder_content_list_file5 = 'temp_files/original/folder5.txt'
folder_content_list_file6 = 'temp_files/original/folder6.txt'
folder_content_list_file7 = 'temp_files/original/folder7.txt'

folder_content_list_file1_bbs = 'temp_files/bbcode_size/folder1_bbs.txt'
folder_content_list_file2_bbs = 'temp_files/bbcode_size/folder2_bbs.txt'
folder_content_list_file3_bbs = 'temp_files/bbcode_size/folder3_bbs.txt'
folder_content_list_file4_bbs = 'temp_files/bbcode_size/folder4_bbs.txt'
folder_content_list_file5_bbs = 'temp_files/bbcode_size/folder5_bbs.txt'
folder_content_list_file6_bbs = 'temp_files/bbcode_size/folder6_bbs.txt'
folder_content_list_file7_bbs = 'temp_files/bbcode_size/folder7_bbs.txt'

folder_content_list_file1_diff = 'temp_files/diff/folder1.txt'
folder_content_list_file2_diff = 'temp_files/diff/folder2.txt'
folder_content_list_file3_diff = 'temp_files/diff/folder3.txt'
folder_content_list_file4_diff = 'temp_files/diff/folder4.txt'
folder_content_list_file5_diff = 'temp_files/diff/folder5.txt'
folder_content_list_file6_diff = 'temp_files/diff/folder6.txt'
folder_content_list_file7_diff = 'temp_files/diff/folder7.txt'

folder_content_list_file_new = 'temp_files/all_lists_new.txt'
folder_content_list_file1_new = 'temp_files/new/folder1.txt'
folder_content_list_file2_new = 'temp_files/new/folder2.txt'
folder_content_list_file3_new = 'temp_files/new/folder3.txt'
folder_content_list_file4_new = 'temp_files/new/folder4.txt'
folder_content_list_file5_new = 'temp_files/new/folder5.txt'
folder_content_list_file6_new = 'temp_files/new/folder6.txt'
folder_content_list_file7_new = 'temp_files/new/folder7.txt'

global process_update
process_update = "..."
global process_finished
global process_finished1
global process_finished2
global process_finished3
global process_finished4
global process_finished5
global process_finished6
global process_finished7
process_finished = 0
process_finished1 = 0
process_finished2 = 0
process_finished3 = 0
process_finished4 = 0
process_finished5 = 0
process_finished6 = 0
process_finished7 = 0

global process_started1
global process_started2
global process_started3
global process_started4
global process_started5
global process_started6
global process_started7
process_started1 = 0
process_started2 = 0
process_started3 = 0
process_started4 = 0
process_started5 = 0
process_started6 = 0
process_started7 = 0

global folder_size
global folder1_size
global folder2_size
global folder3_size
global folder4_size
global folder5_size
global folder6_size
global folder7_size
folder_size = 0
folder1_size = 0
folder2_size = 0
folder3_size = 0
folder4_size = 0
folder5_size = 0
folder6_size = 0
folder7_size = 0

global folder_size_format
global folder1_size_format
global folder2_size_format
global folder3_size_format
global folder4_size_format
global folder5_size_format
global folder6_size_format
global folder7_size_format

folder_size_format = ""
folder1_size_format = ""
folder2_size_format = ""
folder3_size_format = ""
folder4_size_format = ""
folder5_size_format = ""
folder6_size_format = ""
folder7_size_format = ""

global check1
global check2
global check3
global check4
global check5
global check6
global check7

def get_file_count(directory):
    totalFiles = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                totalFiles += 1
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                totalFiles += get_file_count(entry.path)
    except NotADirectoryError:
         # if `directory` isn't a directory, get the file size then
         return 1
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return totalFiles

def get_directory_size(directory):
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                total += get_directory_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total

def get_size_format(b, factor=1024, suffix="B"):
    for unit in [" ", " K", " M", " G", " T", " P", " E", " Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

def folder_list1():
    if __name__ == "__main__":
        global folder1_path
        global process_update
        global process_finished
        global process_finished1
        global process_started1
        global folder1_size
        global folder1_size_format
        folder1_size = 0
        if os.path.isfile(folder_content_list_file1):
            shutil.copyfile('temp_files/original/folder1.txt', 'temp_files/diff/folder1.txt')
        process_update = "Scanning Folder 1"
        folder_path = folder1_path.get()
        file_path = folder_content_list_file1
        file_path_bbs = folder_content_list_file1_bbs
        file_path_diff = folder_content_list_file1_diff
        file_path_new = folder_content_list_file1_new
        listname = os.path.basename(os.path.normpath(folder_path))
        directory_sizes = []
        names = []
        file_count = []
        # iterate over all the directories inside this path
        for directory in os.listdir(folder_path):
            process_update = directory
            directory = os.path.join(folder_path, directory)
            # get the size of this directory (folder)
            directory_size = get_directory_size(directory)
            # get file count of this directory (folder)
            file_count = get_file_count(directory)
            # print('Files in folder: ',file_count)
            if directory_size == 0:
                continue
            directory_sizes.append(directory_size)
            names.append(os.path.basename(directory).ljust(100, '.') + str(file_count).rjust(5, ".") + " file(s)" + get_size_format(directory_size).rjust(15, "."))
            folder1_size += directory_size
            folder1_size_format = get_size_format(folder1_size)
            with open(file_path, "w", encoding="utf-8") as o:
                with contextlib.redirect_stdout(o):
                    print(*names, sep="\n")

    #Sort file
    with open(file_path, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
    
    #Find difference from old file
    with open(file_path,'r') as f:
            d=set(f.readlines())
    with open(file_path_diff,'r') as f:
            e=set(f.readlines())
    with open(file_path_new, 'w') as f:
        for line in list(d-e):
            f.write(line)
    f.close()
    
    #Sort file
    with open(file_path_new, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
        
    #Add BB code
    process_update = "Calculating File Size in " + listname
    file_object = open(file_path, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_bbs, "w")
    file_object.write('[SPOILER=' + listname + ']' + '[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_bbs, 'a')
    file_object.write('[/SPOILER][/CODE]' + "\n")
    file_object.close()        
    
    #Add size
    file_object = open(file_path_bbs, 'a')
    file_object.write('Folder Size: ' + folder1_size_format)
    file_object.close()
    
    #Add BB code and size to new file
    file_object = open(file_path_new, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_new, "w")
    file_object.write('[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('[/CODE]' + "\n")
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('Folder Size: ' + folder1_size_format)
    file_object.close()
   
    process_update = "Finished scanning " + listname
    process_finished1 = 1
    process_finished += 1
    folder1_path_label["bg"] = "#37b151"
    pb1.stop()
        
def folder_list2():
    if __name__ == "__main__":
        global folder2_path
        global process_update
        global process_finished
        global process_finished2
        global process_started2
        global folder2_size
        global folder2_size_format
        folder2_size = 0
        if os.path.isfile(folder_content_list_file2):
            shutil.copyfile('temp_files/original/folder2.txt', 'temp_files/diff/folder2.txt')
        process_update = "Scanning Folder 2"
        folder_path = folder2_path.get()
        file_path = folder_content_list_file2
        file_path_bbs = folder_content_list_file2_bbs
        file_path_diff = folder_content_list_file2_diff
        file_path_new = folder_content_list_file2_new
        listname = os.path.basename(os.path.normpath(folder_path))
        directory_sizes = []
        names = []
        file_count = []
        # iterate over all the directories inside this path
        for directory in os.listdir(folder_path):
            process_update = directory
            directory = os.path.join(folder_path, directory)
            # get the size of this directory (folder)
            directory_size = get_directory_size(directory)
            # get file count of this directory (folder)
            file_count = get_file_count(directory)
            # print('Files in folder: ',file_count)
            if directory_size == 0:
                continue
            directory_sizes.append(directory_size)
            names.append(os.path.basename(directory).ljust(100, '.') + str(file_count).rjust(5, ".") + " file(s)" + get_size_format(directory_size).rjust(15, "."))
            folder2_size += directory_size
            folder2_size_format = get_size_format(folder2_size)
            with open(file_path, "w", encoding="utf-8") as o:
                with contextlib.redirect_stdout(o):
                    print(*names, sep="\n")
                    
    #Sort file
    with open(file_path, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
    
    #Find difference from old file
    with open(file_path,'r') as f:
            d=set(f.readlines())
    with open(file_path_diff,'r') as f:
            e=set(f.readlines())
    with open(file_path_new, 'w') as f:
        for line in list(d-e):
            f.write(line)
    f.close()
    
    #Sort file
    with open(file_path_new, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
        
    #Add BB code
    process_update = "Calculating File Size in " + listname
    file_object = open(file_path, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_bbs, "w")
    file_object.write('[SPOILER=' + listname + ']' + '[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_bbs, 'a')
    file_object.write('[/SPOILER][/CODE]' + "\n")
    file_object.close()        
    
    #Add size
    file_object = open(file_path_bbs, 'a')
    file_object.write('Folder Size: ' + folder2_size_format)
    file_object.close()
    
    #Add BB code and size to new file
    file_object = open(file_path_new, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_new, "w")
    file_object.write('[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('[/CODE]' + "\n")
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('Folder Size: ' + folder2_size_format)
    file_object.close()
   
    process_update = "Finished scanning " + listname
    process_finished2 = 1
    process_finished += 1
    folder2_path_label["bg"] = "#37b151"
    pb2.stop()
    
def folder_list3():
    if __name__ == "__main__":
        global folder3_path
        global process_update
        global process_finished
        global process_finished3
        global process_started3
        global folder3_size
        global folder3_size_format
        folder3_size = 0
        if os.path.isfile(folder_content_list_file3):
            shutil.copyfile('temp_files/original/folder3.txt', 'temp_files/diff/folder3.txt')
        process_update = "Scanning Folder 3"
        folder_path = folder3_path.get()
        file_path = folder_content_list_file3
        file_path_bbs = folder_content_list_file3_bbs
        file_path_diff = folder_content_list_file3_diff
        file_path_new = folder_content_list_file3_new
        listname = os.path.basename(os.path.normpath(folder_path))
        directory_sizes = []
        names = []
        file_count = []
        # iterate over all the directories inside this path
        for directory in os.listdir(folder_path):
            process_update = directory
            directory = os.path.join(folder_path, directory)
            # get the size of this directory (folder)
            directory_size = get_directory_size(directory)
            # get file count of this directory (folder)
            file_count = get_file_count(directory)
            # print('Files in folder: ',file_count)
            if directory_size == 0:
                continue
            directory_sizes.append(directory_size)
            names.append(os.path.basename(directory).ljust(100, '.') + str(file_count).rjust(5, ".") + " file(s)" + get_size_format(directory_size).rjust(15, "."))
            folder3_size += directory_size
            folder3_size_format = get_size_format(folder3_size)
            with open(file_path, "w", encoding="utf-8") as o:
                with contextlib.redirect_stdout(o):
                    print(*names, sep="\n")

    #Sort file
    with open(file_path, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
    
    #Find difference from old file
    with open(file_path,'r') as f:
            d=set(f.readlines())
    with open(file_path_diff,'r') as f:
            e=set(f.readlines())
    with open(file_path_new, 'w') as f:
        for line in list(d-e):
            f.write(line)
    f.close()
    
    #Sort file
    with open(file_path_new, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
        
    #Add BB code
    process_update = "Calculating File Size in " + listname
    file_object = open(file_path, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_bbs, "w")
    file_object.write('[SPOILER=' + listname + ']' + '[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_bbs, 'a')
    file_object.write('[/SPOILER][/CODE]' + "\n")
    file_object.close()        
    
    #Add size
    file_object = open(file_path_bbs, 'a')
    file_object.write('Folder Size: ' + folder3_size_format)
    file_object.close()
    
    #Add BB code and size to new file
    file_object = open(file_path_new, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_new, "w")
    file_object.write('[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('[/CODE]' + "\n")
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('Folder Size: ' + folder3_size_format)
    file_object.close()
   
    process_update = "Finished scanning " + listname
    process_finished3 = 1
    process_finished += 1
    folder3_path_label["bg"] = "#37b151"
    pb3.stop()

def folder_list4():
    if __name__ == "__main__":
        global folder4_path
        global process_update
        global process_finished
        global process_finished4
        global process_started4
        global folder4_size
        global folder4_size_format
        folder4_size = 0
        if os.path.isfile(folder_content_list_file4):
            shutil.copyfile('temp_files/original/folder4.txt', 'temp_files/diff/folder4.txt')
        process_update = "Scanning Folder 4"
        folder_path = folder4_path.get()
        file_path = folder_content_list_file4
        file_path_bbs = folder_content_list_file4_bbs
        file_path_diff = folder_content_list_file4_diff
        file_path_new = folder_content_list_file4_new
        listname = os.path.basename(os.path.normpath(folder_path))
        directory_sizes = []
        names = []
        file_count = []
        # iterate over all the directories inside this path
        for directory in os.listdir(folder_path):
            process_update = directory
            directory = os.path.join(folder_path, directory)
            # get the size of this directory (folder)
            directory_size = get_directory_size(directory)
            # get file count of this directory (folder)
            file_count = get_file_count(directory)
            # print('Files in folder: ',file_count)
            if directory_size == 0:
                continue
            directory_sizes.append(directory_size)
            names.append(os.path.basename(directory).ljust(100, '.') + str(file_count).rjust(5, ".") + " file(s)" + get_size_format(directory_size).rjust(15, "."))
            folder4_size += directory_size
            folder4_size_format = get_size_format(folder4_size)
            with open(file_path, "w", encoding="utf-8") as o:
                with contextlib.redirect_stdout(o):
                    print(*names, sep="\n")

    #Sort file
    with open(file_path, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
    
    #Find difference from old file
    with open(file_path,'r') as f:
            d=set(f.readlines())
    with open(file_path_diff,'r') as f:
            e=set(f.readlines())
    with open(file_path_new, 'w') as f:
        for line in list(d-e):
            f.write(line)
    f.close()
    
    #Sort file
    with open(file_path_new, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
        
    #Add BB code
    process_update = "Calculating File Size in " + listname
    file_object = open(file_path, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_bbs, "w")
    file_object.write('[SPOILER=' + listname + ']' + '[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_bbs, 'a')
    file_object.write('[/SPOILER][/CODE]' + "\n")
    file_object.close()        
    
    #Add size
    file_object = open(file_path_bbs, 'a')
    file_object.write('Folder Size: ' + folder4_size_format)
    file_object.close()
    
    #Add BB code and size to new file
    file_object = open(file_path_new, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_new, "w")
    file_object.write('[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('[/CODE]' + "\n")
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('Folder Size: ' + folder4_size_format)
    file_object.close()
   
    process_update = "Finished scanning " + listname
    process_finished4 = 1
    process_finished += 1
    folder4_path_label["bg"] = "#37b151"
    pb4.stop()
    
def folder_list5():
    if __name__ == "__main__":
        global folder5_path
        global process_update
        global process_finished
        global process_finished5
        global process_started5
        global folder5_size
        global folder5_size_format
        folder5_size = 0
        if os.path.isfile(folder_content_list_file5):
            shutil.copyfile('temp_files/original/folder5.txt', 'temp_files/diff/folder5.txt')
        process_update = "Scanning Folder 5"
        folder_path = folder5_path.get()
        file_path = folder_content_list_file5
        file_path_bbs = folder_content_list_file5_bbs
        file_path_diff = folder_content_list_file5_diff
        file_path_new = folder_content_list_file5_new
        listname = os.path.basename(os.path.normpath(folder_path))
        directory_sizes = []
        names = []
        file_count = []
        # iterate over all the directories inside this path
        for directory in os.listdir(folder_path):
            process_update = directory
            directory = os.path.join(folder_path, directory)
            # get the size of this directory (folder)
            directory_size = get_directory_size(directory)
            # get file count of this directory (folder)
            file_count = get_file_count(directory)
            # print('Files in folder: ',file_count)
            if directory_size == 0:
                continue
            directory_sizes.append(directory_size)
            names.append(os.path.basename(directory).ljust(100, '.') + str(file_count).rjust(5, ".") + " file(s)" + get_size_format(directory_size).rjust(15, "."))
            folder5_size += directory_size
            folder5_size_format = get_size_format(folder5_size)
            with open(file_path, "w", encoding="utf-8") as o:
                with contextlib.redirect_stdout(o):
                    print(*names, sep="\n")

    #Sort file
    with open(file_path, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
    
    #Find difference from old file
    with open(file_path,'r') as f:
            d=set(f.readlines())
    with open(file_path_diff,'r') as f:
            e=set(f.readlines())
    with open(file_path_new, 'w') as f:
        for line in list(d-e):
            f.write(line)
    f.close()
    
    #Sort file
    with open(file_path_new, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
        
    #Add BB code
    process_update = "Calculating File Size in " + listname
    file_object = open(file_path, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_bbs, "w")
    file_object.write('[SPOILER=' + listname + ']' + '[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_bbs, 'a')
    file_object.write('[/SPOILER][/CODE]' + "\n")
    file_object.close()        
    
    #Add size
    file_object = open(file_path_bbs, 'a')
    file_object.write('Folder Size: ' + folder5_size_format)
    file_object.close()
    
    #Add BB code and size to new file
    file_object = open(file_path_new, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_new, "w")
    file_object.write('[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('[/CODE]' + "\n")
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('Folder Size: ' + folder5_size_format)
    file_object.close()
   
    process_update = "Finished scanning " + listname
    process_finished5 = 1
    process_finished += 1
    folder5_path_label["bg"] = "#37b151"
    pb5.stop()
    
def folder_list6():
    if __name__ == "__main__":
        global folder6_path
        global process_update
        global process_finished
        global process_finished6
        global process_started6
        global folder6_size
        global folder6_size_format
        folder6_size = 0
        if os.path.isfile(folder_content_list_file6):
            shutil.copyfile('temp_files/original/folder6.txt', 'temp_files/diff/folder6.txt')
        process_update = "Scanning Folder 6"
        folder_path = folder6_path.get()
        file_path = folder_content_list_file6
        file_path_bbs = folder_content_list_file6_bbs
        file_path_diff = folder_content_list_file6_diff
        file_path_new = folder_content_list_file6_new
        listname = os.path.basename(os.path.normpath(folder_path))
        directory_sizes = []
        names = []
        file_count = []
        # iterate over all the directories inside this path
        for directory in os.listdir(folder_path):
            process_update = directory
            directory = os.path.join(folder_path, directory)
            # get the size of this directory (folder)
            directory_size = get_directory_size(directory)
            # get file count of this directory (folder)
            file_count = get_file_count(directory)
            # print('Files in folder: ',file_count)
            if directory_size == 0:
                continue
            directory_sizes.append(directory_size)
            names.append(os.path.basename(directory).ljust(100, '.') + str(file_count).rjust(5, ".") + " file(s)" + get_size_format(directory_size).rjust(15, "."))
            folder6_size += directory_size
            folder6_size_format = get_size_format(folder6_size)
            with open(file_path, "w", encoding="utf-8") as o:
                with contextlib.redirect_stdout(o):
                    print(*names, sep="\n")

    #Sort file
    with open(file_path, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
    
    #Find difference from old file
    with open(file_path,'r') as f:
            d=set(f.readlines())
    with open(file_path_diff,'r') as f:
            e=set(f.readlines())
    with open(file_path_new, 'w') as f:
        for line in list(d-e):
            f.write(line)
    f.close()
    
    #Sort file
    with open(file_path_new, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
        
    #Add BB code
    process_update = "Calculating File Size in " + listname
    file_object = open(file_path, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_bbs, "w")
    file_object.write('[SPOILER=' + listname + ']' + '[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_bbs, 'a')
    file_object.write('[/SPOILER][/CODE]' + "\n")
    file_object.close()        
    
    #Add size
    file_object = open(file_path_bbs, 'a')
    file_object.write('Folder Size: ' + folder6_size_format)
    file_object.close()
    
    #Add BB code and size to new file
    file_object = open(file_path_new, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_new, "w")
    file_object.write('[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('[/CODE]' + "\n")
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('Folder Size: ' + folder6_size_format)
    file_object.close()
   
    process_update = "Finished scanning " + listname
    process_finished6 = 1
    process_finished += 1
    folder6_path_label["bg"] = "#37b151"
    pb6.stop()
   
def folder_list7():
    if __name__ == "__main__":
        global folder7_path
        global process_update
        global process_finished
        global process_finished7
        global process_started7
        global folder7_size
        global folder7_size_format
        folder7_size = 0
        if os.path.isfile(folder_content_list_file7):
            shutil.copyfile('temp_files/original/folder7.txt', 'temp_files/diff/folder7.txt')
        process_update = "Scanning Folder 7"
        folder_path = folder7_path.get()
        file_path = folder_content_list_file7
        file_path_bbs = folder_content_list_file7_bbs
        file_path_diff = folder_content_list_file7_diff
        file_path_new = folder_content_list_file7_new
        listname = os.path.basename(os.path.normpath(folder_path))
        directory_sizes = []
        names = []
        file_count = []
        # iterate over all the directories inside this path
        for directory in os.listdir(folder_path):
            process_update = directory
            directory = os.path.join(folder_path, directory)
            # get the size of this directory (folder)
            directory_size = get_directory_size(directory)
            # get file count of this directory (folder)
            file_count = get_file_count(directory)
            # print('Files in folder: ',file_count)
            if directory_size == 0:
                continue
            directory_sizes.append(directory_size)
            names.append(os.path.basename(directory).ljust(100, '.') + str(file_count).rjust(5, ".") + " file(s)" + get_size_format(directory_size).rjust(15, "."))
            folder7_size += directory_size
            folder7_size_format = get_size_format(folder7_size)
            with open(file_path, "w", encoding="utf-8") as o:
                with contextlib.redirect_stdout(o):
                    print(*names, sep="\n")

    #Sort file
    with open(file_path, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
    
    #Find difference from old file
    with open(file_path,'r') as f:
            d=set(f.readlines())
    with open(file_path_diff,'r') as f:
            e=set(f.readlines())
    with open(file_path_new, 'w') as f:
        for line in list(d-e):
            f.write(line)
    f.close()
    
    #Sort file
    with open(file_path_new, 'r+') as f:
        sorted_contents =  ''.join(sorted(f.readlines(), key = lambda x: str(x.split(' ')[0])))
        f.seek(0)
        f.truncate()
        f.write(sorted_contents)
    f.close()
        
    #Add BB code
    process_update = "Calculating File Size in " + listname
    file_object = open(file_path, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_bbs, "w")
    file_object.write('[SPOILER=' + listname + ']' + '[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_bbs, 'a')
    file_object.write('[/SPOILER][/CODE]' + "\n")
    file_object.close()        
    
    #Add size
    file_object = open(file_path_bbs, 'a')
    file_object.write('Folder Size: ' + folder7_size_format)
    file_object.close()
    
    #Add BB code and size to new file
    file_object = open(file_path_new, "r")
    original_text = file_object.read()
    file_object.close()
    file_object = open(file_path_new, "w")
    file_object.write('[b]' + listname + '[/b][CODE]' + "\n")
    file_object.write(original_text)
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('[/CODE]' + "\n")
    file_object.close()
    file_object = open(file_path_new, 'a')
    file_object.write('Folder Size: ' + folder7_size_format)
    file_object.close()
   
    process_update = "Finished scanning " + listname
    process_finished7 = 1
    process_finished += 1
    folder7_path_label["bg"] = "#37b151"
    pb7.stop()

'''
GUI
'''

import tkinter.font as tkFont
from tkinter import *
from tkinter import filedialog
from configparser import ConfigParser
from tkinter.ttk import Progressbar
import tkinter as tk

root = Tk()
root.title("Folder Content List Maker v.6.2")
root.geometry("815x490")
root.resizable(width=False, height=False)

title_label = Label(root)
ft = tkFont.Font(family='Times', size=32)
title_label["font"] = ft
title_label["fg"] = "#333333"
title_label["justify"] = "center"
title_label["text"] = "FOLDER CONTENT LIST MAKER"
title_label["relief"] = "flat"
title_label.place(x=0, y=0, width=815, height=60)

config = ConfigParser()
config.read('config.ini')

folder1_path = (config.get('main', 'folder1_path'))
folder2_path = (config.get('main', 'folder2_path'))
folder3_path = (config.get('main', 'folder3_path'))
folder4_path = (config.get('main', 'folder4_path'))
folder5_path = (config.get('main', 'folder5_path'))
folder6_path = (config.get('main', 'folder6_path'))
folder7_path = (config.get('main', 'folder7_path'))

check1 = (config.get('main', 'check1'))
check2 = (config.get('main', 'check2'))
check3 = (config.get('main', 'check3'))
check4 = (config.get('main', 'check4'))
check5 = (config.get('main', 'check5'))
check6 = (config.get('main', 'check6'))
check7 = (config.get('main', 'check7'))

# Creating a photoimage objects
photo_browse = PhotoImage(file ='temp_files/img/browse.png')
photo_scan = PhotoImage(file ='temp_files/img/scan.png')
photo_single_list = PhotoImage(file ='temp_files/img/single_list.png')
photo_single_list_new = PhotoImage(file ='temp_files/img/single_list_new.png')
# Resizing images to fit on button
photoimage_browse = photo_browse.subsample(4, 4)
photoimage_scan = photo_scan.subsample(4, 4)
photoimage_single_list = photo_single_list.subsample(4, 4)
photoimage_single_list_new = photo_single_list_new.subsample(4, 4)

# Checkboxes
def display_input():
   global check1
   global check2
   global check3
   global check4
   global check5
   global check6
   global check7
      
   config.set('main', 'check1', check1.get())
   with open('config.ini', 'w') as f:
       config.write(f)
       
   config.set('main', 'check2', check2.get())
   with open('config.ini', 'w') as f:
       config.write(f)
    
   config.set('main', 'check3', check3.get())
   with open('config.ini', 'w') as f:
       config.write(f)
      
   config.set('main', 'check4', check4.get())
   with open('config.ini', 'w') as f:
       config.write(f)

   config.set('main', 'check5', check5.get())
   with open('config.ini', 'w') as f:
       config.write(f)

   config.set('main', 'check6', check6.get())
   with open('config.ini', 'w') as f:
       config.write(f)

   config.set('main', 'check7', check7.get())
   with open('config.ini', 'w') as f:
       config.write(f)

check1 = StringVar()
check2 = StringVar()
check3 = StringVar()
check4 = StringVar()
check5 = StringVar()
check6 = StringVar()
check7 = StringVar()

check1 = StringVar(root, (config.get('main', 'check1')), 'PY_VAR12')
check2 = StringVar(root, (config.get('main', 'check2')), 'PY_VAR13')
check3 = StringVar(root, (config.get('main', 'check3')), 'PY_VAR14')
check4 = StringVar(root, (config.get('main', 'check4')), 'PY_VAR15')
check5 = StringVar(root, (config.get('main', 'check5')), 'PY_VAR16')
check6 = StringVar(root, (config.get('main', 'check6')), 'PY_VAR17')
check7 = StringVar(root, (config.get('main', 'check7')), 'PY_VAR18')

t1 = Checkbutton(variable=check1, onvalue="on", offvalue="off", command=display_input)
t1.place(x=440, y=70)
if check1 == 'on':
    t1.select()

t2 = Checkbutton(variable=check2, onvalue="on", offvalue="off", command=display_input)
t2.place(x=440, y=110)
if check2 == 'on':
    t2.select()
    
t3 = Checkbutton(variable=check3, onvalue="on", offvalue="off", command=display_input)
t3.place(x=440, y=150)
if check3 == 'on':
    t5.select()

t4 = Checkbutton(variable=check4, onvalue="on", offvalue="off", command=display_input)
t4.place(x=440, y=190)
if check4 == 'on':
    t4.select()

t5 = Checkbutton(variable=check5, onvalue="on", offvalue="off", command=display_input)
t5.place(x=440, y=230)
if check5 == 'on':
    t5.select()

t6 = Checkbutton(variable=check6, onvalue="on", offvalue="off", command=display_input)
t6.place(x=440, y=270)
if check6 == 'on':
    t6.select()

t7 = Checkbutton(variable=check7, onvalue="on", offvalue="off", command=display_input)
t7.place(x=440, y=310)
if check7 == 'on':
    t7.select()

def make_list1_button():
    if __name__ == '__main__':
        Thread(target = folder_list1).start()
        Thread(target = pb1.start).start()
        
def make_list2_button():
    if __name__ == '__main__':
        Thread(target = folder_list2).start()
        Thread(target = pb2.start).start()
        
def make_list3_button():
    if __name__ == '__main__':
        Thread(target = folder_list3).start()
        Thread(target = pb3.start).start()
        
def make_list4_button():
    if __name__ == '__main__':
        Thread(target = folder_list4).start()
        Thread(target = pb4.start).start()
        
def make_list5_button():
    if __name__ == '__main__':
        Thread(target = folder_list5).start()
        Thread(target = pb5.start).start()
        
def make_list6_button():
    if __name__ == '__main__':
        Thread(target = folder_list6).start()
        Thread(target = pb6.start).start()
        
def make_list7_button():
    if __name__ == '__main__':
        Thread(target = folder_list7).start()
        Thread(target = pb7.start).start()

def browse_button1():
    global folder1_path
    filename = filedialog.askdirectory()
    folder1_path.set(filename)
    config.set('main', 'folder1_path', folder1_path.get())
    print(folder1_path.get())
    with open('config.ini', 'w') as f:
        config.write(f)
    folder1_path_label["bg"] = "#f0f0f0"
    
def browse_button2():
    global folder2_path
    filename = filedialog.askdirectory()
    folder2_path.set(filename)
    config.set('main', 'folder2_path', folder2_path.get())
    print(folder2_path.get())
    with open('config.ini', 'w') as f:
        config.write(f)
    folder2_path_label["bg"] = "#f0f0f0"
        
def browse_button3():
    global folder3_path
    filename = filedialog.askdirectory()
    folder3_path.set(filename)
    config.set('main', 'folder3_path', folder3_path.get())
    print(folder3_path.get())
    with open('config.ini', 'w') as f:
        config.write(f)
    folder3_path_label["bg"] = "#f0f0f0"
        
def browse_button4():
    global folder4_path
    filename = filedialog.askdirectory()
    folder4_path.set(filename)
    config.set('main', 'folder4_path', folder4_path.get())
    print(folder4_path.get())
    with open('config.ini', 'w') as f:
        config.write(f)
    folder4_path_label["bg"] = "#f0f0f0"
        
def browse_button5():
    global folder5_path
    filename = filedialog.askdirectory()
    folder5_path.set(filename)
    config.set('main', 'folder5_path', folder5_path.get())
    print(folder5_path.get())
    with open('config.ini', 'w') as f:
        config.write(f)
    folder5_path_label["bg"] = "#f0f0f0"
        
def browse_button6():
    global folder6_path
    filename = filedialog.askdirectory()
    folder6_path.set(filename)
    config.set('main', 'folder6_path', folder6_path.get())
    print(folder6_path.get())
    with open('config.ini', 'w') as f:
        config.write(f)
    folder6_path_label["bg"] = "#f0f0f0"
        
def browse_button7():
    global folder7_path
    filename = filedialog.askdirectory()
    folder7_path.set(filename)
    config.set('main', 'folder7_path', folder7_path.get())
    print(folder7_path.get())
    with open('config.ini', 'w') as f:
        config.write(f)
    folder7_path_label["bg"] = "#f0f0f0"
        
def open_orginal_list1():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file1_bbs)):
        os.startfile(os.path.abspath(folder_content_list_file1_bbs))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_orginal_list2():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file2_bbs)):
        os.startfile(os.path.abspath(folder_content_list_file2_bbs))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_orginal_list3():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file3_bbs)):
        os.startfile(os.path.abspath(folder_content_list_file3_bbs))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_orginal_list4():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file4_bbs)):
        os.startfile(os.path.abspath(folder_content_list_file4_bbs))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_orginal_list5():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file5_bbs)):
        os.startfile(os.path.abspath(folder_content_list_file5_bbs))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_orginal_list6():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file6_bbs)):
        os.startfile(os.path.abspath(folder_content_list_file6_bbs))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_orginal_list7():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file7_bbs)):
        os.startfile(os.path.abspath(folder_content_list_file7_bbs))
        process_update = ""
    else:
        process_update = "No file found!"

def open_orginal_list():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file)):
        os.startfile(os.path.abspath(folder_content_list_file))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_new_list1():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file1_new)):
        os.startfile(os.path.abspath(folder_content_list_file1_new))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_new_list2():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file2_new)):
        os.startfile(os.path.abspath(folder_content_list_file2_new))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_new_list3():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file3_new)):
        os.startfile(os.path.abspath(folder_content_list_file3_new))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_new_list4():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file4_new)):
        os.startfile(os.path.abspath(folder_content_list_file4_new))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_new_list5():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file5_new)):
        os.startfile(os.path.abspath(folder_content_list_file5_new))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_new_list6():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file6_new)):
        os.startfile(os.path.abspath(folder_content_list_file6_new))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_new_list7():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file7_new)):
        os.startfile(os.path.abspath(folder_content_list_file7_new))
        process_update = ""
    else:
        process_update = "No file found!"
        
def open_new_list():
    global process_update
    if os.path.isfile(os.path.abspath(folder_content_list_file_new)):
        os.startfile(os.path.abspath(folder_content_list_file_new))
        process_update = ""
    else:
        process_update = "No file found!"
        
def full_list():
    global process_finished
    global check1
    global check2
    global check3
    global check4
    global check5
    global check6
    global check7
    global check1_str
    global check2_str
    global check3_str
    global check4_str
    global check5_str
    global check6_str
    global check7_str
    check1_str = check1.get()
    check2_str = check2.get()
    check3_str = check3.get()
    check4_str = check4.get()
    check5_str = check5.get()
    check6_str = check6.get()
    check7_str = check7.get()
    process_finished = 0
    process_finished1 = 0
    process_finished2 = 0
    process_finished3 = 0
    process_finished4 = 0
    process_finished5 = 0
    process_finished6 = 0
    process_finished7 = 0
        
    global numbers_of_folders_to_check
    numbers_of_folders_to_check = 0
    
    if check1_str == "on":
        numbers_of_folders_to_check += 1
    if check2_str == "on":
        numbers_of_folders_to_check += 1
    if check3_str == "on":
        numbers_of_folders_to_check += 1
    if check4_str == "on":
        numbers_of_folders_to_check += 1
    if check5_str == "on":
        numbers_of_folders_to_check += 1
    if check6_str == "on":
        numbers_of_folders_to_check += 1
    if check7_str == "on":
        numbers_of_folders_to_check += 1
    
    if check1_str == "on":
        if process_finished1 == 0:
                make_list1_button()
    
    if check2_str == "on":
        if process_finished2 == 0:
                make_list2_button()
    
    if check3_str == "on":
        if process_finished3 == 0:
                make_list3_button()
    
    if check4_str == "on":
        if process_finished4 == 0:
                make_list4_button()
    
    if check5_str == "on":
        if process_finished5 == 0:
                make_list5_button()
    
    if check6_str == "on":
        if process_finished6 == 0:
                make_list6_button()
    
    if check7_str == "on":
        if process_finished7 == 0:
                make_list7_button()
            
    root.after(1000, every_second)
    
def every_second():
    global process_update
    global process_finished
    global numbers_of_folders_to_check
    stop_update = root.after(1000, every_second)
    if process_finished == numbers_of_folders_to_check:
        
        check1_str = check1.get()
        check2_str = check2.get()
        check3_str = check3.get()
        check4_str = check4.get()
        check5_str = check5.get()
        check6_str = check6.get()
        check7_str = check7.get()
        
        if check1_str == "on":
            if os.path.isfile(os.path.abspath(folder_content_list_file1_bbs)):
                os.rename(folder_content_list_file1_bbs, 'temp_files/bbcode_size/folder1_on.txt')
                os.rename(folder_content_list_file1_new, 'temp_files/new/folder1_on.txt')

        if check2_str == "on":
            if os.path.isfile(os.path.abspath(folder_content_list_file2_bbs)):
                os.rename(folder_content_list_file2_bbs, 'temp_files/bbcode_size/folder2_on.txt') 
                os.rename(folder_content_list_file2_new, 'temp_files/new/folder2_on.txt')

        if check3_str == "on":
            if os.path.isfile(os.path.abspath(folder_content_list_file3_bbs)):
                os.rename(folder_content_list_file3_bbs, 'temp_files/bbcode_size/folder3_on.txt')
                os.rename(folder_content_list_file3_new, 'temp_files/new/folder3_on.txt')

        if check4_str == "on":
            if os.path.isfile(os.path.abspath(folder_content_list_file4_bbs)):
                os.rename(folder_content_list_file4_bbs, 'temp_files/bbcode_size/folder4_on.txt')
                os.rename(folder_content_list_file4_new, 'temp_files/new/folder4_on.txt')

        if check5_str == "on":
            if os.path.isfile(os.path.abspath(folder_content_list_file5_bbs)):
                os.rename(folder_content_list_file5_bbs, 'temp_files/bbcode_size/folder5_on.txt')
                os.rename(folder_content_list_file5_new, 'temp_files/new/folder5_on.txt')

        if check6_str == "on":
            if os.path.isfile(os.path.abspath(folder_content_list_file6_bbs)):
                os.rename(folder_content_list_file6_bbs, 'temp_files/bbcode_size/folder6_on.txt')
                os.rename(folder_content_list_file6_new, 'temp_files/new/folder6_on.txt')

        if check7_str == "on":
            if os.path.isfile(os.path.abspath(folder_content_list_file7_bbs)):
                os.rename(folder_content_list_file7_bbs, 'temp_files/bbcode_size/folder7_on.txt')
                os.rename(folder_content_list_file7_new, 'temp_files/new/folder7_on.txt')

        filenames = glob.glob("temp_files/bbcode_size/*_on.txt")
        folder_size = float(folder1_size) + float(folder2_size) + float(folder3_size) + float(folder4_size) + float(folder5_size) + float(folder6_size) + float(folder7_size)
        folder_size_format = get_size_format(folder_size)
        with open('temp_files/all_lists_full.txt', 'w') as outfile:
            for names in filenames:
                with open(names) as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")
                    outfile.write("\n")
                    outfile.write('Total Folder Size: ' + folder_size_format)
                        
        filenames = glob.glob("temp_files/new/*_on.txt")
        with open('temp_files/all_lists_new.txt', 'w') as outfile:
            for names in filenames:
                with open(names) as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")
                    outfile.write("\n")
        
        if check1_str == "on":
            if os.path.isfile(os.path.abspath('temp_files/bbcode_size/folder1_on.txt')):
                os.rename('temp_files/bbcode_size/folder1_on.txt', folder_content_list_file1_bbs)
                os.rename('temp_files/new/folder1_on.txt', folder_content_list_file1_new)

        if check2_str == "on":
            if os.path.isfile(os.path.abspath('temp_files/bbcode_size/folder2_on.txt')):
                os.rename('temp_files/bbcode_size/folder2_on.txt', folder_content_list_file2_bbs)
                os.rename('temp_files/new/folder2_on.txt', folder_content_list_file2_new)

        if check3_str == "on":
            if os.path.isfile(os.path.abspath('temp_files/bbcode_size/folder3_on.txt')):
                os.rename('temp_files/bbcode_size/folder3_on.txt', folder_content_list_file3_bbs)
                os.rename('temp_files/new/folder3_on.txt', folder_content_list_file3_new)

        if check4_str == "on":
            if os.path.isfile(os.path.abspath('temp_files/bbcode_size/folder4_on.txt')):
                os.rename('temp_files/bbcode_size/folder4_on.txt', folder_content_list_file4_bbs)
                os.rename('temp_files/new/folder4_on.txt', folder_content_list_file4_new)

        if check5_str == "on":
            if os.path.isfile(os.path.abspath('temp_files/bbcode_size/folder5_on.txt')):
                os.rename('temp_files/bbcode_size/folder5_on.txt', folder_content_list_file5_bbs)
                os.rename('temp_files/new/folder5_on.txt', folder_content_list_file5_new)

        if check6_str == "on":
            if os.path.isfile(os.path.abspath('temp_files/bbcode_size/folder6_on.txt')):
                os.rename('temp_files/bbcode_size/folder6_on.txt', folder_content_list_file6_bbs)
                os.rename('temp_files/new/folder6_on.txt', folder_content_list_file6_new)

        if check7_str == "on":
            if os.path.isfile(os.path.abspath('temp_files/bbcode_size/folder7_on.txt')):
                os.rename('temp_files/bbcode_size/folder7_on.txt', folder_content_list_file7_bbs)
                os.rename('temp_files/new/folder7_on.txt', folder_content_list_file7_new)
        
        process_update = "Finished Scanning Selected Folders"
        numbers_of_folders_to_check = 0
        root.after_cancel(stop_update)

        
folder1_path = StringVar(root, (config.get('main', 'folder1_path')), 'PY_VAR1')
folder2_path = StringVar(root, (config.get('main', 'folder2_path')), 'PY_VAR2')
folder3_path = StringVar(root, (config.get('main', 'folder3_path')), 'PY_VAR3')
folder4_path = StringVar(root, (config.get('main', 'folder4_path')), 'PY_VAR4')
folder5_path = StringVar(root, (config.get('main', 'folder5_path')), 'PY_VAR5')
folder6_path = StringVar(root, (config.get('main', 'folder6_path')), 'PY_VAR6')
folder7_path = StringVar(root, (config.get('main', 'folder7_path')), 'PY_VAR7')

#Folder paths
folder1_path_label = Label(root)
folder1_path_label["anchor"] = "w"
ft = tkFont.Font(family='Times', size=12)
folder1_path_label["font"] = ft
folder1_path_label["fg"] = "#333333"
folder1_path_label["justify"] = "left"
folder1_path_label["textvariable"] = folder1_path
folder1_path_label["relief"] = "sunken"
folder1_path_label.place(x=30, y=70, width=400, height=25)

folder2_path_label = Label(root)
folder2_path_label["anchor"] = "w"
ft = tkFont.Font(family='Times', size=12)
folder2_path_label["font"] = ft
folder2_path_label["fg"] = "#333333"
folder2_path_label["justify"] = "left"
folder2_path_label["textvariable"] = folder2_path
folder2_path_label["relief"] = "sunken"
folder2_path_label.place(x=30, y=110, width=400, height=25)

folder3_path_label = Label(root)
folder3_path_label["anchor"] = "w"
ft = tkFont.Font(family='Times', size=12)
folder3_path_label["font"] = ft
folder3_path_label["fg"] = "#333333"
folder3_path_label["justify"] = "left"
folder3_path_label["textvariable"] = folder3_path
folder3_path_label["relief"] = "sunken"
folder3_path_label.place(x=30, y=150, width=400, height=25)

folder4_path_label = Label(root)
folder4_path_label["anchor"] = "w"
ft = tkFont.Font(family='Times', size=12)
folder4_path_label["font"] = ft
folder4_path_label["fg"] = "#333333"
folder4_path_label["justify"] = "left"
folder4_path_label["textvariable"] = folder4_path
folder4_path_label["relief"] = "sunken"
folder4_path_label.place(x=30, y=190, width=400, height=25)

folder5_path_label = Label(root)
folder5_path_label["anchor"] = "w"
ft = tkFont.Font(family='Times', size=12)
folder5_path_label["font"] = ft
folder5_path_label["fg"] = "#333333"
folder5_path_label["justify"] = "left"
folder5_path_label["textvariable"] = folder5_path
folder5_path_label["relief"] = "sunken"
folder5_path_label.place(x=30, y=230, width=400, height=25)

folder6_path_label = Label(root)
folder6_path_label["anchor"] = "w"
ft = tkFont.Font(family='Times', size=12)
folder6_path_label["font"] = ft
folder6_path_label["fg"] = "#333333"
folder6_path_label["justify"] = "left"
folder6_path_label["textvariable"] = folder6_path
folder6_path_label["relief"] = "sunken"
folder6_path_label.place(x=30, y=270, width=400, height=25)

folder7_path_label = Label(root)
folder7_path_label["anchor"] = "w"
ft = tkFont.Font(family='Times', size=12)
folder7_path_label["font"] = ft
folder7_path_label["fg"] = "#333333"
folder7_path_label["justify"] = "left"
folder7_path_label["textvariable"] = folder7_path
folder7_path_label["relief"] = "sunken"
folder7_path_label.place(x=30, y=310, width=400, height=25)

folder1_button = Button(root)
folder1_button["bg"] = "#efefef"
folder1_button["justify"] = "center"
folder1_button["image"] = photoimage_browse
folder1_button["relief"] = "raised"
folder1_button.place(x=470, y=60, width=45, height=35)
folder1_button["command"] = browse_button1

folder2_button = Button(root)
folder2_button["bg"] = "#efefef"
folder2_button["justify"] = "center"
folder2_button["image"] = photoimage_browse
folder2_button["relief"] = "raised"
folder2_button.place(x=470, y=100, width=45, height=35)
folder2_button["command"] = browse_button2

folder3_button = Button(root)
folder3_button["bg"] = "#efefef"
folder3_button["justify"] = "center"
folder3_button["image"] = photoimage_browse
folder3_button["relief"] = "raised"
folder3_button.place(x=470, y=140, width=45, height=35)
folder3_button["command"] = browse_button3

folder4_button = Button(root)
folder4_button["bg"] = "#efefef"
folder4_button["justify"] = "center"
folder4_button["image"] = photoimage_browse
folder4_button["relief"] = "raised"
folder4_button.place(x=470, y=180, width=45, height=35)
folder4_button["command"] = browse_button4

folder5_button = Button(root)
folder5_button["bg"] = "#efefef"
folder5_button["justify"] = "center"
folder5_button["image"] = photoimage_browse
folder5_button["relief"] = "raised"
folder5_button.place(x=470, y=220, width=45, height=35)
folder5_button["command"] = browse_button5

folder6_button = Button(root)
folder6_button["bg"] = "#efefef"
folder6_button["justify"] = "center"
folder6_button["image"] = photoimage_browse
folder6_button["relief"] = "raised"
folder6_button.place(x=470, y=260, width=45, height=35)
folder6_button["command"] = browse_button6

folder7_button = Button(root)
folder7_button["bg"] = "#efefef"
folder7_button["justify"] = "center"
folder7_button["image"] = photoimage_browse
folder7_button["relief"] = "raised"
folder7_button.place(x=470, y=300, width=45, height=35)
folder7_button["command"] = browse_button7

folder1_makelist_button = Button(root)
folder1_makelist_button["bg"] = "#efefef"
folder1_makelist_button["justify"] = "center"
folder1_makelist_button["image"] = photoimage_scan
folder1_makelist_button["relief"] = "raised"
folder1_makelist_button.place(x=525, y=60, width=45, height=35)
folder1_makelist_button["command"] = make_list1_button

folder2_makelist_button = Button(root)
folder2_makelist_button["bg"] = "#efefef"
folder2_makelist_button["justify"] = "center"
folder2_makelist_button["image"] = photoimage_scan
folder2_makelist_button["relief"] = "raised"
folder2_makelist_button.place(x=525, y=100, width=45, height=35)
folder2_makelist_button["command"] = make_list2_button

folder3_makelist_button = Button(root)
folder3_makelist_button["bg"] = "#efefef"
folder3_makelist_button["justify"] = "center"
folder3_makelist_button["image"] = photoimage_scan
folder3_makelist_button["relief"] = "raised"
folder3_makelist_button.place(x=525, y=140, width=45, height=35)
folder3_makelist_button["command"] = make_list3_button

folder4_makelist_button = Button(root)
folder4_makelist_button["bg"] = "#efefef"
folder4_makelist_button["justify"] = "center"
folder4_makelist_button["image"] = photoimage_scan
folder4_makelist_button["relief"] = "raised"
folder4_makelist_button.place(x=525, y=180, width=45, height=35)
folder4_makelist_button["command"] = make_list4_button

folder5_makelist_button = Button(root)
folder5_makelist_button["bg"] = "#efefef"
folder5_makelist_button["justify"] = "center"
folder5_makelist_button["image"] = photoimage_scan
folder5_makelist_button["relief"] = "raised"
folder5_makelist_button.place(x=525, y=220, width=45, height=35)
folder5_makelist_button["command"] = make_list5_button

folder6_makelist_button = Button(root)
folder6_makelist_button["bg"] = "#efefef"
folder6_makelist_button["justify"] = "center"
folder6_makelist_button["image"] = photoimage_scan
folder6_makelist_button["relief"] = "raised"
folder6_makelist_button.place(x=525, y=260, width=45, height=35)
folder6_makelist_button["command"] = make_list6_button

folder7_makelist_button = Button(root)
folder7_makelist_button["bg"] = "#efefef"
folder7_makelist_button["justify"] = "center"
folder7_makelist_button["image"] = photoimage_scan
folder7_makelist_button["relief"] = "raised"
folder7_makelist_button.place(x=525, y=300, width=45, height=35)
folder7_makelist_button["command"] = make_list7_button

folder1_open_list_org_button = Button(root)
folder1_open_list_org_button["fg"] = "#000000"
folder1_open_list_org_button["justify"] = "center"
folder1_open_list_org_button["image"] = photoimage_single_list
folder1_open_list_org_button["relief"] = "raised"
folder1_open_list_org_button.place(x=580, y=60, width=45, height=35)
folder1_open_list_org_button["command"] = open_orginal_list1

folder2_open_list_org_button = Button(root)
folder2_open_list_org_button["bg"] = "#efefef"
folder2_open_list_org_button["justify"] = "center"
folder2_open_list_org_button["image"] = photoimage_single_list
folder2_open_list_org_button["relief"] = "raised"
folder2_open_list_org_button.place(x=580, y=100, width=45, height=35)
folder2_open_list_org_button["command"] = open_orginal_list2

folder3_open_list_org_button = Button(root)
folder3_open_list_org_button["bg"] = "#efefef"
folder3_open_list_org_button["justify"] = "center"
folder3_open_list_org_button["image"] = photoimage_single_list
folder3_open_list_org_button["relief"] = "raised"
folder3_open_list_org_button.place(x=580, y=140, width=45, height=35)
folder3_open_list_org_button["command"] = open_orginal_list3

folder4_open_list_org_button = Button(root)
folder4_open_list_org_button["fg"] = "#000000"
folder4_open_list_org_button["justify"] = "center"
folder4_open_list_org_button["image"] = photoimage_single_list
folder4_open_list_org_button["relief"] = "raised"
folder4_open_list_org_button.place(x=580, y=180, width=45, height=35)
folder4_open_list_org_button["command"] = open_orginal_list4

folder5_open_list_org_button = Button(root)
folder5_open_list_org_button["bg"] = "#efefef"
folder5_open_list_org_button["justify"] = "center"
folder5_open_list_org_button["image"] = photoimage_single_list
folder5_open_list_org_button["relief"] = "raised"
folder5_open_list_org_button.place(x=580, y=220, width=45, height=35)
folder5_open_list_org_button["command"] = open_orginal_list5

folder6_open_list_org_button = Button(root)
folder6_open_list_org_button["bg"] = "#efefef"
folder6_open_list_org_button["justify"] = "center"
folder6_open_list_org_button["image"] = photoimage_single_list
folder6_open_list_org_button["relief"] = "raised"
folder6_open_list_org_button.place(x=580, y=260, width=45, height=35)
folder6_open_list_org_button["command"] = open_orginal_list6

folder7_open_list_org_button = Button(root)
folder7_open_list_org_button["bg"] = "#efefef"
folder7_open_list_org_button["justify"] = "center"
folder7_open_list_org_button["image"] = photoimage_single_list
folder7_open_list_org_button["relief"] = "raised"
folder7_open_list_org_button.place(x=580, y=300, width=45, height=35)
folder7_open_list_org_button["command"] = open_orginal_list7

folder1_open_list_new_button = Button(root)
folder1_open_list_new_button["bg"] = "#efefef"
folder1_open_list_new_button["justify"] = "center"
folder1_open_list_new_button["image"] = photoimage_single_list_new
folder1_open_list_new_button["relief"] = "raised"
folder1_open_list_new_button.place(x=635, y=60, width=45, height=35)
folder1_open_list_new_button["command"] = open_new_list1

folder2_open_list_new_button = Button(root)
folder2_open_list_new_button["bg"] = "#efefef"
folder2_open_list_new_button["justify"] = "center"
folder2_open_list_new_button["image"] = photoimage_single_list_new
folder2_open_list_new_button["relief"] = "raised"
folder2_open_list_new_button.place(x=635, y=100, width=45, height=35)
folder2_open_list_new_button["command"] = open_new_list2

folder3_open_list_new_button = Button(root)
folder3_open_list_new_button["bg"] = "#efefef"
folder3_open_list_new_button["justify"] = "center"
folder3_open_list_new_button["image"] = photoimage_single_list_new
folder3_open_list_new_button["relief"] = "raised"
folder3_open_list_new_button.place(x=635, y=140, width=45, height=35)
folder3_open_list_new_button["command"] = open_new_list3

folder4_open_list_new_button = Button(root)
folder4_open_list_new_button["bg"] = "#efefef"
folder4_open_list_new_button["justify"] = "center"
folder4_open_list_new_button["image"] = photoimage_single_list_new
folder4_open_list_new_button["relief"] = "raised"
folder4_open_list_new_button.place(x=635, y=180, width=45, height=35)
folder4_open_list_new_button["command"] = open_new_list4

folder5_open_list_new_button = Button(root)
folder5_open_list_new_button["bg"] = "#efefef"
folder5_open_list_new_button["justify"] = "center"
folder5_open_list_new_button["image"] = photoimage_single_list_new
folder5_open_list_new_button["relief"] = "raised"
folder5_open_list_new_button.place(x=635, y=220, width=45, height=35)
folder5_open_list_new_button["command"] = open_new_list5

folder6_open_list_new_button = Button(root)
folder6_open_list_new_button["bg"] = "#efefef"
folder6_open_list_new_button["justify"] = "center"
folder6_open_list_new_button["image"] = photoimage_single_list_new
folder6_open_list_new_button["relief"] = "raised"
folder6_open_list_new_button.place(x=635, y=260, width=45, height=35)
folder6_open_list_new_button["command"] = open_new_list6

folder7_open_list_new_button = Button(root)
folder7_open_list_new_button["bg"] = "#efefef"
folder7_open_list_new_button["justify"] = "center"
folder7_open_list_new_button["image"] = photoimage_single_list_new
folder7_open_list_new_button["relief"] = "raised"
folder7_open_list_new_button.place(x=635, y=300, width=45, height=35)
folder7_open_list_new_button["command"] = open_new_list7

selected_label = Label(root)
ft = tkFont.Font(family='Times', size=16)
selected_label["font"] = ft
selected_label["fg"] = "#333333"
selected_label["text"] = "Selected Folders"
selected_label["relief"] = "flat"
selected_label.place(x=300, y=350, width=300, height=35)

full_list_button = Button(root)
full_list_button["bg"] = "#efefef"
full_list_button["justify"] = "center"
full_list_button["image"] = photoimage_scan
full_list_button.place(x=525, y=350, width=45, height=35)
full_list_button["command"] = full_list

full_list_open_list_org_button = Button(root)
full_list_open_list_org_button["bg"] = "#efefef"
full_list_open_list_org_button["justify"] = "center"
full_list_open_list_org_button["image"] = photoimage_single_list
full_list_open_list_org_button.place(x=580, y=350, width=45, height=35)
full_list_open_list_org_button["command"] = open_orginal_list

full_open_list_new_button = Button(root)
full_open_list_new_button["bg"] = "#efefef"
full_open_list_new_button["justify"] = "center"
full_open_list_new_button["image"] = photoimage_single_list_new
full_open_list_new_button.place(x=635, y=350, width=45, height=35)
full_open_list_new_button["command"] = open_new_list

# progressbar
pb1 = Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=400
)
pb1.place(x=30, y=60, width=400, height=10)

pb2 = Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=400
)
pb2.place(x=30, y=100, width=400, height=10)

pb3 = Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=400
)
pb3.place(x=30, y=140, width=400, height=10)

pb4 = Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=400
)
pb4.place(x=30, y=180, width=400, height=10)

pb5 = Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=400
)
pb5.place(x=30, y=220, width=400, height=10)

pb6 = Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=400
)
pb6.place(x=30, y=260, width=400, height=10)

pb7 = Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=400
)
pb7.place(x=30, y=300, width=400, height=10)

status_bar = Label(root)
status_bar["anchor"] = "center"
ft = tkFont.Font(family='Times', size=14)
status_bar["font"] = ft
status_bar["fg"] = "#333333"
status_bar["justify"] = "center"
status_bar["relief"] = "sunken"
status_bar.place(x=30, y=415, width=755, height=60)

status_folder1_size = Label(root)
status_folder1_size["anchor"] = "e"
ft = tkFont.Font(family='Times', size=14)
status_folder1_size["font"] = ft
status_folder1_size["fg"] = "#333333"
status_folder1_size["justify"] = "right"
status_folder1_size["relief"] = "sunken"
status_folder1_size.place(x=690, y=60, width=100, height=35)

status_folder2_size = Label(root)
status_folder2_size["anchor"] = "e"
ft = tkFont.Font(family='Times', size=14)
status_folder2_size["font"] = ft
status_folder2_size["fg"] = "#333333"
status_folder2_size["justify"] = "right"
status_folder2_size["relief"] = "sunken"
status_folder2_size.place(x=690, y=100, width=100, height=35)

status_folder3_size = Label(root)
status_folder3_size["anchor"] = "e"
ft = tkFont.Font(family='Times', size=14)
status_folder3_size["font"] = ft
status_folder3_size["fg"] = "#333333"
status_folder3_size["justify"] = "right"
status_folder3_size["relief"] = "sunken"
status_folder3_size.place(x=690, y=140, width=100, height=35)

status_folder4_size = Label(root)
status_folder4_size["anchor"] = "e"
ft = tkFont.Font(family='Times', size=14)
status_folder4_size["font"] = ft
status_folder4_size["fg"] = "#333333"
status_folder4_size["justify"] = "right"
status_folder4_size["relief"] = "sunken"
status_folder4_size.place(x=690, y=180, width=100, height=35)

status_folder5_size = Label(root)
status_folder5_size["anchor"] = "e"
ft = tkFont.Font(family='Times', size=14)
status_folder5_size["font"] = ft
status_folder5_size["fg"] = "#333333"
status_folder5_size["justify"] = "right"
status_folder5_size["relief"] = "sunken"
status_folder5_size.place(x=690, y=220, width=100, height=35)

status_folder6_size = Label(root)
status_folder6_size["anchor"] = "e"
ft = tkFont.Font(family='Times', size=14)
status_folder6_size["font"] = ft
status_folder6_size["fg"] = "#333333"
status_folder6_size["justify"] = "right"
status_folder6_size["relief"] = "sunken"
status_folder6_size.place(x=690, y=260, width=100, height=35)

status_folder7_size = Label(root)
status_folder7_size["anchor"] = "e"
ft = tkFont.Font(family='Times', size=14)
status_folder7_size["font"] = ft
status_folder7_size["fg"] = "#333333"
status_folder7_size["justify"] = "right"
status_folder7_size["relief"] = "sunken"
status_folder7_size.place(x=690, y=300, width=100, height=35)

status_folder_size = Label(root)
status_folder_size["anchor"] = "e"
ft = tkFont.Font(family='Times', size=14)
status_folder_size["font"] = ft
status_folder_size["fg"] = "#333333"
status_folder_size["justify"] = "right"
status_folder_size["relief"] = "sunken"
status_folder_size.place(x=690, y=350, width=100, height=35)

def refresher():
    status_bar.configure(text=process_update)
    status_folder1_size.configure(text=folder1_size_format)
    status_folder2_size.configure(text=folder2_size_format)
    status_folder3_size.configure(text=folder3_size_format)
    status_folder4_size.configure(text=folder4_size_format)
    status_folder5_size.configure(text=folder5_size_format)
    status_folder6_size.configure(text=folder6_size_format)
    status_folder7_size.configure(text=folder7_size_format)
    folder_size = float(folder1_size) + float(folder2_size) + float(folder3_size) + float(folder4_size) + float(folder5_size) + float(folder6_size) + float(folder7_size)
    folder_size_format = get_size_format(folder_size)
    status_folder_size.configure(text=folder_size_format)
    
    root.after(100, refresher)

def about():
    window = tk.Toplevel()
    canvas = tk.Canvas(window, height=10, width=500)
    window.resizable(width=False, height=False)
    lab1 = Label(window, wraplength=490, justify="center", text="Description: Create a list of folders in up to five root folders with size and file count for each folder and check if new content have been added since last run of script. Output to .txt files with [BB] code for easy posting on forums.")
    lab1.pack(pady=20)
    lab2 = Label(window, wraplength=490, justify="center", text="This script is provided as is and with all faults. You are solely responsible for determining whether this script is compatible with your equipment and other software installed on your equipment. You are also solely responsible for the protection of your equipment and backup of your data, I will not be liable for any damages you may suffer in connection with using, modifying, or distributing this script.")
    lab2.pack(pady=20)
    canvas.pack()
            
about_button = Button(root)
about_button["bg"] = "#efefef"
ft = tkFont.Font(family='Times', size=12)
about_button["font"] = ft
about_button["fg"] = "#000000"
about_button["justify"] = "center"
about_button["text"] = "About"
about_button["relief"] = "raised"
about_button.place(x=30, y=350, width=80, height=50)
about_button["command"] = lambda: about()

refresher()
mainloop()
