import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model(
    r"C:\pythonProjects\DeepLearning\VegHealth\Tomato\tomato_health.keras"
)

img_path = r"C:\pythonProjects\DeepLearning\VegHealth\Tomato\unseenTest\image.png"

# Load image
img = image.load_img(
    img_path,
    target_size=(224, 224)
)

# Convert to NumPy array
img_array = image.img_to_array(img)

# Normalize exactly as during training
img_array = img_array / 255.0

# Add batch dimension
img_array = np.expand_dims(img_array, axis=0)

# Predict
prediction = model.predict(img_array, verbose=0)[0][0]

# Class mapping:
# 0 = Rotten
# 1 = Healthy

if prediction >= 0.5:
    predicted_class = "Healthy"
    confidence = prediction
else:
    predicted_class = "Rotten"
    confidence = 1 - prediction

# Display result
plt.imshow(img)
plt.axis("off")
plt.title(
    f"Prediction: {predicted_class}\n"
    f"Confidence: {confidence:.2%}"
)
plt.show()

print(f"Raw prediction: {prediction:.4f}")
print(f"Prediction: {predicted_class}")
print(f"Confidence: {confidence:.2%}")