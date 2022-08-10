import cv2
import mediapipe as mp

def autoAnnotation(img):
    image = img

    hand_landmarks = []

    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    with mp_hands.Hands(
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmark, mp_hands.HAND_CONNECTIONS)
                hand_landmarks.append(hand_landmark)
    return hand_landmarks

def landmarksToList(landmarks):
    if landmarks is None:
        return False
        
    pos_list = []

    for data_point in landmarks.landmark:
        if data_point.x < 0 or data_point.y < 0:
            x_pos = 0.5
            y_pos = 0.5
        else:
            x_pos = data_point.x
            y_pos = data_point.y
        pos_list.append([x_pos, y_pos])

    return pos_list


'''
if __name__ == '__main__':
    filename = 'Resource/Image/two_hands.jpg'
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    lists = []

    image, landmarks = autoAnnotation(image)
    for landmark in landmarks:
        lists.append(landmarksToList(landmark))

    print(len(lists))
    cv2.imshow('image', image)
    cv2.waitKey()
'''