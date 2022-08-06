# TAL in Long_jump with ActionFormer
## Introduction
This is a short introduction to the this repository. We use the ActionFormer. It is a new way to localize moments of actions with Transformers. You can find some details in [project original link](https://github.com/happyharrycn/actionformer_release). In this project, I will use it to localize the long jump action. 

## ActionFormer Introduction
This code repo implements Actionformer, one of the first Transformer-based model for temporal action localization --- detecting the onsets and offsets of action instances and recognizing their action categories. Without bells and whistles, ActionFormer achieves 71.0% mAP at tIoU=0.5 on THUMOS14, outperforming the best prior model by 14.1 absolute percentage points and crossing the 60% mAP for the first time. Further, ActionFormer demonstrates strong results on ActivityNet 1.3 (36.56% average mAP) and the more challenging EPIC-Kitchens 100 (+13.5% average mAP over prior works).