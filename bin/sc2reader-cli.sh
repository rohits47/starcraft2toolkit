#!/bin/bash

export DEFAULT_REPLAY_FILE="my_sample_replays/2020-07-05_T_grEEngLade_VS_P_Alucardkk.SC2Replay"

# python sc2reader/sc2reader/scripts/sc2printer.py --help

# print json of replay details
python sc2reader/sc2reader/scripts/sc2json.py $DEFAULT_REPLAY_FILE | jq
# python sc2reader/sc2reader/scripts/sc2replayer.py $DEFAULT_REPLAY_FILE

# print high-level game details
# python sc2reader/sc2reader/scripts/sc2printer.py $DEFAULT_REPLAY_FILE
