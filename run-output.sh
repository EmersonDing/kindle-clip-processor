cp /Volumes/Kindle/documents/My\ Clippings.txt resource/clip.txt

python3 kindle_clipper_processor.py -d $1

open resource/output.txt
