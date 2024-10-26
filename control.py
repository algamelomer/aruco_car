from test_2 import *
import requests
import time
import numpy as np

esp32_ip = "http://192.168.43.247"

def run_aruco_marker_pose_estimation(aruco_type): 
    aruco_marker = ArucoMarkers() 
    camera_matrix = np.array([
        [1432.0, 0.0, 983.0], 
        [0.0, 1434.0, 561.0], 
        [0.0, 0.0, 1.0]
    ])  
    dist_coeffs = np.array([0.05994318, -0.26432366, -0.00135378, -0.00081574, 0.29707202])

    for distance in aruco_marker.aruco_marker_pose_estimation(aruco_type, camera_matrix, dist_coeffs):
        print(f"Distance: {distance:.2f} meters")
        
        if distance <= 15:
            command = "turn_right"
            command_url = f"{esp32_ip}:81/cmd?cmd={command}"
            print(command_url)
            # commands = ["forward", "right", "forward"]
            # for command in commands:
            #     command_url = f"{esp32_ip}:81/cmd?cmd={command}"
            #     print(command_url)
            #     try:
            #         response = requests.get(command_url)
            #         print(f"Command sent: {command}, Response: {response.text}")
            #     except requests.RequestException as e:
            #         print(f"Failed to send command {command}: {e}")
                
                # time.sleep(1.5)  # Wait 3 seconds before the next command

if __name__ == "__main__":
    run_aruco_marker_pose_estimation(ArucoType.DICT_6X6_250)
