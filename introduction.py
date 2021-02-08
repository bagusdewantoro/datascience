#======== INITIAL INFORMATION =========================================
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

print("\nUser ID and name:")
for user in users: print(user)

#======== DATA INTEGRITY =========================================
# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j

print("\nFriendships:")
for friends in friendships: print(friends, ":", friendships[friends])


#======== IDENTIFY MOST CONNECTED USER =========================================
# Hitung jumlah connections antar user & rata-rata connection per user
def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)
# print("\nTotal connection = ", total_connections)

num_users = len(users)                            # length of the users list
avg_connections = total_connections / num_users   # 24 / 10 == 2.4
# print("\nAverage connection = ", avg_connections)

# # bikin list yang terdiri dari ("id user", "jumlah teman")
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
# print("\nNumber of friends by id (\"id\", \"num. of friends\") : \n", num_friends_by_id)

# urutkan list di atas berdasarkan "jumlah teman".. x[1]
num_friends_by_id.sort(                                # list yang mau di-sort
       key=lambda x : x[1],             # diurutkan oleh "jumlah teman"
       reverse=True)                                   # largest to smallest
# print("\nSorted list above : \n", num_friends_by_id)


#======== SUGGEST 'USER YOU MAY KNOW' =========================================
# Cara 1 =
def friends_of_friend1(daftar):
    return [anggota
            for teman in friendships[daftar["id"]]
            for anggota in friendships[teman]]

print(f"\nPeople that {users[0]} may knows : ", friends_of_friend1(users[0]))
print(f"People that {users[3]} may knows : ", friends_of_friend1(users[3]))
print(f"People that {users[9]} may knows : ", friends_of_friend1(users[9]))

# Cara 2 =
def friends_of_friend2(daftar):
    a = []
    for teman in friendships[daftar["id"]]:
        for anggota in friendships[teman]:
            a.append(anggota)
    return a

print(f"\nPeople that {users[0]} may knows : ", friends_of_friend2(users[0]))
print(f"People that {users[3]} may knows : ", friends_of_friend2(users[3]))
print(f"People that {users[9]} may knows : ", friends_of_friend2(users[9]))


#======== COUNT OF MUTUAL FRIENDS =========================================
from collections import Counter

# Cara 1 =
def mutual_friends_number1(daftar):
    anggota = daftar["id"]
    return Counter(
        mutual
        for friend in friendships[anggota]
        for mutual in friendships[friend]
        if mutual != anggota
        and mutual not in friendships[anggota]
    )

print("\nCount mutual friends of '3' :", mutual_friends_number1(users[3]))  # {0: 2, 5: 1}
# teman dari '3' adalah '1', '2', '4'
# teman dari 1,2,4  yang tidak termasuk diri sendiri dan '3' adalah '0'(2 orang) dan '5'(1 orang)

# Cara 2  (lebih panjang)=
def mutual_friends_number2(daftar):
    anggota = daftar["id"]
    a = []
    for friend in friendships[anggota]:
        for mutual in friendships[friend]:
            if mutual != anggota and mutual not in friendships[anggota]:
                a.append(mutual)
    return a

mutual3 = mutual_friends_number2(users[3])
print("Friends of a friends of '3' is:", mutual3)
print("Count mutual friends of '3' :", Counter(mutual3))


#======== USER INTERESTS =========================================
hobi = [
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

# cek orang yang suka sama hobi tertentu
# cara 1 :
def orang_yang_suka(target_hobi):
    return [anggota
            for anggota, pilihan_hobi in hobi
            if pilihan_hobi == target_hobi]
sukaJava = orang_yang_suka("Java")
sukaPython = orang_yang_suka("Python")
print("\nOrang yang suka Java:", sukaJava)
print("Orang yang suka Python:", sukaPython)

# cara 2 :
def orang_yang_suka2(target_hobi):
    a = []
    for anggota, pilihan_hobi in hobi:
        if pilihan_hobi == target_hobi:
            a.append(anggota)
    return a
sukaJava2 = orang_yang_suka2("Java")
sukaPython2 = orang_yang_suka2("Python")
print("Orang yang suka Java:", sukaJava2)
print("Orang yang suka Python:", sukaPython2)


#======== CHECK NUMBERS OF SAME INTERESTS WITH OTHER USER =========================================
from collections import defaultdict

anggota_berdasarkan_hobi = defaultdict(list)
for anggota, pilihan_hobi in hobi:
    anggota_berdasarkan_hobi[pilihan_hobi].append(anggota)
print("\nData ID anggota berdasarkan Pilihan Hobi:")
print(anggota_berdasarkan_hobi)

hobi_berdasarkan_anggota = defaultdict(list)
for anggota, pilihan_hobi in hobi:
    hobi_berdasarkan_anggota[anggota].append(pilihan_hobi)
print("\nData Pilihan hobi berdasarkan ID anggota:")
print(hobi_berdasarkan_anggota)

def hobi_yang_sama(daftar):
    return Counter(a
                for pilihan_hobi in hobi_berdasarkan_anggota[daftar["id"]]
                for a in anggota_berdasarkan_hobi[pilihan_hobi]
                if a != daftar["id"])
print("\nUser 0 punya hobi yang sama dengan:", hobi_yang_sama(users[0]))
print("User 6 punya hobi yang sama dengan:", hobi_yang_sama(users[6]))


# Cek jumlah user untuk tiap pilihan hobi:
hitung_user_setiap_hobi = Counter(topik
                                    for anggota, pilihan_hobi in hobi
                                    for topik in pilihan_hobi.lower().split())
for topik, hitung in hitung_user_setiap_hobi.most_common():
    if hitung > 1:
        print(topik, hitung)
