def calculate_profit(qual_bet_stake, qual_bet_odds, lay_bet_odds, commission_rate, free_bet_stake, odds_type):
    if odds_type.lower() == 'american':
        # Convert American odds to decimal odds
        if qual_bet_odds > 0:
            qual_bet_odds = (qual_bet_odds / 100) + 1
        else:
            qual_bet_odds = (100 / abs(qual_bet_odds)) + 1

        if lay_bet_odds > 0:
            lay_bet_odds = (lay_bet_odds / 100) + 1
        else:
            lay_bet_odds = (100 / abs(lay_bet_odds)) + 1

    # Calculate qualifying bet's potential outcomes
    qual_bet_return = qual_bet_stake * qual_bet_odds
    qual_bet_loss = qual_bet_stake

    # Calculate lay bet's potential outcomes considering commission
    lay_bet_liability = qual_bet_stake * (lay_bet_odds - 1) / (1 - commission_rate)

    # Calculate profit/loss from the lay bet
    lay_bet_return = free_bet_stake
    lay_bet_profit = lay_bet_return - lay_bet_liability

    # Calculate total profit or loss
    total_profit = lay_bet_profit - qual_bet_loss

    return total_profit


# Ask for odds type selection and display descriptions for input prompts based on the chosen odds type
while True:
    print("Odds Types:")
    print("1. European (Decimal) Odds: Represent the potential return, including the stake, for a 1-unit bet.")
    print("2. American (Moneyline) Odds: Indicate how much profit you would make on a 100-unit bet if it wins.")
    odds_type = input("Enter the number for the desired Odds Type (1 or 2): ")
    if odds_type in ['1', '2']:
        break
    else:
        print("Invalid input. Please enter 1 or 2.")

# Get user input for bet details with respective descriptions
print("\nThis is the amount of money you're placing as a stake on your initial bet to qualify for a promotion or bonus offered by the bookmaker.")
qualifying_bet_stake = float(input("Enter Qualifying Bet Stake (Amount placed for the initial bet): $"))

print("\nInput the odds provided by the bookmaker for the outcome of the qualifying bet in decimal format. \nDecimal odds represent the potential return, including the stake, for each unit bet. (For example: 1.65 = $165")
qualifying_bet_odds = float(input("Enter Qualifying Bet Odds (Decimal or American, depending on your choice): "))

print("\nThis refers to the odds offered on a betting exchange for the opposite outcome of your qualifying bet, expressed in decimal format. \nIt's the odds you'll use to lay against your qualifying bet.")
lay_bet_odds = float(input("Enter Lay Bet Odds (Decimal or American, based on the chosen odds type): "))

print("\nFor betting exchanges like Betfair, there's usually a commission charged on net winnings. Enter this as a decimal (e.g., 0.05 for 5% commission).")
commission_rate = float(input("Enter Commission Rate (in decimal form, e.g., 0.05 for 5%): "))

print("\nIf the bookmaker offers a free bet as part of the promotion, this is the amount of money you're using for the free bet.")
free_bet_stake = float(input("Enter Free Bet Stake (Amount for the free bet): $"))

# Calculate potential profit
profit = calculate_profit(qualifying_bet_stake, qualifying_bet_odds, lay_bet_odds, commission_rate, free_bet_stake, odds_type)
print(f"\nPotential profit: ${profit:.2f}")
