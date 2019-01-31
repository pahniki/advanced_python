"""Metaclass for properties generation"""


class MetaAccessors(type):
    """Metaclass for properties generation"""

    def __init__(self, cls_name: str, parents: tuple, cls_dict: dict):
        super().__init__(cls_name, parents, cls_dict)

        patterns = ("get_", "set_", "del_")
        prop_data = dict()

        # Collect method names that starts with pattern into prop_data dict
        for attr_name in cls_dict.keys():
            for ind, pattern in enumerate(patterns):
                if attr_name.startswith(pattern):
                    var = attr_name[4:]
                    if var not in prop_data:
                        prop_data[var] = [None, None, None]
                    prop_data[var][ind] = getattr(self, attr_name)

        for prop_name, accessors in prop_data.items():
            setattr(self, prop_name, property(*accessors))


class A(metaclass=MetaAccessors):
    """Working class"""

    def __init__(self):
        self._x = None
        self._y = "y"
        self._z = None

    def get_x(self):
        """x getter"""
        print(self._x)
        return self._x

    def set_x(self, value):
        """x setter"""
        self._x = value

    def del_x(self):
        """x deliter"""
        print("deller x")
        del self._x

    def get_y(self):
        """y getter"""
        print(self._y)
        return self._y

    def set_z(self, value):
        """z setter"""
        self._z = value


if __name__ == '__main__':
    a = A()

    a.x
    a.x = "ssss"
    a.x

    a.y

    del a.x

    a.z = "lola"
    print(a._z)
