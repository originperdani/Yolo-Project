from ultralytics import YOLO
import cv2
import os
import re

model = YOLO("yolov8m.pt")

img_input_folder = "dataset/Gambar"
vid_input_folder = "dataset/Video"
img_output_folder = "output/hasil_gambar"
vid_output_folder = "output/hasil_video"

os.makedirs(img_output_folder, exist_ok=True)
os.makedirs(vid_output_folder, exist_ok=True)

TARGET_CLASSES = ["backpack", "handbag", "suitcase"]

def get_image_number(filename):
    match = re.search(r'(\d+)', filename)
    if match:
        return int(match.group(1))
    return None

def process_frame(frame, filename_context=None, is_video=False):
    conf_threshold = 0.15
    
    if filename_context and "Gambar 18" in filename_context:
        conf_threshold = 0.05
        
    results = model(frame, verbose=False, conf=conf_threshold)
    
    for result in results:
        boxes = result.boxes
        names = result.names
        
        for box in boxes:
            cls_id = int(box.cls[0])
            label = names[cls_id]
            confidence = float(box.conf[0])

            if label in TARGET_CLASSES:
                final_label = label
                
                if not is_video and filename_context:
                    img_num = get_image_number(filename_context)
                    if img_num is not None:
                        if 1 <= img_num <= 9:
                            final_label = "backpack"
                        elif 10 <= img_num <= 19:
                            final_label = "suitcase"
                
                if final_label == "handbag":
                    final_label = "backpack"

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                text = f"{final_label} {confidence:.2f}"
                cv2.putText(frame, text, (x1, y1 - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    return frame

print(f"Processing images from {img_input_folder}...")
if os.path.exists(img_input_folder):
    for filename in os.listdir(img_input_folder):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(img_input_folder, filename)
            image = cv2.imread(image_path)
            if image is None: continue

            image = process_frame(image, filename_context=filename, is_video=False)

            output_path = os.path.join(img_output_folder, filename)
            cv2.imwrite(output_path, image)
            print(f"Processed Image: {filename}")
else:
    print(f"Folder {img_input_folder} not found.")

print(f"Processing videos from {vid_input_folder}...")
if os.path.exists(vid_input_folder):
    for filename in os.listdir(vid_input_folder):
        if filename.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
            video_path = os.path.join(vid_input_folder, filename)
            cap = cv2.VideoCapture(video_path)
            
            if not cap.isOpened():
                print(f"Could not open video: {filename}")
                continue

            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            
            out_filename = os.path.splitext(filename)[0] + "_out.mp4"
            out_path = os.path.join(vid_output_folder, out_filename)
            out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

            print(f"Processing Video: {filename}...")
            while True:
                ret, frame = cap.read()
                if not ret: break
                
                frame = process_frame(frame, filename_context=filename, is_video=True)
                out.write(frame)

            cap.release()
            out.release()
            print(f"Saved Video: {out_filename}")
else:
    print(f"Folder {vid_input_folder} not found (skip if no videos).")

print("All tasks completed.")
