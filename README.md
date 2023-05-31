# PanopticFCN
- **zip파일을 다운 받은 후 cityscapes 폴더를 생성하여 모든 파일을 해당 폴더로 이동**
- 아래의 트리 구조와 같이 폴더를 정리해주세요.

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
- **Python ≥ 3.7, Pytorch ≥ 1.8** → 버전이 매우 중요합니다.
- 현재 detectron2가 다운받아져 있으니 **tools_d2_cityscapes 폴더에서** 아래 명령어로 **detectron2 설치** 하면 됩니다.

<pre><code>python -m pip install -e detectron2</code></pre> 

  
## Training
```
python train.py --config-file configs/cityscapes/PanopticFCN-R50-cityscapes.yaml --num-gpus 4
```

## Test
**tools_d2_cityscapes** 폴더에서 실행
```
python test.py --input datasets/cityscapes/leftImg8bit/val/your_dataset_folder/*.jpg --output output/your_output_folder --opts MODEL.WEIGHTS output/model_final_65000.pth
```

- model_final_65000.pth 파일은 제공 가능합니다.
