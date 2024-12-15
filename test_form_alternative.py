import os
import time

from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_form_submission_with_s_and_banner_removal():
    # Удаление рекламных баннеров
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")


    # Путь к файлу
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'resources', 'test_upload.png')

    # Заполнение формы
    s('#firstName').type('Sonic')
    s('#lastName').type('Syndicate')
    s('#userEmail').type('test@mail.ru')
    s('[for="gender-radio-1"]').click()  # Male
    s('#userNumber').type('9939993388')

    # Выбор даты рождения
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').click().s('[value="2"]').click()  # Март (03)
    s('.react-datepicker__year-select').click().s('[value="1960"]').click()  # 1960
    s('.react-datepicker__day--003:not(.react-datepicker__day--outside-month)').click()  # 03

    # Заполнение поля предметов
    s('#subjectsInput').type('Maths').press_enter()

    # Выбор хобби
    s('[for="hobbies-checkbox-1"]').click()  # Sports
    s('[for="hobbies-checkbox-3"]').click()  # Music

    # Загрузка файла
    s('#uploadPicture').send_keys(file_path)

    # Ввод адреса
    s('#currentAddress').type('Moscow 5')

    # Выбор штата и города
    s('#state').click().s('#react-select-3-option-0').click()  # NCR
    s('#city').click().s('#react-select-4-option-0').click()  # Delhi

    # Отправка формы
    s('#submit').click()

    # Проверка таблицы результатов
    s('.table-responsive').should(have.text('Sonic Syndicate'))
    s('.table-responsive').should(have.text('test@mail.ru'))
    s('.table-responsive').should(have.text('Male'))
    s('.table-responsive').should(have.text('9939993388'))
    s('.table-responsive').should(have.text('03 March,1960'))
    s('.table-responsive').should(have.text('Maths'))
    s('.table-responsive').should(have.text('Sports'))
    s('.table-responsive').should(have.text('Music'))
    s('.table-responsive').should(have.text('test_upload.png'))
    s('.table-responsive').should(have.text('Moscow 5'))
    s('.table-responsive').should(have.text('NCR Delhi'))