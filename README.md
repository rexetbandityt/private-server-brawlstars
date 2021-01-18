# BrawlStars
A first open source Python 3.8 Brawl Stars Server for version 27!
![ScreenShot](https://cdn.discordapp.com/attachments/800750913891467309/800750985889972254/Screenshot_2021-01-18-18-34-04-026_com.brawl.server.jpg) 

## Client
To connect to your server, you need a custom client. Here the only solution is to use a [pre-made client](https://drive.google.com/file/d/10Ovya5fAx6ksflLfKi1JVZG0AjjXF2Q9/view?usp=drivesdk).
Just edit the IP in the frida-gadget config (```/lib/armeabi-v7a/libgg.config.so```)
```{"interaction":{"interaction":{"type":"script","path":"libscript.so","on_change":"reload","parameters":{"redirectHost":"YOUR_IP","relocate":true}}}```

### Friendly reminder
The server is in a very early state. Right now, it is NOT recommended to run this on a production environment. Please not open issues about missing features, i'm well aware of this. 


