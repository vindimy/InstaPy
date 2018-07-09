# -*- coding: UTF-8 -*-

import os
import time
from instapy import InstaPy
from selenium.common.exceptions import TimeoutException, WebDriverException

# Read from INSTA_USER and INSTA_PW bash variables
session = InstaPy(username=os.environ['INSTA_USER'], password=os.environ['INSTA_PW'], nogui=True, multi_logs=True)
session.login()


###### ZERO ######
# Set up options
session.set_relationship_bounds(enabled=True, potency_ratio=0.4, delimit_by_numbers=True, max_followers=3000, max_following=3000, min_followers=10, min_following=50)
session.set_do_comment(enabled=True, percentage=20)
session.set_do_follow(enabled=False, percentage=0, times=0)
session.set_do_like(enabled=True, percentage=50)
session.set_user_interact(amount=3, randomize=True, percentage=50, media='Photo')
session.set_delimit_liking(enabled=True, max=100, min=0)
session.set_delimit_commenting(enabled=True, max=20, min=0)

my_photo_comments = [
	u'super schön 😅',
	u'beeindruckend 😊',
	u'inspirierend 🙌🏻',
	u'atembaraubend 👏🏻',
	u'weiter so 🔥',
	'good one :)',
	'nice pic!',
	'love your profile!',
	'love your posts :)',
	'great photo :)',
	'keep it up!',
	'great profile!',
	'love it :)',
	'beautiful <3',
	'lovely <3',
	'nice :)',
	'nice, very nice',
	'marvelous :)',
	'just great :)',
	'gorgeous',
	'love this',
	'beautiful :)',
	'cool :)',
	'excellent :)',
	'love the framing here',
	'love the composition',
	'yesss <3',
	'wonderful :)',
	'inspiring!',
	'pretty great :)'
]
session.set_comments(my_photo_comments, media='Photo')


my_tags = [
	'#acroyogaberlin',
	'#acroberlin',
	'#fitnessberlin',
	'#yogaeurope',
	'#yogaberlin',
	'#berlinyoga',
	'#yogadeutschland',
	'#berlin',
	'#deutschland',
	'#munich',
	'#barcelona'
]

my_high_locations = [
	'213131048/berlin-germany/',
	'216699620/wedding-berlin/',
	'213359469/munich-germany/',
	'213100244/barcelona-spain/'
]
my_low_locations = [
	'237878116/seestrae/',
	'116971912/yoga-sky-berlin/',
	'250197745354365/yoga-rebellion/',
	'65297733/chimosa/',
	'599299874/yogafurdich/',
	'1020136606/ashtanga-yoga-berlin/',
	'289063685/element-yoga/',
	'96367417/yellow-yoga/',
	'213813394/jivamukti-yoga-berlin/',
	'265803191/lagoa-yoga-berlin/',
	'254570144724325/zen-yoga-by-dynamic-mindfulness/',
	'256159741/ycba-yogacircle-berlin-academy/',
	'1032826954/spirit-yoga-berlin/',
	'1015509393/yoga-delta-berlin/',
	'238701440/spirit-yoga-berlin/',
	'1800120726682395/yoga-barn-berlin/',
	'1022004264/becycle/',
	'32934/aspria-berlin-kudamm/',
	'773405931/ladycompany-fitness-fur-frauen-gmbh/',
	'242061176268639/elixia-berlin/',
	'1844977909085562/elixia-berlin/',
	'105605239994491/elixia-berlin/',
	'1015509393/yoga-delta-berlin/',
	'197030017008189/dharma-yoga-berlin/',
	'293142986/peace-yoga-berlin-jivamukti-yoga-school/',
	'1020116796/runbase-berlin/'
]


while True:
	## Interact with locations ##
	for my_loc in my_high_locations:
		try:
			session.like_by_locations([my_loc], amount=50)
			time.sleep(300)
		except (TimeoutException, WebDriverException) as e:
			print "Caught exception from selenium.common.exceptions: " + str(e)
			os._exit(1)
	for my_loc in my_low_locations:
		try:
			session.like_by_locations([my_loc], amount=3)
			time.sleep(60)
		except (TimeoutException, WebDriverException) as e:
			print "Caught exception from selenium.common.exceptions: " + str(e)
			os._exit(1)

	# Pause
	time.sleep(600)


	## Interact with hashtags ##
	for my_tag in my_tags:
		try:
			session.like_by_tags([my_tag], amount=50)
			time.sleep(300)
		except (TimeoutException, WebDriverException) as e:
			print "Caught exception from selenium.common.exceptions: " + str(e)
			os._exit(1)

	# Pause
	time.sleep(600)


	## Interact with sought-after users ##
	my_users=['yoga_mit_lucie', 'kickassyoga', 'martamwitecka', 'yuvaloz', 'xploreyourfit_by_sinah', 'oliverchamo', 'johnkarvelis', 'skovgaardjeppe', 'ishine_gape', 'jasonnemer']
	for user in my_users:
		try:
			session.interact_user_followers([user], amount=10, randomize=True)
			time.sleep(300)
		except (TimeoutException, WebDriverException) as e:
			print "Caught exception from selenium.common.exceptions: " + str(e)
			os._exit(1)

	# Pause
	time.sleep(600)


	## Interact with own users ##
	#try:
	#	session.set_do_comment(enabled=False, percentage=25)
	#	session.interact_user_followers(['nyamaste'], amount=10, randomize=True)
	#	session.set_do_comment(enabled=True, percentage=25)
	#except (TimeoutException, WebDriverException) as e:
	#	print "Caught exception from selenium.common.exceptions: " + str(e)
	#	os._exit(1)

	# Pause
	#time.sleep(3600)


session.end()
