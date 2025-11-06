import heapq, time

def huffman(freq):
    q = [[f, [c, ""]] for c, f in freq.items()]
    heapq.heapify(q)
    while len(q) > 1:
        a, b = heapq.heappop(q), heapq.heappop(q)
        for x in a[1:]: x[1] = '0' + x[1]
        for x in b[1:]: x[1] = '1' + x[1]
        heapq.heappush(q, [a[0] + b[0]] + a[1:] + b[1:])
    return dict(heapq.heappop(q)[1:])

# --- Input frequencies ---
n = int(input("Enter number of characters: "))
freq = {}
for _ in range(n):
    ch = input("Enter character: ")
    f = int(input(f"Enter frequency of '{ch}': "))
    freq[ch] = f

# --- Build Huffman Codes ---
start = time.time()
codes = huffman(freq)
end = time.time()

print("\nHuffman Codes:")
for ch, code in codes.items():
    print(f"{ch}: {code}")

# --- Encode text ---
text = input("\nEnter text to encode: ")
encoded = ''.join(codes[c] for c in text)

# format to show normal decimal time
time_taken = format(end - start, '.6f')

print("\nEncoded Text:", encoded)
print("Time Taken:", time_taken, "seconds")