# Head and Face Swapping Software

This is a simple Python program that leverages two different libraries for head and face swapping tasks. It utilizes the [**'roop'**](https://github.com/s0md3v/roop) library for face swapping and the [**'HeadSwap'**](https://github.com/LeslieZhoa/HeadSwap) library for head swapping.

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

#### --- Install PIP packages:
  
_if cuda available:_
- pip install -r requirements_cuda.txt
  
_if cuda not available and want to use cpu:_
- pip install -r requirements_cpu.txt

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
To utilize the swapping functionalities of this program, you can run the `main.py` script with the following command line arguments:

- `--source`: Path to the source image file.
- `--target`: Path to the target image file.
- `-o, --output`: Path to the output image file.
- `--alsoswapface`: Optional argument to indicate whether to swap the face after head swapping. If provided, the program will perform face swapping on the output of head swapping. (default: False)
- `--swap`: Specify whether to perform head swapping (`head`) or face swapping (`face`). The default value is `head`.

### **Example Usage:**

To perform head swapping:

`python main.py --source "path/to/source/image.png" --target "path/to/target/image.png" -o "output/image.png" --swap head`

To perform face swapping:

`python main.py --source "path/to/source/image.png" --target "path/to/target/image.png" -o "output/image.png" --swap face`

To perform both head and face swapping:

`python main.py --source "path/to/source/image.png" --target "path/to/target/image.png" -o "output/image.png" --swap head --alsoswapface`

### **Note:**
- Ensure that the paths to source and target images are valid.
- If virtual environment is activated, the required packages will be automatically used from the virtual environment. Otherwise, ensure that the required packages are installed in your Python environment.
- For detailed instructions on installation and setup, please refer to the Installation section above.