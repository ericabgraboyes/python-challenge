# import required modules to read csv
import os
import csv

# create variables for list set up
candidates_running = []
county = []
votes = []
percentage = []
winner_name = ''
candidate_votes = dict()
results = []

# read in csv file
csvpath = os.path.join('.','Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read the header row in first
    csv_header = next(csvreader)

    for row in csvreader:
        if row[2] not in candidates_running:
            candidates_running.append(row[2])

        # create nested list - contains candidate & county associated with vote
        votes.append([row[2], row[1]])

    # create variable to store number of total votes -- used for % calculation
    total_votes = len(votes)

    # initialize an empty dictionary for each distinct candidate
    for candidate in candidates_running:
        candidate_votes[candidate] = dict()

    for vote in votes:
        candidate_name = vote[0]
        county_name = vote[1]
        
        # if county exists in candidate dictionary, increment the value
        if county_name in candidate_votes[candidate_name]:
            candidate_votes[candidate_name][county_name] += 1
        else:
            # add county key to candidate dictionary
            candidate_counties = candidate_votes[candidate_name]
            candidate_counties[county_name] = 1
    
    def total_by_candidate():
        # create variable to determine which candidate has the most votes (combined across counties). Calculate candidate % of votes (of total) 
        most_votes = 0

        for candidate, county in candidate_votes.items():
            candidate_total = 0
    
            for key in county:
                candidate_total += int(county[key])

            if candidate_total > most_votes:
                most_votes = candidate_total
                winner_name = candidate 
            
            percentage = (candidate_total / total_votes) * 100
            percentage = str(round(percentage,3))+"%"

            results_str = candidate + ": " + percentage + " " + "("+str(candidate_total)+")"
            results.append(results_str)

        results.append("-------------------------")

        winner_name = "Winner: " + winner_name
        
        results.append(winner_name)

        return(results)

election_results = total_by_candidate()

# Print results to Terminal
print("Election Results")
print("-" * 25)
print(f"Total Votes: {total_votes}") 
print("-" * 25)
for each in election_results:
    print(each)
print("-" * 25)

# write summary of analysis to text file
output_file = os.path.join('.','Analysis', 'Election Results.txt')
with open(output_file, 'w', newline='') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("-------------------------")    
    for each in election_results:
        text.write('\n%s' % each)

