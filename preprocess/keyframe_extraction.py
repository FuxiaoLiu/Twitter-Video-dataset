import os
import cv2
import subprocess

filename = '/home/andriy/Downloads/video.mp4'

def get_frame_types(video_fn):
    command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    out = subprocess.check_output(command + [video_fn]).decode()
    frame_types = out.replace('pict_type=','').split()
    return zip(range(len(frame_types)), frame_types)

def save_i_keyframes(video_fn):
    frame_types = get_frame_types(video_fn)
    i_frames = [x[0] for x in frame_types if x[1]=='I']
    if i_frames:
        basename = os.path.splitext(os.path.basename(video_fn))[0]
        cap = cv2.VideoCapture(video_fn)
        for frame_no in i_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            ret, frame = cap.read()
            basename1 = './code/sample/'
            outname = basename1+'frame_'+str(frame_no)+'.jpg'
            cv2.imwrite(outname, frame)
            print ('Saved: '+outname)
        cap.release()
    else:
        print ('No I-frames in '+video_fn)

if __name__ == '__main__':
    filename = './code/sample4.mp4'
    save_i_keyframes(filename)
    
    
'''
import os
from concurrent import futures
from tqdm import tqdm

def extract_frames(video_name, out_folder, fps=2):
    if os.path.exists(out_folder):
        os.system('rm -rf ' + out_folder + '/*')
        os.system('rm -rf ' + out_folder)
    os.makedirs(out_folder)
    cmd = 'ffmpeg -v 0 -i %s -r %d -q 0 %s/%s.jpg' % (video_name, fps, out_folder, '%08d')
    os.system(cmd)


target_path = '/fs/vulcan-projects/misc_forensics/DATA_FUXIAO/frame_and_transcript_sample/'
files = os.listdir(target_path)

for file in tqdm(files):
    path1 = target_path + file

    path2 = os.listdir(path1)

    for p in path2:
        if 'mp4' in p:
            path3 = path1 + '/' + p

    input_path = path3
    output_path = path1 + '/frames_fps2'


    if not os.path.exists(output_path):
        os.mkdir(output_path)

    extract_frames(input_path, output_path)
'''
