"""
Generate a sample PDF about AI and Language Models
This creates a PDF relevant to the ERNIE Challenge
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

def create_ai_language_models_pdf(filename="sample_ai_document.pdf"):
    """Create a sample PDF about AI and Language Models"""

    # Create the PDF
    doc = SimpleDocTemplate(filename, pagesize=letter,
                          rightMargin=72, leftMargin=72,
                          topMargin=72, bottomMargin=18)

    # Container for the 'Flowable' objects
    elements = []

    # Define styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    # Title
    title = Paragraph("<b>The Evolution of Large Language Models:<br/>From Transformers to ERNIE</b>",
                     styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Subtitle
    subtitle = Paragraph("<i>A Comprehensive Overview of Modern NLP Technology</i>",
                        styles['Center'])
    elements.append(subtitle)
    elements.append(Spacer(1, 24))

    # Abstract
    abstract_title = Paragraph("<b>Abstract</b>", styles['Heading2'])
    elements.append(abstract_title)
    elements.append(Spacer(1, 12))

    abstract = Paragraph(
        """This document provides an overview of the recent advancements in large language models (LLMs),
        with particular focus on ERNIE (Enhanced Representation through kNowledge IntEgration) developed
        by Baidu. We explore the evolution from traditional NLP methods to modern transformer-based
        architectures, and discuss how knowledge-enhanced pre-training has revolutionized natural
        language understanding tasks.""",
        styles['Justify']
    )
    elements.append(abstract)
    elements.append(Spacer(1, 24))

    # Introduction
    intro_title = Paragraph("<b>1. Introduction</b>", styles['Heading2'])
    elements.append(intro_title)
    elements.append(Spacer(1, 12))

    intro_text = Paragraph(
        """Natural Language Processing (NLP) has undergone a remarkable transformation in recent years.
        The advent of transformer architectures in 2017 marked a paradigm shift in how machines process
        and understand human language. Large Language Models (LLMs) have since become the cornerstone
        of modern AI applications, powering everything from search engines to conversational AI systems.""",
        styles['Justify']
    )
    elements.append(intro_text)
    elements.append(Spacer(1, 12))

    intro_text2 = Paragraph(
        """Among the various LLMs developed globally, ERNIE stands out as a significant contribution from
        Baidu, China's leading AI company. ERNIE's approach to knowledge integration sets it apart from
        other models, enabling superior performance on tasks requiring deep semantic understanding.""",
        styles['Justify']
    )
    elements.append(intro_text2)
    elements.append(Spacer(1, 24))

    # Transformer Architecture
    transformer_title = Paragraph("<b>2. The Transformer Revolution</b>", styles['Heading2'])
    elements.append(transformer_title)
    elements.append(Spacer(1, 12))

    transformer_subtitle = Paragraph("<b>2.1 Self-Attention Mechanism</b>", styles['Heading3'])
    elements.append(transformer_subtitle)
    elements.append(Spacer(1, 12))

    transformer_text = Paragraph(
        """The transformer architecture introduced the self-attention mechanism, allowing models to weigh
        the importance of different words in a sentence when processing each word. This parallel processing
        capability overcame the sequential limitations of previous RNN-based models, enabling faster training
        and better capture of long-range dependencies in text.""",
        styles['Justify']
    )
    elements.append(transformer_text)
    elements.append(Spacer(1, 12))

    transformer_subtitle2 = Paragraph("<b>2.2 Pre-training and Fine-tuning Paradigm</b>", styles['Heading3'])
    elements.append(transformer_subtitle2)
    elements.append(Spacer(1, 12))

    transformer_text2 = Paragraph(
        """The pre-training and fine-tuning approach has become the standard methodology for developing
        language models. Models are first pre-trained on large corpora of text to learn general language
        representations, then fine-tuned on specific downstream tasks. This transfer learning approach
        has proven highly effective across diverse NLP applications.""",
        styles['Justify']
    )
    elements.append(transformer_text2)
    elements.append(Spacer(1, 24))

    # ERNIE Section
    ernie_title = Paragraph("<b>3. ERNIE: Enhanced Representation through kNowledge IntEgration</b>",
                           styles['Heading2'])
    elements.append(ernie_title)
    elements.append(Spacer(1, 12))

    ernie_subtitle = Paragraph("<b>3.1 Knowledge-Enhanced Pre-training</b>", styles['Heading3'])
    elements.append(ernie_subtitle)
    elements.append(Spacer(1, 12))

    ernie_text = Paragraph(
        """ERNIE distinguishes itself through its knowledge-enhanced pre-training strategy. Unlike models
        that learn purely from text patterns, ERNIE incorporates structured knowledge from knowledge graphs
        during pre-training. This approach enables the model to develop a deeper understanding of entities,
        concepts, and their relationships.""",
        styles['Justify']
    )
    elements.append(ernie_text)
    elements.append(Spacer(1, 12))

    ernie_subtitle2 = Paragraph("<b>3.2 Multimodal Capabilities</b>", styles['Heading3'])
    elements.append(ernie_subtitle2)
    elements.append(Spacer(1, 12))

    ernie_text2 = Paragraph(
        """Recent versions of ERNIE have expanded beyond text to support multimodal understanding.
        ERNIE-ViL and other variants can process both text and images, enabling applications in
        visual question answering, image captioning, and cross-modal retrieval. This multimodal
        capability makes ERNIE particularly suitable for real-world applications where information
        comes in multiple formats.""",
        styles['Justify']
    )
    elements.append(ernie_text2)
    elements.append(Spacer(1, 24))

    # OCR Integration
    ocr_title = Paragraph("<b>4. PaddleOCR: Bridging Vision and Language</b>", styles['Heading2'])
    elements.append(ocr_title)
    elements.append(Spacer(1, 12))

    ocr_subtitle = Paragraph("<b>4.1 Optical Character Recognition in the AI Era</b>", styles['Heading3'])
    elements.append(ocr_subtitle)
    elements.append(Spacer(1, 12))

    ocr_text = Paragraph(
        """PaddleOCR represents Baidu's contribution to optical character recognition technology.
        Modern OCR systems go beyond simple character recognition to understand document layout,
        structure, and semantics. PaddleOCR-VL (Vision-Language) combines visual understanding with
        language processing, enabling intelligent document analysis and understanding.""",
        styles['Justify']
    )
    elements.append(ocr_text)
    elements.append(Spacer(1, 12))

    ocr_subtitle2 = Paragraph("<b>4.2 Applications in Document Processing</b>", styles['Heading3'])
    elements.append(ocr_subtitle2)
    elements.append(Spacer(1, 12))

    ocr_text2 = Paragraph(
        """The integration of OCR with language models enables powerful document processing pipelines.
        Documents can be automatically digitized, analyzed for content and structure, and transformed
        into various formats. This capability is crucial for digitizing historical documents, automating
        data entry, and making information more accessible across different platforms and formats.""",
        styles['Justify']
    )
    elements.append(ocr_text2)
    elements.append(Spacer(1, 24))

    # Applications
    app_title = Paragraph("<b>5. Real-World Applications</b>", styles['Heading2'])
    elements.append(app_title)
    elements.append(Spacer(1, 12))

    app_text = Paragraph(
        """The combination of ERNIE and PaddleOCR enables numerous practical applications:""",
        styles['Justify']
    )
    elements.append(app_text)
    elements.append(Spacer(1, 12))

    applications = [
        "<b>Document Understanding:</b> Automatically extract and understand content from scanned documents, PDFs, and images.",
        "<b>Intelligent Search:</b> Enhanced search capabilities that understand semantic meaning beyond keyword matching.",
        "<b>Content Generation:</b> Create summaries, reports, and web content from structured and unstructured data.",
        "<b>Translation Services:</b> Accurate translation that preserves context and cultural nuances.",
        "<b>Question Answering:</b> Build intelligent chatbots and virtual assistants that understand complex queries.",
        "<b>Accessibility:</b> Convert visual content to text for visually impaired users.",
    ]

    for app in applications:
        elements.append(Paragraph(f"• {app}", styles['Normal']))
        elements.append(Spacer(1, 8))

    elements.append(Spacer(1, 16))

    # Fine-tuning Section
    finetune_title = Paragraph("<b>6. Fine-tuning and Customization</b>", styles['Heading2'])
    elements.append(finetune_title)
    elements.append(Spacer(1, 12))

    finetune_text = Paragraph(
        """One of the key advantages of modern LLMs is their adaptability through fine-tuning. Organizations
        can customize ERNIE for specific domains or tasks by fine-tuning on domain-specific data. Tools like
        LLaMA-Factory and Unsloth have made this process more accessible, enabling efficient fine-tuning even
        with limited computational resources.""",
        styles['Justify']
    )
    elements.append(finetune_text)
    elements.append(Spacer(1, 12))

    finetune_text2 = Paragraph(
        """Parameter-efficient fine-tuning techniques such as LoRA (Low-Rank Adaptation) allow practitioners
        to adapt large models with minimal computational overhead. This democratization of AI technology
        enables smaller teams and organizations to leverage state-of-the-art models for their specific needs.""",
        styles['Justify']
    )
    elements.append(finetune_text2)
    elements.append(Spacer(1, 24))

    # Future Directions
    future_title = Paragraph("<b>7. Future Directions</b>", styles['Heading2'])
    elements.append(future_title)
    elements.append(Spacer(1, 12))

    future_text = Paragraph(
        """The future of language models and OCR technology points toward even greater integration and
        capability. We anticipate advancements in several key areas:""",
        styles['Justify']
    )
    elements.append(future_text)
    elements.append(Spacer(1, 12))

    future_text2 = Paragraph(
        """<b>Multimodal Understanding:</b> Deeper integration across text, vision, audio, and other modalities
        will enable more natural human-AI interaction. Models will understand context across different
        sensory inputs, much like humans do.""",
        styles['Justify']
    )
    elements.append(future_text2)
    elements.append(Spacer(1, 12))

    future_text3 = Paragraph(
        """<b>Edge Deployment:</b> Optimization techniques will enable deployment of powerful models on
        edge devices, bringing AI capabilities to smartphones, IoT devices, and robotics platforms. This
        will enable real-time processing without cloud connectivity.""",
        styles['Justify']
    )
    elements.append(future_text3)
    elements.append(Spacer(1, 12))

    future_text4 = Paragraph(
        """<b>Specialized Models:</b> While general-purpose models will continue to improve, we'll see
        more specialized variants optimized for specific domains like healthcare, legal, scientific research,
        and creative industries.""",
        styles['Justify']
    )
    elements.append(future_text4)
    elements.append(Spacer(1, 24))

    # Conclusion
    conclusion_title = Paragraph("<b>8. Conclusion</b>", styles['Heading2'])
    elements.append(conclusion_title)
    elements.append(Spacer(1, 12))

    conclusion_text = Paragraph(
        """The evolution of large language models, exemplified by ERNIE, represents a fundamental shift
        in how machines process and understand human language. Combined with advanced OCR capabilities
        like PaddleOCR, these technologies are transforming how we interact with information, breaking
        down barriers between different modalities and formats.""",
        styles['Justify']
    )
    elements.append(conclusion_text)
    elements.append(Spacer(1, 12))

    conclusion_text2 = Paragraph(
        """As these technologies continue to mature and become more accessible, we can expect to see
        innovative applications that were previously impossible. The key to unlocking this potential
        lies in the community's ability to adapt, fine-tune, and creatively apply these tools to
        real-world problems. The ERNIE ecosystem, with its combination of powerful models, efficient
        fine-tuning tools, and comprehensive documentation, provides an excellent platform for
        developers and researchers to build the next generation of AI applications.""",
        styles['Justify']
    )
    elements.append(conclusion_text2)
    elements.append(Spacer(1, 24))

    # References
    ref_title = Paragraph("<b>References</b>", styles['Heading2'])
    elements.append(ref_title)
    elements.append(Spacer(1, 12))

    references = [
        "Vaswani, A., et al. (2017). Attention is all you need. Advances in neural information processing systems.",
        "Sun, Y., et al. (2019). ERNIE: Enhanced representation through knowledge integration. arXiv preprint.",
        "Devlin, J., et al. (2018). BERT: Pre-training of deep bidirectional transformers for language understanding.",
        "Du, Y., et al. (2020). PP-OCR: A practical ultra lightweight OCR system. arXiv preprint.",
        "Brown, T., et al. (2020). Language models are few-shot learners. Advances in neural information processing systems.",
    ]

    for ref in references:
        elements.append(Paragraph(ref, styles['Normal']))
        elements.append(Spacer(1, 8))

    # Build PDF
    doc.build(elements)
    print(f"✅ PDF created successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_ai_language_models_pdf()
