import torch

# 학습된 weights 경로
weights_path = 'best.pt' 

# 모델 정의 
model = YOLOv3()

# weights 불러오기
model.load_state_dict(torch.load(weights_path))

# 추론 모드 전환
model.eval()

# 이미지 읽어오기
img = Image.open('test.jpg')

# 추론 수행
predictions = model(img)