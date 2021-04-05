import heroku3
cloud = heroku3.from_key("c5fea175-a811-4686-8a44-eca1c9b2ea09")
print(cloud)
app = cloud.create_app("discordo")
