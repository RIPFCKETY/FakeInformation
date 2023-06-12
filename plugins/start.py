# Coded By R.I.P
# Telegram : t.me/RIP_PROJECTS/
from pyrogram import Client , filters
from pyrogram.types import Message , InlineKeyboardButton , InlineKeyboardMarkup , CallbackQuery
from faker import Faker

Countries = InlineKeyboardMarkup(
          [
            [
                 InlineKeyboardButton(text="List of countries" , callback_data="a")
            ],
            [
                 InlineKeyboardButton(text="en_US 🇺🇸" , callback_data="en_US"),
                 InlineKeyboardButton(text="fa_IR 🇮🇷" , callback_data="fa_IR"),
                 InlineKeyboardButton(text="fr_FR 🇫🇷" , callback_data="fr_FR")
            ],
            [
                 InlineKeyboardButton(text="ar_AE 🇦🇪" , callback_data="ar_AE"),
                 InlineKeyboardButton(text="en_GB 🇬🇧" , callback_data="en_GB"),
                 InlineKeyboardButton(text="de_DE 🇩🇪" , callback_data="de_DE")
            ],
            [
                 InlineKeyboardButton(text="tr_TR	🇹🇷" , callback_data="tr_TR"),
                 InlineKeyboardButton(text="ru_RU	🇷🇺" , callback_data="ru_RU"),
                 InlineKeyboardButton(text="fr_CA 🇨🇦" , callback_data="fr_CA")
            ]
          ]
          )

regenerate_us = InlineKeyboardMarkup(
     [
          [
               InlineKeyboardButton(text="Regenerate" , callback_data="regenerate_us")
          ]
     ]
     )
regenerate_fa = InlineKeyboardMarkup([[InlineKeyboardButton(text="Regenerate" , callback_data="regenerate_fa")]])
regenerate_fr = InlineKeyboardMarkup([[InlineKeyboardButton(text="Regenerate" , callback_data="regenerate_fr")]])
regenerate_ae = InlineKeyboardMarkup([[InlineKeyboardButton(text="Regenerate" , callback_data="regenerate_ae")]])
regenerate_gb = InlineKeyboardMarkup([[InlineKeyboardButton(text="Regenerate" , callback_data="regenerate_gb")]])
regenerate_de = InlineKeyboardMarkup([[InlineKeyboardButton(text="Regenerate" , callback_data="regenerate_de")]])
regenerate_tr = InlineKeyboardMarkup([[InlineKeyboardButton(text="Regenerate" , callback_data="regenerate_tr")]])
regenerate_ru = InlineKeyboardMarkup([[InlineKeyboardButton(text="Regenerate" , callback_data="regenerate_ru")]])
regenerate_ca = InlineKeyboardMarkup([[InlineKeyboardButton(text="Regenerate" , callback_data="regenerate_ca")]])


print("Online!")

@Client.on_message()
async def start_private(client : Client , message : Message):
     try:
          await client.get_chat_member("USERNAMECHNNEL", message.chat.id)
         
     except:
          await message.reply_text("⚜️Please Join Channel And Send Again /start⚜️\n🆔 : @USERNAMECHNNEL")
          return False
     

     if message.text == "/start":
          await message.reply_text(f"Hello {message.from_user.first_name}!\nWelcome to fake information bot")
          await message.reply_text("Countries I can generator fake information ",reply_markup=Countries)


@Client.on_callback_query()
async def privatecallback( client : Client , call : CallbackQuery):
     if call.data == "en_US":
          faker = Faker("en_US")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_us)
          
     elif call.data == "regenerate_us":
          faker = Faker("en_US")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_us)
          
     elif call.data == "fa_IR":
          faker = Faker("fa_IR")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_fa)
          
     elif call.data == "regenerate_fa":
          faker = Faker("fa_IR")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_fa)
          
     elif call.data == "fr_FR":
          faker = Faker("fr_FR")
          Faker.seed(2)
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_fr)
          
     elif call.data == "regenerate_fr":
          faker = Faker("fr_FR")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_fr)
          
     elif call.data == "ar_AE":
          faker = Faker("ar_AE")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_ae)
          
     elif call.data == "regenerate_ae":
          faker = Faker("ar_AE")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_ae)
          
     elif call.data == "en_GB":
          faker = Faker("en_GB")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_gb)
          
     elif call.data == "regenerate_gb":
          faker = Faker("en_GB")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_gb)
          
     elif call.data == "de_DE":
          faker = Faker("de_DE")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_de)
          
     elif call.data == "regenerate_de":
          faker = Faker("de_DE")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_de)
          
     elif call.data == "tr_TR":
          faker = Faker("tr_TR")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_tr)
          
     elif call.data == "regenerate_tr":
          faker = Faker("tr_TR")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_tr)
          
     elif call.data == "ru_RU":
          faker = Faker("ru_RU")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_ru)
          
     elif call.data == "regenerate_ru":
          faker = Faker("ru_RU")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_ru)
          
     elif call.data == "fr_CA":
          faker = Faker("fr_CA")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_ca)
          
     elif call.data == "regenerate_ca":
          faker = Faker("fr_CA")
          
          fullname = faker.name()
          job = faker.job() 
          address = faker.address() 
          favorite_color = faker.color_name() 
          credit_card = faker.credit_card_full()
          ID_Credit = faker.bban()
          ipv4P = faker.ipv4_private()
          ipv4 = faker.ipv4()
          ipv6 = faker.ipv6()
          await call.message.reply_text(f"""

Fullname : **{fullname}**
Job : **{job}**
Address : **{address}**
Favorite Color : **{favorite_color}**
IPV4 Private : **{ipv4P}**
IPV4 : **{ipv4}**
IPV6 : **{ipv6}**
ID Credit Card : **{ID_Credit}**
Credit Card : \n**{credit_card}**
                                        """,reply_markup=regenerate_ca)
          
     else : 
          await call.message.reply_text("**Unknown Request🔴**")