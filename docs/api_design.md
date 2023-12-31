#### ACCOUNTS
#### Log in
* Endpoint path: /token
* Endpoint method: POST

* Request shape (form):
  * email: string
  * password: string

* Response: Account information
* Response shape (JSON):
    ```json
    {
      "account": {
        «key»: type»,
      },
      "token": string
    }
    ```
#### Log out
* Endpoint path: /token
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Always true
* Response shape (JSON):
    ```json
    true
    ```
#### Sign up
* Endpoint path: /accounts
* Endpoint method: POST

* Response: Account information
* Response shape:
    ```json
    {
      "account": [
        {
          "name": string,
          "email": string,
          "password": string,
          "password_reentered": string,
          "phone_number": string,
          "picture_url": string,
          "about_me": string


        }
      ]
    }
    ```
#### Update account
* Endpoint path: /accounts/{account_id}
* Endpoint method: PUT

* Response: Account information
* Response shape:
    ```json
    {
      "account": [
        {
          "name": string,
          "email": string,
          "password": string,
          "password_reentered": string,
          "phone_number": string,
          "picture_url": string,
          "about_me": string


        }
      ]
    }
    ```

#### BACH PARTIES
#### List bach parties
* Endpoint path: /api/bach_parties
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: List of bachelor parties
* Response shape:
    ```json
        {
        "bach_party": [
            {
            "name": string,
            "description": string,
            "host": object/int,
            "picture_url": string,
            "location": string,
            "start_date": date,
            "end_date": date,
            "host_notes": string,
            "status": string,
            }
        ]
        }
    ```
#### Create bach party
* Endpoint path: /api/bach_parties
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Response: Bach party information
* Response shape:
    ```json
        {
        "bach_party": [
            {
            "name": string,
            "description": string,
            "host": object/int,
            "picture_url": string,
            "location": string,
            "start_date": date,
            "end_date": date,
            "host_notes": string,
            "status": string,
            }
        ]
        }
    ```
#### Update bach party
* Endpoint path: /api/bach_party/{bach_party_id}
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Response: Bach party information
* Response shape:
    ```json
        {
        "bach_party": [
            {
            "name": string,
            "description": string,
            "host": object/int,
            "picture_url": string,
            "location": string,
            "start_date": date,
            "end_date": date,
            "host_notes": string,
            "status": string,
            }
        ]
        }
    ```
#### Delete bach party
* Endpoint path: /api/bach_party/{bach_party_id}
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Always true
* Response shape (JSON):
    ```json
    true
    ```



#### BACH PARTY EVENTS
#### List bach party events
* Endpoint path: /api/bach_parties/{bach_party_id}
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: List of bach party events
* Response shape:
    ```json
    {
      "bach_party_event": [
        {
          "event_name": string,
          "description": string,
          "location": string,
          "event_date": date,
          "start_time": time,
          "end_time": time,
          "picture_url": string,
          "bach_party": object/int
        }
      ]
    }
    ```
#### Create bach party event
* Endpoint path: /api/bach_parties/{bach_party_id}
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Response: Bach party event information
* Response shape:
    ```json
    {
      "bach_party_event": [
        {
          "event_name": string,
          "description": string,
          "location": string,
          "event_date": date,
          "start_time": time,
          "end_time": time,
          "picture_url": string,
          "bach_party": object/int
        }
      ]
    }
    ```
#### Update bach party event
* Endpoint path: /api/bach_parties/{bach_party_id}/{bach_party_event_id}
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Response: Bach party event information
* Response shape:
    ```json
    {
      "bach_party_event": [
        {
          "event_name": string,
          "description": string,
          "location": string,
          "event_date": date,
          "start_time": time,
          "end_time": time,
          "picture_url": string,
          "bach_party": object/int
        }
      ]
    }
    ```
#### Delete bach party event
* Endpoint path: /api/bach_parties/{batch_party_id}/{bach_party_event_id}
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Always true
* Response shape (JSON):
    ```json
    true

* Endpoint path: /api/bach_party/{bach_party_id}
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

* Response: Bach party information
* Response shape:
    ```json
        {
        "bach_party": [
            {
            "name": string,
            "location": string,
            "start_date": date,
            "end_date": date,
            "status": string
            }
        ]
        }
    ```


#### CHARGES
#### Create charge
* Endpoint path: /api/accounts/charges
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Response: Charge information
* Response shape:
    ```json
        {
        "charge": [
            {
            "title": string,
            "bach_party": object/int,
            "amount": float,
            "description": string,
            "account": object/int,
            "date": date
            }
        ]
        }
    ```
#### List total charges
* Endpoint path: /api/accounts/charges
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: Total charges information
* Response shape:
    ```json
        {
        "charge": [
            {
            "title": string,
            "bach_party": object/int,
            "amount": float,
            "description": string,
            "account": object/int,
            "date": date
            }
        ]
        }
    ```
#### List bach party charges
* Endpoint path: /api/accounts/charges/{bach_party_id}
* Endpoint method: GET

* Headers:
  * Authorization: Bearer token

* Response: Bach party charges information
* Response shape:
    ```json
        {
        "charge": [
            {
            "title": string,
            "bach_party": object/int,
            "amount": float,
            "description": string,
            "account": object/int,
            "date": date
            }
        ]
        }
    ```
#### Update charge
* Endpoint path: /api/accounts/charges/{charge_id}
* Endpoint method: POST

* Headers:
  * Authorization: Bearer token

* Response: Charge information
* Response shape:
    ```json
        {
        "charge": [
            {
            "title": string,
            "bach_party": object/int,
            "amount": float,
            "description": string,
            "account": object/int,
            "date": date
            }
        ]
        }
    ```


#### THINGS TO DO
Logged in users, and non-logged in users, can click a "Get details" button and be re-directed to Yelp for additional details about the business.

* Endpoint path: /api/things_to_do

* Endpoint method: GET

* Response: Yelp API info
* Response shape:
    ```json
        {
            "businesses": [
                {
                "rating": int,
                "price": string,
                "phone": string,
                "review_count": int,
                "name": string,
                "url": string,
                "image_url": string,
                "location": {
                    "city": string,
                    "address2": string,
                    "address3": string,
                    "state": string,
                    "address1": string,
                    "zip_code": string
                }
                },
                // ...
            ]
        }
