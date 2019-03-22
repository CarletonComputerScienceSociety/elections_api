def validate_vote(client_vote, candidates):
    print(client_vote)

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