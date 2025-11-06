import heapq
import time

# Node for Huffman Tree
class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    def __lt__(self, other): return self.freq < other.freq

# Build Huffman Tree from frequency map
def build_tree(freq_map):
    heap = [Node(c, f) for c, f in freq_map.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        l, r = heapq.heappop(heap), heapq.heappop(heap)
        heapq.heappush(heap, Node(None, l.freq + r.freq, l, r))
    return heap[0]

# Generate Huffman Codes
def generate_codes(node, prefix='', code_map={}):
    if node:
        if node.char: code_map[node.char] = prefix
        generate_codes(node.left, prefix + '0', code_map)
        generate_codes(node.right, prefix + '1', code_map)
    return code_map

# Encode text
def encode(text, codes): return ''.join(codes[c] for c in text)

# Decode binary
def decode(bits, root):
    result, node = '', root
    for bit in bits:
        node = node.left if bit == '0' else node.right
        if node.char:
            result += node.char
            node = root
    return result

freqs = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}

# Get input first (user time not counted)
text = input("Enter text to encode (only a-f): ")

start_time = time.time()

root = build_tree(freqs)
codes = generate_codes(root)

sorted_chars = sorted(freqs.items(), key=lambda x: x[1])

print("Char\tFreq\tCode")
for c, f in sorted_chars:
    print(f"{c}\t{f}\t{codes[c]}")

encoded = encode(text, codes)
decoded = decode(encoded, root)

print(f"\nEncoded : {encoded}")
print(f"Decoded : {decoded}")

end_time = time.time()
print(f"\nTime taken : {end_time - start_time:.6f} seconds")

