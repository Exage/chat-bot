from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.carreer_keyboard import make_keyboard

router = Router()

availble_jobs = [
    'Программист',
    'Маркетолог',
    'Менеджер',
    'Аналитик',
    'Бухгалтер',
    'Риелтор',
    'Юрист'
]

availble_grades = [
    'Низкий',
    'Средний',
    'Высокий',
]

class Choice(StatesGroup):
    job = State()
    grade = State()

@router.message(Command(commands=['prof']))
async def prof(message: types.Message, state: FSMContext):
    await message.answer('Какая профессия вас интересует?', reply_markup=make_keyboard(availble_jobs))
    await state.set_state(Choice.job)

@router.message(Choice.job, F.text.in_(availble_jobs))
async def grade(message: types.Message, state: FSMContext):
    await message.answer('Как вы оцениваете свое профессию?', reply_markup=make_keyboard(availble_grades))
    await state.set_state(Choice.grade)

@router.message(Choice.job)
async def job_incorrectly(message: types.Message):
    await message.answer('Неправильно. Попробуй еще раз', reply_markup=make_keyboard(availble_jobs))

@router.message(Choice.grade, F.text.in_(availble_grades))
async def grade(message: types.Message, state: FSMContext):
    await message.answer(f'Вы оценили свой уровень на "{message.text}". Вы все прошли, с вами свяжутся наши hr', reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

@router.message(Choice.grade)
async def grade_incorrectly(message: types.Message):
    await message.answer('Неправильно. Попробуй еще раз', reply_markup=make_keyboard(availble_grades))