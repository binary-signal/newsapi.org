""" all available parameter options for newsapi.org client """

""" defaults to all countries """
county = {'ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de',
          'eg' 'fr' 'gb' 'gr' 'hk' 'hu' 'id' 'ie' 'il' 'in' 'it' 'jp' 'kr' 'lt' 'lv' 'ma',
          'mx' 'my' 'ng' 'nl' 'no' 'nz' 'ph' 'pl' 'pt' 'ro' 'rs' 'ru' 'sa' 'se' 'sg' 'si',
          'sk' 'th' 'tr' 'tw' 'ua' 'us' 've' 'za'}

""" defaults to all languages """
language = {'ar', 'de', 'en', 'es', 'fr', 'he', 'it', 'nl', 'no', 'pt', 'ru', 'se', 'ud', 'zh'}

""" defaults to all categories """
category = {'business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology'}

""" defaults to publishedAt"""
sortBy = {'relevancy', 'popularity', 'publishedAt'}