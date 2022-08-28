import cv2
import torch
import torch.nn as nn
from torchvision import models
import torch.nn.functional as F
import numpy as np
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.autograd import Variable
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from models.models import StoreImage
import requests



class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__() 

        self.fc=nn.Linear(512,6, bias = False)
     
    def forward(self,x):
        
        dim = x.shape[0]
        v=x.view(dim,512,-1)
        x=v.mean(2)
        x=x.view(1,dim,512)
        x= F.sigmoid(self.fc(x))


        return  x.view(-1,6)


def main():
     
    images = []
    pred = []    
    classes = ['Fire', 'Flood', 'humandamage', 'infrastructure', 'nature', 'non-disaster']
    net = models.vgg16(pretrained=True) 
    mod = nn.Sequential(*list(net.children())[:-1])
    model=nn.Sequential(mod,Net())
    model.load_state_dict(torch.load('djangoPytorch/training4.pth',map_location='cpu'))       
    model.eval
    normalize = transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
    preprocess = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        normalize
    ])
    
    qs = StoreImage.objects.all()
    for i in range(len(qs)):
        image_url = qs[i].photo
        images.append(image_url)
        img_pil = Image.open(requests.get(image_url, stream = True).raw)


        img_tensor = preprocess(img_pil)
        img_variable = Variable(img_tensor.unsqueeze(0))
        logit = model(img_variable)
        h_x = F.softmax(logit, dim=1).data.squeeze()
        probs, idx = h_x.sort(0, True)
        probs = probs.detach().numpy()
        idx = idx.numpy()
        predicted = classes[idx[0]]
        pred.append(predicted)
        
    return pred, images
 


