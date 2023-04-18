import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Username and password of your instagram account:
my_username = ''
my_password = ''


# Authorization
def auth(driver, username, password):
	try:
		driver.get('https://instagram.com')

		input_username = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME, "username")))
		input_password = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME, "password")))

		input_username.send_keys(username)
		input_password.send_keys(password)
		input_password.send_keys(Keys.ENTER)

	except Exception as err:
		print(err)
		driver.quit()


# Sending messages:
def send_message(driver, users, message):
	remaining_users = users.copy()
	count = 0
	try:
		# dm button
		click_element(driver, By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
		# dismiss pop up
		click_element(driver, By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
		for usr in users:
			# compose new message button
			click_element(driver, By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')

			# search username
			username_textbox = click_element(driver, By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input')
			username_textbox.send_keys(usr)

			time.sleep(1)
			# click profile
			click_element(driver, By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div')

			# next button
			click_element(driver, By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div")

			time.sleep(4)
			# click textarea and send message
			text_area = click_element(driver, By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
			# time.sleep(1)
			text_area.send_keys(message)
			text_area.send_keys(Keys.ENTER)
			print(f'Message successfully sent to {usr}')
			remaining_users.remove(usr)
			count += 1

	except Exception as err:
		print(err)
		driver.quit()
	except KeyboardInterrupt:
		print('Quitting...')
		driver.quit()

	print(f'{count} messages sent')
	return remaining_users


# Force element retrieval
def click_element(driver, by, identifier):
	count = 0
	element = None
	while True:
		count += 1
		try:
			element = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((by, identifier)))
			element.click()
			break
		except Exception:
			if count > 500:
				print(f'ERROR {identifier}')
				break

	return element


# Get usernames
def get_usernames():
	users = set()
	file = open('network.txt', 'r')
	for usr in file.readlines():
		users.add(usr.strip())
	file.close()
	return users


# Get message
def get_message():
	file = open('message.txt', 'r')
	message = file.readline().strip()
	file.close()
	return message


if __name__ == '__main__':
	DRIVER = webdriver.Chrome('/Applications/chromedriver')
	DRIVER.maximize_window()
	auth(DRIVER, my_username, my_password)
	usernames = get_usernames()
	msg = get_message()
	remaining = send_message(DRIVER, usernames, msg)
	network_file = open('network.txt', 'w+')
	for user in remaining:
		network_file.write(user + '\n')
	network_file.close()
