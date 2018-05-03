from pymongo import MongoClient
import datetime

db = MongoClient().final

db.User.insert({

   "Email": "test0@columbia.edu",
   "Name": "Guanming Qiao",
   "Password": "123456",
   "Follower":
   [
      {"Email": "test1@columbia.edu"},
      {"Email": "test2@columbia.edu"}
   ],
   "Following":
   [
       {"Email": "test1@columbia.edu"},
       {"Email": "test2@columbia.edu"}
   ],
   "Liked":
   [
      {"Email": "test1@columbia.edu", "Name": "test1_pt1"},
      {"Email": "test2@columbia.edu", "Name": "test2_pt1"}

   ],
   "Disliked":
   [
   ],
   "Commented":
   [
      {"Email": "test1@columbia.edu", "Name": "test1_pt1", "Content" : "This is awesome"},
      {"Email": "test2@columbia.edu", "Name": "test2_pt1", "Content" : "This is awesome"}
   ]

})

db.User.insert({

   "Email": "test1@columbia.edu",
   "Name": "Guanhua Qiao",
   "Password": "123456",
   "Follower":
   [
      {"Email": "test0@columbia.edu"},
      {"Email": "test2@columbia.edu"}
   ],
   "Following":
   [
       {"Email": "test0@columbia.edu"},
       {"Email": "test2@columbia.edu"}
   ],
   "Liked":
   [
      {"Email": "test0@columbia.edu", "Name": "test0_pt1"}

   ],
   "Disliked":
   [
      {"Email": "test2@columbia.edu", "Name": "test2_pt1"}
   ],
   "Commented":
   [
      {"Email": "test0@columbia.edu", "Name": "test0_pt1", "Content" : "This is awesome"},
      {"Email": "test2@columbia.edu", "Name": "test2_pt1", "Content" : "This sucks"}
   ]

})

db.User.insert({

   "Email": "test2@columbia.edu",
   "Name": "Guanjun Qiao",
   "Password": "123456",
   "Follower":
   [
      {"Email": "test0@columbia.edu"},
      {"Email": "test1@columbia.edu"}
   ],
   "Following":
   [
       {"Email": "test0@columbia.edu"},
       {"Email": "test1@columbia.edu"}
   ],
   "Liked":
   [
   ],
   "Disliked":
   [
       {"Email": "test0@columbia.edu", "Name": "test0_pt1"},
       {"Email": "test1@columbia.edu", "Name": "test1_pt1"}
   ],
   "Commented":
   [
      {"Email": "test0@columbia.edu", "Name": "test0_pt1", "Content" : "This sucks"},
      {"Email": "test1@columbia.edu", "Name": "test1_pt1", "Content" : "This sucks"}
   ]

})

db.Video.insert({

   "Email": "test0@columbia.edu",
   "Name": "test0_pt1",
   "Created_at": datetime.date(2018, 5, 1),
   "Up_Vote":
   [
      {"Email": "test1@columbia.edu"}
   ],
   "Down_Vote":
   [
      {"Email": "test2@columbia.edu"}
   ],
   "Comment":
   [
       {"Email": "test1@columbia.edu", "Content": "This is awesome"},
       {"Email": "test2@columbia.edu", "Content": "This sucks"}
   ],
   "Views":
   [
      {"Email": "test1@columbia.edu"},
      {"Email": "test2@columbia.edu"}
   ]

})

db.Video.insert({

   "Email": "test1@columbia.edu",
   "Name": "test1_pt1",
   "Created_at": datetime.date(2018, 3, 1),
   "Up_Vote":
   [
      {"Email": "test0@columbia.edu"}
   ],
   "Down_Vote":
   [
      {"Email": "test2@columbia.edu"}
   ],
   "Comment":
   [
       {"Email": "test0@columbia.edu", "Content": "This is awesome"},
       {"Email": "test2@columbia.edu", "Content": "This sucks"}
   ],
   "Views":
   [
      {"Email": "test0@columbia.edu"},
      {"Email": "test2@columbia.edu"}
   ]

})

db.Video.insert({

   "Email": "test2@columbia.edu",
   "Name": "test1_pt2",
   "Created_at": datetime.date(2018, 5, 2),
   "Up_Vote":
   [
      {"Email": "test0@columbia.edu"}
   ],
   "Down_Vote":
   [
      {"Email": "test1@columbia.edu"}
   ],
   "Comment":
   [
       {"Email": "test0@columbia.edu", "Content": "This is awesome"},
       {"Email": "test1@columbia.edu", "Content": "This sucks"}
   ],
   "Views":
   [
      {"Email": "test0@columbia.edu"},
      {"Email": "test1@columbia.edu"}
   ]

})

