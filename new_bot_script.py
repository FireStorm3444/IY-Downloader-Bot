import time
import downloader_script
import telebot
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'This bot is made by IgNxFireStorm.\nThis bot can download YouTube Videos, Audio for '
                          'YouTube Videos, YouTube Shorts, Instagram Reels, Audio for Instagram Reels.\nYou just have '
                          'to select the desired format and provide a valid link.\n \n'
                          'Use /help command to get instructions on how to use this bot')


@bot.message_handler(commands=['help'])
def help_query(message):
    bot.reply_to(message, 'To download YouTube Videos or YouTube Audios or Instagram reels, '
                          'you must select your desired format.\n '
                          '\n'
                          'You can select format by folowing commands:-\n'
                          '/video - Use to download in Video format\n'
                          '/audio - Use to download in Audio format\n '
                          '\n'
                          '/info - You can get information about what this bot can do\n '
                          '\n'
                          '/help - Instructions on how to use this bot')


@bot.message_handler(commands=['info'])
def start(message):
    bot.reply_to(message, 'This bot is made by IgNxFireStorm.\nThis bot can download YouTube Videos, Audio for '
                          'YouTube Videos, YouTube Shorts, Instagram Reels, Audio for Instagram Reels.\nYou just have '
                          'to select the desired format and provide a valid link.\n \n'
                          'Use /help command to get instructions on how to use this bot')


@bot.message_handler(commands=['video', 'audio'])
def format_input(message):
    if message.text == '/video':
        print('Video is selected!!')
        msg = bot.reply_to(message, 'Video is Selected!!')
        bot.register_next_step_handler(msg, video_downloader)
    elif message.text == '/audio':
        print('Audio is selected!!')
        msg = bot.reply_to(message, 'Audio is Selected!!')
        bot.register_next_step_handler(msg, audio_downloader)


@bot.message_handler(func=lambda anything: True)
def select_format(message):
    print('Select format!!')
    bot.reply_to(message, 'Please select Audio or Video first!!')


def video_downloader(video_link):
    if '.' in video_link.text:
        print(video_link.text, 'video downloader')
        # YouTube Link
        if 'yout' in video_link.text:
            if '/shorts/' in video_link.text:
                print('youtube shorts video')
                bot.reply_to(video_link, 'Video is selected!!')
                bot.reply_to(video_link, 'Please wait while I fetch the download link for you.')
                try:
                    ysv_download_link = downloader_script.short_downloader(video_link.text)
                    bot.reply_to(video_link, ysv_download_link)

                    # Update database
                    with open('output.txt', 'a+') as yv_output:
                        yv_output.write(
                            f'\n{time.strftime("%H:%M:%S", time.localtime())}   YouTube Video - {ysv_download_link}\n')

                except Exception as y_e:
                    print(y_e)
                    bot.reply_to(video_link, 'Something went wrong!!')
            else:
                print('youtube video')
                bot.reply_to(video_link, 'Video is selected!!')
                bot.reply_to(video_link, 'Please wait while I fetch the download link for you.')
                try:
                    yv_download_link = downloader_script.video_downloader(video_link.text)
                    bot.reply_to(video_link, yv_download_link)

                    # Update database
                    with open('output.txt', 'a+') as yv_output:
                        yv_output.write(
                            f'\n{time.strftime("%H:%M:%S", time.localtime())}   YouTube Video - {yv_download_link}\n')

                except Exception as y_e:
                    print(y_e)
                    bot.reply_to(video_link, 'Something went wrong!!')
        # Instagram Reel Link
        elif '/reel/' in video_link.text:
            print('Insta video')
            bot.reply_to(video_link, 'Video is selected')
            bot.reply_to(video_link, 'Please wait while I fetch the download link for you.')
            try:
                iv_download_link = downloader_script.reel_downloader(video_link.text)
                bot.reply_to(video_link, iv_download_link)

                # Update database
                with open('output.txt', 'a+') as iv_output:
                    iv_output.write(
                        f'\n{time.strftime("%H:%M:%S", time.localtime())}   Reel Video - {iv_download_link}\n')

            except Exception as i_e:
                print(i_e)
                bot.reply_to(video_link, 'Something went wrong!!')
            bot.reply_to(video_link, 'Please wait while I fetch the download link for you.')
            try:
                ia_download_link = downloader_script.reel_audio_downloader(video_link.text)
                bot.reply_to(video_link, ia_download_link)

                # Update database
                with open('output.txt', 'a+') as ia_output:
                    ia_output.write(
                        f'\n{time.strftime("%H:%M:%S", time.localtime())}   Reel Audio - {ia_download_link}\n')

            except Exception as i_e:
                print(i_e)
                bot.reply_to(video_link, 'Something went wrong!!')
        else:
            bot.reply_to(video_link, 'Please provide YouTube or Instagram Link!!')
        return
    else:
        bot.reply_to(video_link, 'Please provide a valid link!!')


def audio_downloader(video_link):
    if '.' in video_link.text:
        print(video_link.text, 'audio downloader')
        if 'yout' in video_link.text:
            if '/shorts/' in video_link.text:
                print('youtube shorts audio')
                bot.reply_to(video_link, 'Audio is selected!!')
                bot.reply_to(video_link, 'Please wait while I fetch the download link for you.')
                try:
                    ysa_download_link = downloader_script.youtube_audio_downloader(video_link.text)
                    bot.reply_to(video_link, ysa_download_link)

                    # Update database
                    with open('output.txt', 'a+') as yv_output:
                        yv_output.write(
                            f'\n{time.strftime("%H:%M:%S", time.localtime())}   YouTube Short Audio - {ysa_download_link}\n')

                except Exception as y_e:
                    print(y_e)
                    bot.reply_to(video_link, 'Something went wrong!!')
            else:
                print('youtube audio')
                bot.reply_to(video_link, 'Audio is selected!!')
                bot.reply_to(video_link, 'Please wait while I fetch the download link for you.')
                try:
                    yv_download_link = downloader_script.youtube_audio_downloader(video_link.text)
                    bot.reply_to(video_link, yv_download_link)

                    # Update database
                    with open('output.txt', 'a+') as yv_output:
                        yv_output.write(
                            f'\n{time.strftime("%H:%M:%S", time.localtime())}   YouTube Audio - {yv_download_link}\n')

                except Exception as y_e:
                    print(y_e)
                    bot.reply_to(video_link, 'Something went wrong!!')

        elif '/reel/' in video_link.text:
            print('Insta audio')
            bot.reply_to(video_link, 'Audio is selected')
            bot.reply_to(video_link, 'Please wait while I fetch the download link for you.')
            try:
                iv_download_link = downloader_script.reel_audio_downloader(video_link.text)
                bot.reply_to(video_link, iv_download_link)

                # Update database
                with open('output.txt', 'a+') as iv_output:
                    iv_output.write(
                        f'\n{time.strftime("%H:%M:%S", time.localtime())}   Reel Audio - {iv_download_link}\n')

            except Exception as i_e:
                print(i_e)
                bot.reply_to(video_link, 'Something went wrong!!')

        else:
            bot.reply_to(video_link, 'Please provide YouTube or Instagram Link!!')
    else:
        bot.reply_to(video_link, 'Please provide a valid link!!')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
