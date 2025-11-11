from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the homepage ("/")
@app.route('/')
def hello_world():
  """This function is executed when someone visits the homepage."""
  return 'Hello, World!'

# This block ensures the server runs only when this script is executed directly
if __name__ == '__main__':
  # Runs the development server on http://127.0.0.1:5000/
  app.run(debug=True)
