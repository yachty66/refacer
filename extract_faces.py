import cv2
import os
from refacer import Refacer

def extract_faces_from_video(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    refacer = Refacer()
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_count = 0
    face_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        faces = refacer._Refacer__get_faces(frame)
        for face in faces:
            x1, y1, x2, y2 = map(int, face.bbox)
            face_img = frame[y1:y2, x1:x2]
            face_path = os.path.join(output_folder, f"face_{face_count}.jpg")
            cv2.imwrite(face_path, face_img)
            face_count += 1

        frame_count += 1
        print(f"Processed frame {frame_count}/{total_frames}")

    cap.release()
    print(f"Extracted {face_count} faces from the video.")

# Example usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Extract faces from video')
    parser.add_argument("--video", help="Path to the video file", required=True)
    parser.add_argument("--output", help="Path to the output folder", required=True)
    args = parser.parse_args()

    extract_faces_from_video(args.video, args.output)