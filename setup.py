# gethtmlbot - send formatted html text messages and get back plain text messages
# Copyright (C) 2017  Dario 91DarioDev <dariomsn@hotmail.it> <github.com/91dariodev>
#
# gethtmlbot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gethtmlbot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with gethtmlbot.  If not, see <http://www.gnu.org/licenses/>.


import setuptools


setuptools.setup(

    name="gethtmlbot",
    version="1",

    license="AGPL-3.0",

    author="Dario 91DarioDev",
    author_email="dariomsn@hotmail.it",

    install_requires=[
        "python-telegram-bot"
    ],

    packages=[
        "gethtmlbot",
    ],

    entry_points={
        "console_scripts": [
            "gethtmlbot = gethtmlbot.__main__:main",
        ],
    },

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Not on PyPI"
    ],

)
