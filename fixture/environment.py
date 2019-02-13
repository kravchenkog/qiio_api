class Environment:
    def __init__(self, env, token, params={}, baseurls='', cookies=''):

        self.env_value = ''
        if not env:
            self.env_value = '-test'
        if not token:
            token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1zeE1KTUxDSURXTVRQdlp5SjZ0eC1DRHh3MCIsImtpZCI6Ii1zeE1KTUxDSURXTVRQdlp5SjZ0eC1DRHh3MCJ9.eyJhdWQiOiJodHRwczovL3NtYXJ0aG9tZXRlY2hub2xvZ3ljaC5vbm1pY3Jvc29mdC5jb20vNzA1MzM0YWItZDIxZi00ZjlmLThlZmQtMmUxY2NiNTMzYzZhIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzExMDY3NGUtZjgzMC00ZjdmLTg3YTgtYTQ2OTczZTRjNzVmLyIsImlhdCI6MTU1MDA1NjQxMywibmJmIjoxNTUwMDU2NDEzLCJleHAiOjE1NTAwNjAzMTMsImFjciI6IjEiLCJhaW8iOiJBU1FBMi84S0FBQUFhaTFwU2FmKzBmZWR0L3FiUlRkZ1NUUHpSUHRyN1RWd2lrQ0w3Y08yckJZPSIsImFtciI6WyJwd2QiXSwiYXBwaWQiOiJlNDE1MzIxZi0wNDAzLTRkNTYtOWM5Mi03YjAyOGY3MDE0MjMiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IktyYXZjaGVua28iLCJnaXZlbl9uYW1lIjoiR3JpZ29yaWkiLCJpcGFkZHIiOiIyMTIuOTAuMTg3LjIwNiIsIm5hbWUiOiJHcmlnb3JpaSBLcmF2Y2hlbmtvIiwib2lkIjoiZjYyZmYwMzMtOWI4YS00ZTEyLWJhZjAtNjNiNzBjMzA0NmU1Iiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoibEdlM2s1ZzgyMnFaTkhqNFZRX0NGV3BlMU54OGNHZ092NFl3X1pZbElfdyIsInRpZCI6IjcxMTA2NzRlLWY4MzAtNGY3Zi04N2E4LWE0Njk3M2U0Yzc1ZiIsInVuaXF1ZV9uYW1lIjoiZ3JpZ29yaWkua3JhdmNoZW5rb0BxaWlvLmNvbSIsInVwbiI6ImdyaWdvcmlpLmtyYXZjaGVua29AcWlpby5jb20iLCJ1dGkiOiJxQnExQjJTSVlrS0w2SzR5cHhzUUFBIiwidmVyIjoiMS4wIn0.FIP8YbdGm0WT5ZJ2gpmAAr28Xf-qbRrdiLpccdc_GmItr3vzxynqJt2bi9eiF_EzyDQq3iJv-PVnpUb4dR51o9Gro5ZYSgVEvY31ca6xlj_mDwKjODPePDN7aude4mHc2bG2ru8gL7a8ERMfHzPU4uIzkf3d3rLUqSBVbHBKoIciTVlppNG6uVqocIhqc5CWN_TBOVVeOui-IIHc0DpefMnDpdR12zU_AqFn7WxKe_Gt1_I7E5YQzLFMlyMi_4WMUt_KCsQlgxBnhf2-UDZh2Qk6-283Ey6ufpsYEIz-a-e2e36-VhBqnKZZCFYi1KwOtRLPpZyVA2PPCNYAG1SJbg'
        self.base_url = 'https://api{}.qiio.cloud'.format(self.env_value)

        self.headers = {'Content-Type': 'application/json',
                        'Authorization': token}
        self.params = {'url': 'goms-test.qiio.cloud'}
        self.cookies = cookies
