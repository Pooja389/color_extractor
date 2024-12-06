# Flask Color Extractor

This is a Flask web application that extracts the top colors from an uploaded image using the `colorgram` library. Users can upload an image, and the app will display the image along with the top extracted colors.

## Features

- Upload an image to analyze its colors.
- Display the uploaded image and its top 10 colors.
- User-friendly interface with error handling for file uploads.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Pooja389/color_extractor.git
    cd color_extractor
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```
## Usage
1. Navigate to the home page at `http://127.0.0.1:5000/`.
2. Upload an image file using the provided form.
3. View the uploaded image and the top colors extracted from it.
