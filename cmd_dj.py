import os
import yt_dlp
import pyfiglet
from termcolor import colored
import keyboard
import subprocess
import random

# === Tracks (YOUTUBE) ===
vibes = {
    "chill": [
    "https://www.youtube.com/watch?v=-SSgaCAsU6M",   # Rod Wave - 25
    "https://youtu.be/3MLjfnouo88?si=DYwe-Svj4bBmLoCP",   # NoCap - Vaccine?
    "https://www.youtube.com/watch?v=k-z52Y1MoSY",   # Rod Wave - Last Lap
    "https://www.youtube.com/watch?v=3c4AdX7H2A0",   # Loe Shimmy - Permanent Scarz
    "https://www.youtube.com/watch?v=46p-IxAVJ74",   # Chris Brown - Residuals
    "https://www.youtube.com/watch?v=_bptrMV3zHE",   # Yung Bleu - You're Mines Still (feat. Drake)
    "https://www.youtube.com/watch?v=hwkq1qlVbqc",   # 2:00am Soul R&B Bedroom Playlist | SZA, Miguel, PARTYNEXTDOOR, Brent Faiyaz, Kehlani Mix by HelloVee
    "https://www.youtube.com/watch?v=Jx9h3iWudTU",   # Mariah the Scientist - Burning Blue
    "https://www.youtube.com/watch?v=Ygfj6uNlRRo",   # Rylo Rodriguez - Set Me Free
    "https://www.youtube.com/watch?v=tQg5-6DHxQY",   # Fridayy & Meek Mill - Proud Of Me
    "https://www.youtube.com/watch?v=NE5Owakuj8I",   # Fridayy - Without You
    "https://www.youtube.com/watch?v=cB5e0zHRzHc",   # Usher - Love in This Club ft. Young Jeezy
    "https://www.youtube.com/watch?v=X_yyDbsNUWQ",   # Plies - Bust It Baby Pt. 2 (Feat. Ne-Yo)
    "https://www.youtube.com/watch?v=0habxsuXW4g",   # Mariah Carey - We Belong Together
    "https://www.youtube.com/watch?v=3SoYkCAzMBk",   # Tevin Campbell - Can We Talk
    "https://www.youtube.com/watch?v=7flrKMGfwjw",   # New Edition - Can You Stand The Rain
    "https://www.youtube.com/watch?v=caNRc1ER8p4",   # Shai - If I Ever Fall In Love
    "https://www.youtube.com/watch?v=y5pD4nBabMk",   # Jon B. - They Don't Know
    "https://www.youtube.com/watch?v=JpGKWUdRnXE"    # Dave - Location (ft. Burna Boy)
    "https://www.youtube.com/watch?v=ZX_mvoY_Hg0",   #1 Drake - Not You Too ft. Chris Brown
    "https://www.youtube.com/watch?v=Cfs3tk78Qxo",   # Close With Desires - Teo Glacier
    "https://www.youtube.com/watch?v=pa5E4uA3ALY",   # Brent Faiyaz - TRUST
    "https://www.youtube.com/watch?v=O5amIdSD8eI",   # Post Malone - Goodbyes ft. Young Thug
    "https://www.youtube.com/watch?v=XP0fdtXn49s",   # Roy Woods - Drama feat. Drake
    "https://www.youtube.com/watch?v=0Exxu8lsGYE",   # SZA - Broken Clocks
    "https://www.youtube.com/watch?v=Sv5yCzPCkv8",   # SZA - Snooze
    "https://www.youtube.com/watch?v=0BdlKkvjEgA",   # SZA - Good Days
    "https://www.youtube.com/watch?v=iwyAxyE2Ajg",   # SZA - I Hate U
    "https://www.youtube.com/watch?v=-zzP29emgpg",   # Drake - Take Care ft. Rihanna
    "https://www.youtube.com/watch?v=LCnzvyUC57M",   # Drake - Good Ones Go
    "https://www.youtube.com/watch?v=ox7RsX1Ee34",   # Kendrick Lamar - LOVE. ft. Zacari
    "https://www.youtube.com/watch?v=iOpJywrdCuQ",   # Bryson Tiller - Exchange
    "https://www.youtube.com/watch?v=zHZVV02osIw",   # H.E.R. - Could've Been ft. Bryson Tiller
    "https://www.youtube.com/watch?v=FtaW6YMAafk",   # Bryson Tiller - Outta Time ft. Drake
    "https://www.youtube.com/watch?v=THVbtGqEO1o",   # Drake - Fair Trade ft. Travis Scott
    "https://www.youtube.com/watch?v=2_gLD1jarfU",   # Drake - Slime You Out ft. SZA
    "https://www.youtube.com/watch?v=ZlJaInjGAOA",   # DJ Khaled - Beautiful Feat. Future & SZA
    "https://www.youtube.com/watch?v=SQYOL9qU6TY",   # Drake-Jungle
    "https://www.youtube.com/watch?v=fhEqtynX_xc",   # Drake - TSU
    "https://www.youtube.com/watch?v=3tnb2o-cV_0",   # Jhené Aiko - Sativa ft. Swae Lee
    "https://www.youtube.com/watch?v=QvR5JX6hsmE",   # Mariah the Scientist - Spread Thin
    "https://www.youtube.com/watch?v=b8M6N0FTpNc",   # Drake - Girls Want Girls ft. Lil Baby
    "https://www.youtube.com/watch?v=QbskDhzKWk8",   # Jhené Aiko - Stay Ready (What A Life) ft. Kendrick Lamar
    "https://www.youtube.com/watch?v=o_6HGBsMHeA",   # Summer Walker - Playing Games (Extended Version) Feat. Bryson Tiller
    "https://www.youtube.com/watch?v=Xe6OJvzzClM",   # Dave - Starlight
    "https://www.youtube.com/watch?v=cqV2-6sZ01c",   # Drake - Time Flies
    "https://www.youtube.com/watch?v=sZRl7ns3aQI",   # Drake - wants And Needs ft. Lil Baby
    "https://www.youtube.com/watch?v=Y2QpQP8wPG8",   # Future - WAIT FOR U ft. Drake, Tems
    "https://www.youtube.com/watch?v=d7cVLE4SaN0",   # Bryson Tiller - Don't
    "https://www.youtube.com/watch?v=vBy7FaapGRo",   # Daniel Caesar - Best Part ft. H.E.R.
    "https://www.youtube.com/watch?v=PAFAfhod9TU",   # H.E.R. - Damage 
    "https://www.youtube.com/watch?v=uwIIVeGq4Xg",   # Kaash Paige - Love Songs
    "https://www.youtube.com/watch?v=jGMCfshaJuw"    # Drake - Fire & Desire
    ],  
    "trap": [
        "https://www.youtube.com/watch?v=A0mP6H1FOjs",   # Loe Shimmy - Two Faced (feat. YTB Fatt)
        "https://www.youtube.com/watch?v=0yfSqUiSGjE",   # Big Yavo - Faking The Funk
        "https://www.youtube.com/watch?v=pjXdDjUWkjk",   # YoungBoy Never Broke Again - B*tch Let's Do It
        "https://www.youtube.com/watch?v=VoydA7rV5ns",   # Big Yavo - Why You Mad
        "https://www.youtube.com/watch?v=JVDUsaqgSq0",   # BigXthaPlug - 2AM
        "https://www.youtube.com/watch?v=3QwZjhHcLZk",   # BigXthaPlug - The Largest
        "https://www.youtube.com/watch?v=iX85sLKJg2A",   # Future - PLUTOSKI
        "https://www.youtube.com/watch?v=-705T4FioZE",   # Gunna & Future - pushin P (feat. Young Thug)
        "https://www.youtube.com/watch?v=BTivsHlVcGU",   # DJ Khaled - EVERY CHANCE I GET (ft. Lil Baby, Lil Durk)
        "https://www.youtube.com/watch?v=U2SNwtE-0Us",   # Nardo Wick - Who Want Smoke?? ft. Lil Durk, 21 Savage & G Herbo
        "https://www.youtube.com/watch?v=pDddlvCfTiw",   # CENTRAL CEE FT. LIL BABY - BAND4BAND
        "https://www.youtube.com/watch?v=pSY3i5XHHXo",   # Central Cee x Dave - Sprinter
        "https://www.youtube.com/watch?v=Z4N8lzKNfy4",   # Lil Durk - All My Life ft. J. Cole
        "https://www.youtube.com/watch?v=H58vbez_m4E",   # Kendrick Lamar - Not Like Us
        "https://www.youtube.com/watch?v=pGsetzZscws",   # Young Nudy - Peaches & Eggplants ft. 21 Savage
        "https://www.youtube.com/watch?v=brJtbkV6Yq4",   # ROB49 - WTHELLY
        "https://www.youtube.com/watch?v=x24qP3sjrvw",   # BossMan Dlow - Shake Dat Ass
        "https://www.youtube.com/watch?v=cIG5gSp-Wa8",   # BossMan Dlow - Mo Chicken Ft. French Montana
        "https://www.youtube.com/watch?v=-KKbdErJkiY",   # Rich Homie Quan - Type of Way
        "https://www.youtube.com/watch?v=boqqoQbIYdU",   # Young Dolph - Preach
        "https://www.youtube.com/watch?v=Vzkr-G1QEh8",   # Finesse2Tymes - Back End
        "https://www.youtube.com/watch?v=0-Tm65i96TY",   # Pooh Shiesty - Back In Blood (feat. Lil Durk)
        "https://www.youtube.com/watch?v=yt7rJzhuN1c",   # Big Boogie - Mental Healing
        "https://www.youtube.com/watch?v=BTivsHlVcGU",   # DJ Khaled - EVERY CHANCE I GET ft. Lil Baby, Lil Durk
        "https://www.youtube.com/watch?v=WyhU6Zb_fhY",   # Lil Baby - California Breeze
        "https://www.youtube.com/watch?v=NwfVDKGkZfo",   # BossMan Dlow - Finesse ft. GloRilla
        "https://www.youtube.com/watch?v=KmhAQJqOaIY",   # BossMan Dlow - Get In With Me
        "https://www.youtube.com/watch?v=_q6go0G49A0",   # Lil Durk - AHHH HA
        "https://www.youtube.com/watch?v=W4aE8of2znM"    # Young Thug - Money On Money (feat. Future)
        "https://www.youtube.com/watch?v=SxAp27sFaIM"    # Lil Uzi Vert - The Way Life Goes Remix (Feat. Nicki Minaj)
    ],
    "gospel": [
        "https://www.youtube.com/watch?v=CQt4xBGwaI4",   # Marvin Sapp -    The Best In Me
        "https://www.youtube.com/watch?v=BZT8jqsc8lQ",   # Tasha Cobbs  - Your Spirit ft. Kierra Sheard
        "https://www.youtube.com/watch?v=XvV9p-wU4hk",   # Take Me to the King (feat. Kirk Franklin)
        "https://www.youtube.com/watch?v=q2Mwqf40x48",   # Tasha Cobbs - Break Every Chain (Live)
        "https://www.youtube.com/watch?v=MwUoypd-SKE",   # Tasha Cobbs - Put a Praise On It (feat. Kierra Sheard)
        "https://www.youtube.com/watch?v=2x9efwgb9ag",   # Tasha Cobbs Leonard - I'm Getting Ready ft. Nicki Minaj
        "https://youtu.be/fjvvsw_f9jw",                  # Melvin Crispell, III - God Is (Live)
        "https://youtu.be/BQ2iFZPapZs",                  # Tamela Mann - Help Me ft. The Fellas
        "https://youtu.be/ITAhCE9O_lA",                  # Kirk Franklin - Try Love
        "https://youtu.be/UuuZMg6NVeA",                  # Hezekiah Walker New Video "Every Praise"
        "https://youtu.be/nqPLhgy4yLc",                  # Marvin Sapp - Never Would Have Made It
        "https://www.youtube.com/watch?v=tu9j_n0gihE",   # God Favored Me (Extended Version)
        "https://www.youtube.com/watch?v=B0jB1Qudu-U",   # The Georgia Mass Choir - Come On In The Room
        "https://www.youtube.com/watch?v=S0tX_ctp0Gs",   # Donnie McClurkin - We Fall Down
        "https://www.youtube.com/watch?v=Sur8dkPX4l4",   # Yolanda Adams - The Battle Is The Lord's
    ],
    "country": [
        "https://www.youtube.com/watch?v=4QIZE708gJ4",   # Post Malone - I Had Some Help (feat. Morgan Wallen)
        "https://www.youtube.com/watch?v=wIA-4LeRgsc",   # Morgan Wallen - I’m The Problem
        "https://www.youtube.com/watch?v=e7MJrFerYg8",   # Ryan Robinette - Way Back
        "https://www.youtube.com/watch?v=dRX0wDNK6S4",   # Kane Brown - Heaven
        "https://www.youtube.com/watch?v=p_IwENcMPOA",   # Thomas Rhett - Marry Me
        "https://www.youtube.com/watch?v=jLCHpZ6B1gU",   # Jason Aldean - You Make It Easy
        "https://www.youtube.com/watch?v=fM8V1XOI-14",   # Kane Brown - What Ifs ft. Lauren Alaina
        "https://www.youtube.com/watch?v=Thvm6dADOms",   # Brett Young - Mercy
        "https://www.youtube.com/watch?v=c4qgqNS_20s",   # Dan + Shay - Tequila
        "https://www.youtube.com/watch?v=2dPDBU9MC8c",   # Scotty McCreery - Five More Minutes
        "https://www.youtube.com/watch?v=0hjqGN-9anA",   # Jordan Davis - Singles You Up
        "https://www.youtube.com/watch?v=i_nLsG_asQg",   # Blake Shelton - I Lived It
        "https://www.youtube.com/watch?v=uXyxFMbqKYA",   # Luke Combs - When It Rains It Pours
        "https://www.youtube.com/watch?v=pz9yRC-LWhU",   # Dustin Lynch - Small Town Boy
        "https://www.youtube.com/watch?v=4OCcOsPrOeE",   # Midland - Drinkin' Problem (Brindemos) (Static Version) ft. Jay de la Cueva
        "https://www.youtube.com/watch?v=n76vfupfmEc",   # Miley Cyrus - The Bitch Is Back
        "https://www.youtube.com/watch?v=A56p-ZSZ5Vc",   # Walker Hayes - You Broke Up with Me
        "https://www.youtube.com/watch?v=sI0TeFf6uD8",   # Chris Stapleton - Broken Halos
        "https://www.youtube.com/watch?v=CwKp6Xhy3_4",   # Chris Young - Hangin' On
        "https://www.youtube.com/watch?v=Mdh2p03cRfw",   # Sam Hunt - Body Like A Back Road
        "https://www.youtube.com/watch?v=aHl0tlUYDBI",   # LANCO - Greatest Love Story
        "https://www.youtube.com/watch?v=ntCMoh-0ogo",   # Devin Dawson - All On Me
        "https://www.youtube.com/watch?v=PG2azZM4w4o",   # Brett Young - Like I Loved You
        "https://www.youtube.com/watch?v=HAj7Ble3ixg",   # Tegan Marie – “Keep It Lit”
        "https://www.youtube.com/watch?v=WUFpGGe8U_E",   # Brantley Gilbert - The Ones That Like Me
        "https://www.youtube.com/watch?v=7qaHdHpSjX8",   # Brett Young - In Case You Didn't Know
        "https://www.youtube.com/watch?v=idD1C2-ISlo",   # Keith Urban - Parallel Line
        "https://www.youtube.com/watch?v=77qc4ZtufzM",   # Morgan Wallen - Up Down ft. Florida Georgia Line
        "https://www.youtube.com/watch?v=WU1C-zXDHis",   # Cole Swindell - "Break Up In The End"
        "https://www.youtube.com/watch?v=oUqJftD86-o",   # Lee Brice - Boy
        "https://www.youtube.com/watch?v=HgknAaKNaMM",   # Carrie Underwood - The Champion ft. Ludacris
        "https://www.youtube.com/watch?v=pqdaskhEa0I",   # Tim McGraw, Faith Hill - The Rest of Our Life
        "https://www.youtube.com/watch?v=pAsN4lSa7O0",   # Blake Shelton - I'll Name The Dogs
        "https://www.youtube.com/watch?v=A56p-ZSZ5Vc",   # Walker Hayes - You Broke Up with Me
        "https://www.youtube.com/watch?v=_qSW96a2aKY",   # Keith Urban - Female
        "https://www.youtube.com/watch?v=WI7YCYR4EyM",   # Ashley McBryde - A Little Dive Bar In Dahlonega
        "https://www.youtube.com/watch?v=_T8ml-P0GkI",   # Thomas Rhett - Unforgettable
        "https://www.youtube.com/watch?v=GzT4p-OaJ5c",   # Keith Urban - The Fighter ft. Carrie Underwood
        "https://www.youtube.com/watch?v=3yyZ0UOZgcQ",   # Luke Bryan - Light It Up
        "https://www.youtube.com/watch?v=Cg4Eui4sGlk"    #40 Jon Pardi - Heartache On The Dance Floor
    ]
}
def get_audio_url(youtube_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'skip_download': True,
        'extract_flat': False,
        'forceurl': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        return info['url'], info.get('title', 'Unknown Track')

def print_ascii_banner(text, color='cyan'):
    ascii_art = pyfiglet.figlet_format(text[:50])
    print(colored(ascii_art, color))
    
def run_mpv(url):
    return subprocess.Popen(["mpv", "--no-video", url])

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(colored("🎧 Welcome to Command Line DJ 🎧", "magenta"))
    print(colored("     Made By Joseph Morrison", "green"))
    print("Pick a vibe: chill / trap / gospel / country")
    vibe = input("> ").lower()

    if vibe not in vibes:
        print("Invalid vibe. Try again.")
        return

    playlist = random.sample(vibes[vibe], len(vibes[vibe]))

    for url in playlist:
        audio_url, title = get_audio_url(url)
        print_ascii_banner(title, "green")

        player = run_mpv(audio_url)

        while True:
            if keyboard.is_pressed("n"):
                player.terminate()
                break
            elif keyboard.is_pressed("space"):
                player.send_signal(19 if os.name != "nt" else 1)  # pause (ignore on win)
            elif keyboard.is_pressed("q"):
                player.terminate()
                print("🛑 Quitting Command Line DJ...")
                return

if __name__ == "__main__":
    main()
