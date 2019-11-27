test = {
  'name': 'smallest-int-having',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_having LIMIT 50;
          11/17/2019 17:50:00|21
          11/17/2019 14:06:48|24
          11/17/2019 14:08:16|30
          11/17/2019 15:49:03|32
          11/17/2019 14:15:29|33
          11/17/2019 14:13:31|46
          11/17/2019 16:43:05|47
          11/17/2019 14:48:52|55
          11/17/2019 15:02:01|56
          11/17/2019 20:26:06|57
          11/17/2019 14:14:46|64
          11/17/2019 16:14:48|66
          11/17/2019 15:29:28|70
          11/17/2019 15:38:10|73
          11/17/2019 18:47:19|76
          11/17/2019 14:40:03|77
          11/17/2019 16:12:53|78
          11/17/2019 13:59:06|79
          11/17/2019 15:54:16|81
          11/17/2019 13:58:29|84
          11/17/2019 20:53:05|87
          11/17/2019 14:07:53|94
          11/17/2019 22:00:24|101
          11/17/2019 14:50:08|111
          11/17/2019 13:58:04|112
          11/17/2019 16:22:37|114
          11/17/2019 14:10:23|138
          11/17/2019 14:05:41|143
          11/17/2019 14:51:50|153
          11/17/2019 14:37:48|162
          11/17/2019 14:34:00|167
          11/17/2019 14:00:02|179
          11/17/2019 16:45:18|231
          11/17/2019 17:07:04|234
          11/17/2019 16:25:51|271
          11/17/2019 14:25:37|304
          11/17/2019 14:22:36|442
          11/17/2019 14:20:09|1647
          11/17/2019 14:02:47|3025
          11/17/2019 14:06:14|5643
          11/17/2019 19:34:07|16666
          11/17/2019 15:54:14|69420
          11/17/2019 17:22:15|9871230
          11/17/2019 14:08:19|999999999
          11/17/2019 16:38:36|1023123123
          11/17/2019 14:03:54|9870597394507
          11/17/2019 14:16:19|53567823673157
          11/17/2019 15:12:05|100000000000000
          11/17/2019 17:22:10|1e+50
          11/17/2019 13:59:14|1e+72
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}