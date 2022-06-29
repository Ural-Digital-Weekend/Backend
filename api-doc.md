# AviaService Api

## Auth

### `POST` `/auth/register` - Регистрация пользователя

<details>
  <summary>Подробнее</summary>

#### Request body parameters

- email* - email пользователя [**Обязательный**]
- username* - логин пользователя [**Обязательный**]
- password* - пароль пользователя[**Обязательный**]

#### Responses

  ```json
  200 OK
{}
  ```

</details>

### `POST` `/auth/login` - Авторизация пользователя

<details>
  <summary>Подробнее</summary>

#### Request body parameters

- username* - email пользователя [**Обязательный**]
- password* - пароль пользователя[**Обязательный**]

#### Responses

  ```json
  200 OK
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}
  ```

</details>

## Airports

### `GET` `/airports` - Получить сведения об аэропорте

<details>
  <summary>Подробнее</summary>

#### Request path parameters

- page - номер страницы
- count - кол-во элементов на странице
- search - Поиск
- type_id - Идентификатор типа аэропорта
- country_id - Идентификатор страны
- region_id - Идентификатор региона

#### Responses

  ```json
  200 OK
{
  "count": 20,
  "next": 2,
  "previous": null,
  "items": [
    {
      "name": "Total Rf Heliport",
      "region_id": 1,
      "type_id": 2,
      "country_id": 3
    }
  ]
}
  ```

  ```json
  400 Bad Request
  ```

</details>

### `GET` `/airports/:id` - Получить сведения об аэропорте

<details>
  <summary>Подробнее</summary>

#### Request path parameters

- id*  - идентификатор аэропорта [**Обязательный**]

#### Responses

  ```json
  200 OK
{
  "ident": "00A",
  "type": "heliport",
  "name": "Total Rf Heliport",
  "elevation_ft": "11",
  "continent": "NA",
  "iso_country": "US",
  "iso_region": "US-PA",
  "municipality": "Bensalem",
  "gps_code": "00A",
  "iata_code": "",
  "local_code": "00A",
  "coordinates": "-74.93360137939453, 40.07080078125"
}
  ```

  ```json
  404 Not Found
  ```

</details>

## Airports | Comments

### `GET` `/airports/:id/comments` - Получить комментарии об аэропорте

<details>
  <summary>Подробнее</summary>

#### Request path parameters

- id*  - идентификатор аэропорта [**Обязательный**]

#### Responses:

  ```json
  200 OK
{
  "count": 20,
  "next": 2,
  "previous": null,
  "items": [
    {
      "email": "user@example.com",
      "date": "2022-01-01",
      "comment": "Хороший аэропорт"
    }
  ]
}
  ```

</details>

### `POST` `/airport/:id/comments` `[Auth]` - Отправить комментарий об аэропорте

<details>
  <summary>Подробнее</summary>

#### Request headers

- `Authorization: Bearer <access token>`

#### Request path parameters

- id*  - идентификатор аэропорта [**Обязательный**]

#### Request body parameters

- comment* - комментарий [**Обязательный**]

#### Responses:

  ```json
  201 Created
{}
  ```  

  ```json
  400 Bad Request
  ```

</details>

### `PUT` `/airports/comments/:id` `[Auth]` - Изменить комментарий об аэропорте

<details>
  <summary>Подробнее</summary>

#### Request headers

- `Authorization: Bearer <access token>`

#### Request path parameters

- id*  - идентификатор аэропорта [**Обязательный**]

#### Request body parameters

- comment* - комментарий [**Обязательный**]

#### Responses:

  ```json
  200 OK
{}
  ```

  ```json
  400 Bad Request
  ```  

  ```json
  404 Not Found
  ```

</details>

### `DELETE` `/airports/comments/:id` `[Auth]` - Удалить комментарий об аэропорте

<details>
  <summary>Подробнее</summary>

#### Request headers

- `Authorization: Bearer <access token>`

#### Request path parameters

- id*  - идентификатор аэропорта [**Обязательный**]

#### Responses:

  ```json
  204 No content
{}
  ```  

  ```json
  404 Not Found
  ```

</details>

## Handbooks

### `GET` `/hanbooks/countries` - Получить справочник стран

<details>
  <summary>Подробнее</summary>

#### Responses

  ```json
  200 OK
[
  {
    "id": 1,
    "title": "US"
  }
]
  ```

</details>

### `GET` `/hanbooks/regions` - Получить справочник регионов

<details>
  <summary>Подробнее</summary>

#### Responses

  ```json
  200 OK
[
  {
    "id": 1,
    "title": "US-PA"
  }
]
  ```

</details>

### `GET` `/hanbooks/airports-types` - Получить справочник типов аэропортов

<details>
  <summary>Подробнее</summary>

#### Responses

  ```json
  200 OK
[
  {
    "id": 1,
    "title": "heliport"
  }
]
  ```

</details>