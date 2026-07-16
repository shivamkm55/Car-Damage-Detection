# video_processor.py

import cv2
import os
import uuid
from collections import Counter

# --- Local Imports ---
# Import the centralized data and helper function
from config import CAR_PRICES_DATA, get_part_name_from_id

def get_predictions_from_frame(frame, model):
    """
    Runs YOLO prediction on a single frame.
    Returns:
        tuple: (list of detected part names, image with bounding boxes drawn)
    """
    results = model(frame, verbose=False)
    annotated_frame = results[0].plot()

    detected_objects = results[0].boxes
    detected_parts = []
    for box in detected_objects:
        class_id = box.cls.item()
        part_name = get_part_name_from_id(class_id)
        if part_name:
            detected_parts.append(part_name)
            
    return detected_parts, annotated_frame

def process_video_for_repair_estimate(video_path, model, user_car_details):
    """
    Main function to process video, run predictions, and aggregate results.
    Returns a dictionary in the same format as the image processor.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return None, []

    # --- Setup directories for saving frames ---
    STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    DETECTED_VIDEO_FRAMES_DIR = os.path.join(STATIC_DIR, 'detected_video_frames')
    os.makedirs(DETECTED_VIDEO_FRAMES_DIR, exist_ok=True)

    fps = cap.get(cv2.CAP_PROP_FPS) or 30

    max_detections_per_part = Counter()
    detected_image_paths = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process one frame per second for efficiency
        if frame_count % int(fps) == 0:
            parts_in_frame, annotated_frame = get_predictions_from_frame(frame, model)
            
            if parts_in_frame:
                # Count occurrences of each part in the current frame
                current_frame_counts = Counter(parts_in_frame)
                
                # Update the max count for each part seen so far across all frames
                for part, count in current_frame_counts.items():
                    if count > max_detections_per_part[part]:
                        max_detections_per_part[part] = count

                # Save the annotated frame
                unique_filename = f"detected_frame_{uuid.uuid4().hex}.jpg"
                save_path = os.path.join(DETECTED_VIDEO_FRAMES_DIR, unique_filename)
                cv2.imwrite(save_path, annotated_frame)
                
                # Store the relative path for web display
                web_path = f"detected_video_frames/{unique_filename}"
                detected_image_paths.append(web_path)
        
        frame_count += 1
    
    cap.release()

    # --- Aggregation Logic (Now mirrors the image logic) ---
    if not user_car_details:
        return {}, []
    
    car_brand = user_car_details['car_brand'].strip().upper()
    car_model = user_car_details['model'].strip().title()

    final_prices = {}
    for part_name, count in max_detections_per_part.items():
        try:
            price_per_part = CAR_PRICES_DATA[car_brand][car_model][part_name]
            total_price = price_per_part * count
            final_prices[part_name] = {
                'count': count,
                'price': price_per_part,
                'total': total_price
            }
        except KeyError:
            print(f"Price not found for: {car_brand}, {car_model}, {part_name}")
            continue
            
    # Return the final prices and a unique list of image paths
    return final_prices, list(set(detected_image_paths))