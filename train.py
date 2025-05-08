import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split

X = np.load('asl_sequences.npy')  # Shape: (samples, 30, 63)
y = np.load('asl_labels.npy')     # Shape: (samples, num_classes)
actions = np.load('asl_actions.npy')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#LSTM is used for image classification usually
model = Sequential()
model.add(LSTM(128, return_sequences=True, activation='relu', input_shape=(30, 63)))
model.add(Dropout(0.3))
model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(64, activation='relu'))
model.add(Dense(y.shape[1], activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test))

model.save('asl_model.h5')
np.save('asl_actions.npy', actions)

print(" Model training complete. Saved as 'asl_model.h5'")
