from typing import List

from project import Category, Document, Topic


class Storage:
    categories: List[Category]
    topics: List[Topic]
    documents: List[Document]

    def __init__(self) -> None:
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        for c in self.categories:
            if c.id == category_id:
                c.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        for t in self.topics:
            if t.id == topic_id:
                t.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        for d in self.documents:
            if d.id == document_id:
                d.edit(new_file_name)

    def delete_category(self, category_id) -> None:
        for c in self.categories:
            if c.id == category_id:
                self.categories.remove(c)

    def delete_topic(self, topic_id) -> None:
        for t in self.topics:
            if t.id == topic_id:
                self.topics.remove(t)

    def delete_document(self, document_id) -> None:
        for d in self.documents:
            if d.id == document_id:
                self.documents.remove(d)

    def get_document(self, document_id) -> Document:
        for d in self.documents:
            if d.id == document_id:
                return d

    def __repr__(self) -> str:
        message = []
        NL = '\n'

        for d in self.documents:
            message.append(repr(d))

        return NL.join(message)
