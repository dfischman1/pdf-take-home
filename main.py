
import main.llm as llm
import main.extract as extract
import main.write_to_doc as docx
import json


DEFAULT_FILE = "SampleHealthRecord_Redacted.pdf"
prompts = [
    "I will ask you a few questions based on medical data that I give you. The medical data was a series of pdfs that have now been converted to a JSON object, with the JSON object key corresponding to the page of the original PDF.",
    "Using the medical data provided below, tell me what surgeries has this patient had. Include the name of the procedure, the date of surgery, and which page of the pdf this came from. \n Medical Data: ",
    "Using the medical data provided below, tell me what medications has this patient used? Include the name of the medication, the date the medication started, and the date ended (if they exist), and the JSON key where this information is sourced. \n Medical Data: ",
    "Using the medical data provided below, tell me what allergies does the patient have? Include the Allergies and the JSON key where this information is sourced.  \n Medical Data:",
]

questions = ["",
             "1. What Surgeries has this patient had? Include the name of the procedure, the date of surgery, and the page of the pdf where this information is sourced",
             "2. What medications has this patient used? Include the name of the medication, the date the medication started, and the date ended (if they exist), and the page of the pdf where this information is sourced",
             "3. What allergies does the patient have? Include the Allergies, and the page of the pdf where this information is sourced"
             ]



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
    
    extracted_pages = extract.extract_pdf(filename)
    
    print(f"converting {len(extracted_pages)} pages to json")
    extracted_pages_json = json.dumps(extracted_pages)
    print("pages extracted. Sending to LLM")

    with open("example.txt", "w") as file:
        file.write(extracted_pages_json)
        print("Wrote extracted data to example.txt")
    
    question_and_answer = {}
    # Provide the data to the LLM
    print("LLM response to initial data: " + llm.llama3(prompts[0] + extracted_pages_json))

    # Ask the LLM the series of questions
    for prompt_idx in range(1, len(prompts)):
        question_and_answer[questions[prompt_idx]] = llm.llama3(prompts[prompt_idx] + extracted_pages_json)
    
    docx.write_out_docx(question_and_answer)
    print("Questions and answers saved in Word document questions_and_answers_about_medical_record.docx")
    

def only_llm_trial():
    question_and_answer = {}
    med_data = None
    with open("example.txt", "r") as file:
        print("LLM response to initial data: " + llm.llama3(prompts[0]))
        med_data = file.read()

    # Ask the LLM the series of questions
    for prompt_idx in range(1, len(prompts)):
        question_and_answer[questions[prompt_idx]] = llm.llama3(prompts[prompt_idx] + med_data)
    
    file_name = "try1"
    docx.write_out_txt(question_and_answer, file_name)
    print(f"Questions and answers saved in txt document {file_name}.txt")



if __name__ == '__main__':
    # only_llm_trial()
    run()