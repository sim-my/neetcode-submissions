class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followee = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.followee[userId] | {userId}
        tweets = []
        for fol in followees:
            for tweet in self.tweets[fol]:
                tweets.append(tweet)

        results = heapq.nsmallest(10, tweets)
        return [tweetId for _, tweetId in results]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].discard(followeeId)
 



 #time to track the most frequent
 #heap = storing the tweets with time => (time, [userId, tweetId])
 # one more ds => store the followerList of that user Id => Dictionary
 # remove from that list if they are not following
