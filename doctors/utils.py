# myapp/utils.py

import fitz  # PyMuPDF
import os

# Function to extract both text and images from the PDF
def extract_content_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    image_list = []
    
    # Create a media/images directory if it doesn't exist
    image_dir = os.path.join('media', 'images')
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    # Iterate through the pages of the PDF
    for page_num, page in enumerate(doc):
        # Extract text from the page
        page_text = page.get_text() + "\n"  # Adding newlines for better formatting
        text += page_text
        print(f"Extracted text from page {page_num + 1}: {page_text}")

        # Extract images from the page
        images = page.get_images(full=True)
        print(f"Page {page_num + 1} has {len(images)} images.")
        
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"page{page_num + 1}_img{img_index + 1}.{image_ext}"
            image_filepath = os.path.join(image_dir, image_filename)

            # Save the extracted image to the 'media/images' directory
            with open(image_filepath, "wb") as img_file:
                img_file.write(image_bytes)
            
            # Add the image filename to the list for display
            image_list.append(image_filename)

    return text.strip(), image_list  # Returning both text and images
