class Environment:
    def __init__(self, env, token, params={}, baseurls='', cookies=''):

        self.env_value = ''
        if not env:
            self.env_value = '-test'
        if not token:
            token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1zeE1KTUxDSURXTVRQdlp5SjZ0eC1DRHh3MCIsImtpZCI6Ii1zeE1KTUxDSURXTVRQdlp5SjZ0eC1DRHh3MCJ9.eyJhdWQiOiJodHRwczovL3NtYXJ0aG9tZXRlY2hub2xvZ3ljaC5vbm1pY3Jvc29mdC5jb20vNzA1MzM0YWItZDIxZi00ZjlmLThlZmQtMmUxY2NiNTMzYzZhIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzExMDY3NGUtZjgzMC00ZjdmLTg3YTgtYTQ2OTczZTRjNzVmLyIsImlhdCI6MTU1MDA0NjU2OSwibmJmIjoxNTUwMDQ2NTY5LCJleHAiOjE1NTAwNTA0NjksImFjciI6IjEiLCJhaW8iOiI0MkpnWU9pc016NmRmN0MrKzVSa1lYcHRUK1ZsN1JkVEJBKzZHam4xaHg2S2w3NnhzUlFBIiwiYW1yIjpbInB3ZCJdLCJhcHBpZCI6ImU0MTUzMjFmLTA0MDMtNGQ1Ni05YzkyLTdiMDI4ZjcwMTQyMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiS3JhdmNoZW5rbyIsImdpdmVuX25hbWUiOiJHcmlnb3JpaSIsImlwYWRkciI6IjIxMi45MC4xODcuMjA2IiwibmFtZSI6IkdyaWdvcmlpIEtyYXZjaGVua28iLCJvaWQiOiJmNjJmZjAzMy05YjhhLTRlMTItYmFmMC02M2I3MGMzMDQ2ZTUiLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJsR2UzazVnODIycVpOSGo0VlFfQ0ZXcGUxTng4Y0dnT3Y0WXdfWllsSV93IiwidGlkIjoiNzExMDY3NGUtZjgzMC00ZjdmLTg3YTgtYTQ2OTczZTRjNzVmIiwidW5pcXVlX25hbWUiOiJncmlnb3JpaS5rcmF2Y2hlbmtvQHFpaW8uY29tIiwidXBuIjoiZ3JpZ29yaWkua3JhdmNoZW5rb0BxaWlvLmNvbSIsInV0aSI6InJXeTEwZWRvXzBPM18tT0VNTTBJQUEiLCJ2ZXIiOiIxLjAifQ.rT0toOPCoPanCeBBhcQ0ngFMlme-x-dv-yZtgbuSAHP_rV5zXJybjGrR6_bKrIjTbXwsc7s1HnxA-PshBWs4-P3k_1lprc6Aq7qZubNgue6JLRZKOliiUeQxvim5lcy3MiA_1aNTJwKDXZXAmXNTQzMRbuoaNAqC7bNOpo13TDy70VNzOGrqmSpgQ0od2aT9vG_GbV0fbYNnWSqx3cZ6styup2CRuMApGnUrTrskmy6T0-o0S11Duu7SeR3GvCqM0uhOh6PbiaQ0UR58Em3qdjw24DaCTyBDp4TRyFD33sriYOs3wvVnkO6bw8mcdNd7jDonMsajy2GVukYFIKrg6w'
        self.base_url = 'https://api{}.qiio.cloud'.format(self.env_value)

        self.headers = {'Content-Type': 'application/json',
                        'Authorization': token}
        self.params = {'url': 'goms-test.qiio.cloud'}
        self.cookies = cookies
