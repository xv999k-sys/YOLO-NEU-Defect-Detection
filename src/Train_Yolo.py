
from ultralytics import YOLO

model = YOLO('yolov8s.pt') 


model.train(
    data=r"C:\Users\admin\Desktop\YOLO-NEU-Defect-Detection\Dataset\Data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    device='cpu',
    save_period=1,  
    project=r"C:\Users\admin\Desktop\YOLO-NEU-Defect-Detection", 
    name="exp"         
)
