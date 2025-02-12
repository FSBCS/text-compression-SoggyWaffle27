from friendsbalt.acs import MinPQ

class HuffmanEncoding:
    def __init__(self, src=None, encoded_text=None, root=None):
        """
        Initializes a new Huffman Encoding. Either source text or encoded text and root must be provided.
        If source text is provided, it builds the Huffman tree and dictionary, and encodes the text.
        If encoded text and root are provided, it decodes the text.
        Args:
            src (str, optional): The source text to be encoded.
            encoded_text (str, optional): The encoded text to be decoded.
            root (Node, optional): The root node of the Huffman tree for decoding.
        """
        self.src = src
        self.encoded_text = encoded_text
        self.root = root
        if self.encoded_text == None:
            pass #decode text
        else:
            self.encoding()
    ####################
    class Node:
        def __init__(self, freq, char=None, left=None, right=None):
            self.char = char
            self.freq = freq
            self.left = left
            self.right = right
        
        def is_leaf(self):
            return self.char is not None
    ####################
    def encoding(self, str = ""):
        items = self.frequency(self.src)
        PQ = self.PriorityQueue()
        for i in items:  #yeah so I forgot we had a PQ and I had already made my own so I just repurposed it
            PQ.insert(i)
        while True:
            min1 = PQ.findMin()
            min2 = PQ.findMin()
            
        return
    
    def frequency(self, str):
        dict = {}
        for i in str:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        return sorted(dict.items(), key=lambda item: item[1], reverse = True)
    
    def source_text(self):
        """
        Returns the original source text.
        Returns:
            str: The original source text.
        """
        pass

    def root(self):
        """
        Returns the root node of the Huffman tree.
        Returns:
            Node: The root node of the Huffman tree.
        """
        pass
    
    def _build_dictionary(self, node=None, prefix=''):
        """
        Recursively builds a dictionary that maps characters to their corresponding
        Huffman codes based on the Huffman tree.
        Args:
            node (Node, optional): The current node in the Huffman tree. Defaults to None,
                                   which means the function will start from the root node.
            prefix (str, optional): The current Huffman code prefix. Defaults to an empty string.
        Returns:
            dict: A dictionary where keys are characters and values are their corresponding
                  Huffman codes.
        """
        if node is None:
            node = self.root
        
        if node.char is not None:
            return {node.char: prefix}
        
        dictionary = {}
        dictionary.update(self._build_dictionary(node.left, prefix + '0'))
        dictionary.update(self._build_dictionary(node.right, prefix + '1'))
        return dictionary
    
    class PriorityQueue():
        def __init__(self):
            self.queue = [""]
        def parent(self, n):
            return n // 2
        def children(self, n):
            return n * 2, n * 2 + 1 
        def insert(self, n):
            self.queue.append(n)
            self.swap(len(self.queue)-1)
        def swap(self, n):
            parent = self.parent(n)
            if self.queue[parent] == "":
                return
            if self.queue[parent][1] < self.queue[n][1]:
                self.queue[parent], self.queue[n] = self.queue[n], self.queue[parent]
                self.swap(parent)
            return
        def findMin(self):
            min, c = (self.queue[-1], -1), 0
            for i in self.queue:
                if i == "":
                    pass
                elif min[1] >= i[1]:
                    min = i, c
                c += 1
            del(self.queue[min[1]])
            return min
        def display(self):
            print(self.queue)
H = HuffmanEncoding("AAAAABBBBCCCDDE")
print(H.encoding())