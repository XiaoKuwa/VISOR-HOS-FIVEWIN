# VISOR - Hand Object Segmentation (HOS) Challenge Fivewin team

## Environment

Conda environment recommended:
- cv2
- [pytorch](https://pytorch.org/get-started/locally/)
- [detectron2](https://github.com/facebookresearch/detectron2)
```
conda create --name hos
conda activate hos
pip install opencv-python
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu102/torch1.9/index.html
```

## Data Preparation

Download VISOR data from [EPIC-KITCHENS VISOR](https://epic-kitchens.github.io/VISOR/#downloads). Unzip it and rename it as epick_visor.

Generate a COCO format annotation of VISOR data for training:

&emsp;`--epick_visor`:the path to the annotation folder. 

&emsp;`--mode`: coco format data for different tasks, choose from `hos` or `active`.

&emsp;`--split`: generate for which split, choose from `train` and `val`.

&emsp;`--unzip_img`: only need to use this args once to unzip the orginally downloaded compressed images for each video. Worth noting that `unzip` command sometimes has some issue, which affects data loading later.

&emsp;`--copy_img`: copy images to get the same folder structure as in COCO.
```
python gen_coco_format.py \
--epick_visor_store=/path/to/epick_visor/GroundTruth-SparseAnnotations \
--mode=hos \
--split train val \
--unzip_img \
--copy_img \
``` 
```
python gen_coco_format_handside_contact.py \
--epick_visor_store=/path/to/epick_visor/GroundTruth-SparseAnnotations \
--mode=handside \
--split val \
--copy_img \
``` 
```
python gen_coco_format_handside_contact.py \
--epick_visor_store=/path/to/epick_visor/GroundTruth-SparseAnnotations \
--mode=contact \
--split val \
--copy_img \
``` 
```
python gen_coco_combineHO.py \
--epick_visor_store=/path/to/epick_visor/GroundTruth-SparseAnnotations \
--mode=combineHO \
--split val \
--copy_img \
``` 
Put all the test image under 
./datasets/epick_visor_coco_hos/test and
./datasets/epick_visor_coco_handside/test and ./datasets/epick_visor_coco_contact/test and ./datasets/epick_visor_coco_combineHO/test

Then the data structure looks like below:
```
datasets
├── epick_visor_coco_hos
│   ├── annotations
│   │   ├── train.json
│   │   └── val.json
│   ├── train 
│   │   └── *.jpg
│   ├── val 
│   │   └── *.jpg
│   └── test
│       └── *.jpg
├── epick_visor_coco_handside
│   ├── annotations
│   │   └── val.json
│   ├── val 
│   │   └── *.jpg
│   └── test
│       └── *.jpg
├── epick_visor_coco_contact
│   ├── annotations
│   │   └── val.json
│   ├── val 
│   │   └── *.jpg
│   └── test
│       └── *.jpg
└── epick_visor_coco_combineHO
    ├── annotations
    │   └── val.json
    ├── val 
    │   └── *.jpg
    └── test
        └── *.jpg
```

## Train
Download Resnet-101 pre-train weight from 

https://dl.fbaipublicfiles.com/detectron2/ImageNetPretrained/MSRA/R-101.pkl

and put it under ./checkponits

```
python train_net_hos.py \
--config-file ./configs/hos/hos_pointrend_rcnn_R_101_FPN_1x_hos.yaml \
--num-gpus 4 \
--dataset epick_hos  \
OUTPUT_DIR ./checkpoints/hos_train
```



## Test
### Pre-trained Weights
Download our pre-trained weights from

https://drive.google.com/file/d/1ABVR70ZEP00lZYoGlbkFVwX7BNtQY5jZ/view?usp=drive_link

into .checkpoints/hos_train_101 folder to run evaluation or demo code:


Hand and Contacted Object Segmentation (HOS) model:
```
python eval_hos.py \
--config-file ./configs/hos/hos_pointrend_rcnn_R_101_FPN_1x_hos.yaml \
--num-gpus 4 \
--eval-only \
OUTPUT_DIR ./checkpoints/hos \
MODEL.WEIGHTS ./checkpoints/hos_train_101/model_final.pth
```
Evaluate handside:
```
python eval_handside.py \
--config-file ./configs/hos/hos_pointrend_rcnn_R_101_FPN_1x_handside.yaml \
--num-gpus 4 \
--eval-only \
OUTPUT_DIR ./checkpoints/handside \
MODEL.WEIGHTS ./checkpoints/hos_train_101/model_final.pth
```
Evaluate contact:
```
python eval_contact.py \
--config-file ./configs/hos/hos_pointrend_rcnn_R_101_FPN_1x_contact.yaml \
--num-gpus 4 \
--eval-only \
OUTPUT_DIR ./checkpoints/contact \
MODEL.WEIGHTS ./checkpoints/hos_train_101/model_final.pth
```
Evaluate combineHO:
```
python eval_combineHO.py \
--config-file ./configs/hos/hos_pointrend_rcnn_R_101_FPN_1x_combineHO.yaml \
--num-gpus 4 \
--eval-only \
OUTPUT_DIR ./checkpoints/combineHO \
MODEL.WEIGHTS ./checkpoints/hos_train_101/model_final.pth
```