from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# to keep Chrome window open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# YouTube Video Downloader
def video_downloader(link):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://en1.onlinevideoconverter.pro/10/youtube-video-downloader')

    try:
        # enter link and begin
        link_input = driver.find_element(By.XPATH, '//*[@id="texturl"]')
        link_input.clear()
        link_input.send_keys(link)

        # click on start button
        driver.find_element(By.XPATH, '//*[@id="convert1"]').click()

        try:
            while 'block' in driver.find_element(By.XPATH, '//*[@id="stepProcess"]').get_attribute('style'):
                continue
        except:
            pass

        # get download link
        download_link = driver.find_element(By.XPATH, '//*[@id="download-720-MP4"]').get_attribute('href')
        driver.quit()
        return download_link
    except Exception as e:
        print(e)
        driver.quit()
        return 'Error fetching download link:\n1. Requested content does not exist.\n2. Something went wrong.\nYou ' \
               'can consider trying again.'


def youtube_audio_downloader(link):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://tomp3.cc/')

    try:
        # enter link and begin
        link_input = driver.find_element(By.XPATH, '//*[@id="k__input"]')
        link_input.clear()
        link_input.send_keys(link)

        # click on start button
        start_button = driver.find_element(By.XPATH, '//*[@id="btn-start"]')
        start_button.click()

        try:
            while 'disabled' not in start_button.get_attribute('disabled'):
                continue
        except:
            pass

        # select quality
        selector = driver.find_element(By.XPATH, '//*[@id="formatSelect"]')
        selector.click()
        selector.send_keys(Keys.ARROW_UP)
        selector.send_keys(Keys.ARROW_UP)
        selector.send_keys(Keys.ARROW_UP)
        selector.send_keys(Keys.ENTER)

        # click on convert button
        driver.find_element(By.XPATH, '//*[@id="btn-convert"]').click()

        # monitor changes then get download link
        while 'clearfix d-none' in driver.find_element(By.XPATH, '//*[@id="download-box"]').get_attribute('class'):
            continue
        else:
            download_link = driver.find_element(By.XPATH, '//*[@id="asuccess"]').get_attribute('href')
            driver.quit()
            return download_link
    except Exception as e:
        print(e)
        driver.quit()
        return 'Error fetching download link:\n1. Requested content does not exist.\n2. Something went wrong.\nYou ' \
               'can consider trying again.'


# YouTube Shorts Downloader
def short_downloader(link):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://en1.onlinevideoconverter.pro/10/youtube-video-downloader')

    try:
        # enter link and begin
        link_input = driver.find_element(By.XPATH, '//*[@id="texturl"]')
        link_input.clear()
        link_input.send_keys(link)

        # click on start button
        driver.find_element(By.XPATH, '//*[@id="convert1"]').click()

        try:
            while 'block' in driver.find_element(By.XPATH, '//*[@id="stepProcess"]').get_attribute('style'):
                continue
        except:
            pass

        # get download link
        download_link = driver.find_element(By.XPATH, '//*[@id="download-720-MP4"]').get_attribute('href')
        driver.quit()
        return download_link
    except Exception as e:
        print(e)
        driver.quit()
        return 'Error fetching download link:\n1. Requested content does not exist.\n2. Something went wrong.\nYou ' \
               'can consider trying again.'


# Instagram Reels Downloader
def reel_downloader(link):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://indown.io/reels')

    try:
        # enter link and begin
        link_input = driver.find_element(By.XPATH, '//*[@id="link"]')
        link_input.clear()
        link_input.send_keys(link)

        # click on search button
        driver.find_element(By.XPATH, '//*[@id="get"]').click()

        # get download link
        try:
            download_link = driver.find_element(By.XPATH,
                                                '//*[@id="result"]/div/div/div[2]/a'). \
                get_attribute('href')
        except:
            download_link = driver.find_element(By.XPATH, '//*[@id="result"]/div/div/div[2]/div/a[1]').get_attribute(
                'href')
        driver.quit()
        return download_link
    except Exception as e:
        print(e)
        driver.quit()
        return 'Error fetching download link:\n1. Requested content does not exist.\n2. Something went wrong.\nYou ' \
               'can consider trying again.'


# Instagram Reels Downloader
def reel_audio_downloader(link):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://reelsdownloader.io/audio')

    try:
        # enter link and begin
        link_input = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/form/input')
        link_input.clear()
        link_input.send_keys(link)

        # click on get button
        get_button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/form/button[2]')
        get_button.click()

        # if error occurs, try again
        while 'error' in driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[1]'). \
                get_attribute('class'):
            get_button.click()
            continue

        try:
            while 'loading' in driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[1]/div'). \
                    get_attribute('class'):
                continue
        except:
            download_link = driver.find_element(By.XPATH,
                                                '//*[@id="__next"]/main/div/div[1]/div[2]/div[2]/div/audio'). \
                get_attribute('src')
            driver.quit()
            return download_link
    except Exception as e:
        print(e)
        driver.quit()
        return 'Error fetching download link:\n1. Requested content does not exist.\n2. Something went wrong.\nYou ' \
               'can consider trying again.'

# print(youtube_audio_downloader('https://www.youtube.com/watch?v=ZNdKFzyGH08&ab_channel=ThugofMemes'))
