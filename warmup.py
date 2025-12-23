"""
ERNIE Challenge - Warmup Task
Web Builder: Build a Web Page with PaddleOCR & ERNIE

This script:
1. Uses PaddleOCR-VL to extract text and layout from a PDF
2. Converts the content into Markdown
3. Uses ERNIE model to generate a web page
4. Prepares it for deployment on GitHub Pages
"""

import os
import requests
from pathlib import Path
from typing import Dict, Optional
import base64

class PDFToWebPageConverter:
    """Convert PDF to webpage using PaddleOCR-VL and ERNIE"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the converter

        Args:
            api_key: Baidu AI Studio API key (optional, can be set via environment)
        """
        self.api_key = api_key or os.getenv('BAIDU_API_KEY')
        self.api_secret = os.getenv('BAIDU_API_SECRET')
        self.access_token = None

        # Create output directories
        self.output_dir = Path('output')
        self.output_dir.mkdir(exist_ok=True)

    def get_access_token(self) -> str:
        """Get Baidu access token for API calls"""
        if self.access_token:
            return self.access_token

        url = f"https://aip.baidubce.com/oauth/2.0/token"
        params = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            self.access_token = response.json().get("access_token")
            return self.access_token
        except Exception as e:
            print(f"Error getting access token: {e}")
            print("Continuing in demo mode without API...")
            return None

    def extract_text_from_pdf_with_paddleocr(self, pdf_path: str) -> Dict:
        """
        Extract text and layout from PDF using PaddleOCR-VL

        Args:
            pdf_path: Path to the PDF file

        Returns:
            Dictionary containing extracted text and layout information
        """
        print(f"Extracting text from {pdf_path} using PaddleOCR-VL...")

        # For demo purposes, we'll simulate OCR extraction
        # In production, you would use the actual PaddleOCR-VL API

        # Try to use actual API if credentials are available
        if self.get_access_token():
            try:
                # Read PDF file
                with open(pdf_path, 'rb') as f:
                    pdf_content = base64.b64encode(f.read()).decode('utf-8')

                # Note: This is a placeholder for the actual PaddleOCR-VL API endpoint
                # You'll need to use the correct endpoint from Baidu AI Studio
                url = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_analysis"
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                data = {
                    'pdf_file': pdf_content,
                    'access_token': self.access_token
                }

                response = requests.post(url, headers=headers, data=data)
                if response.status_code == 200:
                    return response.json()
            except Exception as e:
                print(f"API call failed: {e}")
                print("Using demo extraction instead...")

        # Demo extraction (simulated structure)
        return {
            'extracted_text': self._demo_extract_from_pdf(),
            'layout': [
                {'type': 'title', 'text': 'Sample Document Title'},
                {'type': 'heading', 'text': 'Introduction'},
                {'type': 'paragraph', 'text': 'This is a sample document.'},
                {'type': 'heading', 'text': 'Main Content'},
                {'type': 'paragraph', 'text': 'Here is the main content of the document.'},
            ]
        }

    def _demo_extract_from_pdf(self) -> str:
        """Demo extraction when API is not available"""
        return """# ERNIE Challenge - Sample Document

## Introduction
Welcome to the ERNIE Challenge warmup task demonstration.

## About ERNIE
ERNIE (Enhanced Representation through kNowledge IntEgration) is Baidu's state-of-the-art language model series.

### Key Features
- Advanced natural language understanding
- Multimodal capabilities
- Efficient fine-tuning support
- Open-source models available

## PaddleOCR
PaddleOCR is a powerful OCR toolkit that supports multiple languages and document types.

### Capabilities
- Text detection and recognition
- Layout analysis
- Document understanding
- Multi-language support

## Conclusion
This demonstration shows the integration of PaddleOCR-VL and ERNIE for web page generation."""

    def convert_to_markdown(self, extracted_data: Dict) -> str:
        """
        Convert extracted data to Markdown format

        Args:
            extracted_data: Data extracted from PDF

        Returns:
            Markdown formatted string
        """
        print("Converting to Markdown...")

        if 'extracted_text' in extracted_data:
            # If we already have formatted text, use it
            markdown = extracted_data['extracted_text']
        else:
            # Build markdown from layout information
            markdown_lines = []

            for item in extracted_data.get('layout', []):
                item_type = item.get('type', 'paragraph')
                text = item.get('text', '')

                if item_type == 'title':
                    markdown_lines.append(f"# {text}\n")
                elif item_type == 'heading':
                    markdown_lines.append(f"## {text}\n")
                elif item_type == 'subheading':
                    markdown_lines.append(f"### {text}\n")
                elif item_type == 'paragraph':
                    markdown_lines.append(f"{text}\n")
                elif item_type == 'list_item':
                    markdown_lines.append(f"- {text}")
                else:
                    markdown_lines.append(f"{text}\n")

            markdown = '\n'.join(markdown_lines)

        # Save markdown
        markdown_path = self.output_dir / 'content.md'
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"Markdown saved to {markdown_path}")
        return markdown

    def generate_webpage_with_ernie(self, markdown_content: str) -> str:
        """
        Use ERNIE model to generate a web page from Markdown

        Args:
            markdown_content: Markdown formatted content

        Returns:
            HTML webpage content
        """
        print("Generating webpage with ERNIE...")

        # Prepare prompt for ERNIE
        prompt = f"""Convert the following Markdown content into a beautiful, modern HTML webpage.
The webpage should include:
- A professional and clean design
- Responsive CSS styling
- Proper semantic HTML5 structure
- A color scheme that is visually appealing
- Smooth typography and spacing

Markdown content:
{markdown_content}

Generate a complete, single-file HTML page with embedded CSS."""

        # Try to use ERNIE API if available
        if self.get_access_token():
            try:
                html = self._call_ernie_api(prompt)
                if html:
                    return html
            except Exception as e:
                print(f"ERNIE API call failed: {e}")
                print("Using template-based generation...")

        # Fallback: Generate using a template
        return self._generate_html_template(markdown_content)

    def _call_ernie_api(self, prompt: str) -> Optional[str]:
        """Call ERNIE API for text generation"""
        # ERNIE API endpoint (use the correct endpoint from Baidu AI Studio)
        url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-4.5-8k?access_token={self.access_token}"

        headers = {'Content-Type': 'application/json'}
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "top_p": 0.9
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result.get('result', '')
        except Exception as e:
            print(f"Error calling ERNIE API: {e}")
            return None

    def _generate_html_template(self, markdown_content: str) -> str:
        """Generate HTML using a template (fallback when API unavailable)"""
        # Convert markdown to basic HTML
        html_content = self._markdown_to_html(markdown_content)

        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ERNIE Challenge - Generated Page</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 3rem;
        }}

        h1 {{
            color: #667eea;
            font-size: 2.5rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 3px solid #667eea;
        }}

        h2 {{
            color: #764ba2;
            font-size: 2rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }}

        h3 {{
            color: #555;
            font-size: 1.5rem;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }}

        p {{
            margin-bottom: 1rem;
            text-align: justify;
        }}

        ul, ol {{
            margin-left: 2rem;
            margin-bottom: 1rem;
        }}

        li {{
            margin-bottom: 0.5rem;
        }}

        code {{
            background: #f4f4f4;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}

        .footer {{
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #eee;
            text-align: center;
            color: #666;
            font-size: 0.9rem;
        }}

        .badge {{
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.85rem;
            margin-bottom: 1rem;
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 1rem;
            }}

            .container {{
                padding: 1.5rem;
            }}

            h1 {{
                font-size: 2rem;
            }}

            h2 {{
                font-size: 1.5rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="badge">🤖 Generated with PaddleOCR-VL & ERNIE</div>
        {html_content}
        <div class="footer">
            <p>Generated for the ERNIE Challenge Warmup Task</p>
            <p>Powered by <strong>PaddleOCR-VL</strong> and <strong>ERNIE Model</strong></p>
        </div>
    </div>
</body>
</html>"""

        return html_template

    def _markdown_to_html(self, markdown: str) -> str:
        """Simple markdown to HTML conversion"""
        lines = markdown.split('\n')
        html_lines = []
        in_list = False

        for line in lines:
            line = line.strip()

            if not line:
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append('<br>')
                continue

            # Headers
            if line.startswith('# '):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append(f'<h1>{line[2:]}</h1>')
            elif line.startswith('## '):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append(f'<h2>{line[3:]}</h2>')
            elif line.startswith('### '):
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append(f'<h3>{line[4:]}</h3>')
            # Lists
            elif line.startswith('- ') or line.startswith('* '):
                if not in_list:
                    html_lines.append('<ul>')
                    in_list = True
                html_lines.append(f'<li>{line[2:]}</li>')
            # Paragraphs
            else:
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append(f'<p>{line}</p>')

        if in_list:
            html_lines.append('</ul>')

        return '\n'.join(html_lines)

    def save_webpage(self, html_content: str, filename: str = 'index.html') -> Path:
        """
        Save the generated webpage

        Args:
            html_content: HTML content to save
            filename: Output filename

        Returns:
            Path to the saved file
        """
        output_path = self.output_dir / filename

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"Webpage saved to {output_path}")
        return output_path

    def process(self, pdf_path: str) -> Path:
        """
        Complete pipeline: PDF -> Markdown -> Webpage

        Args:
            pdf_path: Path to input PDF file

        Returns:
            Path to generated webpage
        """
        print("=" * 60)
        print("ERNIE Challenge - Warmup Task")
        print("PDF to Webpage Converter")
        print("=" * 60)

        # Step 1: Extract text from PDF
        extracted_data = self.extract_text_from_pdf_with_paddleocr(pdf_path)

        # Step 2: Convert to Markdown
        markdown = self.convert_to_markdown(extracted_data)

        # Step 3: Generate webpage with ERNIE
        html = self.generate_webpage_with_ernie(markdown)

        # Step 4: Save webpage
        output_path = self.save_webpage(html)

        print("=" * 60)
        print(f"✅ Success! Webpage generated at: {output_path}")
        print("=" * 60)

        return output_path


def main():
    """Main function to run the warmup task"""
    import sys

    # Check for API credentials in environment
    api_key = os.getenv('BAIDU_API_KEY')
    api_secret = os.getenv('BAIDU_API_SECRET')

    if not api_key or not api_secret:
        print("⚠️  Warning: BAIDU_API_KEY or BAIDU_API_SECRET not found in environment")
        print("Set them with:")
        print("  export BAIDU_API_KEY='your_api_key'")
        print("  export BAIDU_API_SECRET='your_api_secret'")
        print("\nContinuing in demo mode...\n")

    # Initialize converter
    converter = PDFToWebPageConverter()

    # Get PDF path from command line or use demo
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        # Create a demo PDF path
        pdf_path = 'sample.pdf'
        print(f"ℹ️  No PDF specified. Using demo mode.")
        print(f"Usage: python warmup.py <path_to_pdf>\n")

    # Process the PDF
    try:
        output_path = converter.process(pdf_path)

        print("\nNext steps:")
        print("1. Review the generated webpage in the 'output' directory")
        print("2. Initialize a git repository if not already done")
        print("3. Create a GitHub repository")
        print("4. Push your code and enable GitHub Pages")
        print("\nCommands to deploy to GitHub Pages:")
        print("  git init")
        print("  git add .")
        print("  git commit -m 'Add ERNIE warmup task webpage'")
        print("  git branch -M main")
        print("  git remote add origin <your-repo-url>")
        print("  git push -u origin main")
        print("\nThen enable GitHub Pages in your repository settings!")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
