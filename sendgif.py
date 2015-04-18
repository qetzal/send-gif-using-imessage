#!/usr/bin/env python

import requests,json,os,argparse

parser = argparse.ArgumentParser()
parser.add_argument("to", help="Phone number or email that supports iMessage.")
parser.add_argument("-t", "--tag", help="Set Giphy tag. Default tag is 'cats'.")
args = parser.parse_args()

if not args.tag:
	GIPHY_TAG = 'cats'
else: 
	GIPHY_TAG = args.tag

BUDDY = args.to

r = requests.get('http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=' + GIPHY_TAG)
result = json.loads(r.text)
gif_url = result['data']['image_original_url']

gif = requests.get(gif_url)


gif_file = open('giphy.gif', 'w')
gif_file.write(gif.content)
gif_file.close()


gif_file_path = os.path.dirname(os.path.realpath(__file__)) + '/giphy.gif'



cmd = """osascript<<END
set theAttachment to POSIX file "{0}"
tell application "Messages"
	tell application "Messages"
		set targetService to 1st service whose service type = iMessage
		set targetBuddy to buddy "{1}" of targetService
		send theAttachment to targetBuddy
	end tell
end tell
END"""

cmd = cmd.format(gif_file_path,BUDDY)


os.system(cmd)