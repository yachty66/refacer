import os
import subprocess
import argparse
import re

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}\n{result.stderr}")
    else:
        print(result.stdout)

def extract_number(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else None

def main(video_path):
    output_folder = "images"
    destination_folder = "destinations"
    
    # Step 1: Extract faces from the video
    extract_command = f"python extract_faces.py --video {video_path} --output {output_folder}"
    run_command(extract_command)
    
    # Step 2: Prepare the face swap command
    face_swap_command = f"python script.py --video {video_path}"
    
    face_files = {extract_number(f): f for f in os.listdir(output_folder) if f.startswith("face_") and f.endswith(".jpg")}
    dest_files = {extract_number(f): f for f in os.listdir(destination_folder) if f.startswith("dest_") and f.endswith(".jpg")}
    
    for number in face_files:
        if number in dest_files:
            face_path = os.path.join(output_folder, face_files[number])
            dest_path = os.path.join(destination_folder, dest_files[number])
            face_swap_command += f" --face {face_path},{dest_path},0.2"
    
    face_swap_command += " --force_cpu --colab_performance"
    
    # Step 3: Run the face swap command
    run_command(face_swap_command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate face extraction and swapping.")
    parser.add_argument("video_path", type=str, help="Path to the input video file.")
    args = parser.parse_args()
    
    main(args.video_path)