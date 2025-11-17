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

# Function to display menu and options
def menu():
    print("Huffman Coding Compression:")
    print("1. Print Input Text")
    print("2. Frequency Table")
    print("3. Huffman Codes")
    print("4. Encoded Message")
    print("5. Compression Statistics")
    print("6. Exit")



# Main Function
if __name__ == "__main__":
    input_text = read_file()
    frequency_table = build_frequency_table(input_text)
    huffman_tree_root = build_huffman_tree(frequency_table)
    codes = create_codes(huffman_tree_root)
    encoded_message = encode_message(input_text, codes)
    status = compression_ratio(input_text, encoded_message)

    # Display Menu
    menu()

    # User Interaction Loop
    while True:
        choice = input("\nEnter your choice (1-6): ")
        if choice == '1':
            print("\nInput Text:\n", input_text)
        elif choice == '2':
            print("\nFrequency Table:")
            for char, freq in frequency_table.items():
                print(f"'{char}': {freq}")
        elif choice == '3':
            print("\nHuffman Codes:")
            for char, code in codes.items():
                print(f"'{char}': {code}")
        elif choice == '4':
            print("\nEncoded Message:\n", encoded_message)
            print(f"\nTotal bits in encoded message: {len(encoded_message)}")
        elif choice == '5':
            print("\nCompression Statistics:")
            for key, value in status.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")