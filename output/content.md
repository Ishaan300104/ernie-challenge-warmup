# Web Builder using PaddleOCR & ERNIE

## Objective

The goal of this warm-up task is to demonstrate an end-to-end pipeline that converts PDF documents into a deployable web page using OCR, document understanding, and large language models.

## Overall Workflow

### 1. Input PDF Document
A PDF document is provided as input with structured text, headings, tables, and layout information.

### 2. Text and Layout Extraction using PaddleOCR-VL
PaddleOCR-VL extracts textual content along with layout-level information such as paragraphs, headings, lists, and structural blocks.

### 3. Conversion to Markdown
The extracted text and layout information are converted into clean, well-structured Markdown format.

### 4. Web Page Generation using ERNIE Model
The Markdown content is passed to the ERNIE language model to generate a complete HTML-based web page.

### 5. Static Website Deployment
The generated HTML content is deployed using GitHub Pages.

## Dataset Context

The dataset used for this workflow has been web-scraped and curated from Arduino official documentation and Arduino user forums.

## Outcome

The final output is a fully functional static web page generated automatically from a PDF document, demonstrating OCR, document understanding, language modeling, and deployment integration.
