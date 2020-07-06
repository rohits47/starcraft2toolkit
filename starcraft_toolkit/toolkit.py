"""
sc2toolkit main class
"""
import fire
from pprint import pprint

import sc2reader
from sc2reader.engine.plugins import SelectionTracker, APMTracker

# register plugins with game engine
# sc2reader.engine.register_plugin(SelectionTracker())
# sc2reader.engine.register_plugin(APMTracker())


class Starcraft2Toolkit:
    """
    The main toolkit object acts as the entrypoint for most commonly
    used operations.
    """
    def __init__(self,
                 filename="my_sample_replays/sample_replay_TvP.SC2Replay"):
        self._filename = filename
        self._replay_dir = "my_sample_replays"
        self.replay = None
        self.load_level = 4

    def load(self):
        self.replay = sc2reader.load_replay(self._filename,
                                            load_map=True,
                                            load_level=self.load_level)
        self.replay.load_map()
        self.replay.load_all_details()

    def summarize(self):
        self.load()
        # print(self.replay)
        print(self.replay.game_events)


def main():
    fire.Fire(Starcraft2Toolkit)


if __name__ == '__main__':
    main()
