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

## cityscapes dataset 구조
- https://github.com/facebookresearch/detectron2/blob/main/datasets/README.md 를 참고하여 다음과 같이 cityscapes 데이터셋의 폴더 구조를 생성하고 cityscapesScripts를 다운로드한 후, createTrainIdLabelImgs.py, createPanopticImgs.py 두 개의 파이썬 파일을 통해 labelTrainIds.png와 cityscapes panoptic dataset을 생성함

![image](https://user-images.githubusercontent.com/122510029/232689934-2467947b-6d00-41e6-8461-2bde1091bf5e.png)
