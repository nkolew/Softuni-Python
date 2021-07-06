@classmethod
def _get_next_id(cls) -> int:
    return cls._id


def _generic_init(self, *args) -> None:
    attributes = self.__annotations__
    for attr, value in zip(attributes, args):
        setattr(self, attr, value)

    self.id = self.__class__._id
    self.__class__._id += 1


def gym_dataclass(attributes, repr_format):
    class_ = type('_', (), {})
    class_._id = 1
    class_.__init__ = _generic_init
    class_.get_next_id = _get_next_id
    class_.__annotations__ = attributes

    def _generic_repr(self):
        return repr_format.format(self=self)
    class_.__repr__ = _generic_repr

    return class_
