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

print("\nFriendship pairs:")
for friends in friendships: print(friends, ":", friendships[friends])


#======== IDENTIFY MOST CONNECTED USER =========================================
# Hitung jumlah connections antar user & rata-rata connection per user
def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)
print("\nTotal connection = ", total_connections)

num_users = len(users)                            # length of the users list
avg_connections = total_connections / num_users   # 24 / 10 == 2.4
print("\nAverage connection = ", avg_connections)

# # bikin list yang terdiri dari ("id user", "jumlah teman")
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print("\nNumber of friends by id (\"id\", \"num. of friends\") : \n", num_friends_by_id)

# urutkan list di atas berdasarkan "jumlah teman".. x[1]
num_friends_by_id.sort(                                # list yang mau di-sort
       key=lambda x : x[1],   # diurutkan oleh "jumlah teman"
       reverse=True)                                   # largest to smallest
print("\nSorted list above : \n", num_friends_by_id)


#======== SUGGEST 'USER YOU MAY KNOW' =========================================
def friends_of_friend(daftar):
    return [anggota
            for teman in friendships[daftar["id"]]
            for anggota in friendships[teman]]

print(f"\nPeople that {users[0]} may knows : ", friends_of_friend(users[0]))
print(f"People that {users[3]} may knows : ", friends_of_friend(users[3]))
print(f"People that {users[9]} may knows : ", friends_of_friend(users[9]))
