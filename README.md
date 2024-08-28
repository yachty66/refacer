# Refacer Refactored

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1j_KN_nDKutnxTRKhyUTkkX6Q7I-D90ny?usp=sharing)

### How It Works

1. **Face Extraction**:
   - The extracted faces are saved in the `images` folder with filenames like `face_0.jpg`, `face_1.jpg`, etc.

2. **Destination Images**:
   - You can place your destination images in the `destinations` folder.
   - Name the destination images as `dest_0.jpg`, `dest_1.jpg`, etc.
   - The number at the end of the filename is crucial as it determines which extracted face it will replace. For example, `dest_1.jpg` will replace `face_1.jpg`.

3. **Face Swapping**:
   - The script will automatically match the extracted face images with the destination images based on the numbers in their filenames.
   - If there are 3 faces in the video (`face_0.jpg`, `face_1.jpg`, `face_2.jpg`) and you only want to change the face of `face_1.jpg`, you should place the new face image as `dest_1.jpg` in the `destinations` folder.
   - The script will then perform the face swap using the matched images.

This process automates the extraction of faces from the video, matches them with the destination images, and performs the face swap.