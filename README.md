# ERNIE Challenge - Warmup Task

## Web Builder: Build a Web Page with PaddleOCR & ERNIE

> Link: https://Ishaan300104.github.io/ernie-challenge-warmup

This project demonstrates the integration of **PaddleOCR-VL** and **ERNIE** models to automatically convert PDF documents into beautiful web pages.

### 🎯 Challenge Requirements

This warmup task fulfills the ERNIE Challenge requirements:
1. ✅ Uses PaddleOCR-VL to extract text and layout from a PDF
2. ✅ Converts the content into Markdown
3. ✅ Uses ERNIE model to generate a web page
4. ✅ Ready for deployment on GitHub Pages

### 🚀 Features

- **PDF Text Extraction**: Uses PaddleOCR-VL for intelligent text and layout detection
- **Markdown Conversion**: Automatically converts extracted content to structured Markdown
- **AI-Powered Web Generation**: Leverages ERNIE model to create beautiful, responsive web pages
- **Modern Design**: Generated pages feature:
  - Responsive layout
  - Beautiful gradient backgrounds
  - Clean typography
  - Mobile-friendly design
  - Professional styling

### 📋 Prerequisites

- Python 3.7 or higher
- Baidu AI Studio API credentials (optional for demo mode)

### 🔧 Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd ernie
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Set up Baidu API credentials:
```bash
export BAIDU_API_KEY="your_api_key_here"
export BAIDU_API_SECRET="your_api_secret_here"
```

To get API credentials:
- Visit [Baidu AI Studio](https://aistudio.baidu.com/)
- Create an account and generate API keys

### 💻 Usage

#### Basic Usage (Demo Mode)

Run without a PDF to generate a demo webpage:

```bash
python warmup.py
```

This will create a demo webpage in the `output` directory.

#### With Your Own PDF

```bash
python warmup.py path/to/your/document.pdf
```

#### Output

The script generates:
- `output/content.md` - Extracted content in Markdown format
- `output/index.html` - Generated webpage ready for deployment

### 🌐 Deploying to GitHub Pages

1. Initialize git repository (if not already done):
```bash
git init
```

2. Create a new GitHub repository at https://github.com/new

3. Add and commit your files:
```bash
git add .
git commit -m "Add ERNIE warmup task webpage"
```

4. Connect to your GitHub repository:
```bash
git branch -M main
git remote add origin https://github.com/yourusername/your-repo-name.git
git push -u origin main
```

5. Enable GitHub Pages:
   - Go to your repository on GitHub
   - Navigate to Settings → Pages
   - Under "Source", select the `main` branch
   - Select the `/output` folder (or configure to serve from root and move index.html)
   - Click Save

6. Your page will be live at: `https://yourusername.github.io/your-repo-name/`

### 🏗️ Project Structure

```
ernie/
├── warmup.py           # Main script
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── output/            # Generated files (created after running)
    ├── content.md     # Extracted Markdown
    └── index.html     # Generated webpage
```

### 🔍 How It Works

1. **PDF Extraction**: The script uses PaddleOCR-VL API to extract text and analyze document layout
2. **Markdown Conversion**: Extracted content is converted to Markdown format, preserving structure
3. **Webpage Generation**: ERNIE model transforms Markdown into a complete HTML page with styling
4. **Output**: Beautiful, responsive webpage ready for deployment

### 🎨 Customization

The generated webpage includes:
- Gradient background (purple/blue theme)
- Responsive design for mobile and desktop
- Professional typography
- Smooth spacing and layout
- Badge indicating AI generation

To customize the design, modify the `_generate_html_template` method in `warmup.py`.

### 🔑 API Mode vs Demo Mode

**API Mode** (with credentials):
- Uses actual PaddleOCR-VL for text extraction
- Uses ERNIE model for intelligent webpage generation
- Requires Baidu API credentials

**Demo Mode** (without credentials):
- Uses template-based extraction and generation
- No API calls required
- Perfect for testing and demonstration

### 📚 Resources

- [ERNIE Models](https://huggingface.co/collections/baidu/ernie-45)
- [PaddleOCR Documentation](https://aistudio.baidu.com/paddleocr)
- [Baidu AI Studio](https://aistudio.baidu.com/)
- [ERNIE Challenge Information](https://ernie.baidu.com)

### 🐛 Troubleshooting

**Issue**: "BAIDU_API_KEY not found"
- **Solution**: Set environment variables or run in demo mode (credentials optional)

**Issue**: "API call failed"
- **Solution**: Check your API credentials and internet connection. Script will fallback to demo mode.

**Issue**: "Module not found"
- **Solution**: Run `pip install -r requirements.txt`

### 📝 License

This project is created for the ERNIE Challenge warmup task.

### 🤝 Contributing

This is a challenge submission. Feel free to fork and modify for your own use!

### ✨ Acknowledgments

- **Baidu** for the amazing ERNIE and PaddleOCR models
- **ERNIE Challenge** organizers
- Partner organizations: LLaMA-Factory, Unsloth, Novita AI, CAMEL-AI, D-Robotics

---

**Generated for the ERNIE Challenge Warmup Task**

Powered by **PaddleOCR-VL** and **ERNIE Model** 🚀

