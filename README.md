# PanopticFCN
- zip파일을 다운 받은 후 cityscapes 폴더를 생성하여 모든 파일을 해당 폴더로 이동

```
$PanopticFCN/
  cityscapes/
    cityscapesscripts/
    docs/
    tools_d2_cityscapes/
    .
    .
    .
```

## Install instructions을 따라서 detectron2 설치
- (https://detectron2.readthedocs.io/en/latest/tutorials/install.html)
- detectron2 오픈 소스를 다운로드 받은 후, detectron2 폴더 경로에서 설치 가능
- Python ≥ 3.7, Pytorch ≥ 1.8 
- 설치한 라이브리 버전 제공 가능

- 현재 detectron2가 다운받아져 있으니 ** tools_d2_cityscapes 폴더에서 <pre><code>{python -m pip install -e detectron2}</code></pre> 명령어로 detectron2 설치** 하면 됨

## cityscapes dataset 구조
- https://github.com/facebookresearch/detectron2/blob/main/datasets/README.md 를 참고하여 다음과 같이 cityscapes 데이터셋의 폴더 구조를 생성하고 cityscapesScripts를 다운로드한 후, createTrainIdLabelImgs.py, createPanopticImgs.py 두 개의 파이썬 파일을 통해 labelTrainIds.png와 cityscapes panoptic dataset을 생성함

<p align="center">
   <img src="https://user-images.githubusercontent.com/122510029/232689934-2467947b-6d00-41e6-8461-2bde1091bf5e.png"
</p>

- PanopticFCN 폴더 내에 cityscapes 폴더를 생성하여 다운받은 detectron2 폴더와 cityscapesScripts 폴더를 cityscapes 폴더로 이동함

## Evaluation (라이브러리 import 경로가 맞지 않는 경우가 있어서 수동으로 맞춰줘야 함)
- (모델 제공 가능: batch size = 32, max iteration = 65000으로 training 시킨 모델)
  
```
python train.py --config-file configs/cityscapes/PanopticFCN-R50-cityscapes.yaml --num-gpus 8 --eval-only MODEL.WEIGHTS /path/to/model_checkpoint 
```
  
## Visualization
- https://www.youtube.com/watch?v=Pb3opEFP94U 을 참고하여 결과 이미지를 저장함

```
python /path/to/detectron2/demo/Detector_main.py --config-file configs/cityscapes/PanopticFCN-R50-cityscapes.yaml --eval-only MODEL.WEIGHTS /path/to/model_checkpoint
```

<p align="center">
   <img src="https://user-images.githubusercontent.com/122510029/232692449-841da0ac-2029-4dc5-b80f-3c649b31f52d.png"
</p>

<p align="center">
   <img src="https://user-images.githubusercontent.com/122510029/232692544-2244387e-5454-433f-adf2-87c3d3d98897.png"
</p>
  
## Training
```
python train.py --config-file configs/cityscapes/PanopticFCN-R50-cityscapes.yaml --num-gpus 8
```
