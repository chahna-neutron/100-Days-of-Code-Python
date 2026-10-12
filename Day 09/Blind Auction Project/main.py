# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
print(art.logo)

bids_info = {}

def highest_bidder(bids):
    winner=""
    highest_bid = 0
    for person in bids:
        bid_amount=bids[person]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner=person
    print (f"The Winner is {winner} With a bid of ${highest_bid}")

continue_bidding=True

while continue_bidding:
    name = input("What is your name? :")
    bid_Price = int(input("What is your bid? :$"))
    bids_info[name]=bid_Price
    should_continue = input("Are there any other bidders? ( Type 'yes' or 'no')\n").lower()
    if should_continue == "no":
       continue_bidding = False
       highest_bidder(bids_info)
    elif should_continue == "yes":
        print("\n"*100)

