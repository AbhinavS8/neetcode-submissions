class Twitter:

    #
    def __init__(self):
        
        self.count = 0
        self.tweets = {}
        self.connections = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        
        if userId not in self.tweets:
            self.tweets[userId] = [(self.count,tweetId)]
            self.count -= 1
            
            self.connections[userId] = [userId] 
        
        else:
            # heapq.heappush(self.tweets[userId],(self.count,tweetId))
            self.tweets[userId].append((self.count,tweetId))
            self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        # index = 0
        
        ls = []
        for i in self.connections[userId]:
            for tup in self.tweets[i]:
                ls.append(tup)
        
        ls.sort(key= lambda x:x[0])
        return [x[1] for x in ls[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.connections:
            self.connections[followerId] = []
        
        if followeeId in self.connections[followerId]:
            return

        self.connections[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followerId == followeeId or followeeId not in self.connections[followerId]:
            return
        
        self.connections[followerId].remove(followeeId)