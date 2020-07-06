"""
sc2toolkit main class
"""
import fire
import os
from pprint import pprint

# os.environ['SC2READER_CACHE_DIR'] = "sc2reader_cache"
# os.environ['SC2READER_CACHE_MAX_SIZE'] = "100"
import sc2reader

# from sc2reader.engine.plugins import SelectionTracker, APMTracker
# register plugins with game engine
# sc2reader.engine.register_plugin(SelectionTracker())
# sc2reader.engine.register_plugin(APMTracker())


class Starcraft2Toolkit:
    """
    The main toolkit object acts as the entrypoint for most commonly
    used operations.
    """

    def __init__(self, filename="my_sample_replays/sample_replay_TvP.SC2Replay"):
        self._filename = filename
        # self._replay_dir = "my_sample_replays"
        self._replay = None
        self.load_level = 4

    @property
    def replay(self):
        if not self._replay:
            self._replay = sc2reader.load_replay(
                self._filename, load_map=True, load_level=self.load_level
            )
            self._replay.load_map()
            self._replay.load_all_details()
        return self._replay

    def run(self):
        # print(self.replay)
        # print(self.replay.game_events)
        print(dir(self.replay))


def main():
    fire.Fire(Starcraft2Toolkit)


if __name__ == "__main__":
    main()
