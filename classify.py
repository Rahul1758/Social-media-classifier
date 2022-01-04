import tensorflow as tf

class Classifier:
    def __init__(self, labels_map):
        self.labels_map = labels_map

    def get_predictions(self, img_path, model):
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(299,299))
        img_arr = tf.keras.preprocessing.image.img_to_array(img)
        img_arr = tf.expand_dims(img_arr, axis=0)
        preprocessed_img = tf.keras.applications.inception_v3.preprocess_input(img_arr)
        pred_probs = model.predict(preprocessed_img)
        prediction = self.labels_map[tf.argmax(pred_probs, axis=1).numpy()[0]]

        return prediction
