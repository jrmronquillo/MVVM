import sys
import stbt
import time
import requests
sys.path.append("..")
from sanityAutomation import keySend

rack = "A03"
slot = "1-16"

def main():
	print stbt.ocr()
	keySend.keyPressAPI(rack, "exit", slot)
	time.sleep(1)
	# tune to sports mix
	URL = "http://10.23.223.39:5000/postTest/?name=testcaseStarted"
	r = requests.get(url=URL)
	keySend.tune("205", rack, slot)

	# verify snipe red button
	testCase = "verify snipe red button"
	URL = "http://10.23.223.39:5000/postTest/?name="+testCase
	r = requests.get(url=URL)
	stbt.wait_for_match('images/red_button.png')

	# verify blue cells
	verify_cell_highlight()

	# verify highlights can navigate to all cells
	keySend.keyPressAPI(rack, "rightArrow", slot)
	verify_cell_highlight()
	keySend.keyPressAPI(rack, "rightArrow", slot)
	verify_cell_highlight()
	keySend.keyPressAPI(rack, "downArrow", slot)
	verify_cell_highlight()
	keySend.keyPressAPI(rack, "leftArrow", slot)
	verify_cell_highlight()
	keySend.keyPressAPI(rack, "leftArrow", slot)
	verify_cell_highlight()
	keySend.keyPressAPI(rack, "upArrow", slot)
	
	# verify app transitions to channel when press select
	# beware of possible false positive if info banner for 205 shows up
	# first cell
	keySend.keyPressAPI(rack, "select", slot)
	verify_channel_tune()

	# second cell
	keySend.keyPressAPI(rack, "rightArrow", slot)
	keySend.keyPressAPI(rack, "select", slot)
	verify_channel_tune()
	
	# return to mix channel
	keySend.tune("205", rack, slot)
	keySend.keyPressAPI(rack, 'exit', slot)
	time.sleep(2)
	# internet connected, verify scoreguide
	
	keySend.keyPressAPI(rack, "red", slot)
	

	# detect combo mix
	keySend.keyPressAPI(rack, "downArrow", slot)
	stbt.wait_for_match('images/scoreguide_highlight.png')
	keySend.keyPressAPI(rack, "select", slot)
	stbt.wait_for_match('images/scoreguide_banner_hd.png')
	
	# verify scoreguide highlights
	stbt.wait_for_match('images/nba_highlight.png')
	keySend.keyPressAPI(rack, "downArrow", slot)
	print "test output:"+str(image_verified('images/scoreguide_minimize_highlight.png', 3))
	while not image_verified('images/scoreguide_minimize_gray.png', 3):
		keySend.keyPressAPI(rack, "downArrow", slot)
	
	print "test file executed and completed"


def verify_cell_highlight():
	#2 cells
	#stbt.wait_for_match('images/blue_cell_vertical.png')
	#stbt.wait_for_match('images/blue_cell_horizontal.png')
	
	#4 cells
	stbt.wait_for_match('images/blue_cell_highlight_vertical_4_cell.png')
	stbt.wait_for_match('images/blue_cell_highlight_horizontal_4_cell.png')
	print "blue cells detected"

def verify_channel_tune():
	# note: this only check if the info banner was detected, it does not validate the specific channel it was tuned to
	stbt.wait_for_match('images/info_banner_corner.png')
        keySend.keyPressAPI(rack, "prev", slot)
        time.sleep(6)

def image_verified(image, threshold):
	counter = 0
        for x in range(0, threshold):
		if stbt.detect_match(image).next().match:
			print "Detected True"
			counter += 1
		else:
			print "detected false"
	print "counter:"+str(counter)
	if counter < threshold:
		print "checked "+str(threshold)+"times did not find strong  match for image"
		return False
	else:
		return True
	

if __name__ == '__main__':
	main()