"""
sc2toolkit main class
"""
import fire

import sc2reader


class Starcraft2Toolkit:
    """
    The main toolkit object acts as the entrypoint for most commonly
    used operations.
    """
    def __init__(self, filename):
        self._filename = filename
        self._replay_dir = None
        self.replay = None
        self.load_level = 4

    def load(self):
        self.replay = sc2reader.load_replay(self._filename,
                                            load_level=self.load_level)

    def summarize(self):
        self.load()
        # print(self.replay)


def main():
    fire.Fire(Starcraft2Toolkit)


if __name__ == '__main__':
    main()
