__menu = {
    "uri": __package__,
    "name": "티프리카",
    "list": [
        {
            "uri": "setting",
            "name": "설정",
        },
        {
            "uri": "tmovie",
            "name": "영화",
        },
        {
            "uri": "tdrama",
            "name": "드라마",
        },
        {
            "uri": "tent",
            "name": "예능",
        },
        {
            "uri": "tv",
            "name": "TV",
        },
        {
            "uri": "tani",
            "name": "애니",
        },
        {
            "uri": "tmusic",
            "name": "음악",
        },
        {
            "uri": "adult",
            "name": "성인",
        },
        {
            "uri": "log",
            "name": "로그",
        },
    ],
}

setting = {
    "filepath": __file__,
    "use_db": True,
    "use_default_setting": True,
    "home_module": "tmovie",
    "menu": __menu,
    "setting_menu": None,
    "default_route": "single",
}

# pylint: disable=import-error
from plugin import create_plugin_instance

P = create_plugin_instance(setting)

from .module import ModuleMain

P.set_module_list([ModuleMain])
