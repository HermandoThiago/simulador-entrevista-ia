import pymupdf

def read_pdf(curriculum_name: str) -> str:
  """
    Extracts and concatenates all text from a specific PDF file.

    This function attempts to open a PDF located at a hardcoded relative path,
    iterates through every page in the document, and extracts its textual 
    content using the PyMuPDF library.

    Returns:
        str: The full text content of the PDF. Returns an empty string if 
            the file cannot be opened or if an error occurs during extraction.

    Raises:
        Exception: Captures and prints any exceptions to the console instead 
            of letting them propagate, ensuring the function returns a string.
    """
  content = ""

  try:
    doc = pymupdf.open(f"./curriculo/{curriculum_name}.pdf")

    for page in doc:
      content += page.get_text()
    
    return content
  except Exception as error:
    print(f"Ocorreu um erro ao tentar ler seu currículo: \n{error}")

  