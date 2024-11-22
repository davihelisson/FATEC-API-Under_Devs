echo "Activating virtual environment"
source venv/bin/activate
echo "Starting Flask server on port 80"
flask run --debug --host=0.0.0.0 --port=80