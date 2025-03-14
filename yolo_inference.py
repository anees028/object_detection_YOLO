from ultralytics import YOLO

# Check the YOLO github to use the version according to the computer resources. 
model = YOLO('yolov8n') 

# Following code will use for object detection..
results = model.predict('input_video/video_input.mp4', save=True)
print(results[0])
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
for box in results[0].boxes:
    print(box)


