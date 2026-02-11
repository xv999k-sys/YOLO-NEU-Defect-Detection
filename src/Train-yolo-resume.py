from ultralytics import YOLO

model = YOLO(r"C:\Users\admin\Desktop\YOLO-NEU-Defect-Detection\exp\weights\last.pt")

model.train(
    resume=True,
    device='cpu'
)
