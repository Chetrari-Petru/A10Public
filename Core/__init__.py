from Core.Repository.PlayTable import PlayTable

class Core:
    Table = None
    def __init__(self):
        pass

    def set_size(self, size):
        self.Table = PlayTable(size)

    def get_Table(self):
        return self.Table.grid