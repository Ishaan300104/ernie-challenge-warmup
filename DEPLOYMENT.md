# GitHub Pages Deployment Guide

This guide will help you deploy your ERNIE Challenge warmup task webpage to GitHub Pages.

## Method 1: Manual Deployment (Recommended for Beginners)

### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and log in
2. Click the "+" icon in the top right and select "New repository"
3. Name your repository (e.g., `ernie-challenge-warmup`)
4. Choose "Public" visibility
5. Do NOT initialize with README (we already have one)
6. Click "Create repository"

### Step 2: Initialize Git and Push Your Code

```bash
# Navigate to your project directory
cd /home/ishaan/ernie

# Initialize git repository
git init

# Add all files
git add .

# Create your first commit
git commit -m "Initial commit: ERNIE Challenge warmup task"

# Rename branch to main
git branch -M main

# Add your GitHub repository as remote (replace with your URL)
git remote add origin https://github.com/YOUR_USERNAME/ernie-challenge-warmup.git

# Push to GitHub
git push -u origin main
```

### Step 3: Configure GitHub Pages

1. Go to your repository on GitHub
2. Click on "Settings" (top menu bar)
3. Scroll down and click "Pages" in the left sidebar
4. Under "Source":
   - Select branch: `main`
   - Select folder: `/ (root)`
   - Click "Save"
5. Wait a few minutes for deployment

### Step 4: Access Your Webpage

Your page will be available at:
```
https://YOUR_USERNAME.github.io/ernie-challenge-warmup/output/
```

Or you can move `index.html` to the root:
```bash
cp output/index.html index.html
git add index.html
git commit -m "Add index.html to root for easier access"
git push
```

Then access at:
```
https://YOUR_USERNAME.github.io/ernie-challenge-warmup/
```

## Method 2: Automated Deployment with GitHub Actions

Create a GitHub Actions workflow for automatic deployment whenever you push changes.

### Step 1: Create Workflow File

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run warmup script
      run: python warmup.py

    - name: Copy index.html to root
      run: cp output/index.html index.html

    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: .
```

### Step 2: Enable GitHub Actions

1. Commit and push the workflow file
2. Go to your repository on GitHub
3. Click "Actions" tab
4. You should see the workflow running
5. Once complete, your page will be deployed

## Method 3: Custom Domain (Optional)

If you have a custom domain:

1. Go to repository Settings → Pages
2. Under "Custom domain", enter your domain
3. Click "Save"
4. Add a CNAME record in your domain's DNS settings:
   - Type: CNAME
   - Name: www (or desired subdomain)
   - Value: YOUR_USERNAME.github.io

## Troubleshooting

### Issue: Page shows 404

**Solution**:
- Check that GitHub Pages is enabled in settings
- Verify the correct branch and folder are selected
- Wait a few minutes for deployment to complete

### Issue: Styles not loading

**Solution**:
- Ensure `.nojekyll` file exists in repository root
- Check that all files are committed and pushed

### Issue: Page not updating

**Solution**:
- Clear your browser cache
- Try accessing in incognito/private mode
- Wait a few minutes for GitHub Pages to rebuild

## Verification

After deployment, verify your submission:

1. ✅ Page loads correctly
2. ✅ Styling is applied (purple gradient background)
3. ✅ Content is visible and readable
4. ✅ Page is responsive on mobile
5. ✅ Badge shows "Generated with PaddleOCR-VL & ERNIE"

## Submission

For the ERNIE Challenge, submit:

1. **The deployed web page URL**:
   - `https://YOUR_USERNAME.github.io/ernie-challenge-warmup/`

2. **GitHub repository URL**:
   - `https://github.com/YOUR_USERNAME/ernie-challenge-warmup`

3. **Screenshot** (optional but recommended):
   - Take a screenshot of your deployed page
   - Shows completion of the warmup task

## Next Steps

After completing the warmup task:

1. Consider participating in other challenge tracks:
   - Best ERNIE Fine-Tune
   - Best PaddleOCR-VL Fine-Tune
   - Best Multimodal Application
   - Best in Edge AI & Robotics
   - Best Agent System

2. Enhance your submission:
   - Add custom PDF processing
   - Integrate real API calls with credentials
   - Improve webpage design
   - Add more features

Good luck with the ERNIE Challenge! 🚀
