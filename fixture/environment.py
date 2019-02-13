class Environment:
    def __init__(self, env, token, params={}, baseurls='', cookies=''):

        self.env_value = ''
        if not env:
            self.env_value = '-test'
        if not token:
            token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1zeE1KTUxDSURXTVRQdlp5SjZ0eC1DRHh3MCIsImtpZCI6Ii1zeE1KTUxDSURXTVRQdlp5SjZ0eC1DRHh3MCJ9.eyJhdWQiOiJodHRwczovL3NtYXJ0aG9tZXRlY2hub2xvZ3ljaC5vbm1pY3Jvc29mdC5jb20vNzA1MzM0YWItZDIxZi00ZjlmLThlZmQtMmUxY2NiNTMzYzZhIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzExMDY3NGUtZjgzMC00ZjdmLTg3YTgtYTQ2OTczZTRjNzVmLyIsImlhdCI6MTU1MDA2MjI2MSwibmJmIjoxNTUwMDYyMjYxLCJleHAiOjE1NTAwNjYxNjEsImFjciI6IjEiLCJhaW8iOiJBU1FBMi84S0FBQUF5ckIvbnEvMWdZZE8wV1hxaGRyZEh2TEROS0lGWnJ0UlM5Z21RSmZWZit3PSIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiJlNDE1MzIxZi0wNDAzLTRkNTYtOWM5Mi03YjAyOGY3MDE0MjMiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IktyYXZjaGVua28iLCJnaXZlbl9uYW1lIjoiR3JpZ29yaWkiLCJpcGFkZHIiOiIyMTIuOTAuMTg3LjIwNiIsIm5hbWUiOiJHcmlnb3JpaSBLcmF2Y2hlbmtvIiwib2lkIjoiZjYyZmYwMzMtOWI4YS00ZTEyLWJhZjAtNjNiNzBjMzA0NmU1Iiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoibEdlM2s1ZzgyMnFaTkhqNFZRX0NGV3BlMU54OGNHZ092NFl3X1pZbElfdyIsInRpZCI6IjcxMTA2NzRlLWY4MzAtNGY3Zi04N2E4LWE0Njk3M2U0Yzc1ZiIsInVuaXF1ZV9uYW1lIjoiZ3JpZ29yaWkua3JhdmNoZW5rb0BxaWlvLmNvbSIsInVwbiI6ImdyaWdvcmlpLmtyYXZjaGVua29AcWlpby5jb20iLCJ1dGkiOiJKWjMzVWoxQVBrbXpNT1NyOUsydkFBIiwidmVyIjoiMS4wIn0.WKsk6uJ78v_Wg25POwtqaoahbKHBo5J-KnZYbKs0PxgA26dkUE7FeVRgQfjho78if_vh5yzJmk1DD4Zz3IQXqWEy88MXZ3J0ZbnhQtTaFbHWCheLgcSpyk106o_9GcuQjYtOXu-vZfHNkxdR29xIfsfOO9O4CoRmX9sG6l1G8KijX2BQHz9xgM_slLDnhKWRAZg1Lgz1xpXWUT6F0qCybo7UgaVPWiA_0vHOjLtrS0dOwTBfltGgIQMcrZ-xi4nHDlxHsY4S70Pf_JVuXRoRzQQkEdhlKbH60BVZtvnINnsKog4V7X5VnddLhnRJWio9B4uZXeh59NwCjaX61RXrKw'
        self.base_url = 'https://api{}.qiio.cloud'.format(self.env_value)

        self.headers = {'Content-Type': 'application/json',
                        'Authorization': token}
        self.params = {'url': 'goms-test.qiio.cloud'}
        self.cookies = cookies
