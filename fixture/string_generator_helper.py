import random
import string
import datetime
import time


class StringGeneratoHelper:

    def get_random_string(self, num):
        string_rand = ''.join(random.choice(string.ascii_lowercase) for i in range(num))
        return string_rand

    def get_random_email(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3)))
        email = first_part + "@" + secondpart + "." + domain_part
        # email = first_part + '@' + 'carbtc.net'

        return email

    def get_random_incorrect_email_type1(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3)))
        email = 'testliveedu_' + first_part + secondpart + "." + domain_part
        # email = first_part + '@' + 'carbtc.net'

        return email

    def get_random_incorrect_email_type2(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3)))
        email = 'testliveedu_' + first_part + '@' + secondpart
        # email = first_part + '@' + 'carbtc.net'

        return email

    def get_random_incorrect_email_type3(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3)))
        email = 'testliveedu_' + first_part + 'іваіва' + '@' + secondpart + domain_part
        # email = first_part + '@' + 'carbtc.net'

        return email

    def get_random_incorrect_email_type4(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3)))
        email = 'testliveedu_' + first_part + ' ' + '@' + secondpart + "." + domain_part
        # email = first_part + '@' + 'carbtc.net'

        return email

    def get_random_incorrect_email_type5(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3)))
        email = ""
        # email = first_part + '@' + 'carbtc.net'user = app.user_parse.parse_user_properties(resp_dict={'email': email})
        return email

    def get_random_two_passwords(self):
        password1 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(8, 20)))
        password2 = password1

        return [password1, password2]

    def get_random_two_passwords_not_the_same(self):
        password1 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(8, 20)))
        password2 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(8, 20)))

        return [password1, password2]

    def get_random_two_passwords_numeric(self):
        password1 = random.randint(10000000, 100000000000)
        password2 = password1

        return [password1, password2]

    def get_random_two_passwords_short(self):
        password1 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 7)))
        password2 = password1

        return [password1, password2]

    def get_random_two_passwords_uppercase_lowercase_the_same(self):
        password1 = ''.join(random.choice(string.ascii_uppercase) for i in range(random.randint(8, 30)))
        password2 = password1.lower()

        return [password1, password2]

    def get_random_username(self):
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(10, 20)))

        return username

    def get_random_username_short(self):
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 2)))

        return username

    def get_random_username_long(self):
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(30, 60)))

        return username

    def get_random_start_end_dates_unix(self):
        random_year = random.randint(1971, 2018)
        start_date = datetime.date(random_year, random.randint(1, 12), random.randint(1, 28))
        end_year = datetime.date(random.randint(random_year, 2018), random.randint(1, 12), random.randint(1, 28))

        return {'start_date': time.mktime(start_date.timetuple()), 'end_date': time.mktime(end_year.timetuple())}

    def get_current_unix_time(self):
        unix_time = time.time()
        return unix_time
