# import cv2
# import urllib
# import numpy as np
 
# stream=urllib.urlopen('http://192.168.100.103:9000/')
# bytes=''
# while True:
#     bytes+=stream.read(1024)
#     a = bytes.find('\xff\xd8')
#     b = bytes.find('\xff\xd9')
#     if a!=-1 and b!=-1:
#         jpg = bytes[a:b+2]
#         bytes= bytes[b+2:]
#         i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
#         cv2.imshow('i',i)
#         if cv2.waitKey(1) == 27:
#             exit(0)


import cv2
def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    # カメラをキャプチャする
    cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号

    while True:
        # retは画像を取得成功フラグ
        ret, frame = cap.read()

        # 鏡のように映るか否か
        if mirror is True:
            frame = frame[:,::-1]

        # フレームをリサイズ
        # sizeは例えば(800, 600)
        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)

        # フレームを表示する
        cv2.imshow('camera capture', frame)

        k = cv2.waitKey(1) # 1msec待つ
        if k == 27: # ESCキーで終了
            break

    # キャプチャを解放する
    cap.release()
    cv2.destroyAllWindows()