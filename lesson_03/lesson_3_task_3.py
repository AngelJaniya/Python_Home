from address import Address
from mailing import Mailing

Mailing(
    Address('01000', 'Tblisi', 'Mindeli', '22', 11),
    Address('02000', 'Batumi', 'Kazbegi', '33', 44),
    99,
    'ABA67'
).show()
