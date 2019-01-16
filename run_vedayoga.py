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
	u'👏🏻👏🏻👏🏻',
	u'nice 🙌🏻',
	u'𝓛ȯ𝒱𝓮 𝒾𝓉 😝',
	u'good one 👌🏻🔥',
	u'nice one 😜',
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
	'what camera did you use?',
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
	'#yogainstructor',
	'#acroyoga',
	'#fitnessmotivation',
	'#fitnessphotography',
	'#fitnessmodel',
	'#culvercity',
	'#santamonica',
	'#corepoweryoga',
	'#losangeles',
	'#westla'
]

my_high_locations = [
	'212999109/los-angeles-california/',
	'213420290/culver-city-california/',
	'137242643/santa-monica-california/',
	'212970049/beverly-hills-california',
	'212931920/hollywood/'
]
my_low_locations = [
	'214645216/muscle-beach/',
	'7896197/hot8yoga/',
	'47542763/hot-8-yoga/',
	'214469887/your-neighborhood-studio-when-in-doubt-dance/',
	'398168213/danceline-la/',
	'237278133/jagged-vertical-dance-fitness/',
	'696738/yogaworks-larchmont/',
	'10307275/the-choreography-house/',
	'2953516/cirque-school-los-angeles/',
	'222990220/edge-performing-arts-center/',
	'906425066/wanderlust-hollywood/',
	'1030280488/alo-yoga-store/',
	'246780626/la-dancefit/',
	'217840508960653/alo-yoga-at-the-grove',
	'823817134428235/city-of-angels-los-angeles-ca/',
	'2004074866576073/y7-west-hollywood',
	'624809367701911/y7-studio-upper-east-side',
	'600981358/y7-studio-soho',
	'167987390457522/y7-studio-silver-lake',
	'2081171858784991/y7-studio-tribeca',
	'1014870077/set-and-flow-yoga',
	'6185202/inyoga-center',
	'225325532/yoga-nest-venice',
	'251664416/yoga-at-the-raven',
	'18952679/yogaqua',
	'6672274/yoga-house',
	'3474112/black-dog-yoga',
	'146477070/aurayoga',
	'223635232/tempest-freerunning-academy-south-bay',
	'2340612/tempest-freerunning-academy',
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
			session.like_by_locations([my_loc], amount=20)
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
	my_users=[
	]
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
