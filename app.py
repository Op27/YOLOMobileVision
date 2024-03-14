import cv2
import math
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

# Load the YOLOv8 model with classification capabilities
# This model is responsible for object detection and classification.
model = YOLO("yolov8n.pt")

# Specify the IP address and port of the camera stream
# This URL should be replaced with your mobile camera's IP address and port.
camera_url = "http:/Your_IP_address:Your_Port/video" 
cap = cv2.VideoCapture(camera_url)

# Check if the camera stream is opened successfully
if not cap.isOpened():
    print("Error: Unable to open the camera stream.")
    exit()

# Set the video writer parameters if you want to save the output
# These parameters are for recording the video stream with detections.
w, h, fps = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)), int(cap.get(cv2.CAP_PROP_FPS)))
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))

center_point = (w // 2, h)  # Center point of the frame
pixel_per_meter = 234 

txt_color, txt_background, bbox_clr = ((0, 0, 0), (255, 255, 255), (255, 0, 255))

text_font_scale = 0.5  # Adjust this value to change the text size
text_thickness = 2  # Adjust this value to change the text thickness

while True:
    # Read the frame from the camera stream
    ret, im0 = cap.read()

    if not ret:
        print("Error capturing frame from the camera stream.")
        break

    annotator = Annotator(im0, line_width=2)
    results = model(im0)

    for result in results:
        boxes = result.boxes.xyxy.cpu()

        for i, box in enumerate(boxes):
            cls = int(result.boxes.cls[i])
            label = model.names[cls]
            annotator.box_label(box, label, color=colors(cls, True))
            annotator.visioneye(box, center_point)

            x1, y1 = int((box[0] + box[2]) // 2), int((box[1] + box[3]) // 2)  # Bounding box centroid
            distance = (math.sqrt((x1 - center_point[0]) ** 2 + (y1 - center_point[1]) ** 2)) / pixel_per_meter

            text = f"{distance:.2f} m"
            text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, text_font_scale, text_thickness)

            # Adjust the text position based on the bounding box location
            text_x = max(10, x1 - text_size[0] // 2)
            text_x = min(text_x, im0.shape[1] - text_size[0] - 10)
            text_y = max(y1 - text_size[1] - 10, 10)

            cv2.rectangle(im0, (text_x - 5, text_y - 5), (text_x + text_size[0] + 5, text_y + text_size[1] + 5), txt_background, -1)
            cv2.putText(im0, text, (text_x, text_y + text_size[1]), cv2.FONT_HERSHEY_SIMPLEX, text_font_scale, txt_color, text_thickness)
            
    # Write the frame to the video writer (if enabled)
    out.write(im0)

    # Display the frame
    cv2.imshow("visioneye-distance-calculation", im0)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
out.release()
cap.release()
cv2.destroyAllWindows()