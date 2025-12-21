def recommend(results):
    return min(results, key=lambda x: x["worst_regret"])
