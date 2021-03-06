#!/usr/bin/env python3
import sys
import os.path
import induce.track as track
import pickle

if __name__ == "__main__":
    fin = sys.stdin.buffer if len(sys.argv) < 2 else open(sys.argv[1], 'rb')
    fout = sys.stdout.buffer if len(sys.argv) < 2 else open("%s.tmp" % sys.argv[1], 'wb')
    o = track.FrameIter(fin)
    tracker = None
    traces = []
    # this is a single input.
    for i in o:
        event = i['event']
        if event in ['start']:
            inp, ins = i['$input']
            tracker = track.Tracker(inp, ins)
        elif event in ['stop']:
            traces.append((tracker.vars.i, tracker.vars.ins, tracker.vars.defs))
        else:
            tracker.track(i)
    pickle.dump(traces, fout)
