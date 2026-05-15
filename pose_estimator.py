
import cv2
import mediapipe as mp


class HeadPoseEstimator:

    def __init__(self):

        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        self.mp_draw = mp.solutions.drawing_utils

    def estimate_pose(self, frame):

        h, w, _ = frame.shape

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            return None

        face_landmarks = results.multi_face_landmarks[0]

        # Draw face mesh
        self.mp_draw.draw_landmarks(
            frame,
            face_landmarks,
            self.mp_face_mesh.FACEMESH_CONTOURS
        )

        # Nose landmark
        nose = face_landmarks.landmark[1]

        nose_x = int(nose.x * w)
        nose_y = int(nose.y * h)

        # Face boundaries
        left_face = face_landmarks.landmark[234]
        right_face = face_landmarks.landmark[454]

        top_face = face_landmarks.landmark[10]
        bottom_face = face_landmarks.landmark[152]

        left_x = int(left_face.x * w)
        right_x = int(right_face.x * w)

        top_y = int(top_face.y * h)
        bottom_y = int(bottom_face.y * h)

        # Face center
        face_center_x = (left_x + right_x) // 2
        face_center_y = (top_y + bottom_y) // 2

      
        # Head movement LEFT / RIGHT
        yaw = nose_x - face_center_x

       # Better UP / DOWN detection

        chin_distance = bottom_y - nose_y

        pitch = chin_distance



        # Draw direction line
        cv2.line(
            frame,
            (face_center_x, face_center_y),
            (nose_x, nose_y),
            (255, 0, 0),
            3
        )

        # Draw nose point
        cv2.circle(
            frame,
            (nose_x, nose_y),
            5,
            (0, 255, 0),
            -1
        )

        return {
            "yaw": yaw,
            "pitch": pitch,
            "roll": 0,
            "frame": frame
        }

