import fitz 
import io 
from PIL import Image
import pytesseract
  


def extract_pdf(file) -> dict[int, str]:
    pdf_file = fitz.open(file)
    extracted_pages = {}
    # len(pdf_file, 
    for page_index in range(9, 20): 
    
        image_list = pdf_file.get_page_images(page_index)
        page_text = pdf_file.get_page_text(page_index) 
        image_text = ""

        for image_index, img in enumerate(image_list, start=1):
             # get the XREF of the image 
                xref = img[0] 
        
                # extract the image bytes 
                base_image = pdf_file.extract_image(xref) 
                image_bytes = base_image["image"] 
        
                image_ext = base_image["ext"] 
                with open(str(image_index) + str(xref) + "." + image_ext, "wb") as fp:
                        fp.write(image_bytes)
                        image_text = pytesseract.image_to_string(fp.name)
        extracted_pages[page_index + 1] = f"{page_text} \n {image_text}"
                    
        
            # extract the image bytes 
            # base_image = pdf_file.extractImage(xref) 
            # image_bytes = base_image["image"] 
    
            # get the image extension 
            # image_ext = base_image["ext"]

    return extracted_pages