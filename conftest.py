import argparse
import pytest
from fixture.app_manager import AppManager
from fixture.test_data import data_param

fixture = None


def pytest_addoption(parser):
    parser.addoption('--token', action='store', help='Example of token: "Bearer kmdemkwedmwe..."')



@pytest.fixture(scope='function')
def app(request):

    global fixture

    if fixture == None:
        # token = get_token()
        token = request.config.getoption("--token")
        fixture = AppManager(0, token)


    return fixture



#
# @pytest.fixture(scope='module')
# def app_streamer(request):
#     global fixture
#     if fixture == None:
#         fixture = AppManager()
#     # fixture.env = Environment(1)
#     fixture.user_data = UserData()
#     fixture.api_helper.get_registered_and_logged_user(app=fixture)
#     return fixture
#
#
@pytest.fixture(params=data_param.targets_list, scope='function', ids=[str(x) for x in data_param.targets_list])
def target(request):
    return request.param


@pytest.fixture(params=data_param.telemetryTypes, scope='function', ids=[str(x) for x in data_param.telemetryTypes])
def telemetry(request):
    return request.param


@pytest.fixture(params=data_param.template, scope='function', ids=[str(x) for x in data_param.template])
def template(request):
    return request.param

#
# @pytest.fixture(scope="module", autouse=True)
# def my_fixture(request):
#     print ('INITIALIZATION')
#     yield
#     global fixture
#     request.data_help.clean_test_users(request)
#     request.data_help.clean_test_roles(request)

@pytest.fixture(scope="session", autouse=True)
def do_something(request):
    request.addfinalizer(finalizer_function)

def finalizer_function():
    global fixture
    fixture.data_help.clean_test_users(fixture)
    fixture.data_help.clean_test_roles(fixture)

# def get_token():
#     credentials = UserPassCredentials(
#         'grigorii.kravchenko@qiio.com',  # Your new user
#         '<8KA3>s.9/BAv(J$',  # Your password
#     )
#     return credentials.token['access_token']
