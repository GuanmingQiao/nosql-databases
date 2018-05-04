# Put the use case you chose here. Then justify your database choice:
# I chose to write a Youtube-like video sharing database. I choose MongoDB because, in addition to conventional advantages of NoSQL databases, MongoDB also provides Documented Oriented Storage, which stores data in the form of JSON style documents. It also handles auto-sharding and fast in-place updates, which is great for scalability.
#
# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
# MongoDB replicates database into a distributed system, ensuring that as long as a write or insert is successfully propagated to adequate distributed servers, our data is safe. Therefore, if coffee spilled on one of the servers, given that all previous inserts and writes were duplicated, the data is still safe.
#
# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
# User info, especially password is critical. We can avoid explicitly saving the password. We can either use a tokenized structure that does not store user secret, or to encrypt the user secret before saving it.
#
import datetime


# Action 1: <User registers for an account with input Email: input_email, Name: input_name, Password: input_pw>
db.User.insert({

   "Email": input_email,
   "Name": input_name,
   "Password": input_pw,
   "Follower":
   [
   ],
   "Following":
   [
   ],
   "Liked":
   [
   ],
   "Disliked":
   [
   ],
   "Commented":
   [
   ]

})

# Action 2: <User posts a video with Name: input_name>
db.Video.insert({

   "Email": current_user_email,
   "Name": input_name,
   "Created_at": datetime.date.today(),
   "Up_Vote":
   [
   ],
   "Down_Vote":
   [
   ],
   "Comment":
   [
   ],
   "Views":
   [
   ]

})

# Action 3: <A user sees all the video of the people they follow from the last week>
timeDelta = datetime.timedelta(days=7)
today = datetime.date.today()
output = []

following = db.Users.find({ "User.Following": current_user_email })

for matched in following:
    in_range = list(db.Video.find({"$and":[{"Email": matched["Email"]}, {"Created_at": {"$gte" : today - timeDelta, "$lt": today + timeDelta}}]}))
    output += in_range

return output

# Action 4: <A user sees all the video of one particular person they follow, with input target_user_email>
following = db.Users.find({ "User.Following": target_user_email})
return list(db.Video.find({"$and":[{"Email": target_user_email}, {"Created_at": {"$gte" : today - timeDelta, "$lt": today + timeDelta}}]}))

# Action 5: <A user comments on another's video, with input source_user_email, target_user_email, video_name, comment_content>
db.Users.update({"Email" : source_user_email},{"$push": {"Commented": {"Email": target_user_email,"Name": video_name,"Content" : comment_content}}})

# Action 6: <A user starts following a new person, with input source_user_email, target_user_email>
db.Users.update({"Email" : source_user_email},{"$push": {"Following": {"Email": target_user_email}}})
db.Users.update({"Email" : target_user_email},{"$push": {"Follower": {"Email": source_user_email}}})

# Action 7: <A user viewed a video, then dislikes it, input: source_user_email, target_user_email, video_name>
db.Users.update({"Email" : source_user_email},{"$push": {"Disliked": {"Email": target_user_email,"Name": video_name}}})
db.Video.update({"$and": [{"Email" : target_user_email},{"Name": video_name}]},{"$push": {"Down_Vote": {"Email": source_user_email,"Name": video_name}}})
db.Video.update({"$and": [{"Email" : target_user_email},{"Name": video_name}]},{"$push": {"Views": {"Email": source_user_email}}})

# Action 8: <A user viewed a video, then likes it, input: source_user_email, target_user_email, video_name>
db.Users.update({"Email" : source_user_email},{"$push": {"Liked": {"Email": target_user_email,"Name": video_name}}})
db.Video.update({"$and": [{"Email" : target_user_email},{"Name": video_name}]},{"$push": {"Up_Vote": {"Email": source_user_email,"Name": video_name}}})
db.Video.update({"$and": [{"Email" : target_user_email},{"Name": video_name}]},{"$push": {"Views": {"Email": source_user_email}}})























