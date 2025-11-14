# Add Necessary 
import heapq
from collections import Counter

# Class for Huffman Tree Node
class Node:
    # Initialize Node
    def __init__(self, char, freq, left=None, right=None):
        self.char = char      # character (None for internal nodes)
        self.freq = freq      # frequency
        self.left = left      # left child
        self.right = right    # right child

    # define comparison for priority queue (heapq)
    def __lt__(self, other):
        return self.freq < other.freq


# Function to read txt file and output message
def read_file():
    try: # Read File
        with open("./dataset/demofile.txt", "r") as text:
            input_text = text.read()
    except FileNotFoundError: #Error Handling for Missing File
        print("File not found!")
    return input_text

# Function to build the frequency table
def build_frequency_table(text):
    return Counter(text)

# Function to build the Huffman tree
def build_huffman_tree(frequency_table):
    priority_queue = [Node(char, freq) for char, freq in frequency_table.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]  # Root of the Huffman Tree

# Main Function
if __name__ == "__main__":
    input_text = read_file()
    print("Input Text:", input_text)

    frequency_table = build_frequency_table(input_text)
    print("Frequency Table:", frequency_table)

    huffman_tree_root = build_huffman_tree(frequency_table)
    print (" Huffman Tree Root:", huffman_tree_root.freq)
