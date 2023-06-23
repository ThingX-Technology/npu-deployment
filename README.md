# NPU deployment on Khadas VIM3 NPU

Deploying models on the VIM3 requires the use of KSNN, Khadas Software Neural Network. 

First clone the model conversion tool and enter the python directory:
```
git clone https://github.com/khadas/aml_npu_sdk
cd aml_npu_sdk/python
```

Here you will find the full length python conversion tool, which is run using the convert file.
The conversion tool requires models trained using older versions of most depp learning framework. Easier way to get past this is to convert the model to an older format with the scripts provided

For pytorch models, the 1.6 release of PyTorch switched torch.save to use a new zipfile-based file format. torch.load still retains the ability to load files in the old format. To prevent this use kwarg _use_new_zipfile_serialization=False whe nsaving the model. The model needs to be saved in the old format to be loaded by older versions of pytorch.
Running:

```
python3 pytorch_old.py
```
Returns a .pth file with the pre 1.6 serialization method

Create a conda environment with Python3.6 and install dependecies for conversion:
```
conda create -n py36 python=3.6 anaconda
conda activate py36
pip install -r ksnn_requirements.txt 
```
The next step is to convert the model to ONNX as an intermediary format using the older version of pytorch and onnx.
```
python3 torch2onnx.py
```

Finally, the model can be comiled and quantised using the following command:
```
./convert --model-name Fall-with-shift \
           --platform onnx \
           --model ./20jun/opset7.onnx \
           --mean-values '128 128 128 0.0078125' \
           --quantized-dtype asymmetric_affine \
           --source-files ./dataset.txt \
           --kboard VIM3 --print-level 1
```
The dataset file contains space seperated inputs, in this case the 11 inputs required by the model.
