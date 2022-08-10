import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
from cc import checker,checker_two
from db_ import check, del_cc, new_user,statq,add_cc
from markups import delete, start_but,genmarkup,call_markup

bot = Bot(token='TOKEN') #токен бота.
dp = Dispatcher(bot)

@dp.callback_query_handler(lambda c: c.data.split('|')[0] == 'del')
async def stat(call: types.CallbackQuery):
    save_data= (call.data).replace('del|','')

    del_cc(call.message.chat.id,save_data)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='<b>'+save_data+' удалена</b>',parse_mode='html')


@dp.callback_query_handler(lambda c: c.data.split('|')[0] == 'save')
async def stat(call: types.CallbackQuery):
    save_data=[]
    save_data.append((call.data).replace('save|',''))
    add_cc(call.message.chat.id,save_data[0])
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='<b>Сохранено</b>',parse_mode='html')


@dp.callback_query_handler(lambda c: c.data.split('|')[0] == 'show')
async def stat(call: types.CallbackQuery):
    cc_to_delete= call.data.replace('show|','')
    print(cc_to_delete)
    cc_to_show=call.data.replace('show|','').replace('✅ ','').replace('❌ ','')
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=str(await checker_two(cc_to_show.split('|'))),parse_mode='html',reply_markup=delete(cc_to_delete))


@dp.message_handler(text=['🗒 Мои CC','/my_cc'])
async def my_c(message: types.Message):
    
    await bot.send_message(message.chat.id,'<b>@SMOKE_SOFTWARE, Твои CC</b>',parse_mode='html',reply_markup=call_markup(message.chat.id))



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if check(message.chat.id)==False:
        new_user(message.chat.id)
    await bot.send_message(message.chat.id,'<strong>✋ Добро пожаловать в бота для проверки CC</strong>\nBY @SMOKE_SOFTWARE',parse_mode='html',reply_markup=start_but)


@dp.message_handler(commands=['cc'])
async def cc_command(message: types.Message):
    text = message.text.replace('/cc','').replace('/',' ').replace('|',' ').split()
    result = await checker(text)
    if result.replace('<b>','').split()[0]=='❌':
        d=False
    else:
        d=True
    await bot.send_message(message.chat.id,result,parse_mode='html',reply_markup=genmarkup(text,nice=d))


@dp.message_handler(text=['❓ Команды','/help'])
async def help_commande(message: types.Message):
    await bot.send_message(message.chat.id,'<b>⚡️ Команды бота CC CHEKER</b>\n\n<code>/cc</code> 377754002000872|07|2024|000 - <b>чекнуть карту</b>\n<code>/stat</code> - <b>статистика</b>\nСЛИТО В @SMOKE_SOFTWARE',parse_mode='html')


@dp.message_handler(text=['🔄 Статистика','/stat'])
async def stat(message: types.Message):
     await bot.send_message(message.chat.id,str(statq()))


if __name__ == '__main__':
    executor.start_polling(dp)
