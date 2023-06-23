import matplotlib.pyplot as plt
import torch
from torch import nn
from torch import optim
import torch.nn.functional as f
from torchvision import datasets, transforms, models
import cv2
from collections import OrderedDict
import numpy as np
import statistics
import os
from PIL import Image
import random

class DeepCNN(nn.Module):
    def __init__(self):
        super(DeepCNN, self).__init__()
        # Capas convolucionales
        self.conv1 = nn.Conv2d(3, 16, 3)
        self.conv2 = nn.Conv2d(16, 32, 3)
        self.conv3 = nn.Conv2d(32, 64, 3)
        # Capas de pooling
        self.pool = nn.MaxPool2d(2, 2)
        # Capas totalmente conectadas
        self.fc1 = nn.Linear(64 * 26 * 26, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, 3)

    def forward(self, x):
        # Convolucionales + Pooling
        x = self.pool(f.relu(self.conv1(x)))
        x = self.pool(f.relu(self.conv2(x)))
        x = self.pool(f.relu(self.conv3(x)))
        # Aplanar
        x = x.view(x.size(0), -1)
        # Capas totalmente conectadas
        x = f.relu(self.fc1(x))
        x = f.relu(self.fc2(x))
        x = f.log_softmax(self.fc3(x), dim=1)
        return x

def get_cnn():

    modelDeep = DeepCNN()
    stateDictCS = torch.load('saved models/checkpointDeepCNN.pth')
    modelDeep.load_state_dict(stateDictCS)

    return modelDeep