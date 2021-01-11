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

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
            (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


#======== DATA INTEGRITY =========================================
# Tambahkan key "friends" di users dictionary
for user in users:
    user["friends"] = []

# Populate value sesuai 'friendship list' di 'users dictionary'
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

print(users[0])
#for user in users:
#    print(user["id"], user["name"], user["friends"][0])

#======== IDENTIFY MOST CONNECTED USER =========================================
    # Hitung jumlah connections antar user & rata-rata connection per user
def number_of_friends(anggotas):
    jumlah = 0
    for anggota in anggotas:
        panjang = len(anggota["friends"])        #hitung length "friends" untuk setiap id
        jumlah += panjang            #jumlahkan length tersebut untuk setiap id
    return jumlah

connections = number_of_friends(users)
#print("number of connections = ", connections)

average_conn = connections / len(users)
#print("average connection = ", average_conn)

# bikin list yang terdiri dari ("id user", "jumlah teman")
conn_by_id = []
for user in users:
    num = (user['id'], len(user['friends']))
    conn_by_id.append(num)
print(conn_by_id)

# urutkan list di atas berdasarkan "jumlah teman".. x[1]
urutan = sorted(conn_by_id,      # object yang mau di-sort
    key= lambda x : x[1],        # diurutkan oleh "jumlah teman"
    reverse=True)                # largest to smallest
print(urutan)
