class Environment:
    def __init__(self, env, token, params={}, baseurls='', cookies=''):

        self.env_value = ''
        if not env:
            self.env_value = '-test'
        if not token:
            token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1zeE1KTUxDSURXTVRQdlp5SjZ0eC1DRHh3MCIsImtpZCI6Ii1zeE1KTUxDSURXTVRQdlp5SjZ0eC1DRHh3MCJ9.eyJhdWQiOiJodHRwczovL3NtYXJ0aG9tZXRlY2hub2xvZ3ljaC5vbm1pY3Jvc29mdC5jb20vNzA1MzM0YWItZDIxZi00ZjlmLThlZmQtMmUxY2NiNTMzYzZhIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzExMDY3NGUtZjgzMC00ZjdmLTg3YTgtYTQ2OTczZTRjNzVmLyIsImlhdCI6MTU0OTU0NTk5NiwibmJmIjoxNTQ5NTQ1OTk2LCJleHAiOjE1NDk1NDk4OTYsImFjciI6IjEiLCJhaW8iOiI0MkpnWUJDYVVMTDl4MHRYL2g0bDRRUHFiMS9QUDV3UW1yaTZMR0dQUXVocmwxM0dqSXNBIiwiYW1yIjpbInB3ZCJdLCJhcHBpZCI6ImU0MTUzMjFmLTA0MDMtNGQ1Ni05YzkyLTdiMDI4ZjcwMTQyMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiS3JhdmNoZW5rbyIsImdpdmVuX25hbWUiOiJHcmlnb3JpaSIsImlwYWRkciI6IjIxMi45MC4xODcuMjA2IiwibmFtZSI6IkdyaWdvcmlpIEtyYXZjaGVua28iLCJvaWQiOiJmNjJmZjAzMy05YjhhLTRlMTItYmFmMC02M2I3MGMzMDQ2ZTUiLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJsR2UzazVnODIycVpOSGo0VlFfQ0ZXcGUxTng4Y0dnT3Y0WXdfWllsSV93IiwidGlkIjoiNzExMDY3NGUtZjgzMC00ZjdmLTg3YTgtYTQ2OTczZTRjNzVmIiwidW5pcXVlX25hbWUiOiJncmlnb3JpaS5rcmF2Y2hlbmtvQHFpaW8uY29tIiwidXBuIjoiZ3JpZ29yaWkua3JhdmNoZW5rb0BxaWlvLmNvbSIsInV0aSI6ImZzYTdRXzFPMDBpRnhaVkVfaFFiQUEiLCJ2ZXIiOiIxLjAifQ.ctQ0RGDPbIjCC_Ycv5GRGZlXS68HlLPAflFypla1VCSLlPaBSotkTciqrhLVUOEpz2DdLskOzUcf4li1k3cjk0lXGpxjcSwiVIlJ4C2VtbtOhJsS3GZqssuhDLKVUYcYMZ1cWSpHYumRGn9ZUdr6E9_drLcgFACumTCWbs_ui2q0zUrMgqrdHO6ZN-ov-Ft9JWs2VQFg39YRlX5w1QBEGsMnoDFaa6H5ITFo2-H4QdD-5G2zJYrvbTysReWyLY_gdt9gvxurpU-QIcHEcE3S8PsZgWOEjg5wPEOEM22D0BpYOfOIjD0O2Dc3F_0TF73XwlLhs0jYHbkgItOVhRQVeA'
        self.base_url = 'https://api{}.qiio.cloud'.format(self.env_value)

        self.headers = {'Content-Type': 'application/json',
                        'Authorization': token}
        self.params = {'url': 'goms-test.qiio.cloud'}
        self.cookies = cookies
