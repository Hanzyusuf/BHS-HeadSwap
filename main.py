import os
import sys
import cv2

sys.path.append('./HeadSwap')
from inference import Infer

sys.path.append('./roop')
from roop import core


def swap_head(src_img_path, tgt_img_path, save_path):
    # Create an instance of the Infer class
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
        cv2.imwrite(save_path, generated_image)
        print(f"Image saved successfully at {save_path}")
    else:
        print("Error: Generated image is None.")


def swap_face(src_img_path, tgt_img_path, save_path):
    core.runCL(source_path=src_img_path, target_path=tgt_img_path, output_path=save_path)


if __name__ == "__main__":

    # set input source and target image paths
    src_path = './images/src/yusuf.png'
    tgt_path = './images/src/robert.png'

    # Check if source and target files exist, show error and exit if either not found
    if not (os.path.exists(src_path)):
        print(f"Error: Source file does not exist.\nNo file exists with path: {src_path}")
        sys.exit(1)
    elif not (os.path.exists(tgt_path)):
        print(f"Error: Target file does not exist.\nNo file exists with path: {tgt_path}")
        sys.exit(1)

    # create output file path
    save_base = './images/result'
    img_name = os.path.splitext(os.path.basename(src_path))[0] + '-' + os.path.splitext(os.path.basename(tgt_path))[0] + ".png"
    output_path = os.path.join(save_base, img_name)

    # Check if src_path filename contains "bride"
    if 'bride' in os.path.basename(src_path):
        swap_head(src_path, tgt_path, output_path)
        output_path_refined = os.path.join(save_base, img_name + " + faceswap.png")
        swap_face(src_path, output_path, output_path_refined)
        print("swapped head successfully!")
    else:
        swap_face(src_path, tgt_path, output_path)
        print("swapped face successfully!")