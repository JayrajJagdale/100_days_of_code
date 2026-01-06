import art

print(art.logo)

data_dict = {}
should_continue = True

def find_higst_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner += bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    data_dict[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    if other_bidders == 'no':
        should_continue = False
        find_higst_bidder(data_dict)
        
    else:
        print("\n" * 100)




# def calulate_high_bid():
#             max_value = 0
#             for key in data_dict:
#                 if data_dict[key] > max_value:
#                     max_value = data_dict[key]
#             print(f"The winner is {key} with a bid of ${max_value} ")

