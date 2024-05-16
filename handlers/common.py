from aiogram import Router, types, F
from aiogram.filters.command import Command
import random

from datetime import datetime

from keyboards.keyboards import keyboard
from utils.random_fox import fox

router = Router()

@router.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=keyboard)

@router.message(Command(commands=['user']))
async def user(message: types.Message):

    name = f'{message.from_user.first_name} (@{message.from_user.username})' if message.from_user.first_name else f"(@{message.from_user.username})"

    have_premium = "есть премиум" if message.from_user.is_premium else "нет премиума"

    await message.answer(f'Тебя зовут: {name};\n- У тебя {have_premium}\n')

@router.message(Command(commands=['info']))
async def info(message: types.Message):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await message.answer(f'Время сейчас: {date}\nСлучайное число: {random.randint(1, 235)}')

@router.message(F.text.lower() == 'покажи лису')
async def throw_fox(message: types.Message):
    img_fox = fox()
    await message.answer('Ща будет')
    await message.answer_photo(img_fox, 'Лови')