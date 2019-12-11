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
```
Command Line Arguments:
     dir = pet_images/ 
    arch = resnet 
 dogfile = dognames.txt

Pet Image Label Dictionary has 40 key-value pairs.
Below are 10 of them:
 1 key:  German_shepherd_dog_04890.jpg  label:        german shepherd dog
 2 key:                     cat_07.jpg  label:                        cat
 3 key:            Dalmatian_04068.jpg  label:                  dalmatian
 4 key:        great_horned_owl_02.jpg  label:           great horned owl
 5 key:            Dalmatian_04037.jpg  label:                  dalmatian
 6 key:       Boston_terrier_02285.jpg  label:             boston terrier
 7 key:     Golden_retriever_05257.jpg  label:           golden retriever
 8 key:       Boston_terrier_02259.jpg  label:             boston terrier
 9 key:               Poodle_07956.jpg  label:                     poodle
10 key:                     cat_02.jpg  label:                        cat

     MATCH:

 German_shepherd_dog_04890.jpg: 
Real:        german shepherd dog   Classifier: german shepherd, german shepherd dog, german police dog, alsatian

                    cat_07.jpg: 
Real:                        cat   Classifier:              egyptian cat, cat

           Dalmatian_04068.jpg: 
Real:                  dalmatian   Classifier: dalmatian, coach dog, carriage dog

           Dalmatian_04037.jpg: 
Real:                  dalmatian   Classifier: dalmatian, coach dog, carriage dog

      Boston_terrier_02285.jpg: 
Real:             boston terrier   Classifier:    boston bull, boston terrier

    Golden_retriever_05257.jpg: 
Real:           golden retriever   Classifier:               golden retriever

      Boston_terrier_02259.jpg: 
Real:             boston terrier   Classifier:    boston bull, boston terrier

              Poodle_07956.jpg: 
Real:                     poodle   Classifier:        standard poodle, poodle

                    cat_02.jpg: 
Real:                        cat   Classifier:          tabby, tabby cat, cat

             Basenji_00974.jpg: 
Real:                    basenji   Classifier:                        basenji

              Beagle_01141.jpg: 
Real:                     beagle   Classifier:                         beagle

          Great_dane_05320.jpg: 
Real:                 great dane   Classifier:                     great dane

               Boxer_02426.jpg: 
Real:                      boxer   Classifier:                          boxer

           Dalmatian_04017.jpg: 
Real:                  dalmatian   Classifier: dalmatian, coach dog, carriage dog

       Saint_bernard_08036.jpg: 
Real:              saint bernard   Classifier:      saint bernard, st bernard

    Golden_retriever_05223.jpg: 
Real:           golden retriever   Classifier:               golden retriever

                Rabbit_002.jpg: 
Real:                     rabbit   Classifier: wood rabbit, cottontail, cottontail rabbit, rabbit

German_shorthaired_pointer_04986.jpg: 
Real: german shorthaired pointer   Classifier:     german shorthaired pointer

             polar_bear_04.jpg: 
Real:                 polar bear   Classifier: ice bear, polar bear, ursus maritimus, thalarctos maritimus

 German_shepherd_dog_04931.jpg: 
Real:        german shepherd dog   Classifier: german shepherd, german shepherd dog, german police dog, alsatian

      Great_pyrenees_05435.jpg: 
Real:             great pyrenees   Classifier:                 great pyrenees

    Golden_retriever_05195.jpg: 
Real:           golden retriever   Classifier:               golden retriever

              Beagle_01125.jpg: 
Real:                     beagle   Classifier:                         beagle

       Saint_bernard_08010.jpg: 
Real:              saint bernard   Classifier:      saint bernard, st bernard

 Miniature_schnauzer_06884.jpg: 
Real:        miniature schnauzer   Classifier:            miniature schnauzer

              Poodle_07927.jpg: 
Real:                     poodle   Classifier:        standard poodle, poodle

             Basenji_00963.jpg: 
Real:                    basenji   Classifier:                        basenji

      Cocker_spaniel_03750.jpg: 
Real:             cocker spaniel   Classifier: cocker spaniel, english cocker spaniel, cocker

                 skunk_029.jpg: 
Real:                      skunk   Classifier:     skunk, polecat, wood pussy

              Collie_03797.jpg: 
Real:                     collie   Classifier:                         collie

           fox_squirrel_01.jpg: 
Real:               fox squirrel   Classifier: fox squirrel, eastern fox squirrel, sciurus niger

      Boston_terrier_02303.jpg: 
Real:             boston terrier   Classifier:    boston bull, boston terrier

        Basset_hound_01034.jpg: 
Real:               basset hound   Classifier:           basset, basset hound

 NOT A MATCH:

       great_horned_owl_02.jpg: 
Real:           great horned owl   Classifier: great grey owl, great gray owl, strix nebulosa

                  gecko_80.jpg: 
Real:                      gecko   Classifier: tailed frog, bell toad, ribbed toad, tailed toad, ascaphus trui

      Great_pyrenees_05367.jpg: 
Real:             great pyrenees   Classifier:                         kuvasz

                    cat_01.jpg: 
Real:                        cat   Classifier:   norwegian elkhound, elkhound

                  gecko_02.jpg: 
Real:                      gecko   Classifier: african chameleon, chamaeleo chamaeleon

              Beagle_01170.jpg: 
Real:                     beagle   Classifier:  walker hound, walker foxhound

    Golden_retriever_05182.jpg: 
Real:           golden retriever   Classifier:                       leonberg

# Total Images 40 # Matches: 33 # NOT Matches: 7

     MATCH:

 German_shepherd_dog_04890.jpg: 
Real:        german shepherd dog   Classifier: german shepherd, german shepherd dog, german police dog, alsatian  
PetLabelDog: 1  ClassLabelDog: 1

                    cat_07.jpg: 
Real:                        cat   Classifier:              egyptian cat, cat  
PetLabelDog: 0  ClassLabelDog: 0

           Dalmatian_04068.jpg: 
Real:                  dalmatian   Classifier: dalmatian, coach dog, carriage dog  
PetLabelDog: 1  ClassLabelDog: 1

           Dalmatian_04037.jpg: 
Real:                  dalmatian   Classifier: dalmatian, coach dog, carriage dog  
PetLabelDog: 1  ClassLabelDog: 1

      Boston_terrier_02285.jpg: 
Real:             boston terrier   Classifier:    boston bull, boston terrier  
PetLabelDog: 1  ClassLabelDog: 1

    Golden_retriever_05257.jpg: 
Real:           golden retriever   Classifier:               golden retriever  
PetLabelDog: 1  ClassLabelDog: 1

      Boston_terrier_02259.jpg: 
Real:             boston terrier   Classifier:    boston bull, boston terrier  
PetLabelDog: 1  ClassLabelDog: 1

              Poodle_07956.jpg: 
Real:                     poodle   Classifier:        standard poodle, poodle  
PetLabelDog: 1  ClassLabelDog: 1

                    cat_02.jpg: 
Real:                        cat   Classifier:          tabby, tabby cat, cat  
PetLabelDog: 0  ClassLabelDog: 0

             Basenji_00974.jpg: 
Real:                    basenji   Classifier:                        basenji  
PetLabelDog: 1  ClassLabelDog: 1

              Beagle_01141.jpg: 
Real:                     beagle   Classifier:                         beagle  
PetLabelDog: 1  ClassLabelDog: 1

          Great_dane_05320.jpg: 
Real:                 great dane   Classifier:                     great dane  
PetLabelDog: 1  ClassLabelDog: 1

               Boxer_02426.jpg: 
Real:                      boxer   Classifier:                          boxer  
PetLabelDog: 1  ClassLabelDog: 1

           Dalmatian_04017.jpg: 
Real:                  dalmatian   Classifier: dalmatian, coach dog, carriage dog  
PetLabelDog: 1  ClassLabelDog: 1

       Saint_bernard_08036.jpg: 
Real:              saint bernard   Classifier:      saint bernard, st bernard  
PetLabelDog: 1  ClassLabelDog: 1

    Golden_retriever_05223.jpg: 
Real:           golden retriever   Classifier:               golden retriever  
PetLabelDog: 1  ClassLabelDog: 1

                Rabbit_002.jpg: 
Real:                     rabbit   Classifier: wood rabbit, cottontail, cottontail rabbit, rabbit  
PetLabelDog: 0  ClassLabelDog: 0

German_shorthaired_pointer_04986.jpg: 
Real: german shorthaired pointer   Classifier:     german shorthaired pointer  
PetLabelDog: 1  ClassLabelDog: 1

             polar_bear_04.jpg: 
Real:                 polar bear   Classifier: ice bear, polar bear, ursus maritimus, thalarctos maritimus  
PetLabelDog: 0  ClassLabelDog: 0

 German_shepherd_dog_04931.jpg: 
Real:        german shepherd dog   Classifier: german shepherd, german shepherd dog, german police dog, alsatian  
PetLabelDog: 1  ClassLabelDog: 1

      Great_pyrenees_05435.jpg: 
Real:             great pyrenees   Classifier:                 great pyrenees  
PetLabelDog: 1  ClassLabelDog: 1

    Golden_retriever_05195.jpg: 
Real:           golden retriever   Classifier:               golden retriever  
PetLabelDog: 1  ClassLabelDog: 1

              Beagle_01125.jpg: 
Real:                     beagle   Classifier:                         beagle  
PetLabelDog: 1  ClassLabelDog: 1

       Saint_bernard_08010.jpg: 
Real:              saint bernard   Classifier:      saint bernard, st bernard  
PetLabelDog: 1  ClassLabelDog: 1

 Miniature_schnauzer_06884.jpg: 
Real:        miniature schnauzer   Classifier:            miniature schnauzer  
PetLabelDog: 1  ClassLabelDog: 1

              Poodle_07927.jpg: 
Real:                     poodle   Classifier:        standard poodle, poodle  
PetLabelDog: 1  ClassLabelDog: 1

             Basenji_00963.jpg: 
Real:                    basenji   Classifier:                        basenji  
PetLabelDog: 1  ClassLabelDog: 1

      Cocker_spaniel_03750.jpg: 
Real:             cocker spaniel   Classifier: cocker spaniel, english cocker spaniel, cocker  
PetLabelDog: 1  ClassLabelDog: 1

                 skunk_029.jpg: 
Real:                      skunk   Classifier:     skunk, polecat, wood pussy  
PetLabelDog: 0  ClassLabelDog: 0

              Collie_03797.jpg: 
Real:                     collie   Classifier:                         collie  
PetLabelDog: 1  ClassLabelDog: 1

           fox_squirrel_01.jpg: 
Real:               fox squirrel   Classifier: fox squirrel, eastern fox squirrel, sciurus niger  
PetLabelDog: 0  ClassLabelDog: 0

      Boston_terrier_02303.jpg: 
Real:             boston terrier   Classifier:    boston bull, boston terrier  
PetLabelDog: 1  ClassLabelDog: 1

        Basset_hound_01034.jpg: 
Real:               basset hound   Classifier:           basset, basset hound  
PetLabelDog: 1  ClassLabelDog: 1

 NOT A MATCH:

       great_horned_owl_02.jpg: 
Real:           great horned owl   Classifier: great grey owl, great gray owl, strix nebulosa  
PetLabelDog: 0  ClassLabelDog: 0

                  gecko_80.jpg: 
Real:                      gecko   Classifier: tailed frog, bell toad, ribbed toad, tailed toad, ascaphus trui  
PetLabelDog: 0  ClassLabelDog: 0

      Great_pyrenees_05367.jpg: 
Real:             great pyrenees   Classifier:                         kuvasz  
PetLabelDog: 1  ClassLabelDog: 1

                    cat_01.jpg: 
Real:                        cat   Classifier:   norwegian elkhound, elkhound  
PetLabelDog: 0  ClassLabelDog: 1

                  gecko_02.jpg: 
Real:                      gecko   Classifier: african chameleon, chamaeleo chamaeleon  
PetLabelDog: 0  ClassLabelDog: 0

              Beagle_01170.jpg: 
Real:                     beagle   Classifier:  walker hound, walker foxhound  
PetLabelDog: 1  ClassLabelDog: 1

    Golden_retriever_05182.jpg: 
Real:           golden retriever   Classifier:                       leonberg  
PetLabelDog: 1  ClassLabelDog: 1

# Total Images 40 # Matches: 33 # NOT Matches: 7

 ** Statistics from calculates_results_stats() function:
N Images: 40  N Dog Images: 30  N NotDog Images: 10 
Pct Corr dog: 100.0 Pct Corr NOTdog:  90.0  Pct Corr Breed:  90.0

 ** Check Statistics - calculated from this function as a check:
N Images: 40  N Dog Images: 30  N NotDog Images: 10 
Pct Corr dog: 100.0 Pct Corr NOTdog:  90.0  Pct Corr Breed:  90.0
n_images: 40
n_dogs_img: 30
n_notdogs_img: 10
n_match: 33
n_correct_dogs: 30
n_correct_notdogs: 9
n_correct_breed: 27
pct_correct_dogs: 100.0
pct_correct_breed: 90.0
pct_correct_notdogs: 90.0
pct_match: 82.5
cat not equal to norwegian elkhound, elkhound
great pyrenees not equal to kuvasz
beagle not equal to walker hound, walker foxhound
golden retriever not equal to leonberg

** Total Elapsed Runtime: 0:0:6
```
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