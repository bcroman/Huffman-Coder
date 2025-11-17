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
        with open("./dataset/koran.txt", "r") as text:
            input_text = text.read()
            return input_text
    except FileNotFoundError: #Error Handling for Missing File
        print("File not found!")
    

# Function to build the frequency table
def build_frequency_table(text):
    return Counter(text)

# Function to build the Huffman tree
def build_huffman_tree(frequency_table):
    priority_queue = [Node(char, freq) for char, freq in frequency_table.items()]
    heapq.heapify(priority_queue)

    # Build the tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]  # Return the root value

# Function to create hufffman codes
def create_codes(root: Node) -> dict:
    codes = {}

    def traverse(node, current_code):
        if node is None:
            return

        # Leaf node → store its code
        if node.char is not None:
            codes[node.char] = current_code
            return

        # Traverse left = add "0"
        traverse(node.left, current_code + "0")

        # Traverse right = add "1"
        traverse(node.right, current_code + "1")

    traverse(root, "")
    return codes

# Function to encode the input text
def encode_message(text: str, codes: dict) -> str:
    encoded = []
    # Encode each character
    for char in text:
        encoded.append(codes[char])
    return "".join(encoded)

# Function to get compression statistics
def compression_ratio(original_text: str, encoded_text: str) -> dict:
    original_text_size = len(original_text) * 8  # in ASCII
    encoded_text_size = len(encoded_text)  # in bits

    compression_ratio = original_text_size / encoded_text_size
    comp_percent = (original_text_size - encoded_text_size) / original_text_size * 100
    bits_saved = original_text_size - encoded_text_size
    avg_bits_per_char = encoded_text_size / len(original_text)

    compression_ratio = round(compression_ratio, 2)
    comp_percent = round(comp_percent, 2)
    avg_bits_per_char = round(avg_bits_per_char, 2)

    return {
        "original_bits": original_text_size,
        "encoded_bits": encoded_text_size,
        "compression_ratio": compression_ratio,
        "compression_percent_(%)": comp_percent,
        "bits_saved": bits_saved,
        "avg_bits_per_char": avg_bits_per_char
    }


# Main Function
if __name__ == "__main__":
    input_text = read_file()
    print("Input Text:", input_text)

    frequency_table = build_frequency_table(input_text)
    print("Frequency Table:", frequency_table)

    huffman_tree_root = build_huffman_tree(frequency_table)
    print (" Huffman Tree Root:", huffman_tree_root.freq)

    codes = create_codes(huffman_tree_root)

    print("\nHuffman Codes:")
    for char, code in codes.items():
        printable = char if char != " " else "[space]"
        print(f"{printable!r}: {code}")

    encoded_message = encode_message(input_text, codes)
    print("\nEncoded Message:")
    print(encoded_message)
    print("\nEncoded Message Length:", len(encoded_message), "bits")

    status = compression_ratio(input_text, encoded_message)
    print("\nCompression Statistics:")
    for key, value in status.items():
        print(f"{key.replace('_', ' ').title()}: {value}")



