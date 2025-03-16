import torch

model = torch.load('models/01_pytorch_workflow_model_0.pth', weights_only=False)

if (model):
    print("Model loaded")
    print(model)
else:
    print("Model not found!")
    
