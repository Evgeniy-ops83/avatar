


test_dict = {'messages': ['"{\'user_request\': \'What are the categories of products or services offered by Coca-Cola?\', \'assistant_request\': \'Coca-Cola offers a variety of product categories including soft drinks, water, juices, teas, coffees, and energy drinks. Their portfolio features well-known brands such as Coca-Cola, Diet Coke, Sprite, Fanta, Dasani, and Minute Maid, among others.\'}"']}

perf_dict = test_dict['messages'][0][2:-2]

dict1 = dict(perf_dict)

#.split('\',')

print(perf_dist)