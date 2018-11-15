import pymongo


def get_new_article():
    base = pymongo.MongoClient()
    db = base["owner_article"]
    collection = db["article"]
    data_articles = collection.find({}).limit(8).sort([("date", -1)])
    Recommend_articles = []
    for data in data_articles:
        Recommend_articles.append(data)
    return Recommend_articles
