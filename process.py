import os
import cv2
import numpy as np
import mediapipe as mp #library for hand jobs

seqlen = 30
Dozakh = 'data'
sequences = []
labels = []
actions = []

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

print(" Preprocessing data from 'data/' folder...")

# har folder ke andar har frame ke liye
for action_idx, action in enumerate(sorted(os.listdir(Dozakh))):
    Jannat = os.path.join(Dozakh, action)
    #Exception for non-folders
    if not os.path.isdir(Jannat):
        continue
    actions.append(action)

    #har aik frame ke liye
    for sequence_num in os.listdir(Jannat):
        window = []
        for frame_num in range(seqlen):
            frame_path = os.path.join(Jannat, sequence_num, f"{frame_num}.jpg")
            if not os.path.exists(frame_path):
                continue

            #image ko MediaPipe readable banane ke liye converting it into RGB
            #also detecting hand landmarks
            frame = cv2.imread(frame_path)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                #gpt said hand is 21 times each dimension, I just trusted it
                keypoints = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]).flatten()
            else:
                keypoints = np.zeros(63)

            window.append(keypoints)

        if len(window) == seqlen:
            sequences.append(window)
            labels.append(action_idx)

X = np.array(sequences)
y = np.eye(len(actions))[labels]

np.save('asl_sequences.npy', X)
np.save('asl_labels.npy', y)
np.save('asl_actions.npy', np.array(actions))

print(f" Preprocessing complete. {len(actions)} actions, {len(X)} samples saved.")
