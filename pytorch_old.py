# script to convert pytorch model serialization to older format, not using ZIP.

import torch
from mobilenet_v2_tsm import MobileNetV2

num_classes = 1
model = MobileNetV2(n_class=num_classes)

model_path = "./Li_ThingX_21Jun.pth"
model.load_state_dict(torch.load(model_path, map_location=torch.device('cuda:0')))

torch.save(model.state_dict(), '21Jun.pth', _use_new_zipfile_serialization=False)
