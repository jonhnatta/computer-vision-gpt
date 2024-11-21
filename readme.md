## Introduction
This project is a web application developed with Streamlit that uses the GPT-4o-mini model from OpenAI to generate image descriptions.

## Installation
1. Clone the repository:
     ```bash
   git clone https://github.com/jonhnatta/computer-vision-gpt.git
   cd computer-vision-gpt
   ```

2. Create a virtual environment (optional, but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```
3. Install the necessary libraries:

   ```bash
   pip install streamlit python-dotenv openai 
   ```
4. Configure your OpenAI API key:

   Create a `.env` file in the root of the project and add your API key:

   ```
   OPENAI_API_KEY=yourapikeyhere
   ```

## Running the Project

To start the Streamlit application, run the following command:

```bash
streamlit run main.py
```