import json

def validate_vote(client_vote_json, candidates):
    try:
        client_vote = json.loads(client_vote_json)
    except:
        return [-1, "Error, invalid json"]

    if (len(client_vote.keys()) != len(candidates.keys())):
        return [-1, "Error, number of submitted candidates is wrong"]

    valid_vote = {}

    for role in candidates.keys():
        if (role in client_vote):
            client_candidate = client_vote[role]
        else:
            return [-1, "Error, candidates not valid"]

        print(client_candidate["0"])
        if (client_candidate["0"] == None and client_candidate["1"] == None):
            return [-1, "Error, an option must be choosen for " + role]

    return [1, "Valid"]

def load_candidates():
    with open('database/candidates.json') as f:
        candidates_db = json.load(f)

    candidates = {}
    for role in candidates_db.keys():
        candidates[role] = []
        for candidate in candidates_db[role]:
           candidates[role].append(candidate)

    print(candidates)
    return candidates

if __name__ == "__main__":
    import json
    load_candidates()