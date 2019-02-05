import pytest

class TestCompany:

    @pytest.fixture(autouse=True)
    def remove_parameters(self, app):
        app.data_help.remove_all_parameters_exsept_url(app)

    def test_WHEN_get_company_EXPECTED_response_code_200(self, app):
        resp = app.rest.rest_get(app, app.route.company)
        assert resp['status_code'] == 200

    # should not return 200
    def test_WHEN_get_companies_EXPECTED_response_code_200(self, app):
        resp = app.rest.rest_get(app, app.route.companies)
        assert resp['status_code'] == 200
