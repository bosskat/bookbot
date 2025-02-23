def get_book_text(path):
  with open(path) as f:
    text = f.read().lower()
  return text

def word_count(path):
  text = get_book_text(path)
  num_words = len(text.split())
  return f"Found {num_words} total words"

def char_count(path):
  text = get_book_text(path)
  char_dict = {}
  for char in text:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1
  return char_dict

def sort_on(item):
   # Changed 'dict' to 'item' and accessed 'num' key directly
   return item["num"]
   
def report(path):
  dictionary = char_count(path)
  result = []  # Renamed 'list' to 'result'
  
  for char, count in dictionary.items():
    if char.isalpha():
      result.append({"character": char, "num": count})  
  result.sort(reverse=True, key=sort_on)
  return result

# Print the result
# print(report())


def formatting(path):
  num_words = word_count(path)
  dictionary_list = report(path)
  new_list = [{d['character']: d['num']} for d in dictionary_list]

  
  
  print("============ BOOKBOT ============\n")
  print("Analyzing book found at books/frankenstein.txt...\n")
  print("----------- Word Count ----------\n")
  print(f"{num_words}\n")
  print("--------- Character Count -------\n")
  
  for dictionary in new_list:
    # Use the .items() method to get key-value pairs
    for key, value in dictionary.items(): 
        # Directly print the key and value from the loop variables
        print(f"{key}: {value}")
  print("============= END ===============")
   


    




 
 
  
