import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Define the folder where your PDF files are stored
pdf_folder = "C:\\Users\\shiva\\OneDrive\\Desktop\\finalll\\pdfs"  # Create a folder named "pdfs" and place your PDF files inside

@app.route('/')
def index():
    # List all PDF files in the folder
    pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith(".pdf")]
    return render_template('index.html', pdf_files=pdf_files)

@app.route('/pdf/<filename>')
def serve_pdf(filename):
    try:
        # Serve the selected PDF file from the specified folder
        return send_from_directory(pdf_folder, filename)
    except FileNotFoundError:
        return "PDF not found", 404

if __name__ == '__main__':
    app.run(debug=True)
