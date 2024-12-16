import art

bidders_list = {}
print("Welcome to the Secret Auction!")
print(art.logo)

bid_is_running = True


# Function to find the highest bidder
def find_highest_bidder(bidders):
    winner = None
    highest_bid = 0
    for bidder in bidders:
        if highest_bid < bidders[bidder]:
            highest_bid = bidders[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Function to collect bidder info
def bidder_info():
    bidder = input("Bidder Name is:  ")
    bidder_bid = int(input("Bidder's Bid is:... $"))
    bidders_list[bidder] = bidder_bid
    print(f"{bidder} has bid ${bidder_bid}.")


# Main auction loop
while bid_is_running:
    bidder_info()
    print(bidders_list)
    continue_bidding = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n"
    ).lower()
    if continue_bidding == "no":
        bid_is_running = False


find_highest_bidder(bidders_list)
