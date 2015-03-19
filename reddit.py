import praw

r = praw.Reddit(user_agent="mighty mouse")
submissions = r.get_subreddit('CasualConversation').get_new(limit=20)

for x in submissions:
    print(x)


