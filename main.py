
import cv2

from pose_estimator import HeadPoseEstimator
from attention_tracker import AttentionTracker


# Initialize modules
pose_estimator = HeadPoseEstimator()

attention_tracker = AttentionTracker()


# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access webcam")
    exit()


while True:

    success, frame = cap.read()

    if not success:
        break

    # Mirror effect
    frame = cv2.flip(frame, 1)

    # Estimate pose
    result = pose_estimator.estimate_pose(frame)

    if result:

        yaw = result["yaw"]
        pitch = result["pitch"]
        roll = result["roll"]

        print("Yaw:", yaw, "Pitch:", pitch, "Roll:", roll)

        # Check attention
        attention_result = attention_tracker.check_attention(
            yaw,
            pitch
        )

        # Status
        if attention_result["looking_away"]:
            status = "LOOKING AWAY"
            color = (0, 0, 255)

        else:
            status = "ATTENTIVE"
            color = (0, 255, 0)

        # Display Yaw
        cv2.putText(
            frame,
            f"Yaw: {yaw}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        # Display Pitch
        cv2.putText(
            frame,
            f"Pitch: {pitch}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        # Display Roll
        cv2.putText(
            frame,
            f"Roll: {roll}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        # Display Status
        cv2.putText(
            frame,
            f"Status: {status}",
            (20, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            3
        )

        # Print output
        print({
            "looking_away": attention_result["looking_away"],
            "yaw": yaw,
            "pitch": pitch
        })

    # Show window
    cv2.imshow(
        "Real-Time Head Pose Tracking",
        frame
    )

    # ESC key to exit
    key = cv2.waitKey(1)

    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()

