#  colorizer_Ai

AI-powered historical image colorization system built using Deep Learning, OpenCV, and Streamlit.

This project automatically converts black-and-white images into realistic colorized images using a pre-trained Convolutional Neural Network (CNN).

---

# Features

- Upload black & white images
- AI-based automatic image colorization
- Brightness and contrast enhancement
- Image sharpening option
- Before vs after comparison
- Download colorized output
- Streamlit interactive UI
- Deep learning powered restoration

---

# How It Works

The project uses a pre-trained deep learning model trained for image colorization.

The grayscale image is converted into **LAB color space**:

- **L channel** → Lightness/Brightness
- **A channel** → Green ↔ Red
- **B channel** → Blue ↔ Yellow

The AI model takes the **L channel** as input and predicts the missing **A and B color channels**.

Finally, the channels are merged and converted back into an RGB image.

---

#  Technologies Used

- Python
- Streamlit
- OpenCV
- NumPy
- Pillow
- Deep Learning
- CNN (Convolutional Neural Network)
- Caffe Pre-trained Model
- LAB Color Space

---

#  Project Structure

```text
colorizer_Ai/
│
├── app.py
├── colorizer.py
├── enhancement.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── colorization_deploy_v2.prototxt
│   └── pts_in_hull.npy
│
├── outputs/
├── sample_images/
└── screenshots/
```

---

# Installation

##  Clone Repository

```bash
git clone https://github.com/athiraarun06/colorizer_ai.git
cd colorizer_ai
```

---

## 2️Create Virtual Environment

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

##  Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Download Model File

The `.caffemodel` file is too large for GitHub.

Download it manually from:

https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1

After downloading, place it inside:

```text
models/
```

Final structure:

```text
models/
├── colorization_deploy_v2.prototxt
├── colorization_release_v2.caffemodel
└── pts_in_hull.npy
```

---

#  Run the Project

```bash
streamlit run app.py
```

OR

```bash
python3 -m streamlit run app.py
```

---

#  Application Interface

The app allows users to:

- Upload grayscale images
- Generate AI-colorized images
- Enhance image quality
- Download final outputs

---

#  Sample Output

## Before Colorization

(Add screenshot here)

## After Colorization

(Add screenshot here)

---

#  Future Enhancements

- Face enhancement
- Scratch/noise removal
- Batch image colorization
- GAN-based advanced colorization
- Cloud deployment
- Real-time restoration

---

# Applications

- Historical photo restoration
- Digital archiving
- AI image processing research
- Educational deep learning project
- Photography enhancement

---

#  Limitations

- Colors may not always be historically accurate
- Low-quality images may reduce output quality
- Model predicts colors based on learned patterns

---

#  Author

ATHIRA ARUN

B.Tech Computer Science Engineering  
Karunya Institute of Technology and Sciences

---

#  Acknowledgements

- OpenCV
- Streamlit
- Richard Zhang's colorization model
- Deep Learning community
