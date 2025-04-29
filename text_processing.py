chat_logs = [
    "My order is delayed",
    "I want to return my purchase",
    "The app is crashing frequently",
    "Payment issues, please help",
    "Need help with account recovery",
    "Delivery was incomplete",
    "Can't login to my account",
    "Having trouble with checkout",
    "My order was canceled"
]

# Step 1: Function to categorize issues
def categorize_issues(chat_logs):
    categories = {"Order": 0, "App": 0, "Payment": 0, "Account": 0, "Delivery": 0}
    for message in chat_logs:
        words = message.split(" ")
        for word in words:
            if "order" in word.lower() or "purchase" in word.lower():
                categories["Order"] += 1
            elif "app" in word.lower():
                categories["App"] += 1
            elif "payment" in word.lower() or "checkout" in word.lower():
                categories["Payment"] += 1
            elif "account" in word.lower():
                categories["Account"] += 1
            elif "delivery" in word.lower():
                categories["Delivery"] += 1
    return categories

def keyword_search(keyword, chat_logs):
    keyword = keyword.lower().strip()
    results = []
    for message in chat_logs:
        if keyword in message.lower():
            results.append(message)
    if results == []:
       print("Not found")
    return results

def Display_issues(chat_logs):
    categories = categorize_issues(chat_logs)
    print("Issue Categories:")
    for issue, number in categories.items():
        print(f"{issue}: {number}")
    while True:
      print()
      keyword = input("Enter a keyword to search in chat logs or type stop to exit ")
      if keyword.lower().strip() == "stop":
        print("Search Stopped")
        break
      else:
        results = keyword_search(keyword, chat_logs)
        print("Search Results:")
        for result in results:
          print(result)
        
      

Display_issues(chat_logs)
