# class 8/30/23

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


# create a dict where the keys are user ids and the values are lists of friend ids
friends = {}
for user in users: 
    friends[user["id"]] = [x[1] for x in friendship_pairs if x[0] == user["id"]]
    friends[user["id"]] += ([x[0] for x in friendship_pairs if x[1] == user["id"]])

# find total number of connections
total_connections = 0
for key in friends:
    total_connections += len(friends[key])

# create a dict of mutual friends for the user id passed in
def mutual_friends(user_id):
    mutual_friends_dict = {}
    for user in users:
        mutual_friends_dict[user["id"]] = [x for x in friends[user["id"]] if x in friends[user_id]]
    return mutual_friends_dict

def common_interests(user_id):
    common_interests_dict = {}
    search_user_interests = []

    for interest in interests: 
        search_user_interests += interest if interest[0] == user_id

    for user in users: 
        user_interests = []
        for interest in interests:
            user_interests += interest if interest[0] == user["id"]
        common_interests_dict[user["id"]] = [x for x in user_interests[user["id"]] if x in interests[user_id]]

    return common_interests_dict

# output results
print(friends)
print('The average number of friendships is ' + str(total_connections / len(users)))
print(mutual_friends(1))
print(common_interests(3))