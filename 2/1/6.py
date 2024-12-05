from selenium import webdriver
import pyperclip
from selenium.webdriver.common.by import By
import time

usernameStr = 'mrikistilnemen-brohkuhs990947317@folmyra.web.id'
passwordStr = 'Waras123!'

browser = webdriver.Chrome('/Users/rizqi/Documents/chromedriver/chromedriver.exe')
browser.get(('https://script.google.com/d/1CJzEseSrx8joaElcsORUsWyRtgFn_rzFjq4p6c__5o2_WLjVDpQmZqy6/edit?usp=sharing'))
original_window = browser.current_window_handle

# fill in username and hit the next button

email_field = browser.find_element_by_id('identifierId')
email_field.clear()
email_field.send_keys(usernameStr)

email_next_button = browser.find_element_by_id('identifierNext')
email_next_button.click()

time.sleep(5)

password_field = browser.find_element_by_name('Passwd')
password_field.clear()
password_field.send_keys(passwordStr)

password_next_button = browser.find_element_by_id('passwordNext')
password_next_button.click()

time.sleep(5)

try:
        email_accept = browser.find_element(By.NAME, 'confirm')
        email_accept.click()
        time.sleep(2)
except:
        pass  # If the element is not found, just skip it

try:
        email_accept = browser.find_element(By.NAME, 'confirm')
        email_accept.click()
        time.sleep(2)
except:
        pass  # If the element is not found, just skip it

# button = browser.find_element(By.ID, "confirmActionButton")
# button.click()
try:
    deploy_button = browser.find_element(By.XPATH, "//div[contains(text(),'Deploy')]")
    deploy_button.click()
    print("Clicked on 'Deploy'")
    time.sleep(2)
except Exception as e:
    print("Error: {}".format(e))
    

try:
    new_deployment_option = browser.find_element(By.XPATH, "//span[@aria-label='New deployment']")
    new_deployment_option.click()
    print("Clicked on 'New Deployment'")
    time.sleep(5)
except Exception as e:
    print("Error: {}".format(e))
    

try:
    element_to_click = browser.find_element(By.XPATH, "/html/body/div[10]/div[4]/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/span/span/i")
    element_to_click.click()  # Click the element
    print("Webapp clicked successfully!")
    time.sleep(5)
except Exception as e:
    print("Error while trying to click the element: {}".format(e))



try:
    deploy_button = browser.find_element(By.XPATH, "//button[span[text()='Deploy']]")
    deploy_button.click()  # Click the Deploy button
    print("Deploy button clicked successfully!")
    time.sleep(5)
except Exception as e:
    print("Error while trying to click the Deploy button: {}".format(e))
    
    

    
try:
    authorize_button = browser.find_element(By.XPATH, "//button[span[text()='Authorize access']]")
    authorize_button.click()  # Click the Authorize access button
    print("Authorize access button clicked successfully!")
    time.sleep(5)
except Exception as e:
    print("Error while trying to click the Authorize access button: {}".format(e))
    

window_handles = browser.window_handles    

for handle in window_handles:
    if handle != original_window:
        browser.switch_to.window(handle)
        break  # Exit the loop once we've switched to the new tab

time.sleep(3)

try:
    element_to_click = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div")
    element_to_click.click()  # Click the element
    print("User clicked successfully!")
    time.sleep(3)
except Exception as e:
    print("Error while trying to click the User: {}".format(e))
    

try:
    element_to_click = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div/div/button/div[3]")
    element_to_click.click()  # Click the element
    print("Allow clicked successfully!")
    time.sleep(3)
except Exception as e:
    print("Error while trying to click the Allow: {}".format(e))
    

time.sleep(5)
browser.switch_to.window(original_window)
original_page_content = browser.page_source
print("Back to original tab, page content fetched.")
    

try:
    # Find the copy button using the XPath
    copy_button = browser.find_element(By.XPATH, "//button[span[text()='Copy']]")
    
    # Click the button to trigger the copy action
    copy_button.click()
    print("Copy button clicked successfully!")

    # Wait for a short period to ensure the clipboard is updated
    time.sleep(1)

    # Retrieve the copied text from the clipboard using pyperclip
    copied_text = pyperclip.paste()

    if copied_text:
        # Open 'paste.txt' in append mode to add the new text to a new line
        with open('paste.txt', 'a') as file:
            file.write(copied_text + "\n")  # Append text and ensure it is on a new line
        print("Copied text saved to paste.txt successfully!")
    else:
        print("No text copied to clipboard.")

except Exception as e:
    print("An error occurred: {e}")  