import pytest
from playwright.sync_api import sync_playwright,Page,expect

def test_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frames=page.frames
    print("\nTotal number of frames:",len(frames))

    # frame = 1
    frame1=page.frame_locator("frame[src='frame_1.html']") # approach 1
    frame1=page.frame("please write name of the frame") # approach 2, but this frame don't have frame name
    frame1=page.frame(url="https://ui.vision/demo/webtest/frames/frame_1.html") # approach 3

    inputbox=frame1.locator("input[name='mytext1']")
    inputbox.fill("welcome")
    expect(inputbox).to_have_value("welcome")
    page.wait_for_timeout(3000)
