import tensorflow as tf
from tensorflow import keras
from tensorflow import layers

model_dl = tf.keras.Sequential([
    layers.Dense(32, activation="relu", input_shape=(X_train.shape[1],)),
    layers.Dense(16, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])

model_dl.compile(optimizer="adam", loss="binary_crossentropy", metrics=["AUC"])
model_dl.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.1)