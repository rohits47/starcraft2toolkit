#!/bin/bash

export DEFAULT_REPLAY_FILE="my_sample_replays/sample_replay_TvP.SC2Replay"

# python sc2reader/sc2reader/scripts/sc2printer.py --help

# print json of replay details
python sc2reader/sc2reader/scripts/sc2json.py $DEFAULT_REPLAY_FILE | jq

# print high-level game details
# python sc2reader/sc2reader/scripts/sc2printer.py $DEFAULT_REPLAY_FILE
