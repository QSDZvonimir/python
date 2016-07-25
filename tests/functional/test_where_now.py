import unittest

try:
    from mock import MagicMock
except ImportError:
    from unittest.mock import MagicMock

from pubnub.endpoints.presence.where_now import WhereNow
from pubnub.pubnub import PubNub
from tests.helper import pnconf, sdk_name


class TestWhereNow(unittest.TestCase):
    def setUp(self):
        self.pubnub = MagicMock(
            spec=PubNub,
            config=pnconf,
            sdk_name=sdk_name
        )
        self.pubnub.uuid = "UUID_WhereNowTest"
        self.where_now = WhereNow(self.pubnub)

    def test_where_now(self):
        self.where_now.uuid("person_uuid")

        self.assertEquals(self.where_now.build_path(), WhereNow.WHERE_NOW_PATH
                          % (pnconf.subscribe_key, "person_uuid"))

        self.assertEqual(self.where_now.build_params(), {
            'pnsdk': sdk_name,
            'uuid': self.pubnub.uuid
        })