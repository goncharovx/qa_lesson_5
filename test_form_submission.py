import os

from selene import have
from selene.support.shared import browser


def test_form_submission():
    # Путь к файлу
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'resources', 'test_upload.png')

    # Заполнение формы
    browser.element('#firstName').type('Sonic')
    browser.element('#lastName').type('Syndicate')
    browser.element('#userEmail').type('test@mail.ru')
    browser.element('[for="gender-radio-1"]').click() # Male
    browser.element('#userNumber').type('9939993388')

    # Выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="2"]').click()  # Март (03)
    browser.element('.react-datepicker__year-select').click().element('[value="1960"]').click()  # 1960
    browser.element('.react-datepicker__day--003:not(.react-datepicker__day--outside-month)').click()  # 03

    # Заполнение поля предметы
    browser.element('#subjectsInput').type('Maths').press_enter()

    # Выбор хобби
    browser.element('[for="hobbies-checkbox-1"]').click()  # Sports
    browser.element('[for="hobbies-checkbox-3"]').click()  # Music

    # Загрузка файла
    browser.element('#uploadPicture').send_keys(file_path)

    # Ввод адреса
    browser.element('#currentAddress').type('Moscow 5')

    # Выбор штата и города
    browser.element('#state').click().element('#react-select-3-option-0').click()  # NCR
    browser.element('#city').click().element('#react-select-4-option-0').click()  # Delhi

    # Отправка формы
    browser.element('#submit').click()

    # Проверка таблицы результатов
    browser.element('.table-responsive').should(have.text('Sonic Syndicate'))
    browser.element('.table-responsive').should(have.text('test@mail.ru'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('9939993388'))
    browser.element('.table-responsive').should(have.text('03 March,1960'))
    browser.element('.table-responsive').should(have.text('Maths'))
    browser.element('.table-responsive').should(have.text('Sports'))
    browser.element('.table-responsive').should(have.text('Music'))
    browser.element('.table-responsive').should(have.text('test_upload.png'))
    browser.element('.table-responsive').should(have.text('Moscow 5'))
    browser.element('.table-responsive').should(have.text('NCR Delhi'))
