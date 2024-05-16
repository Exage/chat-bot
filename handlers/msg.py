from aiogram import Router, types, F

router = Router()

@router.message(F.text)
async def chating(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет')
    elif 'как дела' in message.text.lower():
        randint = random.randint(0, 3)

        if randint == 0:
            await message.reply('Норм')
        elif randint == 1:
            await message.reply('Все круто')
        elif randint == 2:
            await message.reply('Плохо :(')
        elif randint == 3:
            await message.reply('Живем')


    else:
        await message.reply('Я скинхед!!!!')