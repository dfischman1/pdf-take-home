
from pypdf import PdfReader
import pytesseract
from docx import Document
import main.llm as llm
import main.extract as extract
import json
import fitz 
import io 
from PIL import Image 


DEFAULT_FILE = "SampleHealthRecord_Redacted.pdf"

prompt = """Answer the following questions using only the medical data presented as json provided in this prompt. The questions are:
1. What Surgeries has this patient had?
    1. Name of procedure
    2. Date of surgery
    3. JSON key where this information is sourced from
2. What medications has this patient used?
    1. Name of medication
    2. Date medication started, date ended (if they exist)
    3. JSON key where this information is sourced from
3.  What allergies does the patient have?
    1. Allergies
    2. JSON key where this information is sourced from
    
JSON Medical Data:
"""



def run():
    filename = input(f"Enter the file to search. Default file is {DEFAULT_FILE}: ")

    try:
        if filename:
            file = open(filename)
    except OSError as e:
        print(f"Error opening file: {e}")
        exit(1)

    if filename and not filename.lower().endswith('.pdf'):
        print("Only pdfs are accepted")
        exit(1)

    filename = DEFAULT_FILE if not filename else filename
    
    image_extract.extract_image(filename)
    reader = PdfReader(filename)
    for page_num in range(100):
        page = reader.pages[page_num]
        text = page.extract_text()
        image_text = ""
        try:
            for count, image_file_object in enumerate(page.images):
                with open(str(count) + image_file_object.name, "wb") as fp:
                    fp.write(image_file_object.data)
                    image_text = pytesseract.image_to_string(fp.name)
        except ValueError as e:
            print(f"ValueError on page {page_num}: {e}")
            raise e
        
        extracted_pages[page_num] = (f"{text} \n {image_text}")

    print(f"converting {len(extracted_pages)} pages to json")
    extracted_pages_json = json.dumps(extracted_pages)
    print("pages extracted. Sending to LLM")

    with open("example.txt", "w") as file:
        file.write(prompt + extracted_pages_json)
    

    response = llm.llama3(prompt + extracted_pages_json)
    print(response)
    




if __name__ == '__main__':
    run()