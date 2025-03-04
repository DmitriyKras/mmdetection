_base_ = '../rtmdet/rtmdet_s_8xb32-300e_coco.py'


data_root = '/home/cv-worker/dmitrii/RAT_DATASET/WISTAR_RAT_KPTS_DATASET_COCO/'
metainfo = {
    'classes': ('rat', ),
    'palette': [
        (220, 20, 60),
    ]
}


train_dataloader = dict(
    batch_size=16,
    num_workers=10,
    pin_memory=True,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/train.json',
        data_prefix=dict(img='train/images/')))
val_dataloader = dict(
    batch_size=4, num_workers=10,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='annotations/val.json',
        data_prefix=dict(img='val/images/')))
test_dataloader = val_dataloader

# Modify metric related settings
val_evaluator = dict(ann_file=data_root + 'annotations/val.json')
test_evaluator = val_evaluator
