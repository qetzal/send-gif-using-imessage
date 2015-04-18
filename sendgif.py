#!/usr/bin/env python

import requests,json,os,argparse,sys

parser = argparse.ArgumentParser()
parser.add_argument("to", help="Phone number or email that supports iMessage.")
parser.add_argument("-t", "--tag", help="Set Giphy tag. Default tag is 'cats'.")
args = parser.parse_args()

if not args.tag:
	GIPHY_TAG = 'cats'
else: 
	GIPHY_TAG = args.tag

BUDDY = args.to

print("Starting")

r = requests.get('http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=' + GIPHY_TAG)

print("Found awesome GIF")

result = json.loads(r.text)
gif_url = result['data']['image_original_url']


file_name = "giphy.gif"
with open(file_name, "wb") as f:
        response = requests.get(gif_url, stream=True)
        total_length = response.headers.get('content-length')
        mb = float(total_length) / 1048576
        print('Downloading ' + str(round(mb,2)) + 'Mb..')
        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)

            for data in response.iter_content(100000):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()

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

print("\nSending..")
cmd = cmd.format(gif_file_path,BUDDY)

os.system(cmd)