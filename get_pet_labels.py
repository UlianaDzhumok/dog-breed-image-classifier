##
# Imports python modules to work with directories
from os import listdir, path

def get_pet_labels(image_dir):

    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    filename_list = listdir(image_dir)
    results_dic={}
    
    for i in range(0, len(filename_list), 1):
        if not filename_list[i].startswith("."):
            
            if filename_list[i] not in results_dic:
                pet_name=""
                filename_words=path.splitext(filename_list[i])[0].split("_")

                for word in filename_words:
                    if word.isalpha():
                        pet_name += word + " "
                results_dic[filename_list[i]] = [pet_name.lower().strip()]
            else:
                print("** Warning: Key=", filename_list[i], 
               "already exists in results_dict with value =", 
                results_dic[filename_list[i]])
    
    return results_dic
