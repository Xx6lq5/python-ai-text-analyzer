# Simple AI Text Analyzer & Vocabulary Metrics
# Developed by Abdalrahman Adam

def analyze_text(text):
    words = text.split()
    word_count = len(words)
    
    # Extract basic statistics
    unique_words = set(words)
    vocab_richness = (len(unique_words) / word_count) * 100 if word_count > 0 else 0
    
    print("--- TEXT ANALYSIS REPORT ---")
    print(f"Total Words: {word_count}")
    print(f"Unique Words: {len(unique_words)}")
    print(f"Vocabulary Richness: {vocab_richness:.2f}%")
    print("----------------------------")

# Sample text input
sample_text = """
Artificial Intelligence and Computer Science are transforming the world. 
Learning Python allows developers to build smart applications, analyze data, 
and create generative AI tools that solve real-world problems efficiently.
"""

if __name__ == "__main__":
    analyze_text(sample_text)
