import pytest

import celery_app


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture(scope='module')
def celery_fixture(request):
    celery_app.app.conf.update(CELERY_ALWAYS_EAGER=True)
    return celery_app
