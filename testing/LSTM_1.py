'''
making the dummy LSTM network

'''
#the imports in the network
import torch
import torch.nn as nn

#-------------------------------------------------------------------------------------------------------------

#making the input and the hidden layers
input_dim = 5
hidden_dim = 10
n_layers = 1


#the lstm layer
lstm_layer = nn.LSTM(input_dim, hidden_dim, n_layers, batch_first=True)

#creating some dummy data
batch_size = 1
seq_len = 1

inp = torch.randn(batch_size, seq_len, input_dim)
hidden_state = torch.randn(n_layers, batch_size, hidden_dim)
cell_state = torch.randn(n_layers, batch_size, hidden_dim)
hidden = (hidden_state, cell_state)

out, hidden = lstm_layer(inp, hidden)
print("Output shape: ", out.shape)
print("Hidden: ", hidden)

seq_len = 3
inp = torch.randn(batch_size, seq_len, input_dim)
out, hidden = lstm_layer(inp, hidden)
print(out.shape)
