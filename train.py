import cv2
from PIL import Image
import torchvision.transforms as transforms
from model import PatchEmbed , Attention
import torch
import debugpy

# setting debugpy
debugpy.listen(("localhost", 5678))
print("Waiting for debugger to attach...")
debugpy.wait_for_client()

# 定义图像变换操作列表
transform_pipeline = transforms.Compose([
    transforms.Resize((224, 224)),  # 调整图像大小
    transforms.ToTensor()  # 将图像转换为Tensor
])

# 读取图像并转换为PIL格式，因为torchvision的Transform主要操作PIL图像
image_bgr = cv2.imread('images.jpg')
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
image_pil = Image.fromarray(image_rgb)
print(type(image_pil))

# 应用图像变换
processed_img = transform_pipeline(image_pil)
print(processed_img.shape)

input_tensor = torch.stack([processed_img]*4)
print(input_tensor.shape)

patch_embed = PatchEmbed()

embedded_patches = patch_embed(input_tensor)

print(embedded_patches.shape)
