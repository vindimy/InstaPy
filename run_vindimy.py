import os
import time
from instapy import InstaPy
from selenium.common.exceptions import TimeoutException, WebDriverException

# Read from INSTA_USER and INSTA_PW bash variables
session = InstaPy(username=os.environ['INSTA_USER'], password=os.environ['INSTA_PW'], nogui=True)
session.login()


###### ZERO ######
# Set up options
session.set_upper_follower_count(limit = 2000)
session.set_lower_follower_count(limit = 10)
session.set_do_comment(enabled=True, percentage=15)
session.set_do_follow(enabled=False, percentage=20, times=2)
session.set_do_like(enabled=True, percentage=70)
session.set_user_interact(amount=3, randomize=True, percentage=50, media='Photo')

my_photo_comments = [
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
	'#yogainspiration',
	'#yogainstructor',
	'#acroyoga',
	'#circuslife',
	'#dancerlife',
	'#balletlife',
	'#pointe',
	'#fitnessmotivation',
	'#fitnessphotography',
	'#fitnessmodel',
	'#culvercity',
#	'#jaggedvdf',
#	'#vedayoga',
#	'#corepower',
	'#corepoweryoga',
	'#yogaworks'
]

my_high_locations = [
	'212999109/los-angeles-california/',
	'213420290/culver-city-california/',
	'137242643/santa-monica-california/',
	'212931920/hollywood/'
]
my_low_locations = [
	'214645216/muscle-beach/',
	'1026253633/corepower-yoga/',
	'1026344343/corepower-yoga/',
	'394273176/veda-yoga-center/',
	'129538823/red-diamond-yoga/',
	'243768840/corepower-yoga/',
	'4562253/corepower-yoga/',
	'97618096/corepower-yoga/',
	'121899548455661/love-yoga/',
	'414408751/yogaraj/',
	'2134200/liberation-yoga/',
	'1001363005/namastday-yoga/',
	'1493463307624837/hyperslow/',
	'7896197/hot8yoga/',
	'47542763/hot-8-yoga/',
	'214469887/your-neighborhood-studio-when-in-doubt-dance/',
	'398168213/danceline-la/',
	'237278133/jagged-vertical-dance-fitness/',
	'1619540185028533/create-yoga/',
	'30166282/laughing-frog-yoga/',
	'696738/yogaworks-larchmont/',
	'227812116/yogaworks-main-street/',
	'591038088/yogaworks-brentwood/',
	'23821579/yogaworks-pasadena/',
	'3396943/yogaworks-montana/',
	'1573376/yogaworks-westwood/',
	'684485752/aerial-warehouse/',
	'10307275/the-choreography-house/',
	'694809615/womack-and-bowman/',
	'147233/kinetic-theory/',
	'126189864687304/aeriform-arts/',
	'18119899/aeriform-arts/',
	'2953516/cirque-school-los-angeles/',
	'222990220/edge-performing-arts-center/',
	'402321672/kinship-studios/',
	'1014870077/set-and-flow-yoga/',
	'906425066/wanderlust-hollywood/',
	'235775388/yoga-salt/',
	'1030280488/alo-yoga-store/',
	'8339259/athleta/',
	'483411384/athleta/',
	'279466735/athleta/',
	'1022325093/lululemon-athletica/',
	'981555631/lululemon-athletica/',
	'926224683/lululemon-athletica-studio-city/',
	'246780626/la-dancefit/'
]


###### FIVE ######
## Unfollow ##
#try:
#	session.unfollow_users(amount=50, onlyInstapyFollowed=False, onlyInstapyMethod='LIFO')
#except (TimeoutException, WebDriverException) as e:
#	print "Caught exception from selenium.common.exceptions: " + str(e)
#	pass

while True:
	###### THREE ######
	## Interact with hashtags ##
	for my_tag in my_tags:
		try:
			session.like_by_tags([my_tag], amount=50)
		except (TimeoutException, WebDriverException) as e:
			print "Caught exception from selenium.common.exceptions: " + str(e)
			pass

	# Pause
	time.sleep(600)

	###### FOUR ######
	## Interact with locations ##
	for my_loc in my_high_locations:
		try:
			session.set_upper_follower_count(limit = 2000)
			session.like_by_locations([my_loc], amount=50)
		except (TimeoutException, WebDriverException) as e:
			print "Caught exception from selenium.common.exceptions: " + str(e)
			pass
	for my_loc in my_low_locations:
		try:
			session.set_upper_follower_count(limit = 2000)
			session.like_by_locations([my_loc], amount=2)
		except (TimeoutException, WebDriverException) as e:
			print "Caught exception from selenium.common.exceptions: " + str(e)
			pass

	# Pause
	time.sleep(600)

	###### ONE ######
	## Interact with sought-after users ##
	my_users=[
		'actionhiro',
		'nwoy',
		'omarzrobles',
		'sadsongsnskinnyjeans'
	]
	session.set_upper_follower_count(limit = 200000000)
	session.set_lower_follower_count(limit = 0)
	for user in my_users:
		try:
			session.interact_user_followers([user], amount=10, randomize=True)
		except (TimeoutException, WebDriverException) as e:
			print "Caught exception from selenium.common.exceptions: " + str(e)
			pass
	session.set_upper_follower_count(limit = 2000)
	session.set_lower_follower_count(limit = 10)

	# Pause
	time.sleep(600)

	###### TWO ######
	## Interact with own users ##
	session.set_upper_follower_count(limit = 200000000)
	session.set_lower_follower_count(limit = 0)
	try:
		session.set_do_comment(enabled=False, percentage=25)
		session.interact_user_followers(['nyamaste'], amount=10, randomize=True)
		session.set_do_comment(enabled=True, percentage=25)
	except (TimeoutException, WebDriverException) as e:
		print "Caught exception from selenium.common.exceptions: " + str(e)
		pass
	session.set_upper_follower_count(limit = 2000)
	session.set_lower_follower_count(limit = 10)

	# Pause
	time.sleep(3600)


session.end()
