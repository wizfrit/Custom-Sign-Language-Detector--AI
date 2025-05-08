import cv2 #for video capturing
import os #for directories

num_sequences = 30         # Number of gesture repetitions
sequence_length = 30       # Frames per gesture
save_path = 'data'

cap = cv2.VideoCapture(0)

print("Enter ASL word (e.g., hello, thanks, yes, no) or type 'exit' to finish.")

while True:
    action = input("\n  Enter word to record: ").strip().lower()
    if action == 'exit':
        break

    for sequence in range(num_sequences):
        os.makedirs(os.path.join(save_path, action, str(sequence)), exist_ok=True)
        print(f' Recording: {action} - Sequence {sequence + 1}/{num_sequences}')
        for frame_num in range(sequence_length):
            ret, frame = cap.read()
            if not ret:
                continue
            img = cv2.flip(frame, 1) #for mirroring the image

            #thie code below is responsible for writing on the camera 
            cv2.putText(img, f'{action.upper()} - Seq:{sequence} Frame:{frame_num}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Recording', img)

            # Save the frame to the specified directory
            frame_path = os.path.join(save_path, action, str(sequence), f'{frame_num}.jpg')
            cv2.imwrite(frame_path, img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print(" Recording aborted.")
                break

print(" Data collection complete.")
cap.release()
cv2.destroyAllWindows()
