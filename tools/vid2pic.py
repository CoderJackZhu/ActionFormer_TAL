import os
import cv2


def process_video(root_dir='E:\Project\Long_jump', save_dir='E:\Project\Long_jump_clip', resize_height=720,
                  resize_width=1280):
    files = os.listdir(root_dir)
    for video_filename in files:
        video_filename = video_filename.split('.')[0]
        video = os.path.join(root_dir, video_filename + '.mkv')
        if not os.path.exists(os.path.join(save_dir, video_filename)):
            os.mkdir(os.path.join(save_dir, video_filename))

        capture = cv2.VideoCapture(video)

        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        count = 0
        retaining = True

        while (count < frame_count and retaining):
            retaining, frame = capture.read()
            if frame is None:
                continue
            if (frame_height != resize_height) or (frame_width != resize_width):
                frame = cv2.resize(frame, (resize_width, resize_height))
            cv2.imwrite(filename=os.path.join(save_dir, video_filename, '{}.png'.format(str(count + 1).zfill(3))),
                        img=frame)
            count += 1

        # Release the VideoCapture once it is no longer needed
        capture.release()
        print('{} has finished'.format(video_filename))


if __name__ == '__main__':
    process_video(root_dir='../video', save_dir='../output')
    # process_video(root_dir='E:\Project\Long_jump', save_dir='E:\Project\Long_jump_clip', resize_height=720,
    #                 resize_width=1280)