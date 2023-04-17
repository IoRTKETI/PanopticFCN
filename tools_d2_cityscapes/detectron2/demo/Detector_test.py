# https://www.youtube.com/watch?v=Pb3opEFP94U

from detectron2.engine import DefaultPredictor
from detectron2.configs import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import ColorMode, Visualizer
from detectron2 import model_zoo

import cv2
import numpy as np

import datetime #HM
import os #HM


class Detector:
    def __init__(self):
        self.cfg = get_cfg()
        # self.args = default_argument_parser().parse_args() #HM

        # Load model config and pretrained model
        # self.cfg.merge_from_file(model_zoo.get_config_file("COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml"))
        # self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml")
        self.cfg.merge_from_file(model_zoo.get_config_file("Cityscapes/PanopticFCN_R50_cityscapes.yaml"))
        self.cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("Cityscapes/PanopticFCN_R50_cityscapes.yaml")

        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7
        self.cfg.MODEL.DEVICE = "cuda" # cpu or cuda

        self.predictor = DefaultPredictor(self.cfg)

    # def onImage(self, imagePath):
    #     image = cv2.imread(imagePath)
    #     predictions, segmentInfo = self.predictor(image)["panoptic_seg"]
    #     viz =Visualizer(image[:,:,::-1], metadata = MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]))
    #     output = viz.draw_panoptic_seg_predictions(predictions.to("cpu"), segmentInfo)

    #     file_name = datetime.datetime.now() #HM
    #     filename = file_name.strftime("%Y-%m-%d_%H%M%s.%f")

    #     # cv2.imshow("Results", output.get_image()[:,:,::-1])
    #     # cv2.imwrite("./output/results/test/Resultsv1.png", output.get_image()[:,:,::-1])
    #     cv2.imwrite("./output/results/test/" + filename + ".png", output.get_image()[:,:,::-1])
    #     cv2.waitKey(0)

    def onImage(self, imagePath):
        for i in os.listdir(imagePath):
            path = imagePath + i
            image = cv2.imread(path)
            predictions, segmentInfo = self.predictor(image)["panoptic_seg"]
            viz =Visualizer(image[:,:,::-1], metadata = MetadataCatalog.get(self.cfg.DATASETS.TRAIN[0]))
            output = viz.draw_panoptic_seg_predictions(predictions.to("cpu"), segmentInfo)

            file_name = datetime.datetime.now() #HM
            filename = file_name.strftime("%Y-%m-%d_%H%M%s.%f")

            cv2.imwrite("./output/results/test/" + filename + ".png", output.get_image()[:,:,::-1])
            cv2.waitKey(0)
