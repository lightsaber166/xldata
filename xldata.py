import dill
import random

datpack_ids = set()

class Datpack:
    def __init__(self, id=''):
        self.values = []
        self.subpacks = []
        if id:
            self.id = id
        else:
            while True:
                new_id = random.randint(1000000000, 9999999999)
                if new_id not in datpack_ids:
                    self.id = new_id
                    break
            datpack_ids.add(self.id)

    def save(self, file):
        with open(file, 'wb') as f:
            dill.dump(self, f)

    @classmethod
    def load(cls, file):
        with open(file, 'rb') as f:
            return dill.load(f)

    def get_id(self):
        return self.id

    def add_value(self, value):
        self.values.append(value)

    def add_subpack(self, subpack):
        self.subpacks.append(subpack)

    def change_id(self, new_id):
        if not new_id:
            while True:
                new_id = random.randint(1000000000, 9999999999)
                if new_id not in datpack_ids:
                    self.id = new_id
                    break
        elif len(new_id) != 10 or not new_id.isdigit():
            return 'Datapack IDs should be 10-digit integers.'
        else:
            datpack_ids.discard(self.id)
            self.id = new_id
            datpack_ids.add(self.id)
