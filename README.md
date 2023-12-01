# ROBT407 Final Project
This repository contains the final project for the course ROBT407 - Machine Learning with Applications.

## Models
In this project, we implemented
1. ResNet (50 and 101) architecture as well as custom CNN model (VGG16-like)
2. ViT-lite as well as CVT (Compact Convolutional Transformer) to detect distracted drivers from images.

## Training
In order to train a model, run the following script
```
python3 train.py --task 1 --model_name resnet50
```

## Training Results
In the “Training Results” directory, each model’s subfolder contains its training code, results, accuracy, F1, loss graphs, and a .csv submission file.
```
Trainnig Results
├── Model 1
│   ├── Accuracy graph
│   ├── F1 Score graph
│   ├── Loss graph
│   ├── submission.csv
│   └── Training code
```
