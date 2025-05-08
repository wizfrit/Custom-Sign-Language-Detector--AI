import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model


model = load_model('asl_model.h5')
actions = np.load('asl_actions.npy')


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)


sequence = []
sequence_length = 30
threshold = 0.5  #keep it low taake output dikhe atleast
#thats confidence tho
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract keypoints
            keypoints = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]).flatten()
            sequence.append(keypoints)

            #Exception handling
            if len(sequence) > sequence_length:
                sequence.pop(0)

            # Predict if sequence is ready
            if len(sequence) == sequence_length:
                input_data = np.expand_dims(sequence, axis=0)
                predictions = model.predict(input_data, verbose=0)[0]
                max_index = np.argmax(predictions)
                confidence = predictions[max_index]

                if confidence > threshold:
                    action = actions[max_index]
                    cv2.putText(image, f'{action} ({confidence:.2f})', (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('ASL Word Recognition', image)

    # Exit on 'q' key press
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
