page.on("download", lambda download: download.save_as("downloads/textfile.txt")) # day30


page.on("page",lambda page:page.wait_for_load_state())  # day31

