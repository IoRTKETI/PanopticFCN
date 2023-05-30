# -*- coding: utf-8 -*-
# Copyright (c) Facebook, Inc. and its affiliates.

from .build import META_ARCH_REGISTRY, build_model  # isort:skip

from .panoptic_fpn import PanopticFPN

# import all the meta_arch, so they will be registered
from .rcnn import GeneralizedRCNN, ProposalNetwork
from .dense_detector import DenseDetector
from .retinanet import RetinaNet
from .fcos import FCOS
from .semantic_seg import SEM_SEG_HEADS_REGISTRY, SemanticSegmentor, build_sem_seg_head

# from .config import add_panopticfcn_config # panopticfcn_HM
# from .panoptic_seg import PanopticFCN # panopticfcn_HM
# from .build_solver import build_lr_scheduler # panopticfcn_HM


__all__ = list(globals().keys())
