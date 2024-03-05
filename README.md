# Super-Resolution-Research

### Read the paper for my project [here](https://docs.google.com/document/d/1QNaife9gFpC0sPLoqbTMLohvqakh48oBw7It5ORFvb4/edit?usp=sharing).

## Abstract
The goal of this project was to build a computer vision system that can accurately enhance images and videos into a version that hyperopic people can see. Leveraging computer vision and deep learning, the proposed solution aims to improve virtual reality (VR) experiences for individuals with hyperopia. Despite hardware constraints, relatively high results are achieved, with training and testing accuracies reaching 79.9% and 81.1%, respectively. This approach not only improves VR accessibility but also demonstrates the potential for broader applications beyond visual impairment challenges.

## Training Data
The model was trained on a dataset from Kaggle. It didn't exactly meet my needs so I preprocessed it and put the data into CSV files [here](https://www.kaggle.com/datasets/youssefa12345/super-resolution-2/).

## Usage
To use the model:
  1. Download or clone the repository.
  2. Place the images you want to upscale in the [/use_images](use_images) folder. There are already two example images inside.
  3. Run the [use_generator.py](use_generator.py) file.
  4. The upscaled images will be saved in the [/output](output) folder.

## Dependancies
The following Python packages are required to run the model:
  1. Tensorflow
  2. Keras
  3. PIL
  4. NumPy
  5. MatPlotLib
