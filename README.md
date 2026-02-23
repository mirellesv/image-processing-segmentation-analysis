# 🫁 Chest X-Ray Image Analysis for Medical Image Enhancement  

![Python](https://img.shields.io/badge/Python-3.12-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Dataset](https://img.shields.io/badge/Dataset-Kaggle-orange)
![Status](https://img.shields.io/badge/Project-Academic%20%7C%20Portfolio-success)

## 🇺🇸 English Version

### 📝 Project Overview

This project applies Digital Image Processing techniques to enhance and analyze chest X-ray images using Python.

The implemented pipeline combines spatial filtering and intensity-based segmentation to isolate lung regions while preserving structural similarity. Image quality is quantitatively evaluated using PSNR and SSIM metrics.

In addition to the implementation, a full academic paper detailing the theoretical foundation, mathematical formulation, methodology, and statistical analysis is included in this repository.

This project demonstrates practical computer vision applications in medical imaging and preprocessing pipelines.

## 🎥 Project Demonstration

https://github.com/user-attachments/assets/95ba6e7c-eabb-4c5b-836f-0d6a9077eb26

### 🛠️ Technologies

The experiments were implemented in **Python 3.12**.

The following libraries were used:

- NumPy  
- OpenCV  
- scikit-image  
- Matplotlib  

## 📁 Dataset

The experiments were conducted using the 
[Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) dataset available on Kaggle.

The dataset contains 5,863 chest X-ray images (8-bit grayscale) divided into two classes:

- Normal  
- Pneumonia  

The images are organized into:
- `train`
- `validation`
- `test`

The images were used to:

- Apply Gaussian filtering  
- Perform lung region segmentation  
- Evaluate image quality improvements  

## 📄 Article

The full paper is available here:

[Download the full paper (PDF)](https://github.com/mirellesv/image-processing-segmentation-analysis/raw/main/article/Chest%20X-Ray%20Image%20Analysis%20Using%20Filtering%20and%20Segmentation%20-%20Article.pdf)

The article includes:

- Mathematical formulation of the Gaussian filter  
- Threshold-based segmentation methodology  
- MSE, PSNR and SSIM derivations  
- Statistical analysis across multiple samples  
- Experimental discussion and conclusions  

### 🧠 Technical Implementation

The system follows three main stages:

#### 1️⃣ Preprocessing
- Gaussian filtering for noise reduction  
- Image smoothing for structural clarity  

#### 2️⃣ Segmentation
- Intensity-based thresholding for lung region isolation  
- Interactive threshold control using OpenCV trackbars  

#### 3️⃣ Quality Evaluation
- **PSNR (Peak Signal-to-Noise Ratio)** for signal fidelity  
- **SSIM (Structural Similarity Index)** for perceptual similarity  

Statistical analysis was performed across multiple chest X-ray samples.

### 📊 Results

- **Average PSNR:** ≈ 42.6 dB  
- **Average SSIM:** ≈ 0.97  

These results demonstrate effective noise reduction while preserving structural similarity, reinforcing the robustness of the preprocessing pipeline.

## 📦 Installing Dependencies (Virtual Environment Recommended)

> ⚠️ Recommendation:  
> It is strongly recommended to use a Python virtual environment (`venv`) to ensure dependency isolation and reproducibility.  
> Running the project inside a virtual environment prevents version conflicts with other Python projects.

> 💡 Note:  
> The segmentation step uses an OpenCV trackbar interface, which may not work properly in some notebook environments (e.g., Jupyter).  
> For best results, run this project using Visual Studio Code (VS Code) or directly from the terminal.

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mirellesv/image-processing-segmentation-analysis.git
cd image-processing-segmentation-analysis
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment
- Linux / macOS:
  ```bash
  source venv/bin/activate
  ```
- Windows:
  ```bash
  venv\Scripts\activate
  ```
  
### 4️⃣ Install dependencies
  ```bash
 pip install -r requirements.txt
  ```

### 5️⃣ Run the project
  ```bash
 python src/main.py
  ```
