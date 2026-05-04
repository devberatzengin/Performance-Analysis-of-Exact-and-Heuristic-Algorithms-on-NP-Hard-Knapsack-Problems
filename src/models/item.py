class Item:
    def __init__(self, id: int, value: int, weight: int):
        self.id = id
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Sezgisel yaklaşımlarda yoğunluk (density) gerekebilir

    def __repr__(self):
        return f"Item(ID: {self.id}, V: {self.value}, W: {self.weight})"