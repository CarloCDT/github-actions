import pandas as pd
from datetime import datetime

def load_leaderboard(path='leaderboard/leaderboard.csv'):
    return pd.read_csv(path)

def add_score(leaderboard, user="test_user", score=0):
    
    new_score = pd.DataFrame.from_dict({'user': [user], 'score': [score], 'date': [datetime.utcnow()]})
    leaderboard = pd.concat([leaderboard, new_score], axis=0)

    # Only save top-10
    leaderboard = leaderboard.sort_values(by=['score', 'date'], ascending=[0,1]).head(10).reset_index(drop=True)

    return leaderboard

def save_leaderboard(leaderboard, path='leaderboard/leaderboard.csv'):
    leaderboard.to_csv(path, index=False)

def update_readme(leaderboard):
    f = open("README.md", "w")
    f.write("# Leaderboard - Using GHA\n\n")
    f.write(f"Last Update (UTC): {datetime.utcnow()}\n\n")
    f.write(leaderboard.to_markdown())
    f.write("\n")
    f.close()

if __name__ == "__main__":
    leaderboard = load_leaderboard()
    leaderboard = add_score(leaderboard, user='CarloCDT', score=0.7)
    save_leaderboard(leaderboard)
    update_readme(leaderboard)
