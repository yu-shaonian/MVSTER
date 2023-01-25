import torch
import numpy as np

device = torch.device('cuda:1')

a=torch.rand([1,64,80]).to(device)
b = torch.tensor(127.2000).to(device)
c = 8

a = a.cpu().numpy()
b = b.cpu().numpy()
cur_depth_min = (a - c / 2 * b[:,None,None])  # (B, H, W)
print(a)















