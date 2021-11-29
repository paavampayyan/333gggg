from pyrogram import Client
from pyrogram import filters
import requests
import os
import facebook

#==============================================fb
token = 'EAAbVQUjLkf4BANZCDCtgZAai8O3IKcZBcY6e3XaTn3rHjMrFEDYqh9aQjt0vdp6mEq8GO1axsXM72IOgvPM8fCZCZAHigukO4ZCubIcEGRwA5ijZBnr42mlkwubBScjvdEWOkBYn0kNEzdUXNZB1pL7JHF9x18TdlOGBalfzonZB5ZBCslXjGow5iTtkXpQ3T1N5GdJuQpLFnLwgZDZD'
url='https://graph-video.facebook.com/134800443799546/videos?access_token='+str(token)
fb = facebook.GraphAPI(token)
#==============================================end

video="home/test.mp4"
dfcaption = "കൂടുതൽ വീഡിയോസിനായി നമ്മുടെ ടെലിഗ്രാം ചാനലിൽ ജോയിൻ ചെയ്യൂ 😍😍 👉  https://t.me/whatsapp_statusvideos_malayalam "

app = Client("fbbot",
             api_id=1280226,
             api_hash='40c6be639fd3e699783cbb43c511cef0', 
             bot_token='1570190201:AAFlXm3P-qHB21QeN-AKoP3YScZUV9Um-os')

@app.on_message(filters.command('start'))
def start(client, message):
    
    message.reply_text("hello i am alive bro")

@app.on_message(filters.command('fv'))
def fb_upload(client, message):
    
    if not message.reply_to_message:
        message.reply_text("Error. reply to a message to upload post.")
        return
    if message.reply_to_message.video:
        m = message.reply_text("Downloading 🩸")
    
    target = message.reply_to_message.video.file_id
    print(target)
    client.download_media(target, file_name=f"res/fbpost-{message.message_id}.mp4")
    
    
    
    text = ''
    for i in message.command[1:]:
        text += ' ' + str(i)
    print(text)
    fcap = str(text)
    if fcap == "":
        pcap = dfcaption
    else:
        pcap = (f"{fcap}\n\n{dfcaption}")
    
    m.edit(f"**trying to upload and caption is ** : {pcap}")
        
        
    try:
        post = requests.post(url, files={"file": open(f"res/fbpost-{message.message_id}.mp4", "rb")}, data={"description": f"{pcap}",
                                                                                                            "title" : f"{pcap}"})
        print(post)
        m.edit("successfully Uploaded 😎")
    except Exception as e :
        m.edit(e)
    os.remove(f"res/fbpost-{message.message_id}.mp4")
     
@app.on_message(filters.command('fp'))
def fb_photo(client, message):
    
    if not message.reply_to_message:
        message.reply_text("Error. reply to a message to upload post.")
        return
    if message.reply_to_message.photo:
        m = message.reply_text("Downloading 🩸")
    
    target = message.reply_to_message.photo.file_id
    print(target)
    client.download_media(target, file_name=f"res/fbpost-{message.message_id}.jpg")
    
    
    
    text = ''
    for i in message.command[1:]:
        text += ' ' + str(i)
    print(text)
    fcap = str(text)

    
    m.edit(f"**trying to upload and caption is ** : {fcap}")
        
        
    try:
        fb.put_photo(open(f"res/fbpost-{message.message_id}.jpg", "rb"), message=f"{fcap}")
        m.edit("successfully Uploaded 😎")
    except Exception as e :
        m.edit(e)
    os.remove(f"res/fbpost-{message.message_id}.jpg")

app.run()
