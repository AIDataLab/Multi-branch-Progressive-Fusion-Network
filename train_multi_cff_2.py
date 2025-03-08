import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
#多光谱特征走一个cff
# 训练参数官方详解链接：https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings:~:text=a%20training%20run.-,Train%20Settings,-The%20training%20settings

if __name__ == '__main__':
    model = YOLO('/data/LMX/ultralytics-main-mso/ultralytics/cfg/models/obb/yolov8x-cff-mso-obb.yaml')
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='dataset/duoguang.yaml',
                cache=False,
                imgsz=640,
                epochs=100,
                batch=8,
                close_mosaic=2,
                workers=4,
                device='1',
                optimizer='SGD', # using SGD
                # patience=0, # close earlystop
                # resume=True, # 断点续训,YOLO初始化时选择last.pt
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/train',
                name='multi-cff-2-obb-100epoch',
                )