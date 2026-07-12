import pytest

'''
Маркировки нельзя применять к самим фикстурам.
'''

@pytest.mark.smoke
class TestSuite:

    def test_smoke_case(self):
        pass

    def test_regression_case(self):
        pass


class TestUserAuthentication:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass


@pytest.mark.ui
class TestUserInterface:

    @pytest.mark.smoke
    def test_login_button(self):
        pass

    @pytest.mark.critical
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass
