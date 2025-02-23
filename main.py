import sys
from stats import word_count, char_count, formatting

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    # The rest of your main() stays the same
    path = sys.argv[1]
    word_count(path)
    char_count(path)
    formatting(path)

if __name__ == "__main__":
    main()


  
    