# # utils.py

# import numpy as np
# import cv2
# from PIL import Image
# import io

# def read_imagefile(file) -> np.ndarray:
#     image = np.asarray(bytearray(file), dtype=np.uint8)
#     return cv2.imdecode(image, cv2.IMREAD_COLOR)


# def draw_detections(image: np.ndarray, results) -> np.ndarray:
#     boxes = results.boxes
#     for box in boxes:
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#         conf = float(box.conf[0])
#         cls = int(box.cls[0])
#         label = f"{results.names[cls]} {conf:.2f}"
#         cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
#                     0.6, (255, 0, 0), 2)
#     return image

# def image_to_bytes(image: np.ndarray) -> bytes:
#     _, buffer = cv2.imencode('.jpg', image)
#     return buffer.tobytes()

# ------------------------------------------------------



import numpy as np
import cv2
from PIL import Image
import io


def read_imagefile(file) -> np.ndarray:
    """Read and decode image file"""
    try:
        image = np.asarray(bytearray(file), dtype=np.uint8)
        decoded = cv2.imdecode(image, cv2.IMREAD_COLOR)
        if decoded is None:
            raise ValueError("Failed to decode image")
        return decoded
    except Exception as e:
        print(f"Error reading image: {e}")
        return None



def draw_detections(image: np.ndarray, results) -> np.ndarray:
    """Draw bounding boxes and labels on image"""
    boxes = results.boxes
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = f"{results.names[cls]} {conf:.2f}"
        
        # Draw rectangle
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Draw label background
        label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        cv2.rectangle(image, (x1, y1 - label_size[1] - 10), (x1 + label_size[0], y1), (0, 255, 0), -1)
        
        # Draw label text
        cv2.putText(image, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 0), 2)
    return image


def image_to_bytes(image: np.ndarray) -> bytes:
    """Convert numpy array image to bytes"""
    _, buffer = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 90])
    return buffer.tobytes()
