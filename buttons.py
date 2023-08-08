from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

til = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text = "🇺🇿 O'zbekcha"),
    KeyboardButton(text = "🇷🇺 Русский"),
    ]
  ],
  resize_keyboard=True
  )

kontakt = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text = "Mening raqamim",request_contact=True),
    ],
    [
    KeyboardButton(text = "⬅️Ortga"),
    ],
  ],
  resize_keyboard=True
)

geolakatsya = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text = "📍Geolakatsya",request_location=True),
    ],
    [
    KeyboardButton(text = "Ortga"),
    ],
  ],
  resize_keyboard=True
)

knopka = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text = "✅Xa"),
    KeyboardButton(text = "❌Yo'q")
    ],
    [
    KeyboardButton(text = "Orqaga"),
    ],
  ],
  resize_keyboard=True
)

buyurtma = ReplyKeyboardMarkup(
  keyboard=[
    [
    KeyboardButton(text = "📄 Menu"),
    ],
    [
    KeyboardButton(text = "✏️Fikr bildirish"),
    KeyboardButton(text = "👨‍👩‍👦Biz haqimizda"),
    ],
    [
    KeyboardButton(text = "📋Ma'lumot"),
    KeyboardButton(text = "⚙️Sozlamalar"),
    ],
  ],
  resize_keyboard=True
)

knpka_orqaga = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text = "⬅️Orqaga"),
    ],
  ],
  resize_keyboard=True
)



menu = ReplyKeyboardMarkup(
  keyboard=[
    [
    KeyboardButton(text = "🐑Qo'y go'sht mahsulotlari",callback_data = "qoy_gosht_mahs"),
    KeyboardButton(text = "🐄Mol go'sht mahsulotlari",callback_data = "mol_gosht_mahs"),
    ],
    [
    KeyboardButton(text = "🐴Ot go'sht mahsulotlari",callback_data = "ot_gosht_mahs"),
    KeyboardButton(text = "🐓Tovuq go'sht mahsulotlari",callback_data = "tovuq_gosht_mahs"),
    ],
    [
    KeyboardButton(text = "🍖Kalbasa mahsulotlari",callback_data = "kalbasa_mahs"),
    KeyboardButton(text = "🥩Tushonka",callback_data = "tushonka_mahs"),
    ],
    [
    KeyboardButton(text = "⬅️Orqaga",callback_data="back"),
    ],
  ],
  resize_keyboard = True
)








qoy_g_mahBOSHI = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text = "Mol + Qo'y Rulet", callback_data="mol_qoyBOSHI"),
    KeyboardButton(text = "Qo'y To'sh Rulet", callback_data="qoy_toshBOSHI"),
    ],
    [
    KeyboardButton(text = "Qo'y Tandir Rulet", callback_data="qoy_tandirBOSHI"),
    ],
    [
    KeyboardButton(text = "⬅️Ortga qaytish",callback_data="back"),
    ],
  ],
  resize_keyboard = True
)

qoy_g_m = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="mol_qoy300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="mol_qoy600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="mol_qoy1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back1"),
    ],
  ],
)


qoy_g_mahsulotlari_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_qoy_rulet_300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_qoy_rulet_300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_qoy_rulet_300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_qoy_rulet_300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_qoy_rulet_300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_qoy_rulet_300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_qoy_rulet_300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_qoy_rulet_300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_qoy_rulet_300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back2"),
    ],
  ],
)

qoy_g_mahsulotlari_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_qoy_rulet_600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_qoy_rulet_600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_qoy_rulet_600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_qoy_rulet_600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_qoy_rulet_600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_qoy_rulet_600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_qoy_rulet_600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_qoy_rulet_600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_qoy_rulet_600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back2"),
    ],
  ],
)

qoy_g_mahsulotlari_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_qoy_rulet_1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_qoy_rulet_1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_qoy_rulet_1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_qoy_rulet_1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_qoy_rulet_1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_qoy_rulet_1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_qoy_rulet_1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_qoy_rulet_1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_qoy_rulet_1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back2"),
    ],
  ],
)

#/////////////////////////////////////////////////////////////////////

qoy_g_m1 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="qoy_tosh300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="qoy_tosh600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="qoy_tosh1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back1"),
    ],
  ],
)


qoy_toshRulet_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qoy_tosh300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qoy_tosh300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qoy_tosh300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qoy_tosh300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qoy_tosh300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qoy_tosh300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qoy_tosh300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qoy_tosh300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qoy_tosh300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back3"),
    ],
  ],
)

qoy_toshRulet_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qoy_tosh600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qoy_tosh600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qoy_tosh600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qoy_tosh600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qoy_tosh600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qoy_tosh600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qoy_tosh600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qoy_tosh600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qoy_tosh600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back3"),
    ],
  ],
)

qoy_toshRulet_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qoy_tosh1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="qoy_tosh1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="qoy_tosh1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qoy_tosh1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="qoy_tosh1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="qoy_tosh1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qoy_tosh1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="qoy_tosh1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="qoy_tosh1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back3"),
    ],
  ],
)
#/////////////////////////////////////////////////////////////////////////////////////////


qoy_tandir = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="qoy_tandir300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="qoy_tandir600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="qoy_tandir1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back1"),
    ],
  ],
)

qoy_tandirRulet_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qoy_tandir300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qoy_tandir300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qoy_tandir300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qoy_tandir300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qoy_tandir300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qoy_tandir300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qoy_tandir300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qoy_tandir300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qoy_tandir300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back4"),
    ],
  ],
)


qoy_tandirRulet_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qoy_tandir600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qoy_tandir600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qoy_tandir600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qoy_tandir600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qoy_tandir600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qoy_tandir600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qoy_tandir600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qoy_tandir600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qoy_tandir600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back4"),
    ],
  ],
)

qoy_tandirRulet_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qoy_tandir1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="qoy_tandir1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="qoy_tandir1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qoy_tandir1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="qoy_tandir1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="qoy_tandir1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qoy_tandir1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="qoy_tandir1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="qoy_tandir1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back4"),
    ],
  ],
)


mol_tilmahBOSHI = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text = "Mol Til Rulet", callback_data="mol_til_rulBOSHI"),
    KeyboardButton(text = "Mol Press", callback_data="mol_pressBOSHI"),
    ],
    [
    KeyboardButton(text = "Mol Archa Rulet", callback_data="mol_archa_rulBOSHI"),
    KeyboardButton(text = "Mol Rulet", callback_data="mol_ruletBOSHI"),
    ],
    [
    KeyboardButton(text = "Mol Tarash Rulet", callback_data="mol_tarash_rulBOSHI"),
    ],
    [
    KeyboardButton(text = "Bosh Menuga qaytish",callback_data="back11"),
    ],
  ],
  resize_keyboard = True
)


mol_tilRuletBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="mol_tilRuletBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="mol_tilRuletBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="mol_tilRuletBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back5"),
    ],
  ],
)


mol_pressBOSHI1 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="mol_pressBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="mol_pressBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="mol_pressBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back5"),
    ],
  ],
)


mol_archa_ruletBOSHI1 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="mol_archaBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="mol_archaBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="mol_archaBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back5"),
    ],
  ],
)

mol_ruletBOSHI1 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="mol_ruletBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="mol_ruletBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="mol_ruletBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back5"),
    ],
  ],
)

mol_tarash_ruletBOSHI1 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="mol_tarashBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="mol_tarashBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="mol_tarashBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back5"),
    ],
  ],
)
#//////////////////////////////////MOL TIL RULET///////////////////////////////////////////////////
mol_tilRulet_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tilRule300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tilRule300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tilRule300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tilRule300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tilRule300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tilRule300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tilRule300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tilRule300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tilRule300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back6"),
    ],
  ],
)

mol_tilRulet_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tilRule600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tilRule600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tilRule600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tilRule600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tilRule600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tilRule600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tilRule600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tilRule600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tilRule600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back6"),
    ],
  ],
)

mol_tilRulet_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tilRule1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tilRule1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tilRule1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tilRule1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tilRule1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tilRule1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tilRule1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tilRule1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tilRule1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back6"),
    ],
  ],
)
#///////////////////////////////////MOL PRESS///////////////////////////////////////////

mol_presss_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_presss300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_presss300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_presss300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_presss300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_presss300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_presss300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_presss300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_presss300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_presss300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back7"),
    ],
  ],
)


mol_presss_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_presss600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_presss600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_presss600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_presss600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_presss600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_presss600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_presss600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_presss600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_presss600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back7"),
    ],
  ],
)

mol_presss_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_presss1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_presss1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_presss1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_presss1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_presss1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_presss1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_presss1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_presss1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_presss1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back7"),
    ],
  ],
)
#//////////////////////////////////MOL ARCHA RULET//////////////////////////////////////////

mol_archa_rulet_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_archa_rulet300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_archa_rulet300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_archa_rulet300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_archa_rulet300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_archa_rulet300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_archa_rulet300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_archa_rulet300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_archa_rulet300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_archa_rulet300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back8"),
    ],
  ],
)

mol_archa_rulet_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_archa_rulet600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_archa_rulet600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_archa_rulet600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_archa_rulet600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_archa_rulet600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_archa_rulet600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_archa_rulet600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_archa_rulet600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_archa_rulet600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back8"),
    ],
  ],
)


mol_archa_rulet_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_archa_rulet1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_archa_rulet1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_archa_rulet1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_archa_rulet1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_archa_rulet1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_archa_rulet1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_archa_rulet1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_archa_rulet1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_archa_rulet1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back8"),
    ],
  ],
)
#/////////////////////////////////MOL RULET///////////////////////////////////////////////

mol_ruletBOSHI1 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="mol_ruletBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="mol_ruletBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="mol_ruletBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back11"),
    ],
  ],
)

mol__rulet_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol__rulet300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol__rulet300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol__rulet300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol__rulet300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol__rulet300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol__rulet300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol__rulet300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol__rulet300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol__rulet300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back9"),
    ],
  
  ],
)

mol__rulet_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol__rulet600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol__rulet600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol__rulet600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol__rulet600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol__rulet600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol__rulet600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol__rulet600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol__rulet600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol__rulet600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back9"),
    ],
  
  ],
)

mol__rulet_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol__rulet1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol__rulet1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol__rulet1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol__rulet1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol__rulet1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol__rulet1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol__rulet1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol__rulet1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol__rulet1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back9"),
    ],
  
  ],
)
#////////////////////////////////MOL TARASH RULET//////////////////////////////////////////////

mol_tarash_ruletBOSHI1 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="mol_tarash_ruletBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="mol_tarash_ruletBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="mol_tarash_ruletBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back11"),
    ],
  ],
)


mol_tarash_rulet_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tarash_rulet300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tarash_rulet300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tarash_rulet300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tarash_rulet300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tarash_rulet300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tarash_rulet300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tarash_rulet300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tarash_rulet300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tarash_rulet300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back10"),
    ],
  
  ],
)

mol_tarash_rulet_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tarash_rulet600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tarash_rulet600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tarash_rulet600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tarash_rulet600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tarash_rulet600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tarash_rulet600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tarash_rulet600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tarash_rulet600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tarash_rulet600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back10"),
    ],
  
  ],
)



mol_tarash_rulet_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tarash_rulet1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tarash_rulet1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tarash_rulet1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tarash_rulet1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tarash_rulet1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tarash_rulet1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tarash_rulet1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tarash_rulet1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tarash_rulet1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back10"),
    ],
  
  ],
)







ot_goshtmahBOSHI = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text = "Qazi"),
    KeyboardButton(text = "Ot Bo'yin Rulet"),
    ],
    [
    KeyboardButton(text = "Ot Kachalka Rulet"),
    KeyboardButton(text = "Toy Tarash Rulet"),
    ],
    [
    KeyboardButton(text = "Qarta Go'shtli"),
    KeyboardButton(text = "Qarta"),
    ],
    [
    KeyboardButton(text = "Bosh Menuga Qaytish"),
    ],
  ],
  resize_keyboard = True
)
#////////////////QAZI///////////////////////////////////////

ot_qaziBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text ="300gr", callback_data="ot_qaziBOSHI300gr"),
    InlineKeyboardMarkup(text ="600gr",callback_data="ot_qaziBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text ="1kg",callback_data="ot_qaziBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back99"),
    ],
  ],
)

ot_qazi_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="ot_qazi300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="ot_qazi300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="ot_qazi300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="ot_qazi300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="ot_qazi300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="ot_qazi300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="ot_qazi300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="ot_qazi300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="ot_qazi300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back12"),
    ],
  
  ],
)

ot_qazi_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="ot_qazi600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="ot_qazi600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="ot_qazi600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="ot_qazi600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="ot_qazi600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="ot_qazi600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="ot_qazi600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="ot_qazi600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="ot_qazi600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back12"),
    ],
  
  ],
)

ot_qazi_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="ot_qazi1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="ot_qazi1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="ot_qazi1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="ot_qazi1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="ot_qazi1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="ot_qazi1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="ot_qazi1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="ot_qazi1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="ot_qazi1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back12"),
    ],
  
  ],
)

#/////////////////OT BO'YIN RULET//////////////////////////

ot_boyin_ruletBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="ot_boyin_ruletBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="ot_boyin_ruletBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="ot_boyin_ruletBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back01"),
    ],
  ],
)


ot_boyin_rulet_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="ot_boyin_rulet300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="ot_boyin_rulet300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="ot_boyin_rulet300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="ot_boyin_rulet300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="ot_boyin_rulet300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="ot_boyin_rulet300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="ot_boyin_rulet300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="ot_boyin_rulet300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="ot_boyin_rulet300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back13"),
    ],
  
  ],
)

ot_boyin_rulet_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="ot_boyin_rulet600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="ot_boyin_rulet600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="ot_boyin_rulet600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="ot_boyin_rulet600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="ot_boyin_rulet600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="ot_boyin_rulet600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="ot_boyin_rulet600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="ot_boyin_rulet600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="ot_boyin_rulet600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back13"),
    ],
  
  ],
)


ot_boyin_rulet_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="ot_boyin_rulet1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="ot_boyin_rulet1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="ot_boyin_rulet1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="ot_boyin_rulet1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="ot_boyin_rulet1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="ot_boyin_rulet1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="ot_boyin_rulet1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="ot_boyin_rulet1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="ot_boyin_rulet1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back13"),
    ],
  
  ],
)

#//////////////////////////OT KACHALKA RULET////////////////////////////

ot_kachalka_ruletBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="ot_kachalka_ruletBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="ot_kachalka_ruletBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="ot_kachalka_ruletBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back01"),
    ],
  ],
)

ot_kachalka_rulet_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="ot_kachalka_rulet300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="ot_kachalka_rulet300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="ot_kachalka_rulet300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="ot_kachalka_rulet300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="ot_kachalka_rulet300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="ot_kachalka_rulet300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="ot_kachalka_rulet300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="ot_kachalka_rulet300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="ot_kachalka_rulet300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back14"),
    ],
  
  ],
)


ot_kachalka_rulet_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="ot_kachalka_rulet600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="ot_kachalka_rulet600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="ot_kachalka_rulet600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="ot_kachalka_rulet600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="ot_kachalka_rulet600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="ot_kachalka_rulet600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="ot_kachalka_rulet600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="ot_kachalka_rulet600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="ot_kachalka_rulet600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back14"),
    ],
  
  ],
)

ot_kachalka_rulet_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="ot_kachalka_rulet1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="ot_kachalka_rulet1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="ot_kachalka_rulet1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="ot_kachalka_rulet1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="ot_kachalka_rulet1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="ot_kachalka_rulet1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="ot_kachalka_rulet1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="ot_kachalka_rulet1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="ot_kachalka_rulet1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back14"),
    ],
  
  ],
)

#//////////////////////TOY TARASH RULET/////////////////////////

toy_tarash_ruletBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="toy_tarash_ruletBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="toy_tarash_ruletBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="toy_tarash_ruletBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back01"),
    ],
  ],
)

toy_tarash_rulet_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="toy_tarash_rulet300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="toy_tarash_rulet300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="toy_tarash_rulet300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="toy_tarash_rulet300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="toy_tarash_rulet300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="toy_tarash_rulet300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="toy_tarash_rulet300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="toy_tarash_rulet300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="toy_tarash_rulet300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back15"),
    ],
  
  ],
)


toy_tarash_rulet_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="toy_tarash_rulet600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="toy_tarash_rulet600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="toy_tarash_rulet600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="toy_tarash_rulet600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="toy_tarash_rulet600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="toy_tarash_rulet600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="toy_tarash_rulet600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="toy_tarash_rulet600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="toy_tarash_rulet600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back15"),
    ],
  
  ],
)

toy_tarash_rulet_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="toy_tarash_rulet1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="toy_tarash_rulet1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="toy_tarash_rulet1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="toy_tarash_rulet1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="toy_tarash_rulet1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="toy_tarash_rulet1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="toy_tarash_rulet1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="toy_tarash_rulet1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="toy_tarash_rulet1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back15"),
    ],
  
  ],
)

#///////////////////////////QARTA GOSHTLI///////////////////////////////

qarta_goshtliBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="qarta_goshtliBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="qarta_goshtliBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="qarta_goshtliBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back01"),
    ],
  ],
)

qarta_goshtli_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qarta_goshtli300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qarta_goshtli300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qarta_goshtli300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qarta_goshtli300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qarta_goshtli300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qarta_goshtli300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qarta_goshtli300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qarta_goshtli300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qarta_goshtli300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back16"),
    ],
  
  ],
)

qarta_goshtli_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qarta_goshtli600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qarta_goshtli600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qarta_goshtli600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qarta_goshtli600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qarta_goshtli600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qarta_goshtli600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qarta_goshtli600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qarta_goshtli600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qarta_goshtli600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back16"),
    ],
  
  ],
)


qarta_goshtli_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qarta_goshtli1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="qarta_goshtli1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="qarta_goshtli1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qarta_goshtli1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="qarta_goshtli1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="qarta_goshtli1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qarta_goshtli1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="qarta_goshtli1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="qarta_goshtli1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back16"),
    ],
  
  ],
)

#//////////////////////QARTA////////////////////////////////////////////

qartaBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="qartaBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="qartaBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="qartaBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back01"),
    ],
  ],
)

qarta_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qarta300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qarta300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qarta300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qarta300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qarta300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qarta300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qarta300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qarta300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qarta300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back17"),
    ],
  
  ],
)

qarta_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qarta600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qarta600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qarta600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qarta600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qarta600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qarta600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qarta600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qarta600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qarta600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back17"),
    ],
  
  ],
)

qarta_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qarta1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="qarta1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="qarta1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qarta1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="qarta1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="qarta1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qarta1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="qarta1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="qarta1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back17"),
    ],
  
  ],
)


#///////////////////////TOVUQ GOSHT MAHSULOTLARI///////////////////////////////////

tovuq_goshtmahBOSHI = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text = "Dudlangan Kurka", callback_data="dudlangan_kurkaBOSHI"),
    KeyboardButton(text = "Tovuq Tandir Rulet", callback_data="tovuq_tandir_ruletBOSHI"),
    ],
    [
    KeyboardButton(text = "Dudlangan Tovuq", callback_data="dudlangan_tovuqBOSHI"),
    ],
    [
    KeyboardButton(text = "⬅️Bosh Menuga Qaytish",callback_data="back"),
    ],
  ],
  resize_keyboard = True
)

#////////////////////DUDLANGAN KURKA///////////////////////////////////////////////////////

dudlangan_kurkaaBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="dudlangan_kurkaBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="dudlangan_kurkaBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="dudlangan_kurkaBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back18"),
    ],
  ],
)

dudlangan_kurka_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="dudlangan_kurka300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="dudlangan_kurka300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="dudlangan_kurka300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="dudlangan_kurka300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="dudlangan_kurka300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="dudlangan_kurka300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="dudlangan_kurka300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="dudlangan_kurka300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="dudlangan_kurka300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back19"),
    ],
  
  ],
)

dudlangan_kurka_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="dudlangan_kurka600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="dudlangan_kurka600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="dudlangan_kurka600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="dudlangan_kurka600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="dudlangan_kurka600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="dudlangan_kurka600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="dudlangan_kurka600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="dudlangan_kurka600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="dudlangan_kurka600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back19"),
    ],
  
  ],
)

dudlangan_kurka_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="dudlangan_kurka1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="dudlangan_kurka1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="dudlangan_kurka1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="dudlangan_kurka1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="dudlangan_kurka1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="dudlangan_kurka1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="dudlangan_kurka1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="dudlangan_kurka1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="dudlangan_kurka1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back19"),
    ],
  
  ],
)
#/////////////////////////TOVUQ TANDIR RULET///////////////////////////////////


tovuq_tandir_rulettBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="tovuq_tandir_rulettBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="tovuq_tandir_rulettBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="tovuq_tandir_rulettBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back18"),
    ],
  ],
)

tovuq_tandir_rulett_300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="tovuq_tandir_rulett300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="tovuq_tandir_rulett300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="tovuq_tandir_rulett300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="tovuq_tandir_rulett300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="tovuq_tandir_rulett300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="tovuq_tandir_rulett300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="tovuq_tandir_rulett300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="tovuq_tandir_rulett300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="tovuq_tandir_rulett300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back20"),
    ],
  
  ],
)

tovuq_tandir_rulett_600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="tovuq_tandir_rulett600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="tovuq_tandir_rulett600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="tovuq_tandir_rulett600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="tovuq_tandir_rulett600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="tovuq_tandir_rulett600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="tovuq_tandir_rulett600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="tovuq_tandir_rulett600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="tovuq_tandir_rulett600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="tovuq_tandir_rulett600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back20"),
    ],
  
  ],
)

tovuq_tandir_rulett_1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="tovuq_tandir_rulett1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="tovuq_tandir_rulett1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="tovuq_tandir_rulett1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="tovuq_tandir_rulett1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="tovuq_tandir_rulett1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="tovuq_tandir_rulett1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="tovuq_tandir_rulett1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="tovuq_tandir_rulett1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="tovuq_tandir_rulett1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back20"),
    ],
  
  ],
)

#////////////////////////DUDLANGAN TOVUQ////////////////////////////////////

dudlangan_tovuqqBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="dudlangan_tovuqqBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="dudlangan_tovuqqBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="dudlangan_tovuqqBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back18"),
    ],
  ],
)


dudlangan_tovuq300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="dudlangan_tovuq300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="dudlangan_tovuq300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="dudlangan_tovuq300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="dudlangan_tovuq300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="dudlangan_tovuq300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="dudlangan_tovuq300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="dudlangan_tovuq300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="dudlangan_tovuq300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="dudlangan_tovuq300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back21"),
    ],
  
  ],
)

dudlangan_tovuq600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="dudlangan_tovuq600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="dudlangan_tovuq600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="dudlangan_tovuq600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="dudlangan_tovuq600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="dudlangan_tovuq600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="dudlangan_tovuq600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="dudlangan_tovuq600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="dudlangan_tovuq600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="dudlangan_tovuq600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back21"),
    ],
  
  ],
)

dudlangan_tovuq1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="dudlangan_tovuq1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="dudlangan_tovuq1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="dudlangan_tovuq1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="dudlangan_tovuq1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="dudlangan_tovuq1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="dudlangan_tovuq1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="dudlangan_tovuq1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="dudlangan_tovuq1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="dudlangan_tovuq1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back21"),
    ],
  
  ],
)

















Kal_mahBOSHI = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text = "Mol Va Tovuq Goshtidan Kalbasa", callback_data="mol_tovuq_kalBOSHI"),
    KeyboardButton(text = "Dudlangan Kalbasa", callback_data="dudlangan_kalBOSHI"),
    ],
    [
    KeyboardButton(text = "Qaynatma Kalbasa", callback_data="qaynatma_kalBOSHI"),
    KeyboardButton(text = "Sosiska", callback_data="sosiskaBOSHI"),
    ],
    [
    KeyboardButton(text = "Oxotnichi Sosiska", callback_data="oxotnichi_sosiskaBOSHI"),
    ],
    [
    KeyboardButton(text = "⬅️Bosh Menuga qaytish",callback_data="back"),
    ],
  ],
  resize_keyboard = True
)
#/////////////////////////////////////////////////////////////////////////////////////
mol_tovuq_kalbasaBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="mol_tovuq_kalbasaBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="mol_tovuq_kalbasaBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="mol_tovuq_kalbasaBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back22"),
    ],
  ],
)

mol_tovuq_kalbasa300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tovuq_kalbasa300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tovuq_kalbasa300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tovuq_kalbasa300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tovuq_kalbasa300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tovuq_kalbasa300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tovuq_kalbasa300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tovuq_kalbasa300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tovuq_kalbasa300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tovuq_kalbasa300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back23"),
    ],
  
  ],
)

mol_tovuq_kalbasa600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tovuq_kalbasa600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tovuq_kalbasa600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tovuq_kalbasa600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tovuq_kalbasa600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tovuq_kalbasa600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tovuq_kalbasa600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tovuq_kalbasa600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tovuq_kalbasa600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tovuq_kalbasa600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back23"),
    ],
  
  ],
)


mol_tovuq_kalbasa1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tovuq_kalbasa1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tovuq_kalbasa1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tovuq_kalbasa1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tovuq_kalbasa1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tovuq_kalbasa1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tovuq_kalbasa1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tovuq_kalbasa1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tovuq_kalbasa1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tovuq_kalbasa1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back23"),
    ],
  
  ],
)
#///////////////////////////////////////////////////////////////////////////
dudlangan_kalbasaBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1kg", callback_data="dudlangan_kalbasaBOSHI300gr"),
    InlineKeyboardMarkup(text = "650gr",callback_data="dudlangan_kalbasaBOSHI600gr"),
    ],
    [
    # InlineKeyboardMarkup(text = "Dudlangan Kalbasa 650gr",callback_data="dudlangan_kalbasaBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back22"),
    ],
  ],
)

dudlangan_kalbasa300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="dudlangan_kalbasa300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="dudlangan_kalbasa300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="dudlangan_kalbasa300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="dudlangan_kalbasa300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="dudlangan_kalbasa300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="dudlangan_kalbasa300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="dudlangan_kalbasa300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="dudlangan_kalbasa300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="dudlangan_kalbasa300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back24"),
    ],
  
  ],
)

dudlangan_kalbasa600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="dudlangan_kalbasa600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="dudlangan_kalbasa600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="dudlangan_kalbasa600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="dudlangan_kalbasa600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="dudlangan_kalbasa600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="dudlangan_kalbasa600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="dudlangan_kalbasa600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="dudlangan_kalbasa600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="dudlangan_kalbasa600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back24"),
    ],
  
  ],
)


dudlangan_kalbasa1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="dudlangan_kalbasa1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="dudlangan_kalbasa1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="dudlangan_kalbasa1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="dudlangan_kalbasa1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="dudlangan_kalbasa1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="dudlangan_kalbasa1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="dudlangan_kalbasa1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="dudlangan_kalbasa1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="dudlangan_kalbasa1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back24"),
    ],
  
  ],
)
#///////////////////QAYNATMA KALBASA///////////////////////////////////////

qaynatma_kalbasaBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1kg", callback_data="qaynatma_kalbasaBOSHI300gr"),
    InlineKeyboardMarkup(text = "650gr",callback_data="qaynatma_kalbasaBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "500gr",callback_data="qaynatma_kalbasaBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back22"),
    ],
  ],
)

qaynatma_kalbasa300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qaynatma_kalbasa300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qaynatma_kalbasa300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qaynatma_kalbasa300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qaynatma_kalbasa300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qaynatma_kalbasa300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qaynatma_kalbasa300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qaynatma_kalbasa300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qaynatma_kalbasa300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qaynatma_kalbasa300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back25"),
    ],
  
  ],
)

qaynatma_kalbasa600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qaynatma_kalbasa600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qaynatma_kalbasa600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qaynatma_kalbasa600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qaynatma_kalbasa600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qaynatma_kalbasa600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qaynatma_kalbasa600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qaynatma_kalbasa600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qaynatma_kalbasa600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qaynatma_kalbasa600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back25"),
    ],
  
  ],
)

qaynatma_kalbasa1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qaynatma_kalbasa1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="qaynatma_kalbasa1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="qaynatma_kalbasa1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qaynatma_kalbasa1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="qaynatma_kalbasa1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="qaynatma_kalbasa1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qaynatma_kalbasa1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="qaynatma_kalbasa1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="qaynatma_kalbasa1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back25"),
    ],
  
  ],
)


#//////////////////////////////////SOSISKA/////////////////////////////////////////////////////////

sosiskaaBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "Sosiska 1ta idishda", callback_data="sosiskaaBOSHI300gr"),
    # InlineKeyboardMarkup(text = "Sosiska 600gr",callback_data="sosiskaaBOSHI600gr"),
    ],
    [
    # InlineKeyboardMarkup(text = "Sosiska 1kg",callback_data="sosiskaaBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back22"),
    ],
  ],
)

sosiskaa300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="sosiskaa300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="sosiskaa300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="sosiskaa300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="sosiskaa300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="sosiskaa300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="sosiskaa300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="sosiskaa300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="sosiskaa300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="sosiskaa300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back26"),
    ],
  
  ],
)

sosiskaa600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="sosiskaa600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="sosiskaa600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="sosiskaa600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="sosiskaa600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="sosiskaa600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="sosiskaa600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="sosiskaa600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="sosiskaa600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="sosiskaa600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back26"),
    ],
  
  ],
)

sosiskaa1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="sosiskaa1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="sosiskaa1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="sosiskaa1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="sosiskaa1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="sosiskaa1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="sosiskaa1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="sosiskaa1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="sosiskaa1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="sosiskaa1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back26"),
    ],
  
  ],
)
#//////////////////OXOTNICHI SOSISKA//////////////////////////////

oxotnichi_sosiskaaBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "300gr", callback_data="oxotnichi_sosiskaaBOSHI300gr"),
    InlineKeyboardMarkup(text = "600gr",callback_data="oxotnichi_sosiskaaBOSHI600gr"),
    ],
    [
    InlineKeyboardMarkup(text = "1kg",callback_data="oxotnichi_sosiskaaBOSHI1kg"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back22"),
    ],
  ],
)

oxotnichi_sosiskaa300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="oxotnichi_sosiskaa300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="oxotnichi_sosiskaa300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="oxotnichi_sosiskaa300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="oxotnichi_sosiskaa300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="oxotnichi_sosiskaa300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="oxotnichi_sosiskaa300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="oxotnichi_sosiskaa300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="oxotnichi_sosiskaa300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="oxotnichi_sosiskaa300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back27"),
    ],
  
  ],
)

oxotnichi_sosiskaa600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="oxotnichi_sosiskaa600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="oxotnichi_sosiskaa600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="oxotnichi_sosiskaa600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="oxotnichi_sosiskaa600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="oxotnichi_sosiskaa600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="oxotnichi_sosiskaa600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="oxotnichi_sosiskaa600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="oxotnichi_sosiskaa600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="oxotnichi_sosiskaa600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back27"),
    ],
  
  ],
)

oxotnichi_sosiskaa1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="oxotnichi_sosiskaa1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="oxotnichi_sosiskaa1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="oxotnichi_sosiskaa1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="oxotnichi_sosiskaa1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="oxotnichi_sosiskaa1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="oxotnichi_sosiskaa1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="oxotnichi_sosiskaa1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="oxotnichi_sosiskaa1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="oxotnichi_sosiskaa1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back27"),
    ],
  
  ],
)










tushonka_mahBOSHI = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text = "Mol Til Tushonka", callback_data="mol_til_tushBOSHI"),
    KeyboardButton(text = "Mol Tushonka", callback_data="mol_tushBOSHI"),
    ],
    [
    KeyboardButton(text = "Qo'y Til Tushonka", callback_data="qoy_til_tushBOSHI"),
    KeyboardButton(text = "Quyon Tushonka", callback_data="quyon_tushBOSHI"),
    ],
    [
    KeyboardButton(text = "⬅️Bosh menuga qaytish",callback_data="back"),
    ],
  ],
  resize_keyboard = True
)
#////////////////////////////////////////////////////////////////////////////////

mol_til_tushonkaaBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "700ml", callback_data="mol_til_tushonkaaBOSHI300gr"),
    InlineKeyboardMarkup(text = "1 litr",callback_data="mol_til_tushonkaaBOSHI600gr"),
    ],
    # [
    # InlineKeyboardMarkup(text = "1kg",callback_data="mol_til_tushonkaaBOSHI1kg"),
    # ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back28"),
    ],
  ],
)

mol_til_tushonkaa300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_til_tushonkaa300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_til_tushonkaa300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_til_tushonkaa300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_til_tushonkaa300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_til_tushonkaa300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_til_tushonkaa300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_til_tushonkaa300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_til_tushonkaa300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_til_tushonkaa300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back29"),
    ],
  
  ],
)

mol_til_tushonkaa600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_til_tushonkaa600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_til_tushonkaa600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_til_tushonkaa600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_til_tushonkaa600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_til_tushonkaa600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_til_tushonkaa600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_til_tushonkaa600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_til_tushonkaa600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_til_tushonkaa600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back29"),
    ],
  
  ],
)

mol_til_tushonkaa1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_til_tushonkaa1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_til_tushonkaa1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_til_tushonkaa1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_til_tushonkaa1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_til_tushonkaa1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_til_tushonkaa1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_til_tushonkaa1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_til_tushonkaa1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_til_tushonkaa1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back29"),
    ],
  
  ],
)
#//////////////////////MOL TUSHONKA///////////////////////////////////////////


mol_tushonkaaBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "400ml", callback_data="mol_tushonkaaBOSHI300gr"),
    InlineKeyboardMarkup(text = "1 litr",callback_data="mol_tushonkaaBOSHI600gr"),
    ],
    # [
    # InlineKeyboardMarkup(text = "1kg",callback_data="mol_tushonkaaBOSHI1kg"),
    # ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back28"),
    ],
  ],
)

mol_tushonkaa300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tushonkaa300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tushonkaa300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tushonkaa300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tushonkaa300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tushonkaa300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tushonkaa300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tushonkaa300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tushonkaa300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tushonkaa300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back30"),
    ],
  
  ],
)

mol_tushonkaa600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tushonkaa600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tushonkaa600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tushonkaa600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tushonkaa600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tushonkaa600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tushonkaa600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tushonkaa600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tushonkaa600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tushonkaa600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back30"),
    ],
  
  ],
)

mol_tushonkaa1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="mol_tushonkaa1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="mol_tushonkaa1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="mol_tushonkaa1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="mol_tushonkaa1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="mol_tushonkaa1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="mol_tushonkaa1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="mol_tushonkaa1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="mol_tushonkaa1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="mol_tushonkaa1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back30"),
    ],
  
  ],
)
#///////////////////////////////QOY TIL TUSHONKA//////////////////////////////////////////

qoy_til_tushonkaaBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "700ml", callback_data="qoy_til_tushonkaaBOSHI300gr"),
    InlineKeyboardMarkup(text = "400ml",callback_data="qoy_til_tushonkaaBOSHI600gr"),
    ],
    # [
    # InlineKeyboardMarkup(text = "1kg",callback_data="qoy_til_tushonkaaBOSHI1kg"),
    # ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back28"),
    ],
  ],
)


qoy_til_tushonkaa300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qoy_til_tushonkaa300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qoy_til_tushonkaa300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qoy_til_tushonkaa300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qoy_til_tushonkaa300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qoy_til_tushonkaa300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qoy_til_tushonkaa300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qoy_til_tushonkaa300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qoy_til_tushonkaa300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qoy_til_tushonkaa300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back31"),
    ],
  
  ],
)

qoy_til_tushonkaa600gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qoy_til_tushonkaa600gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="qoy_til_tushonkaa600gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="qoy_til_tushonkaa600gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qoy_til_tushonkaa600gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="qoy_til_tushonkaa600gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="qoy_til_tushonkaa600gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qoy_til_tushonkaa600gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="qoy_til_tushonkaa600gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="qoy_til_tushonkaa600gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back31"),
    ],
  
  ],
)

qoy_til_tushonkaa1kg = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="qoy_til_tushonkaa1kg1"),
    InlineKeyboardMarkup(text = "2",callback_data="qoy_til_tushonkaa1kg2"),
    InlineKeyboardMarkup(text = "3",callback_data="qoy_til_tushonkaa1kg3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="qoy_til_tushonkaa1kg4"),
    InlineKeyboardMarkup(text = "5",callback_data="qoy_til_tushonkaa1kg5"),
    InlineKeyboardMarkup(text = "6",callback_data="qoy_til_tushonkaa1kg6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="qoy_til_tushonkaa1kg7"),
    InlineKeyboardMarkup(text = "8",callback_data="qoy_til_tushonkaa1kg8"),
    InlineKeyboardMarkup(text = "9",callback_data="qoy_til_tushonkaa1kg9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back31"),
    ],
  
  ],
)
#///////////////////////////////QUYON TUSHONKA//////////////////////////////////////////////

quyon_tushonkaaBOSHI = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "700ml", callback_data="quyon_tushonkaaBOSHI300gr"),
    # InlineKeyboardMarkup(text = "1 litr",callback_data="quyon_tushonkaaBOSHI600gr"),
    ],
    # [
    # InlineKeyboardMarkup(text = "1kg",callback_data="quyon_tushonkaaBOSHI1kg"),
    # ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back28"),
    ],
  ],
)


quyon_tushonkaa300gr = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardMarkup(text = "1",callback_data="quyon_tushonkaa300gr1"),
    InlineKeyboardMarkup(text = "2",callback_data="quyon_tushonkaa300gr2"),
    InlineKeyboardMarkup(text = "3",callback_data="quyon_tushonkaa300gr3"),
    ],
    [
    InlineKeyboardMarkup(text = "4",callback_data="quyon_tushonkaa300gr4"),
    InlineKeyboardMarkup(text = "5",callback_data="quyon_tushonkaa300gr5"),
    InlineKeyboardMarkup(text = "6",callback_data="quyon_tushonkaa300gr6"),
    ],
    [
    InlineKeyboardMarkup(text = "7",callback_data="quyon_tushonkaa300gr7"),
    InlineKeyboardMarkup(text = "8",callback_data="quyon_tushonkaa300gr8"),
    InlineKeyboardMarkup(text = "9",callback_data="quyon_tushonkaa300gr9"),
    ],
    [
    InlineKeyboardMarkup(text = "Ortga",callback_data="back32"),
    ],
  
  ],
)

# quyon_tushonkaa600gr = InlineKeyboardMarkup(
#   inline_keyboard = [
#     [
#     InlineKeyboardMarkup(text = "1",callback_data="quyon_tushonkaa600gr1"),
#     InlineKeyboardMarkup(text = "2",callback_data="quyon_tushonkaa600gr2"),
#     InlineKeyboardMarkup(text = "3",callback_data="quyon_tushonkaa600gr3"),
#     ],
#     [
#     InlineKeyboardMarkup(text = "4",callback_data="quyon_tushonkaa600gr4"),
#     InlineKeyboardMarkup(text = "5",callback_data="quyon_tushonkaa600gr5"),
#     InlineKeyboardMarkup(text = "6",callback_data="quyon_tushonkaa600gr6"),
#     ],
#     [
#     InlineKeyboardMarkup(text = "7",callback_data="quyon_tushonkaa600gr7"),
#     InlineKeyboardMarkup(text = "8",callback_data="quyon_tushonkaa600gr8"),
#     InlineKeyboardMarkup(text = "9",callback_data="quyon_tushonkaa600gr9"),
#     ],
#     [
#     InlineKeyboardMarkup(text = "Ortga",callback_data="back32"),
#     ],
  
#   ],
# )


#//////////////////////////////TUGADI///////////////////////////////////////////////


