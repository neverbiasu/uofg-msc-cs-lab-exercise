import argparse
import os
import re
import sys
from pathlib import Path

try:
    import pdfplumber
    import PyPDF2
except ImportError:
    print("Required packages not found. Please install them with:")
    print("pip install PyPDF2 pdfplumber")
    sys.exit(1)


class PDFToMarkdownConverter:
    def __init__(self):
        self.output_text = ""

    def extract_text_with_pdfplumber(self, pdf_path):
        """
        Extract text from PDF using pdfplumber (better for text extraction)
        """
        text_content = []

        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    print(f"Processing page {page_num}...")

                    # Extract text
                    text = page.extract_text()
                    if text:
                        # Add page separator
                        text_content.append(f"\n<!-- Page {page_num} -->\n")
                        text_content.append(text)
                        text_content.append("\n\n")

        except Exception as e:
            print(f"Error extracting text with pdfplumber: {e}")
            return None

        return "".join(text_content)

    def extract_text_with_pypdf2(self, pdf_path):
        """
        Fallback method using PyPDF2
        """
        text_content = []

        try:
            with open(pdf_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)

                for page_num, page in enumerate(pdf_reader.pages, 1):
                    print(f"Processing page {page_num}...")

                    text = page.extract_text()
                    if text:
                        text_content.append(f"\n<!-- Page {page_num} -->\n")
                        text_content.append(text)
                        text_content.append("\n\n")

        except Exception as e:
            print(f"Error extracting text with PyPDF2: {e}")
            return None

        return "".join(text_content)

    def clean_and_format_text(self, text):
        """
        Clean and format the extracted text for Markdown
        """
        if not text:
            return ""

        # Remove excessive whitespace
        text = re.sub(r"\n\s*\n\s*\n", "\n\n", text)

        # Fix common formatting issues
        text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)  # Add space between camelCase
        text = re.sub(r"(\w)(\d)", r"\1 \2", text)  # Add space between word and number
        text = re.sub(r"(\d)(\w)", r"\1 \2", text)  # Add space between number and word

        # Convert common patterns to Markdown
        lines = text.split("\n")
        processed_lines = []

        for line in lines:
            line = line.strip()
            if not line:
                processed_lines.append("")
                continue

            # Detect headers (lines that are all caps or start with numbers)
            if line.isupper() and len(line) > 5:
                processed_lines.append(f"## {line.title()}")
            elif re.match(r"^\d+\.?\s+[A-Z]", line):
                processed_lines.append(f"### {line}")
            elif re.match(r"^[A-Z][a-z]+.*:$", line):
                processed_lines.append(f"**{line}**")
            else:
                processed_lines.append(line)

        return "\n".join(processed_lines)

    def add_metadata(self, pdf_path, text):
        """
        Add metadata header to the Markdown content
        """
        pdf_name = Path(pdf_path).stem
        metadata = f"""# {pdf_name}

*Converted from PDF: {Path(pdf_path).name}*

---

"""
        return metadata + text

    def convert_pdf_to_markdown(self, pdf_path, output_path=None, method="pdfplumber"):
        """
        Main conversion function
        """
        if not os.path.exists(pdf_path):
            print(f"Error: PDF file '{pdf_path}' not found.")
            return False

        print(f"Converting PDF: {pdf_path}")

        # Extract text using specified method
        if method == "pdfplumber":
            text = self.extract_text_with_pdfplumber(pdf_path)
            if text is None:
                print("pdfplumber failed, trying PyPDF2...")
                text = self.extract_text_with_pypdf2(pdf_path)
        else:
            text = self.extract_text_with_pypdf2(pdf_path)
            if text is None:
                print("PyPDF2 failed, trying pdfplumber...")
                text = self.extract_text_with_pdfplumber(pdf_path)

        if text is None:
            print("Failed to extract text from PDF.")
            return False

        # Clean and format text
        formatted_text = self.clean_and_format_text(text)

        # Add metadata
        final_content = self.add_metadata(pdf_path, formatted_text)

        # Determine output path
        if output_path is None:
            pdf_path_obj = Path(pdf_path)
            output_path = pdf_path_obj.parent / f"{pdf_path_obj.stem}.md"

        # Write to file
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(final_content)

            print(f"Successfully converted PDF to Markdown: {output_path}")
            return True

        except Exception as e:
            print(f"Error writing output file: {e}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF files to Markdown format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python pdf_to_md_converter.py document.pdf
  python pdf_to_md_converter.py document.pdf -o output.md
  python pdf_to_md_converter.py document.pdf --method pypdf2
        """,
    )

    parser.add_argument("pdf_file", help="Path to the PDF file to convert")
    parser.add_argument("-o", "--output", help="Output Markdown file path")
    parser.add_argument(
        "--method",
        choices=["pdfplumber", "pypdf2"],
        default="pdfplumber",
        help="Text extraction method",
    )

    args = parser.parse_args()

    # Create converter instance
    converter = PDFToMarkdownConverter()

    # Convert PDF
    success = converter.convert_pdf_to_markdown(args.pdf_file, args.output, args.method)

    if success:
        print("Conversion completed successfully!")
    else:
        print("Conversion failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
