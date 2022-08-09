```shell
python tools/misc/clip_feature_extraction.py \
configs/recognition/tsn/tsn_r50_clip_feature_extraction_1x1x3_rgb.py \
https://download.openmmlab.com/mmaction/recognition/tsn/tsn_r50_320p_1x1x3_100e_kinetics400_rgb/tsn_r50_320p_1x1x3_100e_kinetics400_rgb_20200702-cc665e2a.pth \
--video-list ucf101.txt \
--video-root data/ucf101/videos \
--out ucf101_feature.pkl
```