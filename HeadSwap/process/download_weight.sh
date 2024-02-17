# wget https://github.com/LeslieZhoa/HeSer.Pytorch/releases/download/v0.0/parsing.pth -P ../pretrained_models
# wget https://github.com/LeslieZhoa/HeadSwap/releases/download/v0.0/sr_cf.onnx -P ../pretrained_models
# wget https://github.com/LeslieZhoa/HeadSwap/releases/download/v0.0/Blender-401-00012900.pth -P ../pretrained_models

#wget -P ../pretrained_models https://github.com/LeslieZhoa/HeSer.Pytorch/releases/download/v0.0/parsing.pth
#wget -P ../pretrained_models https://github.com/LeslieZhoa/HeadSwap/releases/download/v0.0/sr_cf.onnx
#wget -P ../pretrained_models https://github.com/LeslieZhoa/HeadSwap/releases/download/v0.0/Blender-401-00012900.pth

cd ./pretrained_models
curl -fL https://github.com/LeslieZhoa/HeSer.Pytorch/releases/download/v0.0/parsing.pth --output parsing.pth
curl -fL https://github.com/LeslieZhoa/HeadSwap/releases/download/v0.0/sr_cf.onnx --output sr_cf.onnx
curl -fL https://github.com/LeslieZhoa/HeadSwap/releases/download/v0.0/Blender-401-00012900.pth --output Blender-401-00012900.pth
cd ../