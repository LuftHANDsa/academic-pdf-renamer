# Academic PDF Renamer

This script automatically renames academic PDF papers based on their content using an LLM. It processes all PDF files in a specified directory, sends them to the OpenAI API, and renames them based on the response.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/academic-pdf-renamer.git
    cd academic-pdf-renamer
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your OpenAI API Key:**
    The script requires an OpenAI API key to be set as an environment variable.
    ```bash
    export API_KEY_OPENAI="your-api-key"
    ```
    Replace `"your-api-key"` with your actual OpenAI API key.

## Usage

1.  **Add PDF files:**
    Place the academic papers you want to rename into the `tests/` directory.

2.  **Run the script:**
    ```bash
    python main.py
    ```
    The script will iterate through all `.pdf` files in the `tests/` directory, rename them, and print the progress.

## Customization

-   **Change the PDF location:**
    To change the directory where the script looks for PDFs, edit the `research_paper_location` variable in `main.py`.

-   **Customize the renaming prompt:**
    You can modify the `prompt.txt` file to change the instructions given to the LLM for renaming the files. This allows you to customize the output format of the new filenames.
