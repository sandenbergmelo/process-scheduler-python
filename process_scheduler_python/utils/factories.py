import random

import factory

from process_scheduler_python.utils.process import Process


class ProcessFactory(factory.Factory):
    class Meta:
        model = Process

    id = factory.Sequence(lambda n: n + 1)
    priority = factory.LazyAttribute(lambda _: random.randint(1, 5))
    execution_time = factory.LazyAttribute(
        lambda _: round(random.uniform(0.00001, 0.01), 6)
    )
