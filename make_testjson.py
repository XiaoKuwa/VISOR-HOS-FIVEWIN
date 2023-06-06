import os
import json
from PIL import Image

# 文件夹路径和输出 JSON 文件路径
folder_path = "/data/epic/baseline/datasets/epick_visor_coco_hos/test"
output_file = "/data/epic/baseline/datasets/epick_visor_coco_hos/annotations/test.json"

# 获取文件夹中的图片文件名列表
image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]
# print(image_files)
# 生成图片信息列表
images = []

with open('/data/epic/baseline/image_id.json') as f:
    getimageid = json.load(f)

for file_name in image_files:
    print(file_name)
    imagefile_path = os.path.join(folder_path, file_name)
    image = Image.open(imagefile_path)
    width, height = image.size
    imageid = getimageid.get(file_name)
    image_info = {
        "id": imageid,
        "file_name": file_name,
        "height": height,  # 设置图片高度
        "width": width  # 设置图片宽度
    }
    images.append(image_info)

# 创建 JSON 数据
data = {
    "images": images
}

# 将数据写入 JSON 文件
with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)
