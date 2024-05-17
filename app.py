#def simple_chatbot(user_query):
 #   if user_query == "What is the total revenue?":
  #      return "The total revenue is [amount]."
   # elif user_query == "How has net income changed over the last year?":
    #    return "The net income has [increased/decreased] by [amount] over the last year."
   # elif user_query == "What are the total assets?":
   
   #     return "The total assets are [amount]."
   # elif user_query == "What are the total liabilities?":
    #    return "The total liabilities are [amount]."
    #elif user_query == "What is the cash flow from operating activities?":
     #   return "The cash flow from operating activities is [amount]."
    #else:
    #    return "Sorry, I can only provide information on predefined queries."

def financial_chatbot(query):
    responses = {
        "net income": "The net income for the fiscal year 2021 was $5 billion, a 10% increase from 2020.",
        "revenue growth": "The revenue grew by 8% from 2020 to 2021, reaching $22 billion.",
        "total assets": "The total assets for the fiscal year 2021 were $50 billion.",
        "total liabilities": "The total liabilities for the fiscal year 2021 were $20 billion.",
        "cash flow from operating activities": "The cash flow from operating activities for the fiscal year 2021 was $10 billion."
    }
    return responses.get(query.lower(), "I'm not sure how to answer that. Can you try a different question?")

# Main function for user interaction
def main():
    while True:
        user_input = input("What would you like to know? ").strip()

        # Check if it's a predefined query for financial chatbot
        if user_input.lower() in ["net income", "revenue growth", "total assets", "total liabilities", "cash flow from operating activities", "cash flow"]:
            print(financial_chatbot(user_input))
        else:
           # print(simple_chatbot(user_input))
           return

        cont = input("Do you want to ask something else? (yes/no): ").lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()
