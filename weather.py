import requests
import json

def get_weather(key,location,days):
    #url="https://api.seniverse.com/v3/weather/daily.json?key=" + key + "&location=" + location + "&language=zh-Hans&unit=c&start=-1&days="+ days
    #url= "https://api.seniverse.com/v3/weather/daily.json?key=S3hlvCzHpv1gUI5IZ&location=neijaing&language=zh-Hans&unit=c&start=-1&days=3"
    url="https://api.seniverse.com/v3/weather/daily.json?key=S3hlvCzHpv1gUI5IZ&location="+ location +"&language=zh-Hans&unit=c&start=-1&days=5"
    res = requests.get(url)
    weather = json.loads(res.text)
    
    location_name = weather["results"][0]["location"]["name"]   # 层级获取地名
    print(location_name)
    daily = weather["results"][0]["daily"]  # 天气预报主要内容部分
    day1 = daily[0] # 第一天天气
    day2 = daily[1] # 第二天天气
    day3 = daily[2] # 第三天天气
    print("日期：%s   白天天气：%s   晚上天气：%s 温度：%s摄氏度~%s摄氏度" % (day1["date"],day1["text_day"],day1["text_night"],day1["low"],day1["high"]))
    print("日期：%s   白天天气：%s   晚上天气：%s 温度：%s摄氏度~%s摄氏度" % (day2["date"],day2["text_day"],day2["text_night"],day2["low"],day2["high"]))
    print("日期：%s   白天天气：%s   晚上天气：%s 温度：%s摄氏度~%s摄氏度" % (day3["date"],day3["text_day"],day3["text_night"],day3["low"],day3["high"]))

if __name__ == "__main__":
    get_weather("S3hlvCzHpv1gUI5IZ","chengdu","3")  