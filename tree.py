from exceptions import InvalidValueError

class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, val):
        if not isinstance(val, (int, float)):
            raise InvalidValueError()
        self.count += 1
        node = {"val": val, "left": None, "right": None}
        if self.root is None:
            self.root = node
            return
        curr = self.root
        while True:
            if val < curr["val"]:
                if curr["left"] is None:
                    curr["left"] = node; break
                curr = curr["left"]
            else:
                if curr["right"] is None:
                    curr["right"] = node; break
                curr = curr["right"]

    def _height(self, node):
        if node is None: return 0
        return 1 + max(self._height(node["left"]), self._height(node["right"]))

    def get_height(self):
        return self._height(self.root)

    def to_dict(self, node="__root__"):
        if node == "__root__": node = self.root
        if node is None: return None
        return {
            "val":   node["val"],
            "left":  self.to_dict(node["left"]),
            "right": self.to_dict(node["right"])
        }