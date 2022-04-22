from typing import List


class Twitter:

    def __init__(self):
        self.follow_data = {}  # followerId : set(followeeIds)
        self.tweets = []  # stack [(userId, tweetId)]

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # 10 most recent tweets 
        # userId must be following user who tweeted most recent tweets
        # tweet made by userId
        newsFeed = []
        cnt, idx = 0, len(self.tweets) - 1
        while (idx - cnt >= 0):
            currUserId, currTweetId = self.tweets[idx - cnt][0], self.tweets[idx - cnt][1]
            if (userId == currUserId):
                newsFeed.append(currTweetId)
                cnt += 1
            elif (userId in self.follow_data) and (currUserId in self.follow_data[userId]):
                newsFeed.append(currTweetId)
                cnt += 1
            else:
                idx -= 1

        return newsFeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # followerId follows followeeId
        if (followerId not in self.follow_data):
            self.follow_data[followerId] = set([followeeId])
        else:
            self.follow_data[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # followerId unfollows followeeId
        if (followerId in self.follow_data) and (followeeId in self.follow_data[followerId]):
            self.follow_data[followerId].remove(followerId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,5)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.follow()