import torch
import torch.nn as nn
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('E:\python_code\house_price\HW7/housing.csv')
print(df.shape)
print(df.head())
all_data = df['price'].values.astype(float)
print(all_data[:10])
#将后面的1597条作为测试，前面的2w条作为训练
test_data_size = 1597
train_data = all_data[:-test_data_size]
test_data = all_data[-test_data_size:]
print(train_data[:5])
from sklearn.preprocessing import MinMaxScaler
#将训练集进行归一化
scaler = MinMaxScaler(feature_range=(-1, 1))
train_data_normalized = scaler.fit_transform(train_data.reshape(-1, 1))
print(train_data_normalized[:5])
print(train_data_normalized[-5:])
#将训练样本进行转换成tensor
train_data_normalized = torch.FloatTensor(train_data_normalized).view(-1)
print(train_data_normalized.shape)
#选择窗口大小
train_window = 15 #自己设置
def create_inout_sequences(input_data, tw):
    inout_seq = []
    L = len(input_data)
    for i in range(L-tw):
        train_seq = input_data[i:i+tw]
        train_seq = train_seq.unsqueeze(0)
        #print(train_seq.shape)
        train_label = input_data[i+tw:i+tw+1]
        inout_seq.append((train_seq,train_label))
    return inout_seq

train_inout_seq = create_inout_sequences(train_data_normalized, train_window)
print(train_inout_seq[:2])
from torch.utils.data import DataLoader

train_loader = DataLoader(dataset=train_inout_seq, 
                          batch_size=64, 
                          shuffle=True)
train_loader
help(nn.Sequential)
#定义模型
class CNN_Series(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1=nn.Sequential(
            nn.Conv1d(
                in_channels=1,
                out_channels=64,
                kernel_size=3,
            ),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2)
        )
        self.conv2=nn.Sequential(
            nn.Conv1d(
                in_channels=64,
                out_channels=32,
                kernel_size=3,
            ),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2)
        )
#         print(self.conv2.shape)
        self.fc=nn.Linear(64,1)
        
    def forward(self,indata):
        x=self.conv1(indata)
        x=self.conv2(x)
        x=x.view(x.size(0),-1)
        out=self.fc(x)
        return out
# 定义损失函数，优化方法
import torch.optim as optim
model = CNN_Series()
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
print(model)
epochs = 10
print(train_loader)
for i in range(epochs):
    for seq, labels in train_loader:
        # print(seq.shape,len(labels))
        optimizer.zero_grad()
        # model.hidden_cell = torch.zeros(1, seq.shape[0], model.hidden_layer_size)
        y_pred = model(seq)
        single_loss = loss_function(y_pred, labels)
        single_loss.backward()
        optimizer.step()
    if i%2 == 1:
        print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')
fut_pred = test_data_size
print(fut_pred)
test_inputs = train_data_normalized[-train_window:].tolist()
print(test_inputs)
model.eval()

for i in range(fut_pred):
    seq = torch.FloatTensor(test_inputs[-train_window:])
    seq = seq.unsqueeze(0)
    seq = seq.unsqueeze(0)
    # print(seq.shape)
    with torch.no_grad():
    # model.hidden = torch.zeros(1, seq.shape[0], model.hidden_layer_size) # (num_layers, batch_size, hidden_size)
                        
        test_inputs.append(model(seq).item())
    # print(test_inputs)
    # print('====================================')
len(test_inputs)
actual_predictions = scaler.inverse_transform(np.array(test_inputs[train_window:] ).reshape(-1, 1))
actual_predictions
actual_predictions.shape