import requests
from functions.online_ops import find_my_ip, get_random_advice, get_random_joke, get_trending_movies,get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email,open_website, play_song, read_news_about
import speech_recognition as sr
from functions.os_ops import open_calculator, open_camera, open_cmd, open_word, open_discord, open_excel, open_pp
from random import choice
from utils import opening_text, hello_text, hello1_text
from pprint import pprint
import time
import wikipedia
from datetime import datetime
import playsound
import os
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from time import strftime
from gtts import gTTS


wikipedia.set_lang('vi')
language = 'vi'

EMAIL='luuvanlam2812@gmail.com'
PASSWORD='phamthimai20'
NEWS_API_KEY='15350f84b11c4c62be0d056f095f804a'
OPENWEATHER_APP_ID='fe8d8c65cf345889139d8e545f57819a'
TMDB_API_KEY='75917d21d84c74724b018347ef2ef457'
USERNAME = 'Lưu Văn Lâm'
BOTNAME = 'Panda'



# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3",True)
    os.remove("sound.mp3")
    #time.sleep(2)


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Chào buổi sáng ngài {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Chào buổi chiều ngài {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Chào buổi tối ngài {USERNAME}")
    elif ((hour >= 19) and (hour < 25))or(hour >= 0) and (hour < 6):
        speak(f"Chào buổi tối ngài {USERNAME}")
    speak(f"Tôi tên là {BOTNAME}. Tôi giúp gì được cho ngài?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f'{BOTNAME} đang nghe lệnh....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(f'{BOTNAME} đang nhận diện giọng nói...')
        query = r.recognize_google(audio, language='vi-VN')
        if ('thoát' in query)or('tạm biệt' in query):
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Tạm biệt ngài, xin hãy bảo trọng!")
            else:
                speak('Chúc ngài 1 ngày tốt lành!')
            exit()
    except Exception:
        speak(f'Xin lỗi, {BOTNAME} không hiểu ngài nói gì. Ngài có thể nói lại được không?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'mở word' in query:
            speak(choice(opening_text))
            open_word()

        elif 'mở excel' in query:
            speak(choice(opening_text))
            open_excel()

        elif 'mở powerpoint' in query:
            speak(choice(opening_text))
            open_pp()

        elif 'xin chào' in query:
            speak(choice(hello_text))

        elif 'khỏe không' in query:
            speak(choice(hello1_text))

        elif 'mở discord' in query:
            speak(choice(opening_text))
            open_discord()

        elif 'mở command prompt' in query or 'mở cmd' in query:
            speak(choice(opening_text))
            open_cmd()

        elif 'mở camera' in query or 'mở máy ảnh' in query:
            speak(choice(opening_text))
            open_camera()

        elif 'mở máy tính' in query:
            speak(choice(opening_text))
            open_calculator()

        elif 'hiện tại' in query or 'bây giờ' in query:
            now = datetime.now()
            if "giờ" in query:
                speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
            elif "ngày" in query:
                speak("Hôm nay là ngày %d tháng %d năm %d" %
                      (now.day, now.month, now.year))
            else:
                speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")

        elif 'mở trang web' in query:
            speak(choice(opening_text))
            if 'youtube' in query:
                if(open_website(query)):
                    speak(f"Trang web đã được mở")
                else:
                    speak(f"Trang web không thể mở")
            if 'facebook' in query:
                if (open_website(query)):
                    speak(f"Trang web đã được mở")
                else:
                    speak(f"Trang web không thể mở")
            if 'google' in query:
                if (open_website(query)):
                    speak(f"Trang web đã được mở")
                else:
                    speak(f"Trang web không thể mở")

        elif 'nghe nhạc' in query:
            speak(f'Xin mời ngài chọn tên bài hát')
            mysong = take_user_input()
            speak(choice(opening_text))
            play_song(mysong)
            speak(f"Bài hát bạn yêu cầu đã được mở.")

        elif 'địa chỉ ip' in query:
            ip_address = find_my_ip()
            speak(f'Địa chỉ ip của ngài là {ip_address}.\n Để tuận tiện, tôi sẽ in ra cho ngài.')
            print(f'Địa chỉ ip của ngài là {ip_address}')

        elif 'wikipedia' in query or 'tìm trên wikipedia' in query:
            speak(f'Ngài muốn tìm gì trên wikipedia ạ?')
            search_query = take_user_input().lower()
            speak(choice(opening_text))
            results = search_on_wikipedia(search_query)
            speak(f"Theo Wikipedia, {results}")
            speak("Để tuận tiện, tôi sẽ in ra cho ngài.")
            print(results)

        elif 'youtube' in query or 'xem youtube' in query:
            speak(f'Ngài muốn xem gì trên Youtube ạ?')
            video = take_user_input().lower()
            speak(choice(opening_text))
            play_on_youtube(video)

        elif 'tìm trên google' in query:
            speak(f'Ngài muốn tìm gì trên Google ạ?')
            query = take_user_input().lower()
            speak(choice(opening_text))
            search_on_google(query)

        elif "gửi 1 email" in query or "email cho" in query or "gửi email cho" in query or "gửi email tới" in query:
            speak(f"Ngài muốn gửi đén ai ạ? Ngài hãy nhập địa chỉ email ạ: ")
            receiver_address = input("Nhập email: ")
            speak(f"Tiêu đề là gì thưa ngài?")
            subject = take_user_input().capitalize()
            speak(f"Ngài hãy nói nội dung ạ?")
            message = take_user_input().capitalize()
            speak(choice(opening_text))
            if send_email(receiver_address, subject, message):
                speak(f"{BOTNAME} đã gửi email thưa ngài.")
            else:
                speak("Có lỗi xảy ra khi gửi email thưa ngài. Hãy kiểm tra lỗi.")

        elif 'truyện cười' in query or 'trò đùa' in query:
            speak(choice(opening_text))
            speak(f"Mong ngài thích cái này")
            joke = get_random_joke()
            speak(joke)
            speak("Để tuận tiện, tôi sẽ in ra cho ngài.")
            pprint(joke)

        elif "lời khuyên" in query:
            speak(choice(opening_text))
            speak(f"Một lời khuyên cho ngài đây ạ")
            advice = get_random_advice()
            speak(advice)
            speak("Để tuận tiện, tôi sẽ in ra cho ngài.")
            pprint(advice)

        elif "phim thịnh hành mới nhất" in query:
            speak(choice(opening_text))
            speak(f"Một vài phim thịnh hành là: {get_trending_movies()}")
            speak("Để tuận tiện, tôi sẽ in ra cho ngài.")
            print(*get_trending_movies(), sep='\n')

        elif 'tin tức mới nhất' in query:
            speak(f"Ngài muốn đọc tin về gì.")
            query = take_user_input().lower()
            speak(choice(opening_text))
            read_news_about(query)

        elif 'xem thời tiết' in query:
            speak(choice(opening_text))
            ip_address = find_my_ip()
            print(ip_address)
            city = requests.get(f'https://ipapi.co/{ip_address}/city/').text
            print(city)
            speak(f"Đang xem thời tiết tại {city}")
            pressure, temperature, feels_like = get_weather_report(city)
            speak(f"Nhiệt độ hiện tại là {temperature}, độ ẩm hiện tại là  {feels_like}, áp suất không khí hiện tại là  {pressure}",)
            speak("Để tuận tiện, tôi sẽ in ra cho ngài.")
            print(f"Thông tin:\nNhiệt độ: {temperature}\nĐộ ẩm: {feels_like}\nÁp suất: {pressure}")

        elif "làm tốt lắm" in query or "làm rất tốt" in query or "bạn thật tuyệt vời" in query:
            speak("Không có gì , tôi có thể giúp gì thêm cho bạn.")
        elif "có thể làm gì" in query:
            speak("""Bot có thể giúp bạn thực hiện các câu lệnh sau đây:
                1. Chào hỏi
                2. Hiển thị giờ
                3. Mở website, application
                4. Tìm kiếm trên Google
                5. Xem thời tiết
                6. Mở video nhạc
                7. Đọc báo hôm nay
                8. Kể bạn biết về thế giới(tìm trên wikipedia) """)
        else:
            speak(f"{BOTNAME} không thực hiện được lệnh đó")