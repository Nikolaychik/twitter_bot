from twitter import api
from twitter.configs import my_configs


a = api.TwitterBot(my_configs)
print(a.get_ids())

a.update_status("Hello, world!")a
