import json
from pprint import pprint

import sc2reader

filename = "my_sample_replays/sample_replay_TvP.SC2Replay"
replay = sc2reader.load_replay(filename, load_map=True, load_level=4)
replay.load_map()
replay.load_all_details()
"""
>>> replay.
replay.active_units                 replay.is_private                   replay.plugins
replay.amm                          replay.length                       replay.practice
replay.archive                      replay.load_all_details(            replay.ranked
replay.attributes                   replay.load_attribute_events(       replay.raw_data
replay.base_build                   replay.load_details(                replay.real_length
replay.battle_net                   replay.load_game_events(            replay.real_type
replay.build                        replay.load_init_data(              replay.recorder
replay.category                     replay.load_level                   replay.region
replay.client                       replay.load_map(                    replay.register_datapack(
replay.clients                      replay.load_message_events(         replay.register_default_datapacks(
replay.competitive                  replay.load_players(                replay.register_default_readers(
replay.computer                     replay.load_tracker_events(         replay.register_reader(
replay.computers                    replay.logger                       replay.registered_datapacks
replay.cooperative                  replay.map                          replay.registered_readers
replay.datapack                     replay.map_file                     replay.release_string
replay.date                         replay.map_hash                     replay.resume_from_replay
replay.end_time                     replay.map_name                     replay.resume_method
replay.entities                     replay.marked_error                 replay.resume_user_info
replay.entity                       replay.message_events               replay.speed
replay.events                       replay.messages                     replay.start_time
replay.expansion                    replay.objects                      replay.team
replay.factory                      replay.observer                     replay.teams
replay.filehash                     replay.observers                    replay.time_zone
replay.filename                     replay.opt                          replay.tracker_events
replay.frames                       replay.packets                      replay.type
replay.game_events                  replay.people                       replay.unit
replay.game_fps                     replay.people_hash                  replay.units
replay.game_length                  replay.person                       replay.unix_timestamp
replay.game_type                    replay.pings                        replay.versions
replay.hero_duplicates_allowed      replay.player                       replay.windows_timestamp
replay.human                        replay.players                      replay.winner
replay.humans                       replay.plugin_failures
replay.is_ladder                    replay.plugin_result
>>> replay.
"""
