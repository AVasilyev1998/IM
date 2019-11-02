from Objects.film import Film

#
# film = Film('name', '1', '2')
# print(film)

#  queue test for food_shop and ticket_office
from collections import deque

q = deque()

q.append(1)
q.append(2)
print(q)

print(q.popleft())
print(q.popleft())
