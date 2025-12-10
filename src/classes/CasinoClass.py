from collections.Chip import ChipCollection
from collections.Goose import GooseCollection
from collections.Player import PlayerCollection


class Casino():
    def __init__(self, chip_collection: ChipCollection, goose_collection: GooseCollection, player_collection: PlayerCollection):
        self.chip_collection = chip_collection
        self.goose_collection = goose_collection
        self.player_collection = player_collection
