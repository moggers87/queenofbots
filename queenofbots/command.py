##
#    Copyright (C) 2018 Matt Molyneaux
#
#    This file is part of queenofbots.
#
#    Inboxen is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Inboxen is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with Inboxen  If not, see <http://www.gnu.org/licenses/>.
##

import logging

import click


logger = logging.getLogger("queenofbots")


@click.group()
@click.option("-v", "--verbose", count=True,
              help="Verbose output, can be used multiple times to increase logging level"))
def queen(verbose):
    logger.addHandler(logging.StreamHandler())
    if verbsose > 1:
        logger.setLevel(logging.DEBUG)
    elif verbose == 1:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARN)
