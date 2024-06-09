import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('models/model_hrs6.h5')

# Convert the model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model to disk
with open('models/model_hrs6.tflite', 'wb') as f_out:
    f_out.write(tflite_model)
