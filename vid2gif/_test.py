#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from moviepy.editor import *


def main(argv=None):
    #clip = VideoFileClip("./rw.mp4").\
    #    subclip(5, 6).\
    #    speedx(0.5)
    clip = VideoFileClip("./rw.mp4").subclip(0,10).resize(.75)
    CompositeVideoClip([clip]).to_gif('rw.gif', fps=12, verbose=False)

    #snapshot = anna_olaf.\
        #crop(x2=anna_olaf.w/2).\
        #to_ImageClip(0.2).\
        #set_duration(anna_olaf.duration)

    #CompositeVideoClip([anna_olaf, snapshot]).\
        #to_gif('anna_olaf.gif', fps=15)
    sys.exit(0)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

# vim: filetype=python
