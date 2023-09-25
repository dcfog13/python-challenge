import os
import csv

# Read CSV file
pypoll_csv = os.path.join("Resources", "election_data.csv")
with open(pypoll_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    # Skip header
    csv_header = next(csv_file)

    # Declare variables
    total_votes = 0
    stockham_votes = 0
    degette_votes = 0
    doane_votes = 0
    
    # Read through file
    for row in csv_reader:
        # Find total number of votes
        total_votes += 1
        # Find total votes for Stockham
        if row[2] == "Charles Casper Stockham":
            stockham_votes += 1
        # Find total votes for DeGette
        elif row[2] == "Diana DeGette":
            degette_votes += 1
        # Find total votes for Doane
        elif row[2] == "Raymon Anthony Doane":    
            doane_votes += 1
            
    # Calculate vote percentages
    stockham_percentage = (stockham_votes/total_votes)*100
    degette_percentage = (degette_votes/total_votes)*100
    doane_percentage = (doane_votes/total_votes)*100
    
    # Find election winner
    most_votes = max(stockham_votes,degette_votes,doane_votes)
    if most_votes == stockham_votes:
        winner = "Charles Casper Stockham"
    elif most_votes == degette_votes:
        winner = "Diana DeGette"
    elif most_votes == doane_votes:
        winner = "Raymon Anthony Doane"
    
    # Print results to terminal
    print(f"\nElection Results\n\n----------------------------\n")
    print(f"Total Votes: {total_votes}\n\n----------------------------\n")
    print(f"Charles Casper Stockham: {stockham_percentage:.3f}% ({stockham_votes})\n")
    print(f"Diana DeGette: {degette_percentage:.3f}% ({degette_votes})\n")
    print(f"Raymon Anthony Doane: {doane_percentage:.3f}% ({doane_votes})\n")
    print(f"----------------------------\n\nWinner: {winner}\n\n----------------------------")
    
    # Print results to output file
    pypoll_results = os.path.join("analysis","pypoll_results.txt")
    with open(pypoll_results, 'w') as results_file:
        results_file.write(f"\nElection Results\n\n----------------------------\n\nTotal Votes: {total_votes}\n\n----------------------------\n\nCharles Casper Stockham: {stockham_percentage:.3f}% ({stockham_votes})\n\nDiana DeGette: {degette_percentage:.3f}% ({degette_votes})\n\nRaymon Anthony Doane: {doane_percentage:.3f}% ({doane_votes})\n\n----------------------------\n\nWinner: {winner}\n\n----------------------------")