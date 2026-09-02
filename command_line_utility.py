import argparse
import requests
parser = argparse.ArgumentParser(description="Image Downloader Utility with the help of url")
parser.add_argument("url", help="URL of the image to download")
parser.add_argument("-o","--output",help="Output file name (default: image.png)",default="image.png")
args=parser.parse_args()
response = requests.get(args.url)
with open(args.output, "wb") as f:   # 'wb' = write binary
    f.write(response.content)
print(f"Downloading image from {args.url} and saving as {args.output}")
#for running open power shell type  'python command_line_utility.py "https://www.example.com/image.png" -o "my_image.png"'