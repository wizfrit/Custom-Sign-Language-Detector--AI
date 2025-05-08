# Sign Language Word-Level Translator

This project uses LSTM and MediaPipe to recognize recorded words like "hello", "thanks", "yes", and "no".

## Files

Word_Level_Translator/
│
├── record.py               # Record gesture frames via webcam
├── process.py              # Extract keypoints from recorded frames
├── train.py                # Train LSTM model on those keypoints
├── predict.py              # Use webcam to predict gestures in real time
├── requirements.txt        # Libraries to install
└── README.txt              # Project description


## Usage

1. Collect data into `data/<word>/<sequence>/<frame>.jpg`
2. Run `process.py` to process and save training data.
3. Run `train.py` to train the model.
4. Run `predict.py` to test real-time ASL word recognition.

Make sure your webcam works and dependencies are installed.
