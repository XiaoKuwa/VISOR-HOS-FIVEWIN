import json

# 读取 JSON 文件
with open("/data/epic/baseline/datasets/epick_visor_coco_hos/annotations/test.json", "r") as json_file:
    data = json.load(json_file)

# 删除 id 为 null 的图片条目
data["images"] = [image for image in data["images"] if image["id"] is not None]

# 写入更新后的 JSON 文件
with open("/data/epic/baseline/datasets/epick_visor_coco_hos/annotations/testnew.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
