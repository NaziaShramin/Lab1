import os
import random

def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list

def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2

def process_dir(path, cat_list, dog_list):
    dir_list, file_list = get_dirs_and_files(path)

    # Your code goes here
    listOfFile = os.listdir(path)
    for file in listOfFile:
        fullPath = os.path.join(path, file)
        if os.path.isdir(fullPath):
            cat_list, dog_list = process_dir(fullPath, cat_list, dog_list)
        else:
            if file[-4:] == ".jpg": # if image type, then only consider that
                if classify_pic(path + file) < 0.5:
                    cat_list.append(file)
                else:
                    dog_list.append(file)

    return cat_list, dog_list

def main():
    start_path = 'C:/Users/Nazia/1.1 CatsDogs/1.1 CatsDogs' # current directory

    cat_list, dog_list = [], []
    cat_list, dog_list = process_dir(start_path, cat_list, dog_list)

    print("Dogs list:", dog_list)
    print("Cat list:", cat_list)
    
    #There are no real changes that one could do to the recursion method that allows it to traverse the folders and populate the lists
    #and the only addition I would include is to the interface. Such as allowing the user to choose which list to look at individually.
    #One could also place a check incase it could not find the directory and display a line of dialogue instead of an error message.
    #The use of the initialization of the lists and the way they are populated is different from my own code but it works just as well
    #and the other changes are more for the user's benefit and to protect from errors.
main()
