import json
import tensorflow as tf
from data_pip_shoplifting import Shoplifting_Live  # Ensure the file is in the same directory

# Function to save the model architecture as JSON
def save_model_json(model, filename="shoplifting_model.json"):
    model_json = model.to_json()
    with open(filename, "w") as json_file:
        json.dump(model_json, json_file)
    print(f"Model architecture saved as {filename}")

# Initialize and retrieve the model
shoplifting_model = Shoplifting_Live().get_gate_flow_slow_fast_model()

# Save model architecture
save_model_json(shoplifting_model)

