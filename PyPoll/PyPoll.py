import os
import csv

election_csv = os.path.join("..","Resources_PyPoll","election_data.csv")

print("Election results:")
print("-----------------------------------------------")

vote_count = 0
total_number = 0
candidate_count = {}

def election_data(election_csv):
    '''
    Put description describing function
    '''
    voter_id = int(election_csv[0])
    county = str(election_csv[1])
    candidate = str(election_csv[2])
    return (candidate,voter_id,county)

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader: 
        candidate, voter_id, county =election_data(row)
        vote_count = vote_count + 1 
        total_number = total_number + 1

        if candidate not in candidate_count.keys():
            candidate_count[candidate]= 0

        candidate_count[candidate]+= 1
    print(f"The total amount of votes is: {vote_count} ")

    for x in candidate_count:
        cand_p = round(((candidate_count[x]/total_number)*100),4)
        print(f"{x}: {(cand_p),candidate_count[x]}")
        
    for candidate in candidate_count: 
        cand_p = round(((candidate_count[candidate]/total_number)*100),4)
        if candidate_count[candidate] > 800000:
            print(f"The winner is {candidate} with {cand_p} percent of the vote!")


with open("PyPoll.txt", "w", newline="") as datafile:
    writer = csv.writer(datafile)









        