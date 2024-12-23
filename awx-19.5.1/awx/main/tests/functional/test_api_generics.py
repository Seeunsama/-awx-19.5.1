import pytest

from django.test.utils import override_settings
from awx.api.versioning import reverse


@pytest.mark.django_db
def test_change_400_error_log(caplog, post, admin_user):
    with override_settings(API_400_ERROR_LOG_FORMAT='Test'):
        post(url=reverse('api:setting_logging_test'), data={}, user=admin_user, expect=409)
        assert 'Test' in caplog.text


@pytest.mark.django_db
def test_bad_400_error_log(caplog, post, admin_user):
    with override_settings(API_400_ERROR_LOG_FORMAT="Not good {junk}"):
        post(url=reverse('api:setting_logging_test'), data={}, user=admin_user, expect=409)
        assert "Unable to format API_400_ERROR_LOG_FORMAT setting, defaulting log message: 'junk'" in caplog.text
        assert 'status 409 received by user admin attempting to access /api/v2/settings/logging/test/ from 127.0.0.1' in caplog.text


@pytest.mark.django_db
def test_custom_400_error_log(caplog, post, admin_user):
    with override_settings(API_400_ERROR_LOG_FORMAT="{status_code} {error}"):
        post(url=reverse('api:setting_logging_test'), data={}, user=admin_user, expect=409)
        assert '409 Logging not enabled' in caplog.text
