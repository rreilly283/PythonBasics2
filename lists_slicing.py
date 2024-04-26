#modules in python - python files: lower case use underscore
        #first_name(snake case)
#sql, java -> listSlicing, FirstName (camel case)


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #3 players
print(players[:3]) # 3 players, by default it starts from index 0
print(players[1:4]) #3 players from the middle
print(players[2:5]) # the last 3 players
print(players[2:]) #3 players, by default it ends with last index
print(players[:]) #runs all elements of the list

new_players =players[:]  #copied to new list, independent from the players list
players.append('martin')
new_players.append('mark')
print("players:", players)
print("new players:", new_players)

players1 =players[:]  #it's not a copy but duplicate reference
players1.append('lucy')
players.append('david')
print("players:", players)
print("players1:", players1)

#Exercise 4-10
#H/W 4-11, 4-12

players=('charles', 'martina', 'michael', 'florence', 'eli')
#players.append()
#players=('charles', 'martina', 'michael', 'florence', 'eli', 'mark')
print(players[2])