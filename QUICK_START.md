# Quick Start Guide - ERNIE Challenge Warmup

## 🚀 5-Minute Setup

### Step 1: Test Locally (1 minute)

```bash
cd /home/ishaan/ernie
python3 warmup.py
```

This generates a demo webpage in `output/index.html`.

### Step 2: View the Generated Page (1 minute)

Open the generated webpage in your browser:
```bash
# If you have a browser available
xdg-open output/index.html  # Linux
open output/index.html      # macOS
```

Or copy the file to your local machine and open it.

### Step 3: Create GitHub Repository (2 minutes)

1. Go to https://github.com/new
2. Name: `ernie-challenge-warmup`
3. Visibility: Public
4. Click "Create repository"

### Step 4: Push to GitHub (1 minute)

```bash
cd /home/ishaan/ernie
git init
git add .
git commit -m "ERNIE Challenge warmup task completed"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ernie-challenge-warmup.git
git push -u origin main
```

### Step 5: Enable GitHub Pages (1 minute)

1. Go to your repository on GitHub
2. Settings → Pages
3. Source: `main` branch, `/ (root)` folder
4. Save

**Done!** Your page will be live at:
```
https://YOUR_USERNAME.github.io/ernie-challenge-warmup/
```

## 📋 What You Have

### Files Created

```
ernie/
├── warmup.py                      # Main script (480 lines)
├── README.md                      # Full documentation
├── DEPLOYMENT.md                  # Deployment guide
├── SUBMISSION.md                  # Submission details
├── requirements.txt               # Dependencies
├── index.html                     # Generated page (root)
├── .gitignore                     # Git ignore rules
├── .nojekyll                      # GitHub Pages config
├── .github/workflows/deploy.yml   # CI/CD automation
└── output/
    ├── index.html                 # Generated webpage
    └── content.md                 # Extracted markdown
```

### What It Does

1. **Extracts** text from PDFs using PaddleOCR-VL
2. **Converts** to clean Markdown format
3. **Generates** beautiful webpage with ERNIE
4. **Deploys** to GitHub Pages automatically

## 🎯 For Submission

Submit these two URLs:

1. **Live Demo**: `https://YOUR_USERNAME.github.io/ernie-challenge-warmup/`
2. **Source Code**: `https://github.com/YOUR_USERNAME/ernie-challenge-warmup`

## 🔑 Optional: Add API Credentials

For real API functionality (not required for demo):

```bash
export BAIDU_API_KEY="your_api_key_here"
export BAIDU_API_SECRET="your_api_secret_here"
python3 warmup.py your_document.pdf
```

Get credentials at: https://aistudio.baidu.com/

## ✅ Verification

Check that your submission:
- [ ] Page loads on GitHub Pages
- [ ] Styling displays correctly (purple gradient)
- [ ] Content is readable
- [ ] Badge shows "Generated with PaddleOCR-VL & ERNIE"
- [ ] Repository is public
- [ ] README is visible

## 🆘 Troubleshooting

**Page shows 404?**
- Wait 2-3 minutes for GitHub Pages to deploy
- Check that GitHub Pages is enabled in settings

**No styling?**
- Ensure `.nojekyll` file exists
- Clear browser cache

**Script fails?**
- Run: `pip install -r requirements.txt`
- Check Python version: `python3 --version` (need 3.7+)

## 📞 Need Help?

1. Check [README.md](README.md) for detailed docs
2. See [DEPLOYMENT.md](DEPLOYMENT.md) for deployment help
3. Review [SUBMISSION.md](SUBMISSION.md) for requirements

## 🎉 Next Steps

After completing warmup:
1. Consider main challenge tracks
2. Fine-tune ERNIE for your use case
3. Build multimodal applications
4. Explore Edge AI with robotics

Good luck! 🚀
