# pdf-take-home

Take home assessment 

Take as input a pdf, parse it to find:
 1. What Surgeries has this patient had?
    1. Name of procedure
    2. Date of surgery
    3. Page numbers where this information is sourced from
2. What medications has this patient used?
    1. Name of medication
    2. Date medication started, date ended (if they exist)
    3. Page numbers where this information is sourced from
3.  What allergies does the patient have?
    1. Allergies
    2. Page numbers where this information is sourced from


Output a word document with questions and answers


# Running this:
This app assumes you have Ollama running locally with llama3 downloaded. You will also need to `pip install -r requirements.txt` .
Run with `python main.py`
You can provide a PDF in the input, or the program will automatically use the sample PDF in the repo.
Other vars such as prompts, and patient name are configured as variables at the top of `main.py`



## Tech

- Pymudf to process pdf into text
- PyTesseract to run ocr on images in pdf
- LLama_3_1 to process text and answer questions
- PyDocx for generating a word document

## To Do
- dockerize other parts of app?
- use poetry for dependencies
- use Ollama in a container


