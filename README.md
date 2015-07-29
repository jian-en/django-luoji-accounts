# django-luoji-accounts


Overview
--------
django-luoji-accounts adds a number of indispensible financial account-related capabilities to your Django application, including:

* Account

* Sub Account

* Transfer

* Transaction 

Please note, this app was developed under Django==1.8.2.

Quick Start
-----------
django-luoji-accounts contains a low level account and sub accounts system that you can get up and running right away. 

To install Django-Accounts from PyPI::
```bash
pip install django-luoji-accounts
```
Alternatively, you can also install Django-luoji-Accounts from GitHub::
https://github.com/hereischen/django-luoji-accounts

Add 'accounts' to your INSTALLED_APPS in your settings.py::

```python
INSTALLED_APPS = (
...
'accounts',
...
)
```
Include the django-luoji-accounts URLs in your urls.py::

```python
urlpatterns = patterns(
...
(r'^accounts/', include('accounts.urls')),
...
)
```

To customise for your speacific usage, use a wrapper class in your project, for example:
```python
from accounts.models import GeneralAccountManager

class AudioAccountManager(GeneralAccountManager):

    """
    音频账户管理类
    """
    def _get_or_create_sub_account_for_jcc(self, user_id, account_type, device_type):
        return self.get_or_create_sub_account(user_id=user_id,
                                              account_type=account_type,
                                              sys_code='AUDIO',
                                              device_type=device_type,
                                              currency='JCC'
                                              )

    def get_or_create_buyer_account_for_android(self, user_id):
        return self._get_or_create_sub_account_for_jcc(user_id,'BUYER', 'ANDROID')
```

That's it!