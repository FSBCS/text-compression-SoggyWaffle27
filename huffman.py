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
        if self.encoded_text != None:
            output = ""
            dict = self._build_dictionary(self.root)
            dict = {v: k for k, v in dict.items()}
            substring = ""
            for char in str(self.encoded_text):
                substring += char
                if substring in dict:
                    output += dict[substring]
                    substring = ""
            self.decoded_text = output
        else:
            out = ""
            items = self.frequency(self.src)
            PQ = self.PriorityQueue()
            for i in items:  #yeah so I forgot we had a PQ and I had already made my own so I just repurposed it
                PQ.insert(self.Node(i[0], i[1]))
            while len(PQ.queue) != 2:
                min1 = PQ.findMin()[0]
                min2 = PQ.findMin()[0]
                PQ.insert(self.Node(freq = (min1.freq + min2.freq), left=min2, right=min1))
            self.root = PQ.queue[1]
            dict = self._build_dictionary()
            for i in self.src:
                out += dict[i]
            self.encoded_text = out

    class Node:
        def __init__(self, freq, char=None, left=None, right=None):
            self.char = char
            self.freq = freq
            self.left = left 
            self.right = right 
        
        def is_leaf(self):
            return self.char is not None
            
    def frequency(self, str):
        dict = {}
        for char in str:
            dict[char] = dict.get(char,0) + 1
        dict = sorted(dict.items(), key=lambda item: item[1], reverse = True)
        dict = [(v, k) for k, v in dict[::-1]]
        return dict
    
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
        return self.root
    
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
            if self.queue[parent].freq <= self.queue[n].freq:
                self.queue[parent], self.queue[n] = self.queue[n], self.queue[parent]
                self.swap(parent)
            return
        def findMin(self):
            min, c = (self.queue[-1], -1), 0
            for i in self.queue:
                if i == "":
                    pass
                elif min[1] >= i.freq:
                    min = i, c
                c += 1
            del(self.queue[min[1]])
            return min
            
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
file_path = os.path.join(os.path.dirname(__file__), 'test_data', 'totc.txt')
with open(file_path, 'r') as file:
    contents = file.read()

encoding = HuffmanEncoding(src = contents)
print("\nLength Test:\n", " - Encoded text length:", len(encoding.encoded_text), "\n  - ASCII text length:", len(contents) * 8 , "\n") #Huffman vs ASCII
decode = HuffmanEncoding(encoded_text = encoding.encoded_text, root = encoding.root)
print(decode.decoded_text)