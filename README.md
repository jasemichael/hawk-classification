# Project 2: Hawk classification
## About
This project uses a CNN to identify two species of hawk: red-tailed and sharp-shinned.
## Installation
Note: use the `python` command instead of `python3` for windows based systems.\
To install, be sure to clone the repository using `git clone git@github.com:jasemichael/hawk-classification.git`.
Once cloned, `cd` into the cloned directory and run `python3 -m venv venv` (if you are familiar with venv, you can name it to whatever you'd like).
This will create the virtual environment which we will host the pip3 packages in.
Activate the environment by running `source venv/vin/activate`.
Once activated, as indicated in the terminal, run `pip3 install -r requirements.txt` to install the required dependencies.
### Dataset
The dataset is located at https://hawk-classification.s3.us-west-2.amazonaws.com/dataset.zip.
Navigate to that URL and download the file to the root directory of the project.
Unzip the dataset.
### Saved model
The saved model is located at https://hawk-classification.s3.us-west-2.amazonaws.com/models.zip.
Navigate to that URL and download the file to the root directory of the project.
Unzip the models.

### Hierarchy
The project directory should now have the following hierarchy:

hawk-classification/\
----models/\
--------model/\
----dataset/\
--------red_tailed/\
--------sharp_shinned/\
----venv\
## Run
There are various ways to run the code, depending on your purpose.\
Note: GPU-enabled running requires CUDA. See this [page](https://www.tensorflow.org/install/gpu) for installation.
### Training
Note: the dataset is required to run correctly.\
To run the training loop, simply run the `cnn.py` file with `python3 cnn.py`. 
This will convert the dataset into their respective numpy arrays and train them on the defined CNN.
### Run prediction
Note: the saved model is required to run correctly.\
To make a prediction, find an image online or use an image within the dataset.
In the make_prediction file under `if __name__ == "__main__":`, replace the input to the make_prediction function with that image's path.
Simply run the `make_prediction.py` file with `python3 make_prediction.py` and see what the saved network predicts.