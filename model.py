import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)
CUDA = torch.cuda.is_available()
