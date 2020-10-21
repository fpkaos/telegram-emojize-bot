import telebot
from telebot import types
from telebot import apihelper

# Deploy: http://blog.disonds.com/2017/03/20/python-bot-dlya-vk-na-heroku/
# pip3 freeze > requirements.txt
# apihelper.proxy = {'https':'socks5://127.0.0.1:9050'}

token = ''
bot = telebot.TeleBot(token)
logo = "\U0001F198"

# Fix my misconceptions: https://unicode.org/emoji/charts/full-emoji-list.html
letters = {
    'з' : '\U00000033\U0000FE0F\U000020E3',
    'г' : '\U0001F3D7',
    'л' : '\U0001F587',
    'е' : '\U0001F4E7',
    'ё' : '\U0001F4E7',
    'э' : '\U0001F4E7',
    'т' : '\U0000271D',
    'к' : '\U0001F38B', #'\U0000262A',
    'у' : '\U0001F4B9', #'\U000026CE',
    'х' : '\U00002716',
    'я' : '\U0001F397', #'\U000000AE',
    'ж' : '\U0000002A\U0000FE0F\U000020E3',
    'а' : '\U0001F170',
    'б' : '\U00000036\U0000FE0F\U000020E3',
    'м' : '\U000024C2',
    'о' : '\U0001F17E',
    'р' : '\U0001F17F',
    'п' : '\U000026E9',
    'и' : '\U00002139',
    'й' : '\U00002139',
    'с' : '\U0000262A',
    'д' : '\U000026FA',
    'ш' : '\U0001F3B9',
    'щ' : '\U0001F531',
    'н' : '\U00002653', #'\U0001F3E8',
    'в' : '\U0001F171',
    'ф' : '\U0001F004',
    'ч' : '\U00000034\U0000FE0F\U000020E3',
    'ц' : '\U0001FA7A',
    'ы' : '\U00002139', #'\U000023EF', #'\U0001F3BC',
    'ь' : '\U0001F300',
    'ъ' : '\U0001F300',
    'ю' : '\U0001F5DD', #'\U0001F9BD',

    # ~  Symbols   ~ #

    '!' : '\U00002757',
    '?' : '\U00002753',
    '#' : '\U00000023\U0000FE0F\U000020E3',
    '-' : '\U00002796',
    ' ' : '    ',

    # ~  English  ~ #

    'a' : '\U0001F170',
    'b' : '\U0001F171',
    'c' : '\U0000262A',
    'd' : '\U0001F4D0',
    'e' : '\U0001F4E7',
    'f' : '\U0001F38F',
    'g' : '\U0001F5DC',
    'h' : '\U0001F3E8',
    'i' : '\U00002139',
    'j' : '\U0001F9E6',
    'k' : '\U0001F38B',
    'l' : '\U0001F6F4',
    'm' : '\U000024C2',
    'n' : '\U000023F8',
    'o' : '\U0001F17E',
    'p' : '\U0001F17F',
    'q' : '\U0001F4CD',
    'r' : '\U000000AE',
    's' : '\U0001F4B2',
    't' : '\U0000271D',
    'u' : '\U000026CE',
    'v' : '\U00002648',
    'w' : '\U00002693',
    'x' : '\U00002716',
    'y' : '\U0001F4B9',
    'z' : '\U000026A1'
}

def num(n):
    return chr(n) + chr(0xFE0F) + chr(0x20E3)

def add_emoji_nums(symbols):
    n = '\U00000030'
    symbols.update({str(i): num(ord(n) + i) for i in range(0,11)})

symbols = {}
symbols.update(letters)
add_emoji_nums(symbols)

jokes = {
        'сос' : '\U0001F198',
        'sos' : '\U0001F198',
        'мит' : '\U0001F969',
        'кат' : '\U0001F63A',
        'cat' : '\U0001F63A',
        'вал' : '\U0001F3E0',
        'бал' : '\U0001F3D0',
        'бат' : '\U0001F987',
        'рет' : '\U0001F400',
        'гот' : '\U0001F410',
        'гав' : '\U0001F436',
        'до' : '\U0001F6AA',
        'дор' : '\U0001F6AA',
        'пиз' : '\U0000262E',
        'лиз' : '\U0001F98A',
        'бас' : '\U0001F68E',
        'ток' : '\U0001F4AC',
        'ice' : '\U00002744',
        'айс' : '\U00002744',
        'рот' : '\U0001F444',
        'dak' : '\U0001F986',
        'дак' : '\U0001F986',
        'кит' : '\U0001F433',
        'пир' : '\U0001F350',
        'пер' : '\U0001F350',
        'баг' : '\U0001F41E',
        'ант' : '\U0001F41C',
        'веб' : '\U0001F578',
        'три' : '\U0001F333',
        'fri' : '\U0001F35F',
        'фри' : '\U0001F35F',
        'рак' : '\U0001F99E',
        'лупа' : '\U0001F50E',
        'meet': '\U0001F969',
        'met' : '\U0001F969',
        'meat' : '\U0001F969',
        'off' : '\U0001F4F4',
        'тако' : '\U0001F32E',
        'сто' : '\U0001F4AF',
        'ай' : '\U0001F441',
        'иг' : '\U0001F95A',
        'of' : '\U0001F4F4',
        'ов' : '\U0001F4F4',
        'ок' : '\U0001F197',
        'ok' : '\U0001F197',
        'уп' : '\U0001F199',
        'up' : '\U0001F199',
        'вс' : '\U0001F19A',
        'vs' : '\U0001F19A',
        'му' : '\U0001F42E',
        'my' : '\U0001F42E',
        'mu' : '\U0001F42E',
        'нг' : '\U0001F196',
        'ng' : '\U0001F196',
        'id' : '\U0001F194',
        'ид' : '\U0001F194',
        'ир' : '\U0001F442',
        'ir' : '\U0001F442',
        'er' : '\U0001F442',
        'ti' : '\U0001F375',
        'ти' : '\U0001F375',
        'ит' : '\U0001F37D',
        'it' : '\U0001F37D',
        'ис' : '\U00002744',
        'on' : '\U0001F51B',
        'он' : '\U0001F51B',
        'oo' : '\U0000267E',
        'ab' : '\U0001F18E',
        'аб' : '\U0001F18E',
        'cl' : '\U0001F191',
        'кл' : '\U0001F191',
    }

def joked(joke) -> str:
    for query in jokes.keys():
        if query in joke:
            joke = joke.replace(query, jokes[query])
    return joke

def build(origin) -> str:
    res = ''
    for l in origin:
        if l in symbols.keys():
            res += symbols[l]
        else:
            res += l
    return res

def emojize(normal : str) -> list:
    try:
        origin = normal.lower()
        joke = joked(origin)
        if len(origin) < 20 and joke != origin:
            return [build(joke), build(origin)]
        return [build(origin)]
    except Exception as e:
        return [f"Error: {e}"]

def answer(query):
    answer = emojize(query.query)
    return [types.InlineQueryResultArticle(
            id=i + 1, title=logo,
            description=j,
            input_message_content=types.InputTextMessageContent(
            message_text=j)) for i, j in enumerate(answer)]

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def main(query):
    bot.answer_inline_query(query.id, answer(query))

bot.polling()
