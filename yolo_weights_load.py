import torch

# �н��� weights ���
weights_path = 'best.pt' 

# �� ���� 
model = YOLOv3()

# weights �ҷ�����
model.load_state_dict(torch.load(weights_path))

# �߷� ��� ��ȯ
model.eval()

# �̹��� �о����
img = Image.open('test.jpg')

# �߷� ����
predictions = model(img)