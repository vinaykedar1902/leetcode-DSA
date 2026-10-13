class DoublyLinkedListNode:
    def __init__(self, key, value, prev: DoublyLinkedListNode=None, next: DoublyLinkedListNode=None, freq: int=1):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        self.freq = freq

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # Mapping between key and DoublyLinkedListNode value
        self.cache = {}

        # Mapping between frequencies of accessed nodes and end of linked list chain for the frequency
        self.freq_map = {}

        # Start of linked list chain will be after a dummy head node - Node to evict
        self.head = DoublyLinkedListNode(-1, -1, freq=-1)
        self.tail = DoublyLinkedListNode(-1, -1, freq=-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        self.updateLFU(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node: DoublyLinkedListNode = self.cache[key]
            node.value = value
            self.updateLFU(self.cache[key])
            return
            
        node = DoublyLinkedListNode(key, value)

        if self.size == self.capacity:
            self.evictNode()

        self.size += 1

        if 1 in self.freq_map:
            nodeToInsertAfter = self.freq_map[1]
        else:
            nodeToInsertAfter = self.head

        self.insertNode(nodeToInsertAfter, node)

        self.freq_map[1] = node
        self.cache[key] = node

    def evictNode(self):
        nodeToEvict: DoublyLinkedListNode = self.head.next

        if self.freq_map[nodeToEvict.freq] == nodeToEvict:
            del self.freq_map[nodeToEvict.freq]

        self.head.next = nodeToEvict.next
        nodeToEvict.next.prev = self.head

        self.size -= 1
        del self.cache[nodeToEvict.key]

    def insertNode(self, node_a: DoublyLinkedListNode, node_b: DoublyLinkedListNode):
        node_a.next.prev = node_b
        node_b.next = node_a.next
        node_a.next = node_b
        node_b.prev = node_a

    def updateLFU(self, node: DoublyLinkedListNode):
        if node.freq + 1 in self.freq_map:
            nodeToInsertAfter = self.freq_map[node.freq + 1]
        else:
            nodeToInsertAfter = self.freq_map[node.freq]
        
        self.freq_map[node.freq + 1] = node

        if self.freq_map[node.freq] == node:
            if node.prev.freq == node.freq:
                self.freq_map[node.freq] = node.prev
            else:
                del self.freq_map[node.freq]

        node.freq += 1

        if nodeToInsertAfter == node:
            return

        node.prev.next = node.next
        node.next.prev = node.prev

        self.insertNode(nodeToInsertAfter, node)