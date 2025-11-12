from instabot import Bot
bot=Bot()
#login

bot.login(username="siwansh578",password="Rajan@123")

#cooment on post
bot.comment("coding","Great content")
#bot follow
bot.follow("spiritualconce")
# like a post
bot.like_hashtag("coding", amount=5)
# send DM to someone

bot.send_message("Hey! Big fan of your work!",["spiritualconce"])


