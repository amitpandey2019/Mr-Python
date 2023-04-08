import fbchat
from getpass import getpass
username = str(raw_input("Username:"))
client = fbchat.Client(username, getpass())
no_of_friends = int(raw_input("Number of friends:"))
for i in xrange(no_of_friends):
    _name = friends[0]
    friends = client.searchForUser(name)# return a list of names
    friend = friends[0]
msg = str(raw_input("Message:"))
sent = client.sendMassage(msg,thread_id=friend.uid)
if send:
    print("Massage sent successfully!")
