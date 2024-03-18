import os
import sys
import subprocess
import cv2
import argparse

# Determine the absolute path of the directory containing main.py
script_dir = os.path.dirname(os.path.abspath(__file__))

headswap_dir = os.path.join(script_dir, 'HeadSwap')
roop_dir = os.path.join(script_dir, 'roop')
sys.path.append(headswap_dir)
sys.path.append(roop_dir)

from inference import Infer
from roop import core

def parseArgs():
    parser = argparse.ArgumentParser(description='Process images.')

    # Add arguments
    parser.add_argument('--source', type=str, help='Path to the source image file')
    parser.add_argument('--target', type=str, help='Path to the target image file')
    parser.add_argument('-o', '--output', type=str, help='Path to the output image file')
    parser.add_argument('--alsoswapface', action='store_true', help='Whether to swap face after head swap or not (default: False)')
    parser.add_argument('--swap', choices=['head', 'face'], default='head', help="Specify whether to swap 'head' or 'face' (default: 'head')")

    # Parse arguments
    args = parser.parse_args()

    # Check if required arguments are provided
    if not (args.source and args.target and args.output):
        parser.error("Please provide source, target, and output paths.")
        return None
    
    return args


def swap_head(src_img_path, tgt_img_path, img_output_path):
    model = Infer(
        'pretrained_models/epoch_00190_iteration_000400000_checkpoint.pt',
        'pretrained_models/Blender-401-00012900.pth',
        'pretrained_models/parsing.pth',
        'pretrained_models/epoch_20.pth',
        'pretrained_models/BFM'
    )

    # Call the run_single method to generate the swapped image
    generated_image = model.run_single(src_img_path, tgt_img_path, crop_align=True, cat=False)

    if generated_image is not None:
        cv2.imwrite(img_output_path, generated_image)
        print(f"Image saved successfully at {img_output_path}")
    else:
        print("Error: Generated image is None.")


def swap_face(src_img_path, tgt_img_path, img_output_path):
    global script_dir

    base_command = [
        "python",
        #"./roop/run.py",
        f"{os.path.join(script_dir,'roop/run.py')}",
        "--execution-provider", "cuda",
        "--frame-processor", "face_swapper", "face_enhancer",
        "--source", src_img_path,
        "--target", tgt_img_path,
        "-o", img_output_path
    ]

    full_command = base_command

    # Run the subprocess with the activated virtual environment
    process = subprocess.Popen(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture and print output and errors
    stdout, stderr = process.communicate()
    if stdout:
        print("Output:", stdout)
    if stderr:
        print("Errors:", stderr)

    # Check the return code
    if process.returncode != 0:
        print("Error occurred while running the subprocess in swap_face function !")
    

# check for args
args = parseArgs()

if(args == None):
    print(f"Error: Source, target and/or output paths not provided!")
    sys.exit(1)

# Check if source and target files exist, show error and exit if either not found
if not (os.path.exists(args.source)):
    print(f"Error: Source file does not exist.\nNo file exists with path: {args.source}")
    sys.exit(1)
elif not (os.path.exists(args.target)):
    print(f"Error: Target file does not exist.\nNo file exists with path: {args.target}")
    sys.exit(1)

# If swap argument is 'head', perform head swap
if args.swap == 'head':
    # Perform head swap
    print(f"performing HeadSwap ...")
    swap_head(args.source, args.target, args.output)
    
    # If 'alsoswapface' is True, modify output filename for head and swap face to original output
    if args.alsoswapface:
        print(f"performing FaceSwap over HeadSwap output ...")
        
        print(f"renaming HeadSwap output file to prevent conflict when performing FaceSwap ...")
        # Create a temporary filename for the output of head swap
        headswap_output_temp = args.output + ".headswap_temp.png"
        # Rename the output file of head swap
        os.rename(args.output, headswap_output_temp)
        
        # Perform face swap on the output of head swap
        swap_face(args.source, headswap_output_temp, args.output)

        print(f"deleting HeadSwap output ...")
        os.remove(headswap_output_temp)  # Remove the headswap original output file

        print(f"Operation completed ! : HeadSwap with FaceSwap")

    else:
        print(f"Operation completed ! : HeadSwap")

# If swap argument is 'face', perform face swap only
elif args.swap == 'face':
    # Perform face swap
    swap_face(args.source, args.target, args.output)
    print(f"Operation completed ! : FaceSwap")
