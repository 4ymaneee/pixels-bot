import cv2
import numpy as np
import pyautogui
import threading
import tkinter as tk

class ImageDetectionApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Detection App")

        # Set window dimensions
        master.geometry("400x250")

        self.start_button = tk.Button(master, text="Start", command=self.start_detection)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_detection, state=tk.DISABLED)
        self.stop_button.pack()

        self.status_label = tk.Label(master, text="Press 'Start' to begin detection.")
        self.status_label.pack()

        self.image_detected_label = tk.Label(master, text="")
        self.image_detected_label.pack()

        self.image1_to_detect = cv2.imread('create.png', cv2.IMREAD_COLOR)
        self.image2_to_detect = cv2.imread('collect.png', cv2.IMREAD_COLOR)
        self.is_detecting = False
        self.is_paused = False
        self.detection_thread = None

    def start_detection(self):
        self.is_detecting = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        if not self.detection_thread or not self.detection_thread.is_alive():
            self.detection_thread = threading.Thread(target=self.continuous_detection)
            self.detection_thread.start()
        self.status_label.config(text="Detection started.")

    def stop_detection(self):
        self.is_paused = True
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Detection paused.")

    def continuous_detection(self):
        while self.is_detecting:
            if self.is_paused:
                continue
            if self.detect_and_click(self.image1_to_detect) or self.detect_and_click(self.image2_to_detect):
                self.image_detected_label.config(text="Image detected!")
                continue
            else:
                self.image_detected_label.config(text="")
                pyautogui.sleep(1)

    def detect_and_click(self, image_to_detect):
        # Capture the screen
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # Convert image to the same color space as screenshot
        image_to_detect_rgb = cv2.cvtColor(image_to_detect, cv2.COLOR_BGR2RGB)

        # Match the template
        result = cv2.matchTemplate(screenshot_rgb, image_to_detect_rgb, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # If the template is found
        if max_val > 0.8:
            # Get the coordinates of the detected image
            top_left = max_loc
            bottom_right = (top_left[0] + image_to_detect.shape[1], top_left[1] + image_to_detect.shape[0])

            # Calculate the center of the image
            center_x = (top_left[0] + bottom_right[0]) // 2
            center_y = (top_left[1] + bottom_right[1]) // 2

            # Click on the center of the detected image
            pyautogui.click(x=center_x, y=center_y)
            print("Image found and clicked.")
            return True
        else:
            print("Image not found.")
            return False

def main():
    root = tk.Tk()
    app = ImageDetectionApp(root)
    root.mainloop()

if __name__ == "__main__":import cv2
import numpy as np
import pyautogui
import threading
import tkinter as tk

class ImageDetectionApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Detection App")

        # Set window dimensions
        master.geometry("300x200")

        self.start_button = tk.Button(master, text="Start", command=self.start_detection, width=10)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_detection, state=tk.DISABLED, width=10)
        self.stop_button.pack(pady=5)

        self.status_label = tk.Label(master, text="Press 'Start' to begin detection.")
        self.status_label.pack()

        self.image_detected_label = tk.Label(master, text="")
        self.image_detected_label.pack()

        self.image1_to_detect = cv2.imread('create.png', cv2.IMREAD_COLOR)
        self.image2_to_detect = cv2.imread('collect.png', cv2.IMREAD_COLOR)
        self.is_detecting = False
        self.is_paused = False
        self.detection_thread = None

    def start_detection(self):
        self.is_detecting = True
        self.is_paused = False
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        if not self.detection_thread or not self.detection_thread.is_alive():
            self.detection_thread = threading.Thread(target=self.continuous_detection)
            self.detection_thread.start()
        self.status_label.config(text="Detection started.")

    def stop_detection(self):
        self.is_paused = True
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Detection paused.")

    def continuous_detection(self):
        while self.is_detecting:
            if self.is_paused:
                continue
            if self.detect_and_click(self.image1_to_detect) or self.detect_and_click(self.image2_to_detect):
                self.image_detected_label.config(text="Image detected!")
                continue
            else:
                self.image_detected_label.config(text="")
                pyautogui.sleep(1)

    def detect_and_click(self, image_to_detect):
        # Capture the screen
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # Convert image to the same color space as screenshot
        image_to_detect_rgb = cv2.cvtColor(image_to_detect, cv2.COLOR_BGR2RGB)

        # Match the template
        result = cv2.matchTemplate(screenshot_rgb, image_to_detect_rgb, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # If the template is found
        if max_val > 0.8:
            # Get the coordinates of the detected image
            top_left = max_loc
            bottom_right = (top_left[0] + image_to_detect.shape[1], top_left[1] + image_to_detect.shape[0])

            # Calculate the center of the image
            center_x = (top_left[0] + bottom_right[0]) // 2
            center_y = (top_left[1] + bottom_right[1]) // 2

            # Click on the center of the detected image
            pyautogui.click(x=center_x, y=center_y)
            print("Image found and clicked.")
            return True
        else:
            print("Image not found.")
            return False

def main():
    root = tk.Tk()
    app = ImageDetectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

    main()
