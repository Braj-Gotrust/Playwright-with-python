import pytest
from playwright.sync_api import sync_playwright,Page,expect

def test_inner_frame(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frames=page.frames
    print("\nTotal number of frames:",len(frames))

    # frame 3
    frame3=page.frame(url="https://ui.vision/demo/webtest/frames/frame_3.html") # approach 1
    inputbox=frame3.locator("input[name='mytext3']")
    inputbox.fill("welcome")
    expect(inputbox).to_have_value("welcome")
    page.wait_for_timeout(3000)

    child_frames = frame3.child_frames
    print("\nTotal number of child frames:",len(child_frames))

    innerframe=child_frames[0]
    radio=innerframe.get_by_label("I am a human")
    radio.check()
    expect(radio).to_be_checked()
    page.wait_for_timeout(3000)

