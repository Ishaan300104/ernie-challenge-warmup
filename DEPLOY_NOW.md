# Quick Deploy Guide - Your PDF to GitHub Pages

## ✅ Everything is Ready!

Your project is configured to use `Warmup_PaddleOCR_ERNIE_Web_Builder.pdf` and deploy to GitHub Pages.

## 🚀 Deploy in 3 Steps (5 minutes)

### Step 1: Initialize Git & Commit (2 minutes)

```bash
cd /home/ishaan/ernie

# Initialize git repository
git init

# Add all files (including your PDF)
git add .

# Commit everything
git commit -m "ERNIE Challenge Warmup: PDF to Web Page Builder

- Uses PaddleOCR-VL for text extraction
- Uses ERNIE for webpage generation
- Automated GitHub Pages deployment
- Source PDF: Warmup_PaddleOCR_ERNIE_Web_Builder.pdf"

# Rename branch to main
git branch -M main
```

### Step 2: Create GitHub Repository & Push (2 minutes)

1. **Go to**: https://github.com/new

2. **Repository settings**:
   - Name: `ernie-warmup-task` (or your preferred name)
   - Description: "ERNIE Challenge Warmup - PDF to Web Page using PaddleOCR & ERNIE"
   - Visibility: **Public** ⚠️ (Required for challenge submission)
   - **Do NOT** check "Initialize with README"

3. **Click "Create repository"**

4. **Push your code** (replace YOUR_USERNAME and YOUR_REPO):
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 3: Enable GitHub Pages (1 minute)

**IMPORTANT**: You need to configure GitHub Pages to use GitHub Actions for deployment.

1. Go to your repository: `https://github.com/YOUR_USERNAME/YOUR_REPO`

2. Click **Settings** (top menu)

3. Click **Pages** (left sidebar)

4. Under "Build and deployment":
   - **Source**: Select **"GitHub Actions"**
   - (NOT "Deploy from a branch")

5. The workflow will automatically run!

### ⏳ Wait for Deployment

1. Go to the **Actions** tab in your repository
2. You'll see the "Deploy to GitHub Pages" workflow running
3. Wait 1-2 minutes for it to complete
4. Once done, your page will be live!

## 🌐 Your Live URL

Your webpage will be available at:
```
https://YOUR_USERNAME.github.io/YOUR_REPO/
```

Example: `https://ishaan.github.io/ernie-warmup-task/`

## 📋 For ERNIE Challenge Submission

Submit these URLs:

1. **Deployed Webpage**: `https://YOUR_USERNAME.github.io/YOUR_REPO/`
2. **GitHub Repository**: `https://github.com/YOUR_USERNAME/YOUR_REPO`

## 🎯 What's Included

Your repository contains:
- ✅ `Warmup_PaddleOCR_ERNIE_Web_Builder.pdf` - Your source PDF
- ✅ `warmup.py` - Main conversion script
- ✅ `output/index.html` - Generated beautiful webpage
- ✅ `output/content.md` - Extracted markdown
- ✅ `.github/workflows/deploy.yml` - Automated deployment
- ✅ Complete documentation (README, guides)

## 🔍 Verify Your Submission

After deployment, check:
- [ ] Page loads correctly
- [ ] Purple gradient background displays
- [ ] Badge shows "Generated with PaddleOCR-VL & ERNIE"
- [ ] Content is readable
- [ ] Responsive on mobile (test by resizing browser)

## 🐛 Troubleshooting

**Workflow fails?**
- Check the Actions tab for error details
- The workflow is already fixed to use non-deprecated actions
- Make sure GitHub Pages source is set to "GitHub Actions"

**Page shows 404?**
- Verify GitHub Pages is enabled in Settings → Pages
- Check that the workflow completed successfully
- Wait 2-3 minutes after workflow completes

**No styling on page?**
- Ensure `.nojekyll` file exists in repo
- Clear browser cache (Ctrl+Shift+R)

## 🎉 You're Done!

Once deployed:
1. Visit your live page
2. Take a screenshot for your records
3. Submit the URLs to the ERNIE Challenge
4. Consider tackling other challenge tracks!

## 📞 Quick Reference

**Repository Setup**:
```bash
git init
git add .
git commit -m "ERNIE Challenge warmup task"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

**Enable Pages**: Settings → Pages → Source: GitHub Actions

**Check Deployment**: Repository → Actions tab

**Live URL**: `https://YOUR_USERNAME.github.io/YOUR_REPO/`

Good luck with the challenge! 🚀
