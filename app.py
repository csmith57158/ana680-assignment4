from flask import Flask, render_template, request
import pickle

# Create a Flask app
app = Flask(__name__)
filename = 'knnmodel.pkl'
model = pickle.load(open(filename, 'rb'))    # load the model

@app.route('/')
def index():
    return render_template('index.html')

# Define the home route
@app.route("/predict", methods=["POST"])
def predict():
    # Initialize the prediction variable
    prediction = None
    # Get the values for the features
    clump_thickness = request.form.get("clump_thickness")
    uniformity_of_cell_size = request.form.get("uniformity_of_cell_size")
    uniformity_of_cell_shape = request.form.get("uniformity_of_cell_shape")
    marginal_adhesion = request.form.get("marginal_adhesion")
    single_epithelial_cell_size = request.form.get("single_epithelial_cell_size")
    bare_nuclei = request.form.get("bare_nuclei")
    bland_chromatin = request.form.get("bland_chromatin")
    normal_nucleoli = request.form.get("normal_nucleoli")
    mitoses = request.form.get("mitoses")
    # Convert the values to a list
    features = [clump_thickness, uniformity_of_cell_size, uniformity_of_cell_shape, marginal_adhesion, single_epithelial_cell_size, bare_nuclei, bland_chromatin, normal_nucleoli, mitoses]
    # Convert the list to a 2D array
    features = [list(map(int, features))]
    # Predict the class using the model
    prediction = model.predict(features)[0]
    # Convert the prediction to a string
    prediction = "Benign" if prediction == 0 else "Malignant"
    # Render the index.html template and pass the prediction variable
    return render_template("index.html", prediction=prediction)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
