import torch
from mobilenet_v2_tsm import MobileNetV2
import io
import onnx 
num_classes = 1
model = MobileNetV2(n_class=num_classes)
model_path = './21Jun.pth'
model.load_state_dict(torch.load(model_path, map_location=torch.device('cuda:0')))
model.eval()

torch_inputs = (torch.rand(1, 3, 224, 224),
                torch.zeros([1, 3, 56, 56]),
                torch.zeros([1, 4, 28, 28]),
                torch.zeros([1, 4, 28, 28]),
                torch.zeros([1, 8, 14, 14]),
                torch.zeros([1, 8, 14, 14]),
                torch.zeros([1, 8, 14, 14]),
                torch.zeros([1, 12, 14, 14]),
                torch.zeros([1, 12, 14, 14]),
                torch.zeros([1, 20, 7, 7]),
                torch.zeros([1, 20, 7, 7]))

input_names = []
input_shapes = {}
with torch.no_grad():
        for index, torch_input in enumerate(torch_inputs):
                name = "i" + str(index)
                input_names.append(name)
                input_shapes[name] = torch_input.shape
        buffer = io.BytesIO()
        torch.onnx.export(model, torch_inputs, buffer, input_names=input_names, output_names=["o" + str(i) for i in range(len(torch_inputs))], opset_version=7)
        outs = model(*torch_inputs)
        buffer.seek(0, 0)
        onnx_model = onnx.load_model(buffer)
        from onnxsim import simplify
        onnx_model, success = simplify(onnx_model)  # this simplifier removes conversion bugs.

        onnx.save(onnx_model, "opset7.onnx")



