from typing import List

from project import Category, Topic


class Document:
    id: int
    category_id: int
    topic_id: int
    file_name: str
    tags: List[str]

    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str) -> None:
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and self.id == o.id

    def __hash__(self) -> int:
        return hash(self.id)

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str) -> 'Document':
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str) -> None:
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str) -> None:
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name: str) -> None:
        self.file_name = file_name

    def __repr__(self) -> str:
        return f'Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {", ".join(self.tags)}'
