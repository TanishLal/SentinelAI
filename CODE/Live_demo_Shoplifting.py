import os
import cv2
import queue
import time
import threading
import numpy as np
from termcolor import colored
from datetime import date, datetime
import tensorflow as tf
import warnings

# Custom modules
import Alert
from data_pip_shoplifting import Shoplifting_Live

# Ignore warnings
warnings.filterwarnings("ignore")

# Disable TensorFlow AVX/FMA warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Use tensorflow.keras instead of keras
from tensorflow.keras.models import load_model, Model, model_from_json
from tensorflow.keras.layers import (
    Input, Dense, Flatten, Conv3D, MaxPooling3D, Dropout, Multiply, Add, Concatenate, Lambda
)
from tensorflow.keras.optimizers import Adam, SGD



# from object_detection.utils import label_map_util
# from object_detection.utils import config_util
# from object_detection.utils import visualization_utils as viz_utils
# from object_detection.builders import model_builder

def get_abuse_model_and_weight_json():
    # read model json
    # load json and create model
    weight_abuse = r"D:\newFolder\Shoplifting-Detection\CODE\weight_steals\GATE_FLOW_SLOW_FAST_RGB_ONLY\weights_at_epoch_3___65.h5"
    json_path = r"D:\newFolder\Shoplifting-Detection\CODE\shoplifting_model.json"
    json_file = open(json_path, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    abuse_model = model_from_json(loaded_model_json)
    # load weights into new model
    abuse_model.load_weights(weight_abuse)
    print("Loaded EMS model,weight_steals from disk")
    return abuse_model

# ABUSE_MODEL = get_abuse_model_and_weight_json()
q = queue.Queue(maxsize=3000)
frame_set = []


Frame_set_to_check = []
Frame_INDEX = 0
lock = threading.Lock()
Email_alert_flag = False
email_alert = Alert.Email_Alert()
shoplifting_SYS = Shoplifting_Live()
W=0
H=0
src_main_dir_path =r"D:\newFolder\Shoplifting-Detection"
# src_main_dir_path = r"C:\Users\amit hayoun\Desktop\test3\3\aaa."

def playVideo(path):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            # Restart video if reached the end
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    cap.release()
    cv2.destroyAllWindows()



def Receive():
    global H,W
    print("start Receive")
    #rtsp://SIMCAM:2K93AG@192.168.1.2/live
    #video_cap_ip = 'rtsp://SIMCAM:S6BG9J@192.168.1.20/live'
    #video_cap_ip = r'rtsp://barloupo@gmail.com:ziggy2525!@192.168.1.9:554/stream2'
    video_cap_ip= r"D:\newFolder\Shoplifting-Detection\DB_Sample\output\SL_event_record_1__ (1).gif"
    cap = cv2.VideoCapture(video_cap_ip)
    # cap.set(3, 640)
    # cap.set(4, 480)
    W = int(cap.get(3))
    H = int(cap.get(4))
    #print("H={}\nW={}".format(H,W))
    ret, frame = cap.read()
    print(colored(ret, 'green'))
    q.put(frame)
    #while cap.isOpened():
    while ret:
        ret, frame = cap.read()
        q.put(frame)


def Display():
    global Frame_set_to_check,Frame_INDEX
    print(colored('Start Displaying', 'blue'))

    while True:
        if q.empty() != True :
            frame = q.get()
            # print(frame)
            if isinstance(frame, type(None)):
                print("[-][-] NoneType frame {}".format(type(frame)))
                break
                # continue

            frame_set.append(frame.copy())
            print(len(frame_set))
            if len(frame_set) >= 44:
                Frame_set_to_check = frame_set.copy()

                #print(type(Frame_set_to_check))
                #p3 = threading.Thread(target=Pred)
                Pred()
                time.sleep(1)
                frame_set.clear()

            #cv2.imshow("frame1", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def Pred():
    global Frame_set_to_check, Frame_INDEX
    #ems = EMS_Live()
    with lock:
        #RGB + OPT NET
        #shoplifting_SYS.build_shoplifting_net_models()

        #RGB NET ONLY
        # shoplifting_SYS.load_model_and_weight_gate_flow_slow_fast_RGB()
        shoplifting_SYS.build_shoplifting_net_models()

        Frame_set_to_check_np = np.array(Frame_set_to_check.copy())

        Frame_set = shoplifting_SYS.make_frame_set_format(Frame_set_to_check_np)

        # reports = shoplifting_SYS.run_Shoplifting_frames_check_live_demo_2_version(Frame_set, Frame_INDEX)
        reports = shoplifting_SYS.run_Shoplifting_frames_check_live_demo(Frame_set, Frame_INDEX)
        print("reports:  ",reports)
        Frame_INDEX = Frame_INDEX + 1
        ##
        Bag = reports[0]
        Clotes = reports[1]
        Normal = reports[2]
        state = reports[3]
        #todo event_index maybe paas a dict
        # event_index = reports[4]
        #print("event_index {}".format(event_index))
        ##


        if not (state):
            print(colored(f"---------------------", 'green'))
            print(colored('Found shopLifting event', 'green'))
            print(colored(f"Bag: {Bag}\nClotes: {Clotes}\nNormal: {Normal}", 'green'))
            #print(colored(f"reports {reports[0], reports[1],reports[2]}", 'green'))
            print(colored(f"Test number:{Frame_INDEX-1}\n---------------------\n", 'green'))
            # print("fight:{}\nnot fight:{}".format(fight,not_fight))

            prob = [Bag, Clotes,Normal]

            found_fall_video_path = shoplifting_SYS.save_frame_set_after_pred_live_demo(src_main_dir_path,
                                                                                 Frame_set_to_check,
                                                                                 Frame_INDEX-1, prob,
                                                                                 0, W, H)
            
            playVideo(src_main_dir_path+"/Shoplifting_event_record_0__.avi")

            if Email_alert_flag:
                file_name = found_fall_video_path.split("\\")[-1]
                print(f"path = to email{found_fall_video_path}")
                print(f"file name: {file_name}")
                absulutefilepath = found_fall_video_path
                email_alert.send_email_alert(email_alert.user_email_address3, file_name,
                                                  absulutefilepath)

        else:
            print(colored(f"---------------------", 'red'))
            print(colored("Normal event", 'red'))
            print(colored(f"Test number:{Frame_INDEX - 1}\n---------------------\n", 'red'))
            Frame_set_to_check.clear()

        #lock.release()
        time.sleep(1)

# def Pred():
#     global Frame_set_to_check, Frame_INDEX
#     with lock:
#         # Load the abuse model instead of calling the undefined method:
#         shoplifting_SYS.shoplifting_model = get_abuse_model_and_weight_json()
#         print("Model loaded successfully!")
        
#         Frame_set_to_check_np = np.array(Frame_set_to_check.copy())
#         Frame_set = shoplifting_SYS.make_frame_set_format(Frame_set_to_check_np)
#         reports = shoplifting_SYS.run_StealsNet_frames_check_live_demo_2_version(Frame_set, Frame_INDEX)
#         Frame_INDEX += 1
#         Bag, Clotes, Normal, state, event_index = reports
        
#         if state:
#             print(colored("---------------------", 'green'))
#             print(colored('Found shopLifting event', 'green'))
#             print(colored(f"Bag: {Bag}\nClotes: {Clotes}\nNormal: {Normal}", 'green'))
#             print(colored(f"Test number: {Frame_INDEX-1}\n---------------------\n", 'green'))
#             prob = [Bag, Clotes, Normal]
#             found_fall_video_path = shoplifting_SYS.save_frame_set_after_pred_live_demo(
#                 src_main_dir_path, Frame_set_to_check, Frame_INDEX-1, prob, 0, W, H
#             )
#             if Email_alert_flag:
#                 file_name = found_fall_video_path.split("\\")[-1]
#                 print(f"path to email: {found_fall_video_path}")
#                 print(f"file name: {file_name}")
#                 absulutefilepath = found_fall_video_path
#                 email_alert.send_email_alert(email_alert.user_email_address3, file_name, absulutefilepath)
#         else:
#             print(colored("---------------------", 'red'))
#             print(colored("Normal event", 'red'))
#             print(colored(f"Test number: {Frame_INDEX-1}\n---------------------\n", 'red'))
#             Frame_set_to_check.clear()

#         time.sleep(1)


if __name__ == '__main__':
    p1 = threading.Thread(target=Receive)
    p2 = threading.Thread(target=Display)
    #p3 = threading.Thread(target=Pred)
    p1.start()
    p2.start()
    #p3.start()