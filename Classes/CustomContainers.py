class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
print(cloud.__tags)


class ListCloud:
    def __init__(self):
        self.__list = []

    def add(self, item):
        self.__list.append(item)

    def __getitem__(self, index):
        return self.__list[index]

    def __str__(self):
        return f"{self.__list}"


list = ListCloud()
list.add(0)
list.add(1)

x = list[1]


print(list)
print(x)
