import cv2
import mediapipe as mp

# Mediapipe 손 모양 인식 초기화
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# 웹캠 초기화
cap = cv2.VideoCapture(0)

def count_fingers(image, hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    thumb_tip = 4
    count = 0

    # 각 손가락의 끝이 손바닥 중앙보다 위에 있는지 확인
    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1

    # 엄지손가락 확인
    if hand_landmarks.landmark[thumb_tip].x < hand_landmarks.landmark[thumb_tip - 1].x:
        count += 1

    return count

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers_count = count_fingers(frame, hand_landmarks)
            
            # 손가락 개수를 화면에 표시
            cv2.putText(frame, f'Fingers: {fingers_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            
            # 손가락 개수를 콘솔에 출력
            print(f'Fingers: {fingers_count}')

    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''
# 가상 환경 생성
python3 -m venv myenv

# 가상 환경 활성화
source myenv/bin/activate

# 가상 환경 종료
source deactivate

'''