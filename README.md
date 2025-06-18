
# 🎨 Skin Tone Classifier - AI-Powered Analysis Tool

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-4.5%2B-orange?logo=opencv" alt="OpenCV">
  <img src="https://img.shields.io/badge/Tkinter-GUI-yellowgreen" alt="Tkinter">
  <img src="https://img.shields.io/badge/ML-Classification-lightgrey" alt="Machine Learning">
</div>


An intelligent desktop application that classifies skin tones using computer vision and machine learning. Built as a mini-project to demonstrate practical AI applications in dermatology and cosmetics.

## ✨ Key Features

- **8-Tone Classification**: Identifies skin tones from Cool Light to Deep Brown
- **Visual Analysis**: Displays original image with annotated results
- **Accuracy Metrics**: Shows confidence percentages for each detection
- **User-Friendly GUI**: Simple Tkinter interface for easy operation
- **JSON Export**: Generates detailed analysis reports

## 🛠️ Technologies Used

| Component | Technology |
|-----------|------------|
| **Core Engine** | `skin-tone-classifier` Python library |
| **Computer Vision** | OpenCV (cv2) |
| **GUI Framework** | Tkinter |
| **Image Processing** | PIL (Pillow) |
| **Data Formatting** | JSON |

## 📦 Installation

1. **Install requirements**:
   ```bash
   pip install skin-tone-classifier opencv-python pillow
   ```

2. **Run the application**:
   ```bash
   python skin_tone_classifier.py
   ```

## 🖥️ Usage Guide

1. Click "Choose Image" to select a photo
2. The system will:
   - Detect all faces in the image
   - Classify each face's skin tone
   - Display original and analyzed images
   - Show detailed tone information
3. Results are also printed in JSON format

## 📊 Sample Output

```json
{
  "faces": [
    {
      "face_id": 1,
      "tone_label": "MW",
      "accuracy": 92.34,
      "description": "Medium Warm"
    }
  ]
}
```

## 🎨 Tone Classification Reference

| Code | Description |
|------|-------------|
| CL | Cool Light |
| CI | Cool Intermediate |
| CG | Cool Fair |
| CW | Cool Warm |
| DW | Dark Warm |
| MW | Medium Warm |
| CE | Cool Sand |
| CD | Deep Brown |


## 🌟 Future Enhancements

- [ ] Batch processing of multiple images
- [ ] Makeup recommendation based on skin tone
- [ ] Webcam real-time analysis
- [ ] Export results to CSV/PDF
- [ ] Dark mode support

## 👨‍💻 Author

**Pavan Kumar K S**   
GitHub: [@Pavan-kumar-ks](https://github.com/Pavan-kumar-ks)    
LinkedIn: [Pavan Kumar K S](www.linkedin.com/in/pavan-kumar-k-s)  
