from selenium import webdriver
import time

moodlelink="" #your Moodle Homepage link
userid="" #your user id to login
password="" #password

driver=webdriver.Firefox()
driver.maximize_window()
driver.get(moodlelink)
driver.find_element_by_xpath("//a[text()='Log in']").click();
driver.find_element_by_id("username").send_keys(userid) #enter in user id
driver.find_element_by_id("password").send_keys(password) #enter in password
driver.find_element_by_id("rememberusername").click()
driver.find_element_by_id("loginbtn").click()

driver.find_element_by_xpath("//a[text()='Attendance']").click();
driver.find_element_by_xpath("//a[text()='Go to activity']").click();
driver.find_element_by_xpath("//a[text()='Submit attendance']").click();
driver.find_element_by_name("status").click()
driver.find_element_by_name("submitbutton").click()

print("attendance Marked,Proceeding To Meet Link")

#to be filled
current_time=time.time()
print("Current Time Is"+current_time)


#driver.findElement(By.cssSelector("label[for='hobbies-checkbox-1']")).click();
