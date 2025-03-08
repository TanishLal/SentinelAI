from tensorflow.keras.models import model_from_json
with open(r"D:\newFolder\Shoplifting-Detection\CODE\shoplifting_model.json", "r") as json_file:
    loaded_model_json = json_file.read()
abuse_model = model_from_json(loaded_model_json)
abuse_model.load_weights(weight_abuse)
