import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from buttons import *
from aiogram.types import Message,CallbackQuery
import sqlite3

logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    conn = sqlite3.connect("User_info.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
        id INTEGER,
        Username varchar(30),
        tel INTEGER NULL,
        kor1 BIGINT NULL,
        kor2 BIGINT NULL
        )""")
    conn.commit()


    user_id = message.chat.id
    username = message.from_user.username
    cursor.execute(f"SELECT id FROM Users WHERE id = {user_id}")
    data = cursor.fetchone()

    if data is None:
        cursor.execute("INSERT INTO Users VALUES ({},'{}',NULL,NULL,NULL)".format(user_id,username))
        conn.commit()
        await message.answer(f"""Juda yaxshi keling birgalikda buyurtma beramiz😊""", reply_markup=buyurtma) 
    else:
        await message.answer(f"""Juda yaxshi keling birgalikda buyurtma beramiz😊""", reply_markup=buyurtma) 


# @dp.message_handler(text = "🇺🇿 O'zbekcha")
# async def uzb(message: types.Message):
#     await message.answer(f"""Assalomu alaykum {message.from_user.first_name}. Men Safo Go'sht yetkazib berish xizmati botiman!
# Buyurtma berishingiz uchun telefon nomeringizni yuboring""", parse_mode="HTML", reply_markup=kontakt)


@dp.message_handler(text="📄 Menu")
async def Menu(message:Message):
    await message.answer("""<b>📍Manzilingizni yuboring</b>""",parse_mode="HTML",reply_markup=geolakatsya)


@dp.message_handler(text="⚙️Sozlamalar")
async def Menu(message:Message):
    await message.answer("""<b>Sozlamalar vaqtinchalik mavjud emas</b>""",parse_mode="HTML",reply_markup=buyurtma)


@dp.message_handler(text="👨‍👩‍👦Biz haqimizda")
async def biz_haqimizda(message:Message):
    await message.answer_photo(
        photo=open('images/Manzil.jpg','rb'),
        caption="""<b>Manzil: Shahriston ko'chasi 83a</b>""",parse_mode = "HTML",reply_markup=knpka_orqaga)

@dp.message_handler(text="⬅️Orqaga")
async def Orqaga1(message:Message):
    await message.answer("""<b>Juda yaxshi keling birgalikda buyurtma beramiz😊</b>""",parse_mode="HTML",reply_markup=buyurtma)


@dp.message_handler(text="📋Ma'lumot")
async def malumot(message:Message):
    await message.answer_photo(
        photo=open('images/Telefon_nomer.jpg','rb'),
        caption="""<b>Tel: +998 33 77 303 77</b>""",parse_mode = "HTML",reply_markup=knpka_orqaga)


@dp.message_handler(content_types=["location"])
async def location(message:Message):
    conn = sqlite3.connect("User_info.db")
    cursor = conn.cursor()
    user_id = message.chat.id
    kor1 = message.location.latitude
    kor2 = message.location.longitude
    cursor.execute(f"UPDATE Users SET kor1 = {kor1},kor2 = {kor2} WHERE id = {user_id}")
    conn.commit()
    await message.answer("""<b>📍Manzilni to'g'ri yubordingizmi?</b>""",parse_mode="HTML",reply_markup=knopka)

@dp.message_handler(text="✅Xa")
async def Xa(message:Message):
    await message.answer("""<b>👇Telefon nomeringizni yuboring</b>""",parse_mode="HTML",reply_markup=kontakt)


@dp.message_handler(text="❌Yo'q")
async def Yoq(message:Message):
    await message.answer("""<b>Manzilingizni boshidan yuboring</b>""",parse_mode="HTML",reply_markup=geolakatsya)
   


@dp.message_handler(content_types=["contact"])
async def contact(message):
    conn = sqlite3.connect("User_info.db")
    cursor = conn.cursor()
    user_id = message.chat.id
    telefon_raqam = int(message.contact['phone_number'])
    cursor.execute(f"UPDATE Users SET tel = {telefon_raqam} WHERE id = {user_id}")
    conn.commit()
    await message.answer(f"""Sizning ma'lumotlaringiz tasdiqlandi:""",reply_markup=menu)
    cursor.execute(f"SELECT * FROM Users WHERE id = {user_id}")
    data = cursor.fetchone()
    await bot.send_message(1734391430,f"ID: #{data[0]}\nUsername : @{data[1]}\nTelefon Raqami: +{data[2]}\n\n Joylashuvi:👇👇👇")
    await bot.send_location(1734391430,data[3],data[4])
    await bot.send_message(622321207,f"ID: #{data[0]}\nUsername : @{data[1]}\nTelefon Raqami: +{data[2]}\n\n Joylashuvi:👇👇👇")
    await bot.send_location(622321207,data[3],data[4])
    await bot.send_message(279361769,f"ID: #{data[0]}\nUsername : @{data[1]}\nTelefon Raqami: +{data[2]}\n\n Joylashuvi:👇👇👇")
    await bot.send_location(279361769,data[3],data[4])

@dp.message_handler(text="Orqaga")
async def Orqaga(message:Message):
    await message.answer("""<b>📍Manzilingizni yuboring</b>""",parse_mode="HTML",reply_markup=geolakatsya)
    


@dp.message_handler(text="Ortga")
async def Ortga(message:Message):
    await message.answer("""<b>Juda yaxshi keling birgalikda buyurtma beramiz😊</b>""",parse_mode="HTML",reply_markup=buyurtma)
    


@dp.message_handler(text="⬅️Ortga")
async def Ortga1(message:Message):
    await message.answer("""<b>📍Manzilingizni yuboring</b>""",parse_mode="HTML",reply_markup=geolakatsya)
    


@dp.message_handler(text="🐑Qo'y go'sht mahsulotlari")
async def qoy_gosht_m(message:Message):
    await message.answer("""<b>Qo'y Go'sht Mahsulotlari</b>""",parse_mode="HTML",reply_markup=qoy_g_mahBOSHI)
    # await message.delete()

@dp.message_handler(text="🐄Mol go'sht mahsulotlari")
async def mol_gosht_m(message:Message):
    await message.answer("""<b>Mol Go'sht Mahsulotlari</b>""",parse_mode="HTML",reply_markup=mol_tilmahBOSHI)
    # await message.delete()

@dp.message_handler(text="🐴Ot go'sht mahsulotlari")
async def ot_gosht_m(message:Message):
    await message.answer("""<b>Ot Go'sht Mahsulotlari</b>""",parse_mode="HTML",reply_markup=ot_goshtmahBOSHI)
    # await message.delete()


@dp.message_handler(text="🐓Tovuq go'sht mahsulotlari")
async def tovuq_gosht_m(message:Message):
    await message.answer("""<b>Tovuq Go'sht Mahsulotlari</b>""",parse_mode="HTML",reply_markup=tovuq_goshtmahBOSHI)
    # await message.delete()


@dp.message_handler(text="🍖Kalbasa mahsulotlari")
async def kalbasa_gosht_m(message:Message):
    await message.answer("""<b>Kalbasa Go'sht Mahsulotlari</b>""",parse_mode="HTML",reply_markup=Kal_mahBOSHI)
    # await message.delete()


@dp.message_handler(text="🥩Tushonka")
async def tushonka_gosht_m(message:Message):
    await message.answer("""<b>Tushonka Go'sht Mahsulotlari</b>""",parse_mode="HTML",reply_markup=tushonka_mahBOSHI)
    # await message.delete()


@dp.message_handler(text="⬅️Orqaga")
async def ortga_q(message:Message):
    await message.answer("""<b>Juda yaxshi keling birgalikda buyurtma beramiz😊</b>""",parse_mode="HTML",reply_markup=buyurtma)
    await message.delete()



@dp.message_handler(text="Mol + Qo'y Rulet")
async def mol_qoyBOSHI(message:Message):
    await message.answer_photo(
        photo=open('images/mol_qoy_rulet.jpg','rb'),
        caption="""<b>Narxi:   1kg-135.000 so'm
Tarkibi: Tandirda pishirilgan qo’y goshti juda mazali ta’mga ega. Ushbu tansiq taom o’rama ko’rinishda bo’lsachi, bunisiga nima deysiz❓😋 Kesilgan holda odatiy va bayramona dasturhoningizni birdek betakror bezagiga aylanuvchi o’ramani taqdim etishtan mamnunmiz 😊</b>""",parse_mode="HTML",reply_markup=qoy_g_m)
    # await message.delete()

@dp.message_handler(text="Qo'y To'sh Rulet")
async def qoy_toshBOSHI(message:Message):
    await message.answer_photo(
        photo=open('images/qoy_tosh_rulet.jpg','rb'),
        caption="""<b>Narxi:   1kg-150.000 so'm
Tarkibi: Qo'yning sur to'shidan rulet yog'liqni sevuchilar uchun.</b>""",parse_mode="HTML",reply_markup=qoy_g_m1)
    # await message.delete()

@dp.message_handler(text="Qo'y Tandir Rulet")
async def qoy_tandirBOSHI(message:Message):
    await message.answer_photo(
        photo=open('images/qoy_tandir_rulet.jpg','rb'),
        caption="""<b>Narxi:   1kg-165.000 so'm
Tarkibi: Tandirda pishirilgan qo’y goshti juda mazali ta’mga ega. Ushbu tansiq taom o’rama ko’rinishda bo’lsachi, bunisiga nima deysiz❓😋 Kesilgan holda odatiy va bayramona dasturhoningizni birdek betakror bezagiga aylanuvchi o’ramani taqdim etishtan mamnunmiz 😊</b>""",parse_mode="HTML",reply_markup=qoy_tandir)
    # await message.delete()

@dp.message_handler(text="⬅️Ortga qaytish")
async def bosh_menuga_q(message:Message):
    await message.answer("""<b>Safo Go'sht mahsulotlari menusi</b>""",parse_mode="HTML",reply_markup=menu)
    await message.delete()



@dp.message_handler(text="Mol Til Rulet")
async def qoy_tandirBOSHI(message:Message):
    await message.answer_photo(
        photo=open('images/mol_til_rulet.jpg','rb'),
        caption="""<b>Narxi:   1kg-130.000 so'm
Tarkibi: Bu til oramamiz parhez mahsulotlari qatoridan joy olgan. Shu kunlarda siz uchun ayni muddao!</b>""",parse_mode="HTML",reply_markup=mol_tilRuletBOSHI)
    # await message.delete()

@dp.message_handler(text="Mol Press")
async def mol_pressBOSHI(message:Message):
    await message.answer_photo(
        photo=open('images/mol_press.jpg','rb'),
        caption="""<b>Narxi:   1kg-120.000 so'm
        Yogsiz, ajoyib ta’mli, ishtaha ochuvchi ko’rinishga ega bo’lgan mol go’shtidan press 🤤</b>""",parse_mode="HTML",reply_markup=mol_pressBOSHI1)
    # await message.delete()


@dp.message_handler(text="Mol Archa Rulet")
async def mol_archa_ruletBOSHI(message:Message):
    await message.answer_photo(
        photo=open('images/mol_archa_rulet.jpg','rb'),
        caption="""<b>Narxi:   1kg-130000 so'm
Tarkibi: Xilma xillikni xohlovchilar uchun mol go'shtidan archa o’rama 😍. Uning nozik archa ignabarglari  mayin ifor taratadi va ishtahangizni ochadi .Yozning issiq kunlarida ham barchaga yoquvchi mahsulot.  Bu aynan siz istagan narsa. Tanlovda adashmang.😋</b>""",parse_mode="HTML",reply_markup=mol_archa_ruletBOSHI1)
    # await message.delete()


@dp.message_handler(text="Mol Rulet")
async def mol_ruletBOSHI(message:Message):
    await message.answer_photo(
        photo=open('images/mol_rulet.jpg','rb'),
        caption="""<b>Narxi:   1kg-135000 so'm
Tarkibi: Buqa go’shtidan bo’lgan o’rama. 🥩
Tatib ko’rmoqchimisiz❓
Bu o’ramada dafna yaprog’i, tuz va oq par zira bilan  uyg’unligini topasiz. Bu ta’m siz uchun ❗️</b>""",parse_mode="HTML",reply_markup=mol_ruletBOSHI1)
    # await message.delete()


@dp.message_handler(text="Mol Tarash Rulet")
async def mol_tarash_ruletBOSHI(message:Message):
    await message.answer_photo(
        photo=open('images/mol_tarash.jpg','rb'),
        caption="""<b>Narxi:   1kg-145000 so'm
Tarkibi: Molning tarash qismidan bo’lgan bu o’rama eng sifatli, mazali tami sizni lol qoldiradigon darajada tayorlangan bo’lgan bo’lib sizga lozim bo’lishi aniq</b>""",parse_mode="HTML",reply_markup=mol_tarash_ruletBOSHI1)
    # await message.delete()


@dp.message_handler(text="Bosh Menuga qaytish")
async def bosh_menuga_q(message:Message):
    await message.answer("""<b>Safo Go'sht mahsulotlari menusi</b>""",parse_mode="HTML",reply_markup=menu)
    await message.delete()




@dp.message_handler(text="Qazi")
async def ot_qaziBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/qazi.jpg','rb'),
        caption="""<b>Narxi:   1kg-145.000 so'm
Tarkibi: Uzoq vaqt davomida ortrilgan tajriba asosida  tayorlangan bu qazilarimiz sizga o’z tami bilan  manzur kelishi aniq.</b>""",parse_mode="HTML",reply_markup=ot_qaziBOSHI)
    # await message.delete()


@dp.message_handler(text="Ot Bo'yin Rulet")
async def ot_boyin_ruletBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/ot_boyin_rulet.jpg','rb'),
        caption="""<b>Narxi:   1kg-110.000 so'm
Tarkibi: Otning bo'yin go'shtidan o'rama  hamyonbop narxlarda kundalik nonushta dasturxoningiz bezagi.</b>""",parse_mode="HTML",reply_markup=ot_boyin_ruletBOSHI)
    # await message.delete()


@dp.message_handler(text="Ot Kachalka Rulet")
async def ot_kachalka_ruletBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/ot_kachalka_rulet.jpg','rb'),
        caption="""<b>Narxi:   1kg-100.000 so'm
Tarkibi: Otning kachalka go'shtidan o'rama hamyonbop narxlarda kundalik nonushta dasturxoningiz bezagi.</b>""",parse_mode="HTML",reply_markup=ot_kachalka_ruletBOSHI)
    # await message.delete()


@dp.message_handler(text="Toy Tarash Rulet")
async def toy_tarash_ruletBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/toy_tarash_rulet.jpg','rb'),
        caption="""<b>Narxi:   1kg-150.000 so'm
Tarkibi: Tarash toy qovurg'alarini qoplaydigan  go'sht bo'lib uning eng mazali qismi hisoblanadi,  uni yana “Go'shtlar qiroli” deb ham atashadi. .
Uning energetik qiymati juda yuqori darajada , shuning uchun ingichka bo'laklarga bo'lib iste'mol qilish tavsiya etiladi. 😊 .</b>""",parse_mode="HTML",reply_markup=toy_tarash_ruletBOSHI)
    # await message.delete()


@dp.message_handler(text="Qarta Go'shtli")
async def qarta_goshtliBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/qarta_goshtli.jpg','rb'),
        caption="""<b>Narxi:   1kg-110.000 so'm
Tarkibi: Yanada sizning talablaringizga moslashtirilgan holda.
Qartaning ichiga solingan ot goshti bilan birga bo’lgan mahsulotimizni sizlarga tortiq etamiz 🤤</b>""",parse_mode="HTML",reply_markup=qarta_goshtliBOSHI)
    # await message.delete()


@dp.message_handler(text="Qarta")
async def qartaBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/qarta.jpg','rb'),
        caption="""<b>Narxi:   1kg-60.000 so'm
Tarkibi: Qarta😍 Uzbek va Qozoq milliy taomlaridan biri bo’lib u otning eng yo’g’on va yog’liq ichakidan qilinadi. Hechqanday ziravorlarsiz istemol qilinadi. Bu ta’m siz uchun❗️</b>""",parse_mode="HTML",reply_markup=qartaBOSHI)
    # await message.delete()


@dp.message_handler(text="Bosh Menuga Qaytish")
async def Bosh_menuga_q(message:Message):
    await message.answer("""<b>Safo Go'sht mahsulotlari menusi</b>""",parse_mode="HTML",reply_markup=menu)
    # await message.delete()









@dp.message_handler(text="Dudlangan Kurka")
async def dudlangan_kurkaBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/dudlangan_kurka.jpg','rb'),
        caption="""<b>Narxi:   1kg-75.000 so'm
Tarkibi: Kurka go'shtini kerakli ziravorlar meyorida bolgan tuz bilan qaynatib yarim tayyor bo'lgan mahsulotni qayta dudlamasini sizga tortiq etishtan behat mamnunmiz</b>""",parse_mode="HTML",reply_markup=dudlangan_kurkaaBOSHI)
    # await message.delete()


@dp.message_handler(text="Tovuq Tandir Rulet")
async def tovuq_tandir_rulettBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/tovuq_tandir_rulet.jpg','rb'),
        caption="""<b>Narxi:   1kg-70.000 so'm
Tarkibi: Ajoyib yangilik 🤩 ! To'vuq tandir- ideal parxez mahsulot hisoblanadi uning tarkibida past kaloriya va yuqori miqdorda protain mavjud. To'vuq tandirning mazasidagi ta'mlar uyg'unligi sizni lol qoldirishi aniq.</b>""",parse_mode="HTML",reply_markup=tovuq_tandir_rulettBOSHI)
    # await message.delete()

1
@dp.message_handler(text="Dudlangan Tovuq")
async def dudlangan_tovuqBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/dudlangan_tovuq_rulet.jpg','rb'),
        caption="""<b>Narxi:   1kg-55.000 so'm
        Dudlangan Tovuq - ideal parxez mahsulot hisoblanadi uning tarkibida past kaloriya va yuqori miqdorda protain mavjud. Dudlangan to'vuq mazasidagi ta'mlar uyg'unligi sizni lol qoldirishi aniq.</b>""",parse_mode="HTML",reply_markup=dudlangan_tovuqqBOSHI)
    # await message.delete()


@dp.message_handler(text="⬅️Bosh Menuga Qaytish")
async def Bosh_Menuga_q(message:Message):
    await message.answer("""<b>Safo Go'sht mahsulotlari menusi</b>""",parse_mode="HTML",reply_markup=menu)
    # await message.delete()








@dp.message_handler(text="Mol Va Tovuq Goshtidan Kalbasa")
async def mol_tovuq_kalBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/mol_plus_tovuq_kal.jpg','rb'),
        caption="""<b>Narxi:   1kg-75.000 so'm
Tarkibi: Mol va tovuq go'shtidan kolbasa</b>""",parse_mode="HTML",reply_markup=mol_tovuq_kalbasaBOSHI)
    # await message.delete()


@dp.message_handler(text="Dudlangan Kalbasa")
async def dudlangan_kalBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/dudlangan_kalbasa.jpg','rb'),
        caption="""<b>Narxi: 650gr-40.000so'm
        Dudlangan kolbasa molva kurka go'shtidan 70% go'sht.</b>""",parse_mode="HTML",reply_markup=dudlangan_kalbasaBOSHI)
    # await message.delete()


@dp.message_handler(text="Qaynatma Kalbasa")
async def qaynatma_kalBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/qaynatma_kalbasa.jpg','rb'),
        caption="""<b>Narxi:   1kg-60000 so'm
Tarkibi: Qaynatma kolbasa mol go'shtidan 70% go'sht.</b>""",parse_mode="HTML",reply_markup=qaynatma_kalbasaBOSHI)
    # await message.delete()


@dp.message_handler(text="Sosiska")
async def sosiskaBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/sosiska.jpg','rb'),
        caption="""<b>Narxi:   1ta idishda 12ta - 25.000 so'm
Tarkibi: Sosiska mol go'shtidan 70% go'sht</b>""",parse_mode="HTML",reply_markup=sosiskaaBOSHI)
    # await message.delete()


@dp.message_handler(text="Oxotnichi Sosiska")
async def oxotnichi_sosiskaBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/oxotnichi_sosiska.jpg','rb'),
        caption="""<b>Narxi:   1-kg-65.000 so'm
Tarkibi: Oxotnichi sosiska mol go'shtidan.</b>""",parse_mode="HTML",reply_markup=oxotnichi_sosiskaaBOSHI)
    # await message.delete()


@dp.message_handler(text="⬅️Bosh Menuga qaytish")
async def Bosh_Menuga_q(message:Message):
    await message.answer("""<b>Safo Go'sht mahsulotlari menusi</b>""",parse_mode="HTML",reply_markup=menu)
    # await message.delete()







@dp.message_handler(text="Mol Til Tushonka")
async def mol_til_tushBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/mol_til_tushonka.jpg','rb'),
        caption="""<b>Narxi:   1-litr-80.000 so'm
Tarkibi: Xolsizlik bezovta qilyaptimi ,bizda buning ajoyib yechimi bor Til tusho'nkasi , uning tarkibida bir qancha moddalar bo'lib ular insonga quvvat va tetiklik bag'shlaydi , farzand kutuvchilar uchun esa ayni muddao😋</b>""",parse_mode="HTML",reply_markup=mol_til_tushonkaaBOSHI)
    # await message.delete()


@dp.message_handler(text="Mol Tushonka")
async def mol_tushBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/mol_tushonka.jpg','rb'),
        caption="""<b>Narxi:   1-Litr-65.000 so'm
Tarkibi: Tog' mavsumi boshlanib,xordiq maskaniga yo'l oldingizmi taom tayyorlashga ortiqcha urinmang bizda sizga xamroh bo'luvchi va xalqimiz sevib iste'mol qiladigan sifatli mol tushonkasi bor.</b>""",parse_mode="HTML",reply_markup=mol_tushonkaaBOSHI)
    # await message.delete()


@dp.message_handler(text="Qo'y Til Tushonka")
async def qoy_til_tushBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/qoy_til_tushonka.jpg','rb'),
        caption="""<b>Narxi:   700ml-55.000 so'm
Tarkibi: Til tusho'nkasi , uning tarkibida bir qancha moddalar bo'lib ular insonga quvvat va tetiklik bag'shlaydi , farzand kutuvchilar uchun esa ayni muddao.</b>""",parse_mode="HTML",reply_markup=qoy_til_tushonkaaBOSHI)
    # await message.delete()


@dp.message_handler(text="Quyon Tushonka")
async def quyon_tushBOSHI1(message:Message):
    await message.answer_photo(
        photo=open('images/quyon_tushonka.jpg','rb'),
        caption="""<b>Narxi:   1-Litr-100.000 so'm
Tarkibi: Қуён гўшти жуда мулойим, хуштам ҳамда оқсилларга бой бўлади. Шунинг учун ёш болаларга, кексаларга ва бемор кишиларга пархез таом сифатида
танаввул қилиш тавсия этилади. Енгил ҳазм бўлиши сабабли ортиқча вазнга эга инсонлар учун айни муддао.</b>""",parse_mode="HTML",reply_markup=quyon_tushonkaaBOSHI)
    # await message.delete()


@dp.message_handler(text="⬅️Bosh menuga qaytish")
async def Bosh_Menuga_q(message:Message):
    await message.answer("""<b>Safo Go'sht mahsulotlari menusi</b>""",parse_mode="HTML",reply_markup=menu)
    # await message.delete()











@dp.callback_query_handler(text="back1")
async def back1(call:CallbackQuery):
    await call.message.answer("""Qo'y Go'sht Mahsulotlari""",parse_mode='HTML',reply_markup=qoy_g_mahBOSHI)
    await call.message.delete()

@dp.callback_query_handler(text="back2")
async def back2(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_qoy_rulet.jpg','rb'),
        caption="""Narxi:   1kg-135.000 so'm
Tarkibi: Tandirda pishirilgan qo’y goshti juda mazali ta’mga ega. Ushbu tansiq taom o’rama ko’rinishda bo’lsachi, bunisiga nima deysiz❓😋 Kesilgan holda odatiy va bayramona dasturhoningizni birdek betakror bezagiga aylanuvchi o’ramani taqdim etishtan mamnunmiz 😊""",parse_mode='HTML',reply_markup=qoy_g_m)
    await call.message.delete()


@dp.callback_query_handler(text="back3")
async def back3(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qoy_tosh_rulet.jpg','rb'),
        caption="""Narxi:   1kg-150.000 so'm
Tarkibi: Qo'yning sur to'shidan rulet yog'liqni sevuchilar uchun.""",parse_mode='HTML',reply_markup=qoy_g_m1)
    await call.message.delete()


@dp.callback_query_handler(text="back4")
async def back4(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qoy_tandir_rulet.jpg','rb'),
        caption="""Narxi:   1kg-165.000 so'm
Tarkibi: Tandirda pishirilgan qo’y goshti juda mazali ta’mga ega. Ushbu tansiq taom o’rama ko’rinishda bo’lsachi, bunisiga nima deysiz❓😋 Kesilgan holda odatiy va bayramona dasturhoningizni birdek betakror bezagiga aylanuvchi o’ramani taqdim etishtan mamnunmiz 😊""",parse_mode='HTML',reply_markup=qoy_tandir)
    await call.message.delete()


@dp.callback_query_handler(text="back5")
async def back5(call:CallbackQuery):
    await call.message.answer("""Mol Go'sht Mahsulotlari""",parse_mode='HTML',reply_markup=mol_tilmahBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back6")
async def back6(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_til_rulet.jpg','rb'),
        caption="""Narxi:   1kg-130.000 so'm
Tarkibi: Bu til oramamiz parhez mahsulotlari qatoridan joy olgan. Shu kunlarda siz uchun ayni muddao!""",parse_mode='HTML',reply_markup=mol_tilRuletBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back7")
async def back7(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_press.jpg','rb'),
        caption="""Narxi:   1kg-120.000 so'm
        Yogsiz, ajoyib ta’mli, ishtaha ochuvchi ko’rinishga ega bo’lgan mol go’shtidan press 🤤""",parse_mode='HTML',reply_markup=mol_pressBOSHI1)
    await call.message.delete()


@dp.callback_query_handler(text="back8")
async def back8(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_archa_rulet.jpg','rb'),
        caption="""Narxi:   1kg-130000 so'm
Tarkibi: Xilma xillikni xohlovchilar uchun mol go'shtidan archa o’rama 😍. Uning nozik archa ignabarglari  mayin ifor taratadi va ishtahangizni ochadi .Yozning issiq kunlarida ham barchaga yoquvchi mahsulot.  Bu aynan siz istagan narsa. Tanlovda adashmang.😋""",parse_mode='HTML',reply_markup=mol_archa_ruletBOSHI1)
    await call.message.delete()



@dp.callback_query_handler(text="back9")
async def back9(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_rulet.jpg','rb'),
        caption="""Narxi:   1kg-135000 so'm
Tarkibi: Buqa go’shtidan bo’lgan o’rama. 🥩
Tatib ko’rmoqchimisiz❓
Bu o’ramada dafna yaprog’i, tuz va oq par zira bilan  uyg’unligini topasiz. Bu ta’m siz uchun ❗️""",parse_mode='HTML',reply_markup=mol_ruletBOSHI1)
    await call.message.delete()



@dp.callback_query_handler(text="back10")
async def back10(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_tarash.jpg','rb'),
        caption="""Narxi:   1kg-145000 so'm
Tarkibi: Molning tarash qismidan bo’lgan bu o’rama eng sifatli, mazali tami sizni lol qoldiradigon darajada tayorlangan bo’lgan bo’lib sizga lozim bo’lishi aniq""",parse_mode='HTML',reply_markup=mol_tarash_ruletBOSHI1)
    await call.message.delete()




@dp.callback_query_handler(text="back11")
async def back11(call:CallbackQuery):
    await call.message.answer("""Mol Go'sht Mahsulotlari""",parse_mode='HTML',reply_markup=mol_tilmahBOSHI)
    await call.message.delete()

@dp.callback_query_handler(text="back99")
async def back99(call:CallbackQuery):
    await call.message.answer("""Ot Go'sht Mahsulotlari""",parse_mode='HTML',reply_markup=ot_goshtmahBOSHI)
    await call.message.delete()

@dp.callback_query_handler(text="back01")
async def back01(call:CallbackQuery):
    await call.message.answer("""Ot Go'sht Mahsulotlari""",parse_mode='HTML',reply_markup=ot_goshtmahBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back12")
async def back12(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qazi.jpg','rb'),
        caption="""Narxi:   1kg-145.000 so'm
Tarkibi: Uzoq vaqt davomida ortrilgan tajriba asosida  tayorlangan bu qazilarimiz sizga o’z tami bilan  manzur kelishi aniq.""",parse_mode='HTML',reply_markup=ot_qaziBOSHI)
    await call.message.delete()



@dp.callback_query_handler(text="back13")
async def back13(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ot_boyin_rulet.jpg','rb'),
        caption="""Narxi:   1kg-110.000 so'm
Tarkibi: Otning bo'yin go'shtidan o'rama  hamyonbop narxlarda kundalik nonushta dasturxoningiz bezagi.""",parse_mode='HTML',reply_markup=ot_boyin_ruletBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back14")
async def back14(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ot_kachalka_rulet.jpg','rb'),
        caption="""Narxi:   1kg-100.000 so'm
Tarkibi: Otning kachalka go'shtidan o'rama hamyonbop narxlarda kundalik nonushta dasturxoningiz bezagi.""",parse_mode='HTML',reply_markup=ot_kachalka_ruletBOSHI)
    await call.message.delete()



@dp.callback_query_handler(text="back15")
async def back15(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/toy_tarash_rulet.jpg','rb'),
        caption="""Narxi:   1kg-150.000 so'm
Tarkibi: Tarash toy qovurg'alarini qoplaydigan  go'sht bo'lib uning eng mazali qismi hisoblanadi,  uni yana “Go'shtlar qiroli” deb ham atashadi. .
Uning energetik qiymati juda yuqori darajada , shuning uchun ingichka bo'laklarga bo'lib iste'mol qilish tavsiya etiladi. 😊 .""",parse_mode='HTML',reply_markup=toy_tarash_ruletBOSHI)
    await call.message.delete()



@dp.callback_query_handler(text="back16")
async def back16(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qarta_goshtli.jpg','rb'),
        caption="""Narxi:   1kg-110.000 so'm
Tarkibi: Yanada sizning talablaringizga moslashtirilgan holda.
Qartaning ichiga solingan ot goshti bilan birga bo’lgan mahsulotimizni sizlarga tortiq etamiz 🤤""",parse_mode='HTML',reply_markup=qarta_goshtliBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back17")
async def back17(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qarta.jpg','rb'),
        caption="""Narxi:   1kg-60.000 so'm
Tarkibi: Qarta😍 Uzbek va Qozoq milliy taomlaridan biri bo’lib u otning eng yo’g’on va yog’liq ichakidan qilinadi. Hechqanday ziravorlarsiz istemol qilinadi. Bu ta’m siz uchun❗️""",parse_mode='HTML',reply_markup=qartaBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back18")
async def back18(call:CallbackQuery):
    await call.message.answer("""Tovuq Go'sht Mahsulotlari""",parse_mode='HTML',reply_markup=tovuq_goshtmahBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back19")
async def back19(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dudlangan_kurka.jpg','rb'),
        caption="""Narxi:   1kg-75.000 so'm
Tarkibi: Kurka go'shtini kerakli ziravorlar meyorida bolgan tuz bilan qaynatib yarim tayyor bo'lgan mahsulotni qayta dudlamasini sizga tortiq etishtan behat mamnunmiz""",parse_mode='HTML',reply_markup=dudlangan_kurkaaBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back20")
async def back20(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuq_tandir_rulet.jpg','rb'),
        caption="""Narxi:   1kg-70.000 so'm
Tarkibi: Ajoyib yangilik 🤩 ! To'vuq tandir- ideal parxez mahsulot hisoblanadi uning tarkibida past kaloriya va yuqori miqdorda protain mavjud. To'vuq tandirning mazasidagi ta'mlar uyg'unligi sizni lol qoldirishi aniq.""",parse_mode='HTML',reply_markup=tovuq_tandir_rulettBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back21")
async def back21(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dudlangan_tovuq_rulet.jpg','rb'),
        caption="""Dudlangan Tovuq""",parse_mode='HTML',reply_markup=dudlangan_tovuqqBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back22")
async def back22(call:CallbackQuery):
    await call.message.answer("""Kalbasa Mahsulotlari""",parse_mode='HTML',reply_markup=Kal_mahBOSHI)
    await call.message.delete()



@dp.callback_query_handler(text="back23")
async def back23(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_plus_tovuq_kal.jpg','rb'),
        caption="""Narxi:   1kg-75.000 so'm
Tarkibi: Mol va tovuq go'shtidan kolbasa""",parse_mode='HTML',reply_markup=mol_tovuq_kalbasaBOSHI)
    await call.message.delete()



@dp.callback_query_handler(text="back24")
async def back24(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dudlangan_kalbasa.jpg','rb'),
        caption="""Narxi:   650gr-40.000 so'm
        Dudlangan kolbasa molva kurka go'shtidan 70% go'sht.""",parse_mode='HTML',reply_markup=dudlangan_kalbasaBOSHI)
    await call.message.delete()



@dp.callback_query_handler(text="back25")
async def back25(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qaynatma_kalbasa.jpg','rb'),
        caption="""Narxi:   1kg-60000 so'm
Tarkibi: Qaynatma kolbasa mol go'shtidan 70% go'sht.""",parse_mode='HTML',reply_markup=qaynatma_kalbasaBOSHI)
    await call.message.delete()



@dp.callback_query_handler(text="back26")
async def back26(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sosiska.jpg','rb'),
        caption="""Narxi:   1ta idishda 12ta - 25.000 so'm
Tarkibi: Sosiska mol go'shtidan 70% go'sht""",parse_mode='HTML',reply_markup=sosiskaaBOSHI)
    await call.message.delete()



@dp.callback_query_handler(text="back27")
async def back27(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/oxotnichi_sosiska.jpg','rb'),
        caption="""Narxi:   1-kg-65.000 so'm
Tarkibi: Oxotnichi sosiska mol go'shtidan.""",parse_mode='HTML',reply_markup=oxotnichi_sosiskaaBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back28")
async def back28(call:CallbackQuery):
    await call.message.answer("""Tushonka Mahsulotlari""",parse_mode='HTML',reply_markup=tushonka_mahBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back29")
async def back29(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_til_tushonka.jpg','rb'),
        caption="""Narxi:   1-litr-80.000 so'm
Tarkibi: Xolsizlik bezovta qilyaptimi ,bizda buning ajoyib yechimi bor Til tusho'nkasi , uning tarkibida bir qancha moddalar bo'lib ular insonga quvvat va tetiklik bag'shlaydi , farzand kutuvchilar uchun esa ayni muddao😋""",parse_mode='HTML',reply_markup=mol_til_tushonkaaBOSHI)
    await call.message.delete()



@dp.callback_query_handler(text="back30")
async def back30(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_tushonka.jpg','rb'),
        caption="""Narxi:   1-Litr-65.000 so'm
Tarkibi: Tog' mavsumi boshlanib,xordiq maskaniga yo'l oldingizmi taom tayyorlashga ortiqcha urinmang bizda sizga xamroh bo'luvchi va xalqimiz sevib iste'mol qiladigan sifatli mol tushonkasi bor.""",parse_mode='HTML',reply_markup=mol_tushonkaaBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back31")
async def back31(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qoy_til_tushonka.jpg','rb'),
        caption="""Narxi:   700ml-55.000 so'm
Tarkibi: Til tusho'nkasi , uning tarkibida bir qancha moddalar bo'lib ular insonga quvvat va tetiklik bag'shlaydi , farzand kutuvchilar uchun esa ayni muddao.""",parse_mode='HTML',reply_markup=qoy_til_tushonkaaBOSHI)
    await call.message.delete()


@dp.callback_query_handler(text="back32")
async def back32(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/quyon_tushonka.jpg','rb'),
        caption="""Narxi:   1-Litr-100.000 so'm
Tarkibi: Қуён гўшти жуда мулойим, хуштам ҳамда оқсилларга бой бўлади. Шунинг учун ёш болаларга, кексаларга ва бемор кишиларга пархез таом сифатида
танаввул қилиш тавсия этилади. Енгил ҳазм бўлиши сабабли ортиқча вазнга эга инсонлар учун айни муддао.""",parse_mode='HTML',reply_markup=quyon_tushonkaaBOSHI)
    await call.message.delete()















@dp.callback_query_handler(text="mol_qoy300gr")
async def mol_qoy300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_qoy_rulet.jpg','rb'),
        caption="""Narxi:   300gr-40.500 so'm
Tarkibi: Tandirda pishirilgan qo’y goshti juda mazali ta’mga ega. Ushbu tansiq taom o’rama ko’rinishda bo’lsachi, bunisiga nima deysiz❓😋 Kesilgan holda odatiy va bayramona dasturhoningizni birdek betakror bezagiga aylanuvchi o’ramani taqdim etishtan mamnunmiz 😊
        """,reply_markup=qoy_g_mahsulotlari_300gr)
          
    await call.message.delete()

@dp.callback_query_handler(text="mol_qoy600gr")
async def mol_qoy600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_qoy_rulet.jpg','rb'),
        caption="""Narxi:   600gr-81.000 so'm
Tarkibi: Tandirda pishirilgan qo’y goshti juda mazali ta’mga ega. Ushbu tansiq taom o’rama ko’rinishda bo’lsachi, bunisiga nima deysiz❓😋 Kesilgan holda odatiy va bayramona dasturhoningizni birdek betakror bezagiga aylanuvchi o’ramani taqdim etishtan mamnunmiz 😊
        """,reply_markup=qoy_g_mahsulotlari_600gr)
          
    await call.message.delete()


@dp.callback_query_handler(text="mol_qoy1kg")
async def mol_qoy1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_qoy_rulet.jpg','rb'),
        caption="""Narxi:   1kg-135.000 so'm
Tarkibi: Tandirda pishirilgan qo’y goshti juda mazali ta’mga ega. Ushbu tansiq taom o’rama ko’rinishda bo’lsachi, bunisiga nima deysiz❓😋 Kesilgan holda odatiy va bayramona dasturhoningizni birdek betakror bezagiga aylanuvchi o’ramani taqdim etishtan mamnunmiz 😊
        """,reply_markup=qoy_g_mahsulotlari_1kg)
    await call.message.delete()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////
# qoy_toshRulet_300gr
@dp.callback_query_handler(text="qoy_tosh300gr")
async def qoy_tosh300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qoy_tosh_rulet.jpg','rb'),
        caption="""Narxi:   300gr-45.000 so'm
Tarkibi: Qo'yning sur to'shidan rulet yog'liqni sevuchilar uchun.
        """,reply_markup=qoy_toshRulet_300gr)
    await call.message.delete()


# qoy_toshRulet_600gr
@dp.callback_query_handler(text="qoy_tosh600gr")
async def qoy_tosh600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qoy_tosh_rulet.jpg','rb'),
        caption="""Narxi:   600gr-90.000 so'm
Tarkibi: Qo'yning sur to'shidan rulet yog'liqni sevuchilar uchun.
        """,reply_markup=qoy_toshRulet_600gr)
    await call.message.delete()

# qoy_toshRulet_1kg
@dp.callback_query_handler(text="qoy_tosh1kg")
async def qoy_tosh1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qoy_tosh_rulet.jpg','rb'),
        caption="""Narxi:   1kg-150.000 so'm
Tarkibi: Qo'yning sur to'shidan rulet yog'liqni sevuchilar uchun.
        """,reply_markup=qoy_toshRulet_1kg)
    await call.message.delete()

#///////////////////////////////////////////////////////////


@dp.callback_query_handler(text="qoy_tandir300gr")
async def qoy_tandir300gr1(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qoy_tandir_rulet.jpg','rb'),
        caption="""Narxi:   300gr-49.500 so'm
Tarkibi: Tandirda pishirilgan qo’y goshti juda mazali ta’mga ega. Ushbu tansiq taom o’rama ko’rinishda bo’lsachi, bunisiga nima deysiz❓😋 Kesilgan holda odatiy va bayramona dasturhoningizni birdek betakror bezagiga aylanuvchi o’ramani taqdim etishtan mamnunmiz 😊
        """,reply_markup=qoy_tandirRulet_300gr)
    await call.message.delete()



@dp.callback_query_handler(text="qoy_tandir600gr")
async def qoy_tandir600gr1(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qoy_tandir_rulet.jpg','rb'),
        caption="""Narxi:   600gr-99.000 so'm
Tarkibi: Tandirda pishirilgan qo’y goshti juda mazali ta’mga ega. Ushbu tansiq taom o’rama ko’rinishda bo’lsachi, bunisiga nima deysiz❓😋 Kesilgan holda odatiy va bayramona dasturhoningizni birdek betakror bezagiga aylanuvchi o’ramani taqdim etishtan mamnunmiz 😊
        """,reply_markup=qoy_tandirRulet_600gr)
    await call.message.delete()


@dp.callback_query_handler(text="qoy_tandir1kg")
async def qoy_tandir1kg1(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qoy_tandir_rulet.jpg','rb'),
        caption="""Narxi:   1kg-165.000 so'm
Tarkibi: Tandirda pishirilgan qo’y goshti juda mazali ta’mga ega. Ushbu tansiq taom o’rama ko’rinishda bo’lsachi, bunisiga nima deysiz❓😋 Kesilgan holda odatiy va bayramona dasturhoningizni birdek betakror bezagiga aylanuvchi o’ramani taqdim etishtan mamnunmiz 😊
        """,reply_markup=qoy_tandirRulet_1kg)
    await call.message.delete()












@dp.callback_query_handler(text="mol_tilRuletBOSHI300gr")
async def mol_tilRuletBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_til_rulet.jpg','rb'),
        caption="""Narxi:   300gr-39.000 so'm
Tarkibi: Bu til oramamiz parhez mahsulotlari qatoridan joy olgan. Shu kunlarda siz uchun ayni muddao!
        """,reply_markup=mol_tilRulet_300gr)
    await call.message.delete()

@dp.callback_query_handler(text="mol_tilRuletBOSHI600gr")
async def mol_tilRuletBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_til_rulet.jpg','rb'),
        caption="""Narxi:   600gr-78.000 so'm
Tarkibi:Bu til oramamiz parhez mahsulotlari qatoridan joy olgan. Shu kunlarda siz uchun ayni muddao!
        """,reply_markup=mol_tilRulet_600gr)
    await call.message.delete()

@dp.callback_query_handler(text="mol_tilRuletBOSHI1kg")
async def mol_tilRuletBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_til_rulet.jpg','rb'),
        caption="""Narxi:   1kg-130.000 so'm
Tarkibi: Bu til oramamiz parhez mahsulotlari qatoridan joy olgan. Shu kunlarda siz uchun ayni muddao!
        """,reply_markup=mol_tilRulet_1kg)
    await call.message.delete()


@dp.callback_query_handler(text="mol_pressBOSHI300gr")
async def mol_pressBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_press.jpg','rb'),
        caption="""Narxi:   1kg-130.000 so'm
Tarkibi: Xilma xillikni xohlovchilar uchun mol go'shtidan archa o’rama 😍. Uning nozik archa ignabarglari  mayin ifor taratadi va ishtahangizni ochadi .Yozning issiq kunlarida ham barchaga yoquvchi mahsulot.  Bu aynan siz istagan narsa. Tanlovda adashmang.😋
        """,reply_markup=mol_presss_300gr)
    await call.message.delete()


@dp.callback_query_handler(text="mol_pressBOSHI600gr")
async def mol_pressBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_press.jpg','rb'),
        caption="""Narxi:   1kg-130000 so'm
Tarkibi: Xilma xillikni xohlovchilar uchun mol go'shtidan archa o’rama 😍. Uning nozik archa ignabarglari  mayin ifor taratadi va ishtahangizni ochadi .Yozning issiq kunlarida ham barchaga yoquvchi mahsulot.  Bu aynan siz istagan narsa. Tanlovda adashmang.😋
        """,reply_markup=mol_presss_600gr)
    await call.message.delete()


@dp.callback_query_handler(text="mol_pressBOSHI1kg")
async def mol_pressBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_press.jpg','rb'),
        caption="""Narxi:   1kg-130000 so'm
Tarkibi: Xilma xillikni xohlovchilar uchun mol go'shtidan archa o’rama 😍. Uning nozik archa ignabarglari  mayin ifor taratadi va ishtahangizni ochadi .Yozning issiq kunlarida ham barchaga yoquvchi mahsulot.  Bu aynan siz istagan narsa. Tanlovda adashmang.😋
        """,reply_markup=mol_presss_1kg)
    await call.message.delete()


@dp.callback_query_handler(text="mol_archaBOSHI300gr")
async def mol_archaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_archa_rulet.jpg','rb'),
        caption="""Narxi:   300gr-37500 so'm
Tarkibi: Xilma xillikni xohlovchilar uchun mol go'shtidan archa o’rama 😍. Uning nozik archa ignabarglari  mayin ifor taratadi va ishtahangizni ochadi .Yozning issiq kunlarida ham barchaga yoquvchi mahsulot.  Bu aynan siz istagan narsa. Tanlovda adashmang.😋
        """,reply_markup=mol_archa_rulet_300gr)
    await call.message.delete()


@dp.callback_query_handler(text="mol_archaBOSHI600gr")
async def mol_archaBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_archa_rulet.jpg','rb'),
        caption="""Narxi:   600gr-75000 so'm
Tarkibi: Xilma xillikni xohlovchilar uchun mol go'shtidan archa o’rama 😍. Uning nozik archa ignabarglari  mayin ifor taratadi va ishtahangizni ochadi .Yozning issiq kunlarida ham barchaga yoquvchi mahsulot.  Bu aynan siz istagan narsa. Tanlovda adashmang.😋
        """,reply_markup=mol_archa_rulet_600gr)
    await call.message.delete()


@dp.callback_query_handler(text="mol_archaBOSHI1kg")
async def mol_archaBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_archa_rulet.jpg','rb'),
        caption="""Narxi:   1kg-125000 so'm
Tarkibi: Xilma xillikni xohlovchilar uchun mol go'shtidan archa o’rama 😍. Uning nozik archa ignabarglari  mayin ifor taratadi va ishtahangizni ochadi .Yozning issiq kunlarida ham barchaga yoquvchi mahsulot.  Bu aynan siz istagan narsa. Tanlovda adashmang.😋
        """,reply_markup=mol_archa_rulet_1kg)
    await call.message.delete()



@dp.callback_query_handler(text="mol_ruletBOSHI300gr")
async def mol_ruletBOSHI300gr1(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_rulet.jpg','rb'),
        caption="""Narxi:   300gr-405000 so'm
Tarkibi: Buqa go’shtidan bo’lgan o’rama. 🥩
Tatib ko’rmoqchimisiz❓
Bu o’ramada dafna yaprog’i, tuz va oq par zira bilan  uyg’unligini topasiz. Bu ta’m siz uchun ❗️
        """,reply_markup=mol__rulet_300gr)
    await call.message.delete()


@dp.callback_query_handler(text="mol_ruletBOSHI600gr")
async def mol_ruletBOSHI600gr1(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_rulet.jpg','rb'),
        caption="""Narxi:   600gr-81000 so'm
Tarkibi: Buqa go’shtidan bo’lgan o’rama. 🥩
Tatib ko’rmoqchimisiz❓
Bu o’ramada dafna yaprog’i, tuz va oq par zira bilan  uyg’unligini topasiz. Bu ta’m siz uchun ❗️
        """,reply_markup=mol__rulet_600gr)
    await call.message.delete()


@dp.callback_query_handler(text="mol_ruletBOSHI1kg")
async def mol_ruletBOSHI1kg1(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_rulet.jpg','rb'),
        caption="""Narxi:   1kg-135000 so'm
Tarkibi: Buqa go’shtidan bo’lgan o’rama. 🥩
Tatib ko’rmoqchimisiz❓
Bu o’ramada dafna yaprog’i, tuz va oq par zira bilan  uyg’unligini topasiz. Bu ta’m siz uchun ❗️
        """,reply_markup=mol__rulet_1kg)
    await call.message.delete()




@dp.callback_query_handler(text="mol_tarash_ruletBOSHI300gr")
async def mol_tarashBOSHI300gr1(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_tarash.jpg','rb'),
        caption="""Narxi:   300gr-43500 so'm
Tarkibi: Molning tarash qismidan bo’lgan bu o’rama eng sifatli, mazali tami sizni lol qoldiradigon darajada tayorlangan bo’lgan bo’lib sizga lozim bo’lishi aniq
        """,reply_markup=mol_tarash_rulet_300gr)
    await call.message.delete()

@dp.callback_query_handler(text="mol_tarash_ruletBOSHI600gr")
async def mol_tarashBOSHI600gr1(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_tarash.jpg','rb'),
        caption="""Narxi:   600gr-87000 so'm
Tarkibi: Molning tarash qismidan bo’lgan bu o’rama eng sifatli, mazali tami sizni lol qoldiradigon darajada tayorlangan bo’lgan bo’lib sizga lozim bo’lishi aniq
        """,reply_markup=mol_tarash_rulet_600gr)
    await call.message.delete()

@dp.callback_query_handler(text="mol_tarash_ruletBOSHI1kg")
async def mol_tarashBOSHI1kg1(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_tarash.jpg','rb'),
        caption="""Narxi:   1kg-145000 so'm
Tarkibi: Molning tarash qismidan bo’lgan bu o’rama eng sifatli, mazali tami sizni lol qoldiradigon darajada tayorlangan bo’lgan bo’lib sizga lozim bo’lishi aniq""",reply_markup=mol_tarash_rulet_1kg)
    await call.message.delete()












@dp.callback_query_handler(text="ot_qaziBOSHI300gr")
async def ot_qaziBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qazi.jpg','rb'),
        caption="""Narxi:   300gr-43.500 so'm
Tarkibi: Uzoq vaqt davomida ortrilgan tajriba asosida  tayorlangan bu qazilarimiz sizga o’z tami bilan  manzur kelishi aniq.
        """,reply_markup=ot_qazi_300gr)
    await call.message.delete()

@dp.callback_query_handler(text="ot_qaziBOSHI600gr")
async def ot_qaziBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qazi.jpg','rb'),
        caption="""Narxi:   600gr-87.000 so'm
Tarkibi: Uzoq vaqt davomida ortrilgan tajriba asosida  tayorlangan bu qazilarimiz sizga o’z tami bilan  manzur kelishi aniq.
        """,reply_markup=ot_qazi_600gr)
    await call.message.delete()

@dp.callback_query_handler(text="ot_qaziBOSHI1kg")
async def ot_qaziBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qazi.jpg','rb'),
        caption="""Narxi:   1kg-145.000 so'm
Tarkibi: Uzoq vaqt davomida ortrilgan tajriba asosida  tayorlangan bu qazilarimiz sizga o’z tami bilan  manzur kelishi aniq.
        """,reply_markup=ot_qazi_1kg)
    await call.message.delete()




@dp.callback_query_handler(text="ot_boyin_ruletBOSHI300gr")
async def ot_boyin_ruletBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ot_boyin_rulet.jpg','rb'),
        caption="""Narxi:   300gr-33.000 so'm
Tarkibi: Otning bo'yin go'shtidan o'rama  hamyonbop narxlarda kundalik nonushta dasturxoningiz bezagi.
        """,reply_markup=ot_boyin_rulet_300gr)
    await call.message.delete()

@dp.callback_query_handler(text="ot_boyin_ruletBOSHI600gr")
async def ot_boyin_ruletBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ot_boyin_rulet.jpg','rb'),
        caption="""Narxi:   600gr-66.000 so'm
Tarkibi: Otning bo'yin go'shtidan o'rama  hamyonbop narxlarda kundalik nonushta dasturxoningiz bezagi.
        """,reply_markup=ot_boyin_rulet_600gr)
    await call.message.delete()

@dp.callback_query_handler(text="ot_boyin_ruletBOSHI1kg")
async def ot_boyin_ruletBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ot_boyin_rulet.jpg','rb'),
        caption="""Narxi:   1kg-110.000 so'm
Tarkibi: Otning bo'yin go'shtidan o'rama  hamyonbop narxlarda kundalik nonushta dasturxoningiz bezagi.
        """,reply_markup=ot_boyin_rulet_1kg)
    await call.message.delete()







@dp.callback_query_handler(text="ot_kachalka_ruletBOSHI300gr")
async def ot_kachalka_ruletBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ot_kachalka_rulet.jpg','rb'),
        caption="""Narxi:   300gr-30.000 so'm
Tarkibi: Otning kachalka go'shtidan o'rama hamyonbop narxlarda kundalik nonushta dasturxoningiz bezagi. 
        """,reply_markup=ot_kachalka_rulet_300gr)
    await call.message.delete()

@dp.callback_query_handler(text="ot_kachalka_ruletBOSHI600gr")
async def ot_boyin_ruletBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ot_kachalka_rulet.jpg','rb'),
        caption="""Narxi:   600gr-60.000 so'm
Tarkibi: Otning kachalka go'shtidan o'rama hamyonbop narxlarda kundalik nonushta dasturxoningiz bezagi. 
        """,reply_markup=ot_kachalka_rulet_600gr)
    await call.message.delete()

@dp.callback_query_handler(text="ot_kachalka_ruletBOSHI1kg")
async def ot_boyin_ruletBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ot_kachalka_rulet.jpg','rb'),
        caption="""Narxi:   1kg-100.000 so'm
Tarkibi: Otning kachalka go'shtidan o'rama hamyonbop narxlarda kundalik nonushta dasturxoningiz bezagi. 
        """,reply_markup=ot_kachalka_rulet_1kg)
    await call.message.delete()








@dp.callback_query_handler(text="toy_tarash_ruletBOSHI300gr")
async def toy_tarash_ruletBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/toy_tarash_rulet.jpg','rb'),
        caption="""Narxi:   300gr-45.000 so'm
Tarkibi: Tarash toy qovurg'alarini qoplaydigan  go'sht bo'lib uning eng mazali qismi hisoblanadi,  uni yana “Go'shtlar qiroli” deb ham atashadi. .
Uning energetik qiymati juda yuqori darajada , shuning uchun ingichka bo'laklarga bo'lib iste'mol qilish tavsiya etiladi. 😊 . 
        """,reply_markup=toy_tarash_rulet_300gr)
    await call.message.delete()

@dp.callback_query_handler(text="toy_tarash_ruletBOSHI600gr")
async def toy_tarash_ruletBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/toy_tarash_rulet.jpg','rb'),
        caption="""Narxi:   600gr-90.000 so'm
Tarkibi: Tarash toy qovurg'alarini qoplaydigan  go'sht bo'lib uning eng mazali qismi hisoblanadi,  uni yana “Go'shtlar qiroli” deb ham atashadi. .
Uning energetik qiymati juda yuqori darajada , shuning uchun ingichka bo'laklarga bo'lib iste'mol qilish tavsiya etiladi. 😊 .
        """,reply_markup=toy_tarash_rulet_600gr)
    await call.message.delete()

@dp.callback_query_handler(text="toy_tarash_ruletBOSHI1kg")
async def toy_tarash_ruletBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/toy_tarash_rulet.jpg','rb'),
        caption="""Narxi:   1kg-150.000 so'm
Tarkibi: Tarash toy qovurg'alarini qoplaydigan  go'sht bo'lib uning eng mazali qismi hisoblanadi,  uni yana “Go'shtlar qiroli” deb ham atashadi. .
Uning energetik qiymati juda yuqori darajada , shuning uchun ingichka bo'laklarga bo'lib iste'mol qilish tavsiya etiladi. 😊 . 
        """,reply_markup=toy_tarash_rulet_1kg)
    await call.message.delete()








@dp.callback_query_handler(text="qarta_goshtliBOSHI300gr")
async def qarta_goshtliBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qarta_goshtli.jpg','rb'),
        caption="""Narxi:   300gr-33.000 so'm
Tarkibi: Yanada sizning talablaringizga moslashtirilgan holda.
Qartaning ichiga solingan ot goshti bilan birga bo’lgan mahsulotimizni sizlarga tortiq etamiz 🤤 
        """,reply_markup=qarta_goshtli_300gr)
    await call.message.delete()

@dp.callback_query_handler(text="qarta_goshtliBOSHI600gr")
async def qarta_goshtliBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qarta_goshtli.jpg','rb'),
        caption="""Narxi:   600gr-66.000 so'm
Tarkibi: Yanada sizning talablaringizga moslashtirilgan holda.
Qartaning ichiga solingan ot goshti bilan birga bo’lgan mahsulotimizni sizlarga tortiq etamiz 🤤 
        """,reply_markup=qarta_goshtli_600gr)
    await call.message.delete()

@dp.callback_query_handler(text="qarta_goshtliBOSHI1kg")
async def toy_tarash_ruletBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qarta_goshtli.jpg','rb'),
        caption="""Narxi:   1kg-110.000 so'm
Tarkibi: Yanada sizning talablaringizga moslashtirilgan holda.
Qartaning ichiga solingan ot goshti bilan birga bo’lgan mahsulotimizni sizlarga tortiq etamiz 🤤 
        """,reply_markup=qarta_goshtli_1kg)
    await call.message.delete()




@dp.callback_query_handler(text="qartaBOSHI300gr")
async def qartaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qarta.jpg','rb'),
        caption="""Narxi:   300gr-18.000 so'm
Tarkibi: Qarta😍 Uzbek va Qozoq milliy taomlaridan biri bo’lib u otning eng yo’g’on va yog’liq ichakidan qilinadi. Hechqanday ziravorlarsiz istemol qilinadi. Bu ta’m siz uchun❗️
        """,reply_markup=qarta_300gr)
    await call.message.delete()

@dp.callback_query_handler(text="qartaBOSHI600gr")
async def qartaBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qarta.jpg','rb'),
        caption="""Narxi:   600gr-36.000 so'm
Tarkibi: Qarta😍 Uzbek va Qozoq milliy taomlaridan biri bo’lib u otning eng yo’g’on va yog’liq ichakidan qilinadi. Hechqanday ziravorlarsiz istemol qilinadi. Bu ta’m siz uchun❗️ 
        """,reply_markup=qarta_600gr)
    await call.message.delete()

@dp.callback_query_handler(text="qartaBOSHI1kg")
async def qartaBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qarta.jpg','rb'),
        caption="""Narxi:   1kg-60.000 so'm
Tarkibi: Qarta😍 Uzbek va Qozoq milliy taomlaridan biri bo’lib u otning eng yo’g’on va yog’liq ichakidan qilinadi. Hechqanday ziravorlarsiz istemol qilinadi. Bu ta’m siz uchun❗️ 
        """,reply_markup=qarta_1kg)
    await call.message.delete()












@dp.callback_query_handler(text="dudlangan_kurkaBOSHI300gr")
async def dudlangan_kurkaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dudlangan_kurka.jpg','rb'),
        caption="""Narxi:   300gr-22.500 so'm
Tarkibi: Kurka go'shtini kerakli ziravorlar meyorida bolgan tuz bilan qaynatib yarim tayyor bo'lgan mahsulotni qayta dudlamasini sizga tortiq etishtan behat mamnunmiz
        """,reply_markup=dudlangan_kurka_300gr)
    await call.message.delete()

@dp.callback_query_handler(text="dudlangan_kurkaBOSHI600gr")
async def dudlangan_kurkaBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dudlangan_kurka.jpg','rb'),
        caption="""Narxi:   600gr-45.000 so'm
Tarkibi: Kurka go'shtini kerakli ziravorlar meyorida bolgan tuz bilan qaynatib yarim tayyor bo'lgan mahsulotni qayta dudlamasini sizga tortiq etishtan behat mamnunmiz 
        """,reply_markup=dudlangan_kurka_600gr)
    await call.message.delete()

@dp.callback_query_handler(text="dudlangan_kurkaBOSHI1kg")
async def dudlangan_kurkaBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dudlangan_kurka.jpg','rb'),
        caption="""Narxi:   1kg-75.000 so'm
Tarkibi: Kurka go'shtini kerakli ziravorlar meyorida bolgan tuz bilan qaynatib yarim tayyor bo'lgan mahsulotni qayta dudlamasini sizga tortiq etishtan behat mamnunmiz
        """,reply_markup=dudlangan_kurka_1kg)
    await call.message.delete()




@dp.callback_query_handler(text="tovuq_tandir_rulettBOSHI300gr")
async def tovuq_tandir_rulettBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuq_tandir_rulet.jpg','rb'),
        caption="""Narxi:   300gr-21.000 so'm
Tarkibi: Ajoyib yangilik 🤩 ! To'vuq tandir- ideal parxez mahsulot hisoblanadi uning tarkibida past kaloriya va yuqori miqdorda protain mavjud. To'vuq tandirning mazasidagi ta'mlar uyg'unligi sizni lol qoldirishi aniq.
        """,reply_markup=tovuq_tandir_rulett_300gr)
    await call.message.delete()

@dp.callback_query_handler(text="tovuq_tandir_rulettBOSHI600gr")
async def tovuq_tandir_rulettBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuq_tandir_rulet.jpg','rb'),
        caption="""Narxi:   600gr-42.000 so'm
Tarkibi: Ajoyib yangilik 🤩 ! To'vuq tandir- ideal parxez mahsulot hisoblanadi uning tarkibida past kaloriya va yuqori miqdorda protain mavjud. To'vuq tandirning mazasidagi ta'mlar uyg'unligi sizni lol qoldirishi aniq.
        """,reply_markup=tovuq_tandir_rulett_600gr)
    await call.message.delete()

@dp.callback_query_handler(text="tovuq_tandir_rulettBOSHI1kg")
async def dudlangan_kurkaBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuq_tandir_rulet.jpg','rb'),
        caption="""Narxi:   1kg-70.000 so'm
Tarkibi: Ajoyib yangilik 🤩 ! To'vuq tandir- ideal parxez mahsulot hisoblanadi uning tarkibida past kaloriya va yuqori miqdorda protain mavjud. To'vuq tandirning mazasidagi ta'mlar uyg'unligi sizni lol qoldirishi aniq.
        """,reply_markup=tovuq_tandir_rulett_1kg)
    await call.message.delete()




@dp.callback_query_handler(text="dudlangan_tovuqqBOSHI300gr")
async def dudlangan_tovuqqBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dudlangan_tovuq_rulet.jpg','rb'),
        caption="""Narxi:   300gr-16.500 so'm
Tarkibi: Ajoyib yangilik 🤩 ! To'vuq tandir- ideal parxez mahsulot hisoblanadi uning tarkibida past kaloriya va yuqori miqdorda protain mavjud. To'vuq tandirning mazasidagi ta'mlar uyg'unligi sizni lol qoldirishi aniq.
        """,reply_markup=dudlangan_tovuq300gr)
    await call.message.delete()

@dp.callback_query_handler(text="dudlangan_tovuqqBOSHI600gr")
async def dudlangan_tovuqqBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dudlangan_tovuq_rulet.jpg','rb'),
        caption="""Narxi:   600gr-33.000 so'm
Tarkibi: Ajoyib yangilik 🤩 ! To'vuq tandir- ideal parxez mahsulot hisoblanadi uning tarkibida past kaloriya va yuqori miqdorda protain mavjud. To'vuq tandirning mazasidagi ta'mlar uyg'unligi sizni lol qoldirishi aniq.
        """,reply_markup=dudlangan_tovuq600gr)
    await call.message.delete()

@dp.callback_query_handler(text="dudlangan_tovuqqBOSHI1kg")
async def dudlangan_tovuqqBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dudlangan_tovuq_rulet.jpg','rb'),
        caption="""Narxi:   1kg-55.000 so'm
Tarkibi: Ajoyib yangilik 🤩 ! To'vuq tandir- ideal parxez mahsulot hisoblanadi uning tarkibida past kaloriya va yuqori miqdorda protain mavjud. To'vuq tandirning mazasidagi ta'mlar uyg'unligi sizni lol qoldirishi aniq.
        """,reply_markup=dudlangan_tovuq1kg)
    await call.message.delete()








@dp.callback_query_handler(text="mol_tovuq_kalbasaBOSHI300gr")
async def mol_tovuq_kalbasaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_plus_tovuq_kal.jpg','rb'),
        caption="""Narxi:   300gr-22.500 so'm
Tarkibi: Mol va tovuq go'shtidan kolbasa 
        """,reply_markup=mol_tovuq_kalbasa300gr)
    await call.message.delete()

@dp.callback_query_handler(text="mol_tovuq_kalbasaBOSHI600gr")
async def mol_tovuq_kalbasaBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_plus_tovuq_kal.jpg','rb'),
        caption="""Narxi:   600gr-45.000 so'm
Tarkibi: Mol va tovuq go'shtidan kolbasa 
        """,reply_markup=mol_tovuq_kalbasa600gr)
    await call.message.delete()

@dp.callback_query_handler(text="mol_tovuq_kalbasaBOSHI1kg")
async def dudlangan_kurkaBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_plus_tovuq_kal.jpg','rb'),
        caption="""Narxi:   1kg-75.000 so'm
Tarkibi: Mol va tovuq go'shtidan kolbasa 
        """,reply_markup=mol_tovuq_kalbasa1kg)
    await call.message.delete()



@dp.callback_query_handler(text="dudlangan_kalbasaBOSHI300gr")
async def dudlangan_kalbasaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dudlangan_kalbasa.jpg','rb'),
        caption="""Narxi:   1kg-75000 so'm
Tarkibi: Mol va tovuq go'shtidan kolbasa 
        """,reply_markup=dudlangan_kalbasa300gr)
    await call.message.delete()

@dp.callback_query_handler(text="dudlangan_kalbasaBOSHI600gr")
async def dudlangan_kalbasaBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dudlangan_kalbasa.jpg','rb'),
        caption="""Narxi:   650gr-40.000 so'm
Tarkibi: Mol va tovuq go'shtidan kolbasa 
        """,reply_markup=dudlangan_kalbasa600gr)
    await call.message.delete()





@dp.callback_query_handler(text="qaynatma_kalbasaBOSHI300gr")
async def qaynatma_kalbasaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qaynatma_kalbasa.jpg','rb'),
        caption="""Narxi:   1kg-60000 so'm
Tarkibi: Qaynatma kolbasa mol go'shtidan 70% go'sht. 
        """,reply_markup=qaynatma_kalbasa300gr)
    await call.message.delete()

@dp.callback_query_handler(text="qaynatma_kalbasaBOSHI600gr")
async def qaynatma_kalbasaBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qaynatma_kalbasa.jpg','rb'),
        caption="""Narxi:   650gr-40000 so'm
Tarkibi: Qaynatma kolbasa mol go'shtidan 70% go'sht.
        """,reply_markup=qaynatma_kalbasa600gr)
    await call.message.delete()

@dp.callback_query_handler(text="qaynatma_kalbasaBOSHI1kg")
async def qaynatma_kalbasaBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qaynatma_kalbasa.jpg','rb'),
        caption="""Narxi:   500gr-30000 so'm
Tarkibi: Qaynatma kolbasa mol go'shtidan 70% go'sht. 
        """,reply_markup=qaynatma_kalbasa1kg)
    await call.message.delete()






@dp.callback_query_handler(text="sosiskaaBOSHI300gr")
async def sosiskaaBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sosiska.jpg','rb'),
        caption="""Narxi:   1ta idishda 12ta - 25.000 so'm
Tarkibi: Sosiska mol go'shtidan 70% go'sht
        """,reply_markup=sosiskaa300gr)
    await call.message.delete()




@dp.callback_query_handler(text="oxotnichi_sosiskaaBOSHI300gr")
async def oxotnichi_sosiskaaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/oxotnichi_sosiska.jpg','rb'),
        caption="""Narxi:   300gr-19.500 so'm
Tarkibi: Oxotnichi sosiska mol go'shtidan.
        """,reply_markup=oxotnichi_sosiskaa300gr)
    await call.message.delete()

@dp.callback_query_handler(text="oxotnichi_sosiskaaBOSHI600gr")
async def oxotnichi_sosiskaaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/oxotnichi_sosiska.jpg','rb'),
        caption="""Narxi:   600gr-39.000 so'm
Tarkibi: Oxotnichi sosiska mol go'shtidan.
        """,reply_markup=oxotnichi_sosiskaa600gr)
    await call.message.delete()

@dp.callback_query_handler(text="oxotnichi_sosiskaaBOSHI1kg")
async def oxotnichi_sosiskaaBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/oxotnichi_sosiska.jpg','rb'),
        caption="""Narxi:   1-kg-65.000 so'm
Tarkibi: Oxotnichi sosiska mol go'shtidan.
        """,reply_markup=oxotnichi_sosiskaa1kg)
    await call.message.delete()








@dp.callback_query_handler(text="mol_til_tushonkaaBOSHI300gr")
async def mol_til_tushonkaaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_til_tushonka.jpg','rb'),
        caption="""Narxi:   1-litr-80.000 so'm
Tarkibi: Xolsizlik bezovta qilyaptimi ,bizda buning ajoyib yechimi bor Til tusho'nkasi , uning tarkibida bir qancha moddalar bo'lib ular insonga quvvat va tetiklik bag'shlaydi , farzand kutuvchilar uchun esa ayni muddao😋
        """,reply_markup=mol_til_tushonkaa300gr)
    await call.message.delete()

@dp.callback_query_handler(text="mol_til_tushonkaaBOSHI600gr")
async def mol_til_tushonkaaBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_til_tushonka.jpg','rb'),
        caption="""Narxi:   700ml-65.000 so'm
Tarkibi: Xolsizlik bezovta qilyaptimi ,bizda buning ajoyib yechimi bor Til tusho'nkasi , uning tarkibida bir qancha moddalar bo'lib ular insonga quvvat va tetiklik bag'shlaydi , farzand kutuvchilar uchun esa ayni muddao😋
        """,reply_markup=mol_til_tushonkaa600gr)
    await call.message.delete()

@dp.callback_query_handler(text="mol_til_tushonkaaBOSHI1kg")
async def mol_til_tushonkaaBOSHI1kg(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_til_tushonka.jpg','rb'),
        caption="""Narxi:   1-kg-65.000 so'm
Tarkibi: Xolsizlik bezovta qilyaptimi ,bizda buning ajoyib yechimi bor Til tusho'nkasi , uning tarkibida bir qancha moddalar bo'lib ular insonga quvvat va tetiklik bag'shlaydi , farzand kutuvchilar uchun esa ayni muddao😋
        """,reply_markup=mol_til_tushonkaa1kg)
    await call.message.delete()



@dp.callback_query_handler(text="mol_tushonkaaBOSHI300gr")
async def mol_tushonkaaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_tushonka.jpg','rb'),
        caption="""Narxi:   400ml-45.000 so'm
Tarkibi: Tog' mavsumi boshlanib,xordiq maskaniga yo'l oldingizmi taom tayyorlashga ortiqcha urinmang bizda sizga xamroh bo'luvchi va xalqimiz sevib iste'mol qiladigan sifatli mol tushonkasi bor.
        """,reply_markup=mol_tushonkaa300gr)
    await call.message.delete()

@dp.callback_query_handler(text="mol_tushonkaaBOSHI600gr")
async def mol_tushonkaaBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_tushonka.jpg','rb'),
        caption="""Narxi:   1-Litr-65.000 so'm
Tarkibi: Tog' mavsumi boshlanib,xordiq maskaniga yo'l oldingizmi taom tayyorlashga ortiqcha urinmang bizda sizga xamroh bo'luvchi va xalqimiz sevib iste'mol qiladigan sifatli mol tushonkasi bor.
        """,reply_markup=mol_tushonkaa600gr)
    await call.message.delete()

# @dp.callback_query_handler(text="mol_tushonkaaBOSHI1kg")
# async def mol_tushonkaaBOSHI1kg(call:CallbackQuery):
#     await call.message.answer_photo(
#         photo=open('images/mol_tushonka.jpg','rb'),
#         caption="""Narxi:   1-kg-65000 so'm
# Tarkibi: Tog' mavsumi boshlanib,xordiq maskaniga yo'l oldingizmi taom tayyorlashga ortiqcha urinmang bizda sizga xamroh bo'luvchi va xalqimiz sevib iste'mol qiladigan sifatli mol tushonkasi bor.
#         """,reply_markup=mol_tushonkaa1kg)
#     await call.message.delete()



@dp.callback_query_handler(text="qoy_til_tushonkaaBOSHI300gr")
async def qoy_til_tushonkaaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qoy_til_tushonka.jpg','rb'),
        caption="""Narxi:   700ml-55.000 so'm
Tarkibi: Til tusho'nkasi , uning tarkibida bir qancha moddalar bo'lib ular insonga quvvat va tetiklik bag'shlaydi , farzand kutuvchilar uchun esa ayni muddao.
        """,reply_markup=qoy_til_tushonkaa300gr)
    await call.message.delete()

@dp.callback_query_handler(text="qoy_til_tushonkaaBOSHI600gr")
async def qoy_til_tushonkaaBOSHI600gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qoy_til_tushonka.jpg','rb'),
        caption="""Narxi:   400ml-35.000 so'm
Tarkibi: Til tusho'nkasi , uning tarkibida bir qancha moddalar bo'lib ular insonga quvvat va tetiklik bag'shlaydi , farzand kutuvchilar uchun esa ayni muddao.
        """,reply_markup=qoy_til_tushonkaa600gr)
    await call.message.delete()

# @dp.callback_query_handler(text="qoy_til_tushonkaaBOSHI1kg")
# async def qoy_til_tushonkaaBOSHI1kg(call:CallbackQuery):
#     await call.message.answer_photo(
#         photo=open('images/qoy_til_tushonka.jpg','rb'),
#         caption="""Narxi:   1-kg-65000 so'm
# Tarkibi: Til tusho'nkasi , uning tarkibida bir qancha moddalar bo'lib ular insonga quvvat va tetiklik bag'shlaydi , farzand kutuvchilar uchun esa ayni muddao.
#         """,reply_markup=qoy_til_tushonkaa1kg)
#     await call.message.delete()




@dp.callback_query_handler(text="quyon_tushonkaaBOSHI300gr")
async def quyon_tushonkaaBOSHI300gr(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/quyon_tushonka.jpg','rb'),
        caption="""Narxi:   700ml-65.000 so'm
Tarkibi: Қуён гўшти жуда мулойим, хуштам ҳамда оқсилларга бой бўлади. Шунинг учун ёш болаларга, кексаларга ва бемор кишиларга пархез таом сифатида
танаввул қилиш тавсия этилади. Енгил ҳазм бўлиши сабабли ортиқча вазнга эга инсонлар учун айни муддао.
        """,reply_markup=quyon_tushonkaa300gr)
    await call.message.delete()


# @dp.callback_query_handler(text="quyon_tushonkaaBOSHI600gr")
# async def quyon_tushonkaaBOSHI300gr(call:CallbackQuery):
#     await call.message.answer_photo(
#         photo=open('images/quyon_tushonka.jpg','rb'),
#         caption="""Narxi:   1-Litr-100.000 so'm
# Tarkibi: Қуён гўшти жуда мулойим, хуштам ҳамда оқсилларга бой бўлади. Шунинг учун ёш болаларга, кексаларга ва бемор кишиларга пархез таом сифатида
# танаввул қилиш тавсия этилади. Енгил ҳазм бўлиши сабабли ортиқча вазнга эга инсонлар учун айни муддао.
#         """,reply_markup=quyon_tushonkaa600gr)
#     await call.message.delete()






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)