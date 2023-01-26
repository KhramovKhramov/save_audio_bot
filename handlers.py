from database import db, get_or_create_user, save_to_db
import os
from utils import has_oblect_on_image, export_to_wav


async def save_pic(update, context):
    user = get_or_create_user(db,
    user_id=update.message.from_user.id,
    username=update.message.from_user.username)

    os.makedirs('downloads', exist_ok=True)
    photo_file = await context.bot.getFile(update.message.photo[-1].file_id)
    file_name = os.path.join(
        'downloads',
        f'{update.message.photo[-1].file_id}.jpg')
    await photo_file.download_to_drive(custom_path=file_name)

    if has_oblect_on_image(file_name, object_name='headshot'):
        save_to_db(db, user, file_name, folder='images')

        os.makedirs(f'files/user_{user["user_id"]}/pics', exist_ok=True)
        new_filename = os.path.join(f'files/user_{user["user_id"]}/pics', f'{update.message.photo[-1].file_id}.jpg')
        os.rename(file_name, new_filename)

        await update.message.reply_text('Фото сохранено')
    else:
        os.remove(file_name)
        await update.message.reply_text('На фото нет лица')


async def save_voice(update, context):
    user = get_or_create_user(db,
    user_id=update.message.from_user.id,
    username=update.message.from_user.username)

    os.makedirs('downloads', exist_ok=True)
    file_id = update.message.voice.file_id
    voice_file = await context.bot.getFile(file_id)
    file_name = os.path.join(
        'downloads',
        f'{file_id}.ogg')
    await voice_file.download_to_drive(custom_path=file_name)

    export_to_wav(file_name, user['user_id'], file_id, format='ogg')
    save_to_db(db, user, file_name, folder='audio')

    os.remove(file_name)
    
    await update.message.reply_text('Войс сохранен!')


async def save_audio(update, context):
    user = get_or_create_user(db,
    user_id=update.message.from_user.id,
    username=update.message.from_user.username)

    os.makedirs('downloads', exist_ok=True)
    file_id = update.message.audio.file_id
    audio_file = await context.bot.getFile(file_id)
    file_name = os.path.join(
        'downloads',
        f'{file_id}.mp3')
    await audio_file.download_to_drive(custom_path=file_name)

    export_to_wav(file_name, user['user_id'], file_id, format='mp3')
    save_to_db(db, user, file_name, folder='audio')

    os.remove(file_name)
    
    await update.message.reply_text('Аудио сохранено!')

