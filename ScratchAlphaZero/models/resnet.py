import torch
import torch.nn as nn
import torch.nn.functional as F

class AlphaZeroNet(nn.Module):
    def __init__(self):
        super(AlphaZeroNet,self).__init__()
        self.conv1 = nn.Conv2d(12,256,kernel_size=3,padding=1)
        self.bn1 = nn.BatchNorm2d(256)

        self.res_blocks = nn.ModuleList([
            self._build_res_block(256)
            for _ in range(5)
        ])
        
        self.policy_conv = nn.Conv2d(256,2,kernel_size=1)
        self.policy_bn = nn.BatchNorm2d(2)
        self.policy_fc = nn.Linear(2*8*8,4672) 

        self.value_conv = nn.Conv2d(256,1,kernel_size=1)
        self.value_bn = nn.BatchNorm2d(1)
        self.value_fc1 = nn.Linear(8*8,256)
        self.value_fc2 = nn.Linear(256,1)
    
    def _build_res_block(self,channels):
        return nn.Sequential(
            nn.Conv2d(channels,channels,kernel_size=3,padding=1),
            nn.BatchNorm2d(channels),
            nn.ReLU(),
            nn.Conv2d(channels,channels,kernel_size=3,padding=1),
            nn.BatchNorm2d(channels),
        )
    
    def forward(self,x):
        x = F.relu(self.bn1(self.conv1(x)))

        for block in self.res_blocks:
            residual = x
            x = F.relu(block(x)+residual)
        
        policy = F.relu(self.policy_bn(self.policy_conv(x)))
        policy = policy.view(-1,2*8*8)
        policy = self.policy_fc(policy)

        value = F.relu(self.value_bn(self.value_conv(x)))
        value = value.view(-1,8*8)
        value = F.relu(self.value_fc1(value))
        value = torch.tanh(self.value_fc2(value))
        return policy,value
    