#!/usr/bin/env python
import argparse
import datetime as D

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert timestamp to datetime')
    parser.add_argument('timestamp', metavar='N', type=int,
            help="Unix timestamp to convert.")

    args = parser.parse_args()
    print "Local: %s\n  UTC: %s" % (
            D.datetime.fromtimestamp(args.timestamp),
            D.datetime.utcfromtimestamp(args.timestamp))
