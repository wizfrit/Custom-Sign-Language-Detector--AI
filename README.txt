# ASL Word-Level Translator

This project uses LSTM and MediaPipe to recognize ASL words like "hello", "thanks", "yes", and "no".

## Files

ASL_Word_Level_Translator/
│
├── record_data.py               # Record gesture frames via webcam
├── asl_datapreprocessing.py     # Extract keypoints from recorded frames
├── asl_model_training.py        # Train LSTM model on those keypoints
├── predict_asl.py               # Use webcam to predict gestures in real time
├── requirements.txt             # Libraries to install
└── README.txt                   # Project description


## Usage

1. Collect data into `data/<word>/<sequence>/<frame>.jpg`
2. Run `asl_datapreprocessing.py` to process and save training data.
3. Run `asl_model_training.py` to train the model.
4. Run `predict_asl.py` to test real-time ASL word recognition.

Make sure your webcam works and dependencies are installed.
