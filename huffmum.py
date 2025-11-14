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

# Main Function
if __name__ == "__main__":
    input_text = read_file()
    #print("Input Text:", input_text)

    frequency_table = build_frequency_table(input_text)
    print("Frequency Table:", frequency_table)
