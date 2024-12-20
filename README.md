## Это приложение сравнивает погодные условия в двух заданных географических точках, используя API AccuWeather. В процессе разработки были учтены и обработаны следующие типы ошибок:

### 1. Ошибки валидации входных данных:

**Тип ошибки:** ValueError при преобразовании введенных пользователем координат (широта и долгота) в числа с плавающей запятой. Возникает, если пользователь вводит некорректные данные (текст, символы, и т.д.). \

**Обработка:** Исключение ValueError перехватывается, и пользователю выводится сообщение flash("Вводимые параметры должны быть числами с плавающей точкой", 'warning'). Это предотвращает крах приложения и информирует пользователя о некорректном вводе. \

**Влияние на систему:** При возникновении данной ошибки, приложение не обрабатывает запрос, а возвращает пользователю форму ввода с предупреждением. Общая работоспособность не нарушается.

### 2. Ошибки HTTP:

**Тип ошибки:** requests.exceptions.HTTPError — обозначает ошибку при обращении к API AccuWeather. В частности, обрабатываются ошибки со статусом кода 503 (Service Unavailable). \

**Обработка:** Исключение requests.exceptions.HTTPError перехватывается. \
Если код ошибки 503, это может указывать на проблему с API ключом или временную недоступность сервиса. В этом случае пользователю выводится сообщение flash("API ключ не авторизирован", 'warning').
Для других кодов ошибок выводится более информативное сообщение flash(f"API Error: {e.response.status_code}"), позволяющее определить природу проблемы.

**Влияние на систему:** При возникновении ошибок API приложение не выполняет запрос к API и не вычисляет сравнение погоды. Пользователю возвращается стартовая стра
ница с сообщением об ошибке. Общая работоспособность сохраняется, но запрос пользователя не обрабатывается.
