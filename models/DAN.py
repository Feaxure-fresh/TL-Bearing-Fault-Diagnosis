import torch
from torch import nn
from utils import *


class CNN(nn.Module):

    def __init__(self, in_channel=1):
        super(CNN, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv1d(in_channel, 32, kernel_size=7),
            nn.BatchNorm1d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool1d(kernel_size=2, stride=2))

        self.layer2 = nn.Sequential(
            nn.Conv1d(32, 64, kernel_size=3),
            nn.BatchNorm1d(64),
            nn.ReLU(inplace=True))

        self.layer3 = nn.Sequential(
            nn.Conv1d(64, 128, kernel_size=3),
            nn.BatchNorm1d(128),
            nn.ReLU(inplace=True))

        self.layer4 = nn.Sequential(
            nn.Conv1d(128, 256, kernel_size=3),
            nn.BatchNorm1d(256),
            nn.ReLU(inplace=True))

        self.layer5 = nn.Sequential(
            nn.Conv1d(256, 512, kernel_size=3),
            nn.BatchNorm1d(512),
            nn.ReLU(inplace=True),
            nn.AdaptiveMaxPool1d(4),
            nn.Flatten())

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)

        return x


class DAN(nn.Module):

    def __init__(self, in_channel=1, num_classes=3):
        super(DAN, self).__init__()

        self.cnn = CNN(in_channel=in_channel)

        self.fc1 = nn.Sequential(
            nn.Linear(512 * 4, 256),
            nn.ReLU(inplace=True))

        self.fc2 = nn.Sequential(
            nn.Linear(256, 64),
            nn.ReLU(inplace=True))

        self.fc3 = nn.Linear(64, num_classes)

        self.mkmmd = MultipleKernelMaximumMeanDiscrepancy(
            kernels=[GaussianKernel(alpha=2 ** k) for k in range(-3, 2)])

    def forward(self, source_data, target_data):
        mmd_loss = 0.0
        f_s = self.cnn(source_data)
        f_t = self.cnn(target_data)

        f_s = self.fc1(f_s)
        f_t = self.fc1(f_t)
        mmd_loss += self.mkmmd(f_s, f_t)
        
        f_s = self.fc2(f_s)
        f_t = self.fc2(f_t)
        mmd_loss += self.mkmmd(f_s, f_t)

        f_s = self.fc3(f_s)
        f_t = self.fc3(f_t)
        mmd_loss += self.mkmmd(f_s, f_t)

        return f_s, mmd_loss