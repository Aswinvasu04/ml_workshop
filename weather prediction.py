import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

df = pd.read_csv('seattle-weather(1).csv')
df.head()

training_set = df.iloc[:, 2:3].values  # Adjust the index as needed based on your CSV structure

def df_to_XY(data, window_size=10):
    x_train = []
    y_train = []

    for i in range(window_size, len(data)):
        x_train.append(data[i-window_size:i, 0])  # Use window size to create features
        y_train.append(data[i, 0])  # Target variable is the next value
    return np.array(x_train), np.array(y_train)


Window = 10
x, y = df_to_XY(training_set, Window)

x_train = x[:800]
y_train = y[:800]
x_val = x[800:1000]
y_val = y[800:1000]
x_test = x[1000:]
y_test = y[1000:]

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_val = np.reshape(x_val, (x_val.shape[0], x_val.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

regressor = Sequential()
regressor.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=50, return_sequences=True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=50))
regressor.add(Dropout(0.2))

regressor.add(Dense(units=1))
regressor.compile(optimizer='adam', loss='mean_squared_error')

history = regressor.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=100, batch_size=32)

his = pd.DataFrame(history.history)

plt.figure(figsize=(14, 8))
plt.subplot(2, 1, 1)
plt.title("Loss & Validation Loss")
sns.lineplot(data=his[['loss', 'val_loss']], palette="flare")
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(['Training Loss', 'Validation Loss'])


plt.tight_layout()
plt.show()
