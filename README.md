# Sign Language Word-Level Translator 

This is a desktop-based real-time Sign Language word-level translator. It uses **MediaPipe** for hand gesture detection, **LSTM** for sequence modeling, and **OpenCV** for webcam input. The model recognizes basic ASL words like **\"hello\"**, **\"thanks\"**, **\"yes\"**, and **\"no\"**.

---

##  Project Structure

├── record.py           # Record gesture frames via webcam

├── process.py          # Extract keypoints from recorded frames

├── train.py            # Train LSTM model on processed data

├── predict.py          # Use webcam to predict gestures in real time

├── requirements.txt    # Required libraries

└── README.md           # Project documentation

---

## ⚙️ Getting Started

### 1. Clone the Repository

git clone https://github.com/yourusername/word-level-translator.git

cd word-level-translator

### 3. Install Dependencies

pip install -r requirements.txt

---

##  Usage Instructions

### Step 1: Collect Data

Record gesture frames using:
python record.py
This will save frames into the format:
data/<word>/<sequence>/<frame>.jpg


### Step 2: Process Data

Extract keypoints from the collected images:    "python process.py"


### Step 3: Train the Model

Train the LSTM-based gesture recognition model:  "python train.py"


### Step 4: Run Real-Time Prediction

Use your webcam for live gesture translation:   "python predict.py"

---
## Important Note
If you have already recorded the gesture data and nothing new has been added, you can skip the processing and training steps — just run the prediction script.

However, if you record new gesture data or modify the existing dataset, make sure to run the processing and training scripts again before predicting. This ensures the model includes the updated data.

---
##  Requirements

- Ensure your **webcam is working**.
- Dependencies must be installed from requirements.txt.
---

##  Technologies Used

- [MediaPipe](https://google.github.io/mediapipe/) – Hand Tracking
- [OpenCV](https://opencv.org/) – Real-time video capture
- [TensorFlow / Keras](https://www.tensorflow.org/) – LSTM model training
- Python 3.x

---

##  License

This project is open-source and free to use for educational and research purposes." > README.md
