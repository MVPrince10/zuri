import instaloader


def get_followers():
	loader = instaloader.Instaloader()

	# Login or load session
	loader.login('', '')        # (login)

	# Obtain profile metadata
	profile = instaloader.Profile.from_username(loader.context, "christellebraids")

	# Print list of followers
	follow_list = []
	file = open("followers.txt", "w+")
	for follower in profile.get_followers():
		follow_list.append(follower.username)
		file.write(follower.username + '\n')

	file.close()
	print(len(follow_list))


def get_followees():
	loader = instaloader.Instaloader()

	# Login or load session
	loader.login('', '')        # (login)

	# Obtain profile metadata
	profile = instaloader.Profile.from_username(loader.context, "christellebraids")

	# Print list of followees
	follow_list = []
	file = open("followees.txt", "w+")
	for followee in profile.get_followees():
		follow_list.append(followee.username)
		file.write(followee.username + '\n')

	file.close()
	print(len(follow_list))


def combine_lists():
	followers = open('followers.txt', 'r')
	followees = open('followees.txt', 'r')
	network = set()
	for follower in followers.readlines():
		network.add(follower.strip())
	followers.close()
	for followee in followees.readlines():
		network.add(followee.strip())
	followees.close()

	file = open("network.txt", "w+")
	for username in network:
		file.write(username + '\n')
	file.close()
	print(len(network))


def clean_list():
	SENT = [
		"amberannh",
	"keylashxtoronto",
	"joyilbey",
	"mommamouse0816",
	"zirhumana__",
	"missafricautah",
	"queenbee1490",
	"marj.alexandra",
	"chanti.dosier",
	"_riah30",
	"sharperthanaharper",
	"barebloombeauty",
	"notsoav",
	"lettieann1995",
	"kin.fin",
	"shanekaserr",
	"julioarmando3362",
	"lexx_0296",
	"dericgurley",
	"laceycisnerosphotography",
	"boujeeislandgrl",
	"bruhitsbria_",
	"isha_shire",
	"marselamurillo",
	"lettii____",
	"dajaamani",
	"___sylvi___",
	"agnes.yourutahhomegirl",
	"braidsnowdotcom",
	"brenda_boo88",
	"harmony_4",
	"claire_peru",
	"tansha187",
	"warstarmel",
	"closmartinez15",
	"christinamomusic",
	"nadinebahati",
	"exclusivebebe",
	"tkabharper",
	"saimandaumu",
	"kritzia.mer",
	"habdi_17",
	"notyourbabyfather",
	"belhp",
	"digeronimomd",
	"adjisowdiop",
	"mama.mery",
	"alannhurst",
	"skincare_bykena",
	"rhino_the_don",
	"practicallykadija"]
	network_file = open('network.txt', 'r')
	network = set()
	for user in network_file.readlines():
		if user.strip() in SENT:
			continue
		network.add(user.strip())

	file = open("remaining_users.txt", "w+")
	for username in network:
		file.write(username + '\n')
	file.close()
	print(len(network))



if __name__ == '__main__':
	# get_followers()
	# get_followees()
	# combine_lists()
	clean_list()