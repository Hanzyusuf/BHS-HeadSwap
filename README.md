# Head and Face Swapping Software

This is a simple Python program that leverages two different libraries for head and face swapping tasks. It utilizes the 'roop' library for face swapping and the 'HeadSwap' library for head swapping.

## Features

- **Head Swapping**: Utilizes the 'HeadSwap' library to swap heads in images.
- **Face Swapping**: Utilizes the 'roop' library to swap faces in images.
- **Combined Swapping**: Capable of performing both head and face swapping tasks.

### **Note:** built and tested on **_python 3.10.11_**

### **Reminder:** activate your virtual environment if desired

### **--- Installation ---**

clone and cd into repo
- git clone https://github.com/Hanzyusuf/BHS-HeadSwap.git
- cd BHS-HeadSwap

install pip packages:
- pip install -r requirements.txt

install nvdiffrast:
- git clone https://github.com/NVlabs/nvdiffrast
- cd nvdiffrast
- pip install .

remove nvdiffrast folder as it is irrelevant now:
- cd ../
- rm -r nvdiffrast

install ffmpeg, c++ redist and build tools:
- [instructions can be followed from this page](https://github.com/s0md3v/roop/wiki/1.3-Setup-Windows)

setup pretrained_models dir
- mkdir pretrained_models
- setup the **_pretrained_models_** [exactly as done in this repo](https://github.com/LeslieZhoa/HeadSwap), no need to follow rest of the things there

### **--- How To Use ---**
- modify main.py by setting the values of **src_path** and **tgt_path** as desired.
- run in terminal: **python main.py**