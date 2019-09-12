import csv

total_votes = 0
results = {}

with open('02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv', newline='') as f:
    reader = csv.reader(f)

    # Voter Id, County, Candidate
    next(reader)

    # Loop over votes
    for row in reader:
        total_votes += 1
        candidate = row[-1]
        if candidate in results:
            current_vote_total = results[candidate]
            results[candidate] = current_vote_total + 1
        else:
            results[candidate] = 1

# Determine results

print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_votes))
print('-------------------------')

winner = None
winner_total_count = 0
for candidate,vote in results.items():
    percent_won = (vote / total_votes) * 100
    percent_display = '{:0.3f}'.format(percent_won)
    print(f'{candidate}: {percent_display}% ({vote})')

    if vote > winner_total_count:
        winner_total_count = vote
        winner = candidate

print('-------------------------')
print('Winner: ' + winner)
print('-------------------------')
