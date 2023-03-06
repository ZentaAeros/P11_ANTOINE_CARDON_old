from datetime import datetime

def sort_competition_by_date(competition):
    past = []
    actually = []

    for compet in competition:
        if compet['date'] < datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
            past.append(compet)
        elif compet['date'] > datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
            actually.append(compet)
    
    return {"past_compet": past, "actually_compet": actually}