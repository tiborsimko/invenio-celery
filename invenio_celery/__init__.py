# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2013, 2014, 2015, 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Celery distributed task queue module for Invenio.

Invenio-Celery is a small discovery layer that takes care of discovering and
loading tasks from other Invenio modules, as well as providing configuration
defaults for Celery usage in Invenio. Invenio-Celery relies on Flask-CeleryExt
for integrating Flask and Celery with application factories.

Defining tasks
--------------
Invenio modules that wish to define Celery tasks should use the
``@shared_task`` decorator (usually in ``tasks.py``):

.. code-block:: python

    # mymodule/tasks.py
    from celery import shared_task

    @shared_task
    def sum(x, y):
     return x + y

Additionally the Invenio module should add the task module into the
``invenio_celery.tasks`` entry point:

.. code-block:: python

    # setup.py
    setup(
        # ...
        entry_points=[
            'invenio_celery.tasks' : [
                'mymodule = mymodule.tasks'
            ]
        ]
    )

Using tasks
-----------
Invenio modules that need to call tasks do not need to do anything special as
long as the Invenio-Celery extension has been initialized. Hence calling tasks
is as simple as:

.. code-block:: python

    from mymoudle.tasks import sum
    result = sum.delay(2, 2)


Celery workers
--------------
Invenio-Celery hooks into the Celery application loading process so that when
a worker starts, all the tasks modules defined in ``invenio_celery.tasks`` will
be imported and cause the tasks to be registered in the worker. Note that this
only happens on the Celery worker side which needs to know upfront all the
possible tasks.

For further details on how to setup Celery and define an Celery application
factory please see `Flask-CeleryExt <https://flask-celeryext.readthedocs.io/>`_
"""

from __future__ import absolute_import, print_function

from .ext import InvenioCelery
from .version import __version__

__all__ = ('__version__', 'InvenioCelery')
