class Environment:
    def __init__(self, env, token, params={}, baseurls='', cookies=''):

        self.env_value = ''
        if not env:
            self.env_value = '-test'
        if not token:
            token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1zeE1KTUxDSURXTVRQdlp5SjZ0eC1DRHh3MCIsImtpZCI6Ii1zeE1KTUxDSURXTVRQdlp5SjZ0eC1DRHh3MCJ9.eyJhdWQiOiJodHRwczovL3NtYXJ0aG9tZXRlY2hub2xvZ3ljaC5vbm1pY3Jvc29mdC5jb20vNzA1MzM0YWItZDIxZi00ZjlmLThlZmQtMmUxY2NiNTMzYzZhIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzExMDY3NGUtZjgzMC00ZjdmLTg3YTgtYTQ2OTczZTRjNzVmLyIsImlhdCI6MTU0OTM1MTI4NSwibmJmIjoxNTQ5MzUxMjg1LCJleHAiOjE1NDkzNTUxODUsImFjciI6IjEiLCJhaW8iOiI0MkpnWU5DVVpidXlZRzVFZEhTcjFzS3pZbjhtT1gyTitYSmNWK3p5Zk5WcnpDNXhhZW9BIiwiYW1yIjpbInB3ZCJdLCJhcHBpZCI6ImU0MTUzMjFmLTA0MDMtNGQ1Ni05YzkyLTdiMDI4ZjcwMTQyMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiS3JhdmNoZW5rbyIsImdpdmVuX25hbWUiOiJHcmlnb3JpaSIsImlwYWRkciI6IjIxMi45MC4xODcuMjA2IiwibmFtZSI6IkdyaWdvcmlpIEtyYXZjaGVua28iLCJvaWQiOiJmNjJmZjAzMy05YjhhLTRlMTItYmFmMC02M2I3MGMzMDQ2ZTUiLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJsR2UzazVnODIycVpOSGo0VlFfQ0ZXcGUxTng4Y0dnT3Y0WXdfWllsSV93IiwidGlkIjoiNzExMDY3NGUtZjgzMC00ZjdmLTg3YTgtYTQ2OTczZTRjNzVmIiwidW5pcXVlX25hbWUiOiJncmlnb3JpaS5rcmF2Y2hlbmtvQHFpaW8uY29tIiwidXBuIjoiZ3JpZ29yaWkua3JhdmNoZW5rb0BxaWlvLmNvbSIsInV0aSI6IkFub0VCT2F2djAtSW9KcDFRdUJqQUEiLCJ2ZXIiOiIxLjAifQ.pYxzFbaMTpBigwlI2fYP3766HkCzYKiq4w6Gnmo40kj0jRBMh6z4OP2ARTz014aSdUatdW4IZ0QRuNFm1d6i3VM1GjTUDJQNEnas1gFCt03eXXHGg77TXZJ2NTZSK8ie5xbTdzpwVkV2gwTOOuL17wp2hHY5LfAVcadLf0D-COqt_x9WiIS4_t_-q-dCp_Ap2UAcadvokbBB_XTWgS427e8KfbCR7SzA3OTJv4FWi3HVx-5ZzKRDBZSWQ7whqNsMAwxznngUZV1gJgbDqp7_v8pXQBSAdy0D-6YjIiUUZgf1N47wip8kKRJ3lbv3gRS2e8F5RG2b2-A7Wh_sZ2liBg'
        self.base_url = 'https://api{}.qiio.cloud'.format(self.env_value)

        self.headers = {'Content-Type': 'application/json',
                        'Authorization': token}
        self.params = {'url': 'goms-test.qiio.cloud'}
        self.cookies = cookies
