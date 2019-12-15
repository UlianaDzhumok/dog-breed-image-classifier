# dog-breed-image-classifier
This repository contains the console example of implementing **a pretrained convolutional neural network** to check dog breeds by uploaded images. The program was created during [Udacity's AI Programming with Python Nanodegree Program](https://www.udacity.com/course/ai-programming-python-nanodegree--nd089).

## Dependencies
The next points are necessary for correct execution:
- **Python 3.6** or later
- **Torch 0.4.0**
- **Pillow 5.2.0**
- **torchvision 0.2.1**

Please, check your environment.

## Quickstart
`check_images.py` is the main script in this repository.
You can run it **without** any parameters with command:
```
python check_images.py
```
And got a result with default command line arguments:
![General results](https://github.com/UlianaDzhumok/dog-breed-image-classifier/blob/dev/assets/general_results.png)

You can uncomment a few lines to print additional information in `check_images.py`:
- line 29 for command line arguments

![Command line arguments](https://github.com/UlianaDzhumok/dog-breed-image-classifier/blob/dev/assets/command_line_arguments.png)

- line 43 for checking dog breed's keys

![Breeds](https://github.com/UlianaDzhumok/dog-breed-image-classifier/blob/dev/assets/image_label_dictionary.png)

- line 58 for the first step of classification

![First step](https://github.com/UlianaDzhumok/dog-breed-image-classifier/blob/dev/assets/basic_image_classification)

- line 72 for classified images with label flags

![Classified images](https://github.com/UlianaDzhumok/dog-breed-image-classifier/blob/dev/assets/classificaion_with_flags.jpg)

- line 84 for short resume

![Statistics](https://github.com/UlianaDzhumok/dog-breed-image-classifier/blob/dev/assets/statistics.png)

## Command Line arguments
If you want you can **manage** command line arguments `--dir`, `--arch` and `--dognames`.
#### Directory with images
The argument `--dir` defines a directory with images to recognise.
**By default  `pet_images` folder is used.**
You can create your own folder, for example `uploaded_images`, and upload different images there, then run `check_images.py` with directory path after the optional argument `--dir`:
```
python check_images.py --dir uploaded_images/
```
#### Neural network architecture
You can choose one architecture from **ResNet**, **AlexNet** and **VGG** to check which one is the most effective for you using `--arch`.
**By default ResNet is choosen.**
This is the example of using **VGG**:
```
python check_images.py --dir uploaded_images/ --arch='vgg'
```
#### The list of valid dog's breeds
You can change the list of breeds by creating another `.txt` file and using argument `--dogfile`.
**By default the program uses `dognames.txt`.**
Please check your file has the same structure as `dognames.txt`.
Usage of another list:
```
python check_images.py --dir uploaded_images/ --arch='alexnet' --dogfile='breeds.txt'
```
## Issues
- The classifier works with `JPEG` images
- Images should begin with an object's name and contain only Latin alphabet, digits and underscore symbols. For example `Irish_setter_02.jpeg`,`cat.jpg`,`german_shepherd_86547.jpg`.

## License
The contents of this repository are covered under the [MIT License](https://github.com/UlianaDzhumok/dog-breed-image-classifier/blob/master/license.txt).
