queue = []


def enqueue(item):
    queue.append(item)
    print(f"enqueue({item}): {queue}")


def dequeue():
    if not queue:
        print("dequeue: очередь пустая")
        return None
    item = queue.pop(0)
    print(f"dequeue() == {item}: {queue}")
    return item


enqueue(10)
enqueue(20)
enqueue(30)
dequeue()
enqueue(40)
dequeue()
dequeue()
dequeue()
dequeue()
