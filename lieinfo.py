import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr


Bl='\033[30m'
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

stderr.writelines(f"""{Re}
     /$$ /$$           /$$$$$$            /$$$$$$         
    | $$|__/          |_  $$_/           /$$__  $$        
    | $$ /$$  /$$$$$$   | $$   /$$$$$$$ | $$  \__//$$$$$$ 
    | $$| $$ /$$__  $$  | $$  | $$__  $$| $$$$   /$$__  $$
    | $$| $$| $$$$$$$$  | $$  | $$  \ $$| $$_/  | $$  \ $$
    | $$| $$| $$_____/  | $$  | $$  | $$| $$    | $$  | $$
    | $$| $$|  $$$$$$$ /$$$$$$| $$  | $$| $$    |  $$$$$$/
    |__/|__/ \_______/|______/|__/  |__/|__/     \______/ 
    [ + ]  C O D E   B Y  L I E  [ + ]  

    
        
    {Wh}[ 1 ] {Re}IP Tracker {Wh}[ 2 ] {Re}Phone Tracker {Wh}[ 0 ] {Re}Exit
""")

input_user = input(f'\n   {Wh}@Lie~# {Wh}') 


if input_user == '1': 
    os.system('clear')
    time.sleep(1)
    stderr.writelines(f"""{Re}

                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!        {Re}--------------------------------
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!        {Re}| {Re}Lie Info Tracker - tools for hacking {Re}|
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!        {Re}|     {Re}github.com/Igthz      {Re}|
               ~?WuxiW*`   `"#$$$$8!!!!??!!!        {Re}--------------------------------
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

    """)

    try:
        def IP_Track():
            ip = input(f"{Wh}\n Enter IP target : {Re}") 
            print()
            print(f'{Wh}= = = = = = = {Re}IP ADDRES INFO {Wh}= = = = = = =')
            req_api = requests.get(f"http://ipwho.is/{ip}") 
            ip_data = json.loads(req_api.text)
            time.sleep(2)
            print(f"{Wh}\n IP target       :{Re}", ip)
            print(f"{Wh} Type IP         :{Re}", ip_data["type"])
            print(f"{Wh} Country         :{Re}", ip_data["country"])
            print(f"{Wh} Country Code    :{Re}", ip_data["country_code"])
            print(f"{Wh} City            :{Re}", ip_data["city"])
            print(f"{Wh} Continent       :{Re}", ip_data["continent"])
            print(f"{Wh} Continent Code  :{Re}", ip_data["continent_code"])
            print(f"{Wh} Region          :{Re}", ip_data["region"])
            print(f"{Wh} Region Code     :{Re}", ip_data["region_code"])
            print(f"{Wh} Latitude        :{Re}", ip_data["latitude"])
            print(f"{Wh} Longitude       :{Re}", ip_data["longitude"])
            lat = int(ip_data['latitude'])
            lon = int(ip_data['longitude'])
            print(f"{Wh} Maps            :{Re}",f"https://www.google.com/maps/@{lat},{lon},8z")
            print(f"{Wh} EU              :{Re}", ip_data["is_eu"])
            print(f"{Wh} Postal          :{Re}", ip_data["postal"])
            print(f"{Wh} Calling Code    :{Re}", ip_data["calling_code"])
            print(f"{Wh} Capital         :{Re}", ip_data["capital"])
            print(f"{Wh} Borders         :{Re}", ip_data["borders"])
            print(f"{Wh} Country Flag    :{Re}", ip_data["flag"]["emoji"])
            print(f"{Wh} ASN             :{Re}", ip_data["connection"]["asn"])
            print(f"{Wh} ORG             :{Re}", ip_data["connection"]["org"])
            print(f"{Wh} ISP             :{Re}", ip_data["connection"]["isp"])
            print(f"{Wh} Domain          :{Re}", ip_data["connection"]["domain"])
            print(f"{Wh} ID              :{Re}", ip_data["timezone"]["id"])
            print(f"{Wh} ABBR            :{Re}", ip_data["timezone"]["abbr"])
            print(f"{Wh} DST             :{Re}", ip_data["timezone"]["is_dst"])
            print(f"{Wh} Offset          :{Re}", ip_data["timezone"]["offset"])
            print(f"{Wh} UTC             :{Re}", ip_data["timezone"]["utc"])
            print(f"{Wh} Current Time    :{Re}", ip_data["timezone"]["current_time"])
        if __name__ == '__main__':
            IP_Track()
    except KeyboardInterrupt:
        print(f" {Wh}[{Ye}!{Wh}] {Ye}PROGRAM STOPPED...")

elif input_user == '2': #OPSI 2
    os.system('clear')
    time.sleep(1)
    stderr.writelines(f"""{Re}

                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!        {Re}--------------------------------
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!        {Re}| {Re}Lie Info Tracker - tools for hacking {Re}|
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!        {Re}|     {Re}github.com/Igthz      {Re}|
               ~?WuxiW*`   `"#$$$$8!!!!??!!!        {Re}--------------------------------
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

    """)

    try:
        def phoneGW():
            User_phone = input(f"\n {Wh}Enter phone number target {Gr}Ex [+5521xxxxxxxxx] {Wh}: {Re}") 
            default_region = "ID" 

            parsed_number = phonenumbers.parse(User_phone, default_region) 
            region_code = phonenumbers.region_code_for_number(parsed_number)
            jenis_provider = carrier.name_for_number(parsed_number, "en")
            location = geocoder.description_for_number(parsed_number, "id")
            is_valid_number = phonenumbers.is_valid_number(parsed_number)
            is_possible_number = phonenumbers.is_possible_number(parsed_number)
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
            number_type = phonenumbers.number_type(parsed_number)
            timezone1 = timezone.time_zones_for_number(parsed_number)
            timezoneF = ', '.join(timezone1)

            print(f"\n {Wh}= = = = = {Re}SHOW INFORMATION PHONE NUMBERS {Wh}= = = = =")
            print(f"\n {Wh}Location             :{Re} {location}")
            print(f" {Wh}Region Code          :{Re} {region_code}")
            print(f" {Wh}Timezone             :{Re} {timezoneF}")
            print(f" {Wh}Operator             :{Re} {jenis_provider}")
            print(f" {Wh}Valid number         :{Re} {is_valid_number}")
            print(f" {Wh}Possible number      :{Re} {is_possible_number}")
            print(f" {Wh}International format :{Re} {formatted_number}")
            print(f" {Wh}Mobile format        :{Re} {formatted_number_for_mobile}")
            print(f" {Wh}Original number      :{Re} {parsed_number.national_number}")
            print(f" {Wh}E.164 format         :{Re} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
            print(f" {Wh}Country code         :{Re} {parsed_number.country_code}")
            print(f" {Wh}Local number         :{Re} {parsed_number.national_number}")
            if number_type == phonenumbers.PhoneNumberType.MOBILE:
                print(f" {Wh}Type                 :{Re} This is a mobile number")
            elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
                print(f" {Wh}Type                 :{Re} This is a fixed-line number")
            else:
                print(f" {Wh}Type                 :{Re} This is another type of number")
        if __name__ == '__main__':
            phoneGW()
    except KeyboardInterrupt:
        print(f" {Wh}[{Ye}!{Wh}] {Ye}PROGRAM STOPPED...")
    
elif input_user == '0': 
    print(f"\n  {Wh}[{Ye}!{Wh}] {Ye}thx for using this tool {Ye}LieInfo")
else:
    print(f" {Ye}No have options in this number!") 
