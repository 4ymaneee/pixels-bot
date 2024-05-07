import cv2
import numpy as np
import pyautogui
import keyboard

# Load the images to be detected
image1_to_detect = cv2.imread('create.png', cv2.IMREAD_COLOR)
image2_to_detect = cv2.imread('collect.png', cv2.IMREAD_COLOR)

# Function to detect image and click on its center
def detect_and_click(image_to_detect):
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

# Continuously detect and click on images until F6 is pressed
try:
    while True:
        if detect_and_click(image1_to_detect) or detect_and_click(image2_to_detect):
            continue
        else:
            # Wait for a moment before trying again
            pyautogui.sleep(1)
        if keyboard.is_pressed('f6'):
            print("Script stopped by user.")
            break
except KeyboardInterrupt:
    print("Script interrupted by user.")
