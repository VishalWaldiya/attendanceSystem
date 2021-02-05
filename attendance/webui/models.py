from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

GENDER_TYPE = (
    ('M', 'Male'),
    ('F', 'Female'),
)

ACTIVE_TYPE = (
    ('ACT', 'Active'), # Green State
    ('TRAN', 'Transit'), # Orange State
    ('INACT', 'InActive'), # Orange State
)

class MemberType(models.Model):
    """Model definition for MemberType.
    Using this as to identify Sewadar, IC, and Admin"""

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        """Meta definition for MemberType."""

        verbose_name = 'MemberType'
        verbose_name_plural = 'MemberTypes'

    def __str__(self):
        """Unicode representation of MemberType."""
        return self.name

    # def save(self):
    #     """Save method for MemberType."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for MemberType."""
    #     return ('')

    # TODO: Define custom methods here

class Member(models.Model):
    """Model definition for Member."""

    # ID and FK
    MemberTypeDetails = models.ForeignKey('webui.MemberType', on_delete=models.DO_NOTHING)
    CenterDetails = models.ForeignKey('webui.Center', on_delete=models.DO_NOTHING)
    id = models.BigIntegerField(unique=True,primary_key=True)

    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50,blank=True)
    # Can make a relation
    gender = models.CharField(choices=GENDER_TYPE,default='M', max_length=10)
    contact = PhoneNumberField()
    altcontact = PhoneNumberField(blank=True)
    department = models.CharField(max_length=50, default="Security")

    class Meta:
        """Meta definition for Member."""

        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        """Unicode representation of Member."""
        return '{}'.format(self.name ) # TODO

    # def save(self):
    #     """Save method for Member."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for Member."""
    #     return ('')

    # TODO: Define custom methods here

class Center(models.Model):
    """Model definition for Center."""

    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Center."""

        verbose_name = 'Center'
        verbose_name_plural = 'Centers'

    def __str__(self):
        """Unicode representation of Center."""
        return '{}'.format(self.name ) # TODO

    # def save(self):
    #     """Save method for Center."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for Center."""
    #     return ('')

    # TODO: Define custom methods here

class SecurityPost(models.Model):
    """Model definition for SecurityPost."""

    name = models.CharField(max_length=50)


    class Meta:
        """Meta definition for SecurityPost."""

        verbose_name = 'SecurityPost'
        verbose_name_plural = 'SecurityPosts'

    def __str__(self):
        """Unicode representation of SecurityPost."""
        return '{}'.format(self.name ) # TODO

    # def save(self):
    #     """Save method for SecurityPost."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for SecurityPost."""
    #     return ('')

    # TODO: Define custom methods here

class Transaction(models.Model):
    """Model definition for Transaction."""

    MemberDetails = models.ForeignKey('webui.Member', on_delete=models.DO_NOTHING)
    SecurityPostDetails = models.ForeignKey('webui.SecurityPost', on_delete=models.DO_NOTHING)

    inTime = models.DateTimeField(auto_now=False)
    outtime = models.DateTimeField(auto_now=False)
    status = models.CharField(choices=ACTIVE_TYPE, max_length=50, default='ACT')
    misc = models.TextField(blank=True)

    class Meta:
        """Meta definition for Transaction."""

        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        """Unicode representation of Transaction."""
        return '{}'.format(self.inTime ) # TODO

    # def save(self):
    #     """Save method for Transaction."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for Transaction."""
    #     return ('')

    # TODO: Define custom methods here

# OPen Transdaction 

class MemberTemporary(models.Model):
    """Model definition for MemberTemporary."""

    # ID and FK
    CenterDetails = models.ForeignKey('webui.Center', on_delete=models.DO_NOTHING)

    MemberTypeDetails = models.CharField(default='Sewadaar', max_length=50)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50,blank=True)
    # Can make a relation
    gender = models.CharField(choices=GENDER_TYPE,default='M', max_length=10)
    contact = PhoneNumberField()
    altcontact = PhoneNumberField(blank=True)
    department = models.CharField(max_length=50, default="Security")

    class Meta:
        """Meta definition for MemberTemporary."""

        verbose_name = 'MemberTemporary'
        verbose_name_plural = 'MemberTemporarys'

    def __str__(self):
        """Unicode representation of MemberTemporary."""
        return '{}'.format(self.name ) # TODO

    # def save(self):
    #     """Save method for MemberTemporary."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for MemberTemporary."""
    #     return ('')

    # TODO: Define custom methods here


class TransactionTemporary(models.Model):
    """Model definition for TransactionTemporary."""

    MemberDetails = models.ForeignKey('webui.MemberTemporary', on_delete=models.DO_NOTHING)
    inTime = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for TransactionTemporary."""

        verbose_name = 'TransactionTemporary'
        verbose_name_plural = 'TransactionTemporarys'

    def __str__(self):
        """Unicode representation of TransactionTemporary."""
        return '{}'.format(self.inTime ) # TODO

    # def save(self):
    #     """Save method for TransactionTemporary."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for TransactionTemporary."""
    #     return ('')

    # TODO: Define custom methods here

class MiscContact(models.Model):
    """Model definition for MiscContact."""

    name = models.CharField(max_length=500)
    role = models.CharField(max_length=500)
    contact = models.CharField(max_length=50)

    class Meta:
        """Meta definition for MiscContact."""

        verbose_name = 'MiscContact'
        verbose_name_plural = 'MiscContacts'

    def __str__(self):
        """Unicode representation of MiscContact."""
        return '{}'.format(self.name)

    # def save(self):
    #     """Save method for MiscContact."""
    #     pass

    # def get_absolute_url(self):
    #     """Return absolute url for MiscContact."""
    #     return ('')

    # TODO: Define custom methods here
