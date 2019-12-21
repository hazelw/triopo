from enum import Enum


class TicketStatus(Enum):
    NEW = 'new'
    TRIAGED = 'triaged'
    # TODO: on hold with who? Is there a difference between something being
    # with an engineer and awaiting fix and waiting on information from another
    # source?
    ON_HOLD = 'on hold'
    DONE = 'done'
